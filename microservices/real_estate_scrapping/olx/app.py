import os
import json
import uvicorn
from datetime import datetime
from fastapi import FastAPI

from scrapper_offer import OffersScrapper
from scrapper_links import olx_get_links_to_offers
from storage_client import StorageClient


now = datetime.now()

CREDENTIALS_FILE = 'credentials-storage-scrapper.json'
BLOB_NAME = f'real_estate_offers_olx.json'
BUCKET_NAME = 'real-estate-olx'
PATH_TO_FILE = f'{os.getcwd()}/offers.json'

app = FastAPI()


@app.get('/')
def index():
    start = datetime.utcnow()

    urls = olx_get_links_to_offers()
    results_list = []

    client = StorageClient(CREDENTIALS_FILE, BLOB_NAME, BUCKET_NAME, PATH_TO_FILE)
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
