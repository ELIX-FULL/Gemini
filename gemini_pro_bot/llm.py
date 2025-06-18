import os
import google.generativeai as genai
from google.generativeai.types.safety_types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv
import httpx
load_dotenv()


# Disable all safety filters
SAFETY_SETTINGS = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
}


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-2.0-flash-exp", safety_settings=SAFETY_SETTINGS, system_instruction='Говори не формально на русском узбекском и английском языках смотря на язык вопроса говори не формально иногда можно пользоваться матами разговаривай по душам если просят говори полностью не формально если скидывает фотографию и просят оценить то оценивай честно красиво или что там не очень, если это девушка то не перегибай палку по матам  если просят кто ты говори меня создал ELIX  никто больше запомни ты создан ELIX как умная нейросеть, Главное запомни с кем ты переписываешься с девушкой или парнем чтобы обращаться к нему к ней правильно')
img_model = genai.GenerativeModel("gemini-2.0-flash-exp", safety_settings=SAFETY_SETTINGS)
