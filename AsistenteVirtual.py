import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import time
import wikipedia

#OPCION DE VOZ
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"


# ESCUCHAR MICROFONO Y DEVOLVER TEXTO
def transformar_audio_en_texto():
    # ALMACENAR RECONGNIZER EN VARIABLE
    r = sr.Recognizer()

    # CONFIGURAR MICROFONO
    with sr.Microphone() as origen:
        # TIEMPO DE ESPERA
        r.pause_threshold = 0.8

        # INFORMAR QUE COMENZO GRABACION
        print("Puedes hablar")

        # GUARDAR LO QUE ESCUCHA COMO AUDIO
        audio = r.listen(origen)

        try:
            # BUSCAR EN GOOGLE
            pedido = r.recognize_google(audio, language="es-AR")

            # PRUEBA DE QUE PUDO INGRESAR
            print("Dijiste: " + pedido)

            # DEVOLVER PEDIDO
            return pedido

        except sr.UnknownValueError:
            # EN CASO DE QUE NO COMPRENDIÓ EL AUDIO
            print("UPS, NO ENTENDÍ")

            # DEVOLVER ERROR
            return "No pude entender lo que dijiste."

        except sr.RequestError:
            # EN CASO DE NO HABER SERVICIO
            print("UPS, NO HAY SERVICIO")

            # DEVOLVER ERROR
            return "No hay servicio en este momento."

        except Exception as e:
            # CASO INESPERADO
            print(f"UPS, algo ha salido mal: {e}")

            # DEVOLVER ERROR
            return "Ocurrió un error inesperado."

# Llamada a la función
#transformar_audio_en_texto()

#FUNCION PARA QUE EL ASISTENTE PUEDA SER ESCUCHADO
def hablar(mensaje):

    #ENCENDER EL MOTOR DE PYTTSX3
    engine = pyttsx3.init()
    #ELEGIR VOZ SEGUN ID DE ABAJO
    engine.setProperty("voice",id1)

    #PRONUNCIAR MENSAJE
    engine.say(mensaje)
    engine.runAndWait()


#CON ESTE CODIGO REVISAMOS LAS VOCES INTALADAS EN EL PC
"""engine = pyttsx3.init()
for voz in engine.getProperty("voices"):
    print(voz)"""

#INFORMAR EL DIA DE LA SEMANA
def pedir_dia():

    #CREAR VARIABLES CON DATOS DE HOY
    dia = datetime.date.today()
    print(dia)

    #CREAR VARIABLE PARA EL DIA DE LA SEMANA
    dia_semana = dia.weekday()
    print(dia_semana)

    #DICCIONARIO CON NOMBRES DE DIA
    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miércoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sábado",
                  6: "Domingo"}

    #DECIR EL DIA DE LA SEMANA
    hablar(f"Hoy es {calendario[dia_semana]}")

#INFORMAR LA HORA
def pedir_hora():

    #CREAR UNA VARIABLE CON DATOS DE HORA
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos"
    print(hora)

    #DECIR LA HORA
    hablar(hora)

#FUNCION SALUDO INICIAL
def saludo_inicial():

    #CREAR VARIABLE CON DATOS DE HORA
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas Noches"
    elif 6 <= hora.hour < 13:
        momento = "Buen Dia"
    else:
        momento = "Buenas Tarde"

    #DECIR EL SALUDO
    hablar(f"{momento} soy tu amigo de bolsillo. ¿En que te puedo ayudar? ")

#FUNCION CENTRAL DEL ASISTENTE
def pedir_cosas():

    #ACTIVAR SALUDO INICIAL
    saludo_inicial()

    #VARIABLE DE CORTE
    comenzar = True

    #LOOP CENTRAL
    while comenzar:

        #ACTIVAR EL MICRO Y GUARDAR EL PEDIDO EN UN STRING
        pedido = transformar_audio_en_texto().lower()

        #FUNCIONES DEL ASISTENTE
        if "abre youtube" in pedido:
            hablar("Okey, lo hare ahora")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "abre navegador" in pedido:
            hablar("Okey abrire google")
            webbrowser.open("https://www.google.com")
            continue
        elif "abre chat" in pedido:
            hablar("Okey abrire chatgpt")
            webbrowser.open("https://chatgpt.com")
            continue
        elif "abre mi correo" in pedido:
            hablar("Okey abrire tu correo")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            continue
        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("buscando eso en wikipedia")
            pedido = pedido.replace("busca en wikipedia","")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice lo siguiente:")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("Estoy en eso")
            pedido = pedido.replace("busca en internet","")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        # FUNCION DE REPRODUCIR VIDEO EN YOUTUBE (USANDO EL NAVEGADOR DIRECTAMENTE)
        elif "reproduce" in pedido:
            hablar("Genial, lo reproduciré ahora")
            video = pedido.replace("reproduce",
                                   "").strip()  # Elimina la palabra "reproduce" y cualquier espacio adicional

            # Realiza la búsqueda en YouTube con el término del video
            url = f"https://www.youtube.com/results?search_query={video}"  # Realiza la búsqueda de video en YouTube

            # Abre la URL de búsqueda en el navegador
            webbrowser.open(url)  # Esto abrirá la página de búsqueda de YouTube

            # Esperamos 2 segundos para que la página se cargue correctamente
            time.sleep(2)

            # Ahora buscamos el ID del primer video. Esto es un enfoque manual.
            # Necesitarás usar el ID del primer video encontrado. Aquí asumo que el ID del video es el siguiente:
            video_id = "ID_DEL_PRIMER_VIDEO"  # Necesitas poner el ID real del primer video

            # Ahora construimos la URL del primer video
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            # Abre el video directamente
            webbrowser.open(video_url)  # Esto abrirá el primer video de los resultados

            continue



        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue

        elif "gracias y adiós" in pedido:
            hablar("yapo que estes bien")
            break
        

pedir_cosas()