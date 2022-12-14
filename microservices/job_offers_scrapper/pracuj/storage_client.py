import os
from functools import lru_cache
from google.cloud import storage

CREDENTIALS_FILE = '/secrets/credentials-storage-scrapper.json'
BLOB_NAME = f'job_offers_pracuj.json'
BUCKET_NAME = 'job-offers-pracuj'
PATH_TO_FILE = f'{os.getcwd()}/offers.json'


class StorageClient:
    def __init__(self, credentials_file, blob_name, bucket_name, path_to_file):
        self._credentials_file = credentials_file
        self._blob_name = blob_name
        self._bucket_name = bucket_name
        self._path_to_file = path_to_file
        self._client = storage.Client.from_service_account_json(self._credentials_file)
        self._bucket = self._client.get_bucket(self._bucket_name)

    def upload(self):
        blob = self._bucket.blob(self._blob_name)
        blob.upload_from_filename(self._path_to_file)
        print(f'File uploaded.')


@lru_cache
def get_client():
    return StorageClient(CREDENTIALS_FILE, BLOB_NAME, BUCKET_NAME, PATH_TO_FILE)
