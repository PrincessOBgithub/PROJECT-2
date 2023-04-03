import PySimpleGUI as sg
import pyttsx3
speech = pyttsx3.init()
voices = speech.getProperty('voices')
speech.setProperty('voice', voices[0].id)
speech.setProperty('voice', voices[1].id)
speech.setProperty('rate', 100)
speech.setProperty('volume',1.0)

sg.theme('DarkAmber')
layout = [
    [sg.Text('Enter text'), sg.InputText(key = '-INPUT-'), sg.Button('Speak')],
    [sg.Text('Select Voice Type'), sg.Radio('Male','group 1', default= True), sg.Radio('Female', 'group 1')]
]

Window = sg.Window('Text to speech App', layout)

def switch_voice():
    current_voice = speech.getProperty('voices')
    if current_voice == voices[0].id:
        speech.setProperty('voice', voices[0].id)
        print("Switched to Male")
    else:
        speech.setProperty('voice', voices[1].id)
        print("Switched to Female")
        


while True:
    event, values = Window.read()
    if event == sg.WINDOW_CLOSED:
        break
    else: 
        event == 'Speak'
        text = values['-INPUT-']
        
        if values[0]:
          speech.setProperty('voice', voices[0].id)
          print(voices[0].id)
        else:
           if values[1]:
             speech.setProperty('voice', voices[1].id)
             print(voices[1].id)
    switch_voice
    speech.say(text)
    speech.runAndWait()
    Window['-INPUT-'].update(text)

       
        

Window.close()


# PRINCESS OSEI BONSU
# 10979224
# BIOMEDICAL ENGINEERING