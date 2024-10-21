from textToMorse import TextToMorse

text = input('Enter a text to convert into morse code:\n')
text_to_morse = TextToMorse(text)
text_to_morse.convert_to_morse()