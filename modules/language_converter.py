from googletrans import Translator

translator = Translator()

text = input("Enter English sentence: ")

result = translator.translate(text, src='en', dest='de')

print("German Translation:")
print(result.text)
