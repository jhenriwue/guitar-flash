import cv2
import numpy as np
import mss
from PIL import Image
import pytesseract
from pynput.keyboard import Controller
from PIL import ImageGrab, ImageEnhance
import re


SPECIAL_KEY = ' '  
NOTAS_ESPECIAL = [186,274,410,669]  

  
keyboard = Controller()

def extrair_numeros(texto):
    match = re.search(r'\d+', texto)
    if match:
        return int(match.group(0))
    return None  

def guitarSpecialBot():
    specialActivated = False

    with mss.mss() as sct:
        monitor = {"top": 100, "left": 100, "width": 500, "height": 400}
        
    i = 0
    while True:
        try:
            tela_completa = np.array(ImageGrab.grab())

            x_inicial = 635  
            y_inicial = 737 
            largura = 64
            altura = 20

            img = tela_completa[y_inicial:y_inicial + altura, x_inicial:x_inicial + largura] 

        except Exception as e:
            print("Erro ao capturar a tela:", e)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        config_tesseract = '--psm 7'
        contador_texto = pytesseract.image_to_string(gray, config=config_tesseract).strip()
        
        try:
            contador = extrair_numeros(contador_texto)
            print("Contador de Notas:", contador)

            if contador != None:
                if contador > NOTAS_ESPECIAL[i] and contador < NOTAS_ESPECIAL[i]+10:
                    # Pressiona a tecla especial
                    keyboard.press(SPECIAL_KEY)
                    keyboard.release(SPECIAL_KEY)
                    print("Especial ativado!")
                    specialActivated = True
                    i += 1
                elif contador != NOTAS_ESPECIAL:
                    specialActivated = False

        except ValueError:
            print("Falha ao reconhecer o número. Texto detectado2:", contador_texto)
            
if __name__ == '__main__':
    guitarSpecialBot()
