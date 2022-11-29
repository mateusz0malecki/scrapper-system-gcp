import os
import json
import uvicorn
from datetime import datetime
from fastapi import FastAPI, Depends

from scrapper_offer import OffersScrapper
from scrapper_links import get_links_to_offers_pracuj
from storage_client import StorageClient, get_client, PATH_TO_FILE

now = datetime.now()
app = FastAPI()


@app.get('/')
def index(client: StorageClient = Depends(get_client)):
    start = datetime.utcnow()

    urls = get_links_to_offers_pracuj()
    results_list = []

    for i, url in enumerate(urls):
        print(f"{i} / {len(urls)} | {url}")
        offer_scraper = OffersScrapper(url)
        result = offer_scraper.scrap()
        results_list.append(result)

    with open(PATH_TO_FILE, 'w') as file:
        json.dump(results_list, file, default=str)

    client.upload()

    return {"time": str(datetime.utcnow() - start)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
