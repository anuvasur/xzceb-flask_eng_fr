import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('8edLVNVGQ1kHqRCEmOquuqHjdxseqzVjuMby6XtuS1uC')
language_translator =LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/76e644ae-fbd0-4ed0-a68b-9be8b1bece9a')

def english_to_french(english_text):
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text