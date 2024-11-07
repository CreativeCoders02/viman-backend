from storages.backends.azure_storage import AzureStorage
from os import environ as env
from dotenv import load_dotenv
load_dotenv()

STORAGE_ACCOUNT_NAME = env.get('STORAGE_ACCOUNT_NAME')
STORAGE_ACCOUNT_KEY = env.get('STORAGE_ACCOUNT_KEY')

print(STORAGE_ACCOUNT_NAME)
class AzureMediaStorage(AzureStorage):
    account_name = STORAGE_ACCOUNT_NAME
    account_key = STORAGE_ACCOUNT_KEY
    azure_container = 'creativecodersmedia'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = STORAGE_ACCOUNT_NAME
    account_key = STORAGE_ACCOUNT_KEY
    azure_container = 'creativecodersstatic'
    expiration_secs = None
