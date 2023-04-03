import qrcode
import PySimpleGUI as sg
import os

sg.theme('DarkAmber')
layout = [
    [sg.Text('Enter link'), sg.InputText(key = '-INPUT-')],
    [sg.Button('Create')],
    [sg.Image(key='-IMAGE-', size =(300,300))]
]
Window = sg.Window('QR Code Generator', layout)

def generate_qr_code(link):
     qr = qrcode.QRCode(
          version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_L,
                  box_size=15,
                  border=2
     )
     qr.add_data(link)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     file_name = 'qr_code' + '.png'
    
     file_path = os.path.join(os.getcwd(),file_name)
     print(file_path)
     img.save(file_path)
     return file_path
while True:
          event, values = Window.read()
          if event == sg.WIN_CLOSED:
             break
          
          if event == 'Create':
                link = values['-INPUT-']
                image_path = generate_qr_code(link)
                Window['-IMAGE-'].update(filename=image_path)
               
                

Window.close()


# PRINCESS OSEI BONSU
# 10979224
# BIOMEDICAL ENGNEERING
