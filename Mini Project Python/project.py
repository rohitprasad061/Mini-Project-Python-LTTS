from gtts import gTTS
import os

def convert_to_audio():
    fh = open("output.txt")
    x = fh.read()
    
    language = 'en'
    
    audio = gTTS(text = x, lang = language, slow = False)

    audio.save("output.wav")
    os.system("output.wav")


def fun1():
    fh = open("output.txt", "w")
    print("Enter the text you want to hear : ")
    
    strng = input()

    fh.write(strng)

    fh.close()
    convert_to_audio()

def fun2():
    fh = open("output.txt", "w")
    
    fo = open("input.txt")
    strng = fo.read()

    fh.write(strng)

    fh.close()
    convert_to_audio()


print("Press 1 if you want to enter the text you want to hear")
print("Press 2 if you want that the text should be converted to audio taking input from an input file")

x = int(input())
if x == 1:
    fun1()
elif x == 2:
    print("Just copy the text you want to hear and paste the copied text to the input text file")
    fun2()
else:
    print("Unsupported Input !!")
