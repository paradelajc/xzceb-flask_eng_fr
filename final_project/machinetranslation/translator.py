# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=E0401

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
  version='2018-05-01',
  authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    if english_text:
        translation = language_translator.translate(english_text, model_id='en-fr').get_result()
        json.dumps(translation, indent=2, ensure_ascii=False)
        french_text = translation['translations'][0]['translation']
        return french_text
    return None

def french_to_english(french_text):
    if french_text:
        translation = language_translator.translate(french_text, model_id='fr-en').get_result()
        json.dumps(translation, indent=2, ensure_ascii=False)
        english_text = translation['translations'][0]['translation']
        return english_text
    return None
