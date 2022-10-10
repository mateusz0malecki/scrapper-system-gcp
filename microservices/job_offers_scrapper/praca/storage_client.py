from google.cloud import storage


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
