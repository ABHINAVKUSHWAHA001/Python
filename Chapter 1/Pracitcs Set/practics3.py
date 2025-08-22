# this is women sound for the text to voice in mp3

from gtts import gTTS
language = "en"
text = ('''saurabh bhai ka Haal ba''')
speach = gTTS(text=text, lang=language, slow=False, tld="com.au")
speach.save("textToSpeach.mp3")