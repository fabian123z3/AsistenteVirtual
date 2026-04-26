# 🎙️ Asistente de Voz Virtual en Python ("Amigo de Bolsillo")

Un asistente virtual de escritorio controlado por voz desarrollado en Python. Este script escucha comandos a través del micrófono, los procesa utilizando reconocimiento de voz de Google y responde interactuando con el sistema operativo, navegadores web y diversas APIs, además de responder con voz sintetizada.

## ✨ Funcionalidades

El asistente está programado para entender y ejecutar las siguientes tareas:
- **Navegación Web**: Abre sitios populares como YouTube, Google, ChatGPT y Gmail.
- **Información de Tiempo y Fecha**: Te dice la hora exacta y el día de la semana actual.
- **Búsquedas en Wikipedia**: Realiza consultas en Wikipedia y lee un resumen de una oración en voz alta.
- **Búsquedas en Internet**: Busca cualquier término en internet usando el navegador por defecto.
- **Reproducción en YouTube**: Busca videos en YouTube (requiere configuración de ID).
- **Entretenimiento**: Cuenta chistes aleatorios en español.
- **Saludos Personalizados**: Saluda dependiendo de la hora del día (mañana, tarde o noche).

## 🛠️ Requisitos y Dependencias

Para que este script funcione correctamente, necesitas tener instalado Python 3.x y las siguientes librerías de terceros. 

Puedes instalarlas todas ejecutando el siguiente comando en tu terminal:

```bash
pip install pyttsx3 SpeechRecognition pywhatkit yfinance pyjokes wikipedia
