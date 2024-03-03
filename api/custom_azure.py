from storages.backends.azure_storage import AzureStorage
from os import environ as env

STORAGE_ACCOUNT_NAME = env.get('STORAGE_ACCOUNT_NAME')
STORAGE_ACCOUNT_KEY = env.get('STORAGE_ACCOUNT_KEY')


class AzureMediaStorage(AzureStorage):
    account_name = STORAGE_ACCOUNT_NAME
    account_key = STORAGE_ACCOUNT_KEY
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = STORAGE_ACCOUNT_NAME
    account_key = STORAGE_ACCOUNT_KEY
    azure_container = 'static'
    expiration_secs = None