from gtts import gTTS
from playsound import playsound

text = '여러분들은 곧 있으면 귀가하실 시간입니다. 안녕히 가세요'
tts = gTTS(text, lang='ko')
tts.save('result.mp3')
playsound('result.mp3')

