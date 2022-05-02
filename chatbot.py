import openai
import deepl
import config

def answere(input):
  openai.api_key = config.openai_api_key
  gpt3_response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=input,
  temperature=1.0,
  max_tokens=260,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
  )
  return gpt3_response["choices"][0]["text"]

def translate(input_text, target_language):
  translator = deepl.Translator(config.deepl_api_key) 
  translation_result = translator.translate_text(input_text, target_lang=target_language) 
  return translation_result.text

def response(input):
  return translate(str(answere(translate(input,"EN-US"))).replace("\n",""), config.target_language)
