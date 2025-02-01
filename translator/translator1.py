import sys
import speech_recognition as sr
from googletrans import Translator

# 确保输出使用 UTF-8 编码 make sure to format in 'utf-8'
sys.stdout.reconfigure(encoding='utf-8')

# 初始化语音识别器和翻译器 initialize the recongnizer and translator
recognizer = sr.Recognizer()
translator = Translator()

# 从麦克风捕获音频 get text
with sr.Microphone() as source:
    print("Please speak...")
    audio_data = recognizer.listen(source)

    try:
        # 将语音转换为文本 voice convert to text
        text = recognizer.recognize_google(audio_data)
        print(f"recongniaze text：{text}")

        # 翻译成英文 translate to English
        translated = translator.translate(text, dest='en')
        print(f"convert to English：{translated.text}")

    except sr.UnknownValueError:
        print("can't recongnize")
    except sr.RequestError as e:
        print(f"error")
