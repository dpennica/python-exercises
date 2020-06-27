import requests
import sentry_sdk
import os

sentry_sdk.init(os.getenv("SENTRY_KEY"))
