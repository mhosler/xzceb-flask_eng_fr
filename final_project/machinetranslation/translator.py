"""
This module is used for translating texts between English and French using IBM Watson
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

# initialize IBM Watson Language Translator
AUTHENTICATOR = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2023-05-27',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def english_to_french(english_text):
    """
    This function translates English text to French using IBM Watson

    Args:
    english_text (str): The text to be translated from English to French

    Returns:
    str: The translated text in French
    """
    if english_text is None:
        return None
    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    This function translates French text to English using IBM Watson

    Args:
    french_text (str): The text to be translated from French to English

    Returns:
    str: The translated text in English
    """
    if french_text is None:
        return None
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
