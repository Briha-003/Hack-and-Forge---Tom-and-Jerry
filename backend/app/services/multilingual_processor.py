from deep_translator import GoogleTranslator

def translate(text):

try:

translated = GoogleTranslator(
source='auto',
target='en'
).translate(text)

return translated

except:

return text
