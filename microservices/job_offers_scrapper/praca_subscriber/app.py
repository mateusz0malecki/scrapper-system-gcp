import json
import sqlalchemy.orm
import uvicorn
import os
from datetime import datetime
from fastapi import FastAPI

from storage_client import StorageClient
from db_models import JobOffer
from database import connect_tcp_socket, Base

now = datetime.now()

CREDENTIALS_FILE = 'credentials-storage-scrapper.json'
BLOB_NAME = f'job_offers_praca.json'
BUCKET_NAME = 'job-offers-praca'

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
                job_offer_to_add = JobOffer(**element)
                db_session.add(job_offer_to_add)

        db_session.commit()
        db_session.close()

    return {"time": str(datetime.utcnow() - start)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
