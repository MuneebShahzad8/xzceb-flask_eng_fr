import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=IAMAuthenticator(apikey),
    service_name='my_translator'
)

def english_to_french(english_text):
    #write the code here
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()

    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    # Translate the text from French to English
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()

    # Extract the translated text from the response
    english_text = translation['translations'][0]['translation']

    return english_text

