import os
import firebase_admin
from firebase_admin import credentials


# initialize firebase admin sdk
def initialize():
    cred = credentials.Certificate(os.environ["SERVICE_ACCOUNT_KEY_PATH"])
    firebase_admin.initialize_app(cred)
