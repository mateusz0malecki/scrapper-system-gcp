from functools import lru_cache
from google.cloud import storage

CREDENTIALS_FILE = '/secrets/credentials-storage-scrapper.json'
BLOB_NAME = f'job_offers_pracuj.json'
BUCKET_NAME = 'job-offers-pracuj'


class StorageClient:
    def __init__(self, credentials_file, blob_name, bucket_name):
        self._credentials_file = credentials_file
        self._blob_name = blob_name
        self._bucket_name = bucket_name
        self._client = storage.Client.from_service_account_json(self._credentials_file)

    def download_blob_into_memory(self):
        bucket = self._client.bucket(self._bucket_name)
        blob = bucket.blob(self._blob_name)
        contents = blob.download_as_string()
        print("Downloaded storage object {} from bucket {}.".format(self._blob_name, self._bucket_name))
        return contents


@lru_cache
def get_client():
    return StorageClient(CREDENTIALS_FILE, BLOB_NAME, BUCKET_NAME)
