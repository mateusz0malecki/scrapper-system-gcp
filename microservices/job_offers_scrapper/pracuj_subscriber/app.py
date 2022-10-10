import json
import sqlalchemy.orm
import uvicorn
import os
from datetime import datetime
from fastapi import FastAPI

from storage_client import StorageClient
from db_models import JobOffer, Benefit, Requirement, Responsibility
from database import connect_tcp_socket, Base

now = datetime.now()

CREDENTIALS_FILE = 'credentials-storage-scrapper.json'
BLOB_NAME = f'job_offers_pracuj.json'
BUCKET_NAME = 'job-offers-pracuj'

engine = connect_tcp_socket()

app = FastAPI()


@app.post('/')
def handle_db():
    start = datetime.utcnow()
    with engine.connect() as db:
        Base.metadata.create_all(bind=engine)
        session_local = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db_session = session_local()
        client = StorageClient(CREDENTIALS_FILE, BLOB_NAME, BUCKET_NAME)
        content = json.loads(client.download_blob_into_memory())

        for element in content:
            check_if_link_exists = JobOffer.get_offer_by_link(db_session, element["link"])

            if not check_if_link_exists:

                responsibilities_to_add = []
                for responsibility in element["responsibilities"]:
                    responsibility_to_add = Responsibility(
                        responsibility=responsibility
                    )
                    responsibilities_to_add.append(responsibility_to_add)

                requirements_to_add = []
                for requirement in element["requirements"]:
                    requirement_to_add = Requirement(
                        requirement=requirement.get("requirement"),
                        must_have=requirement.get("must_have")
                    )
                    requirements_to_add.append(requirement_to_add)

                benefits_to_add = []
                for benefit in element["benefits"]:
                    benefit_to_add = Benefit(
                        benefit=benefit
                    )
                    benefits_to_add.append(benefit_to_add)

                job_offer_to_add = JobOffer(
                    link=element["link"],
                    city=element["city"],
                    category=element["category"],
                    title=element["title"],
                    company_name=element["company_name"],
                    earning_value_from=element["earning_value_from"],
                    earning_value_to=element["earning_value_to"],
                    contract_type=element["contract_type"],
                    seniority=element["seniority"],
                    offer_deadline=element["offer_deadline"],
                    working_mode=element["working_mode"],
                    working_time=element["working_time"],
                    remote_recruitment=element["remote_recruitment"],
                    immediate_employment=element["immediate_employment"],
                    responsibilities=responsibilities_to_add,
                    requirements=requirements_to_add,
                    benefits=benefits_to_add,
                )

                db_session.add_all(responsibilities_to_add + requirements_to_add + benefits_to_add)
                db_session.add(job_offer_to_add)

        db_session.commit()
        db_session.close()

    return {"time": str(datetime.utcnow() - start)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
