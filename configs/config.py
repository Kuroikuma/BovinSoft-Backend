from ctypes import cast
from email.policy import default
from decouple import config

# ##configurando variables de entorno
DEBUG = True  # O False, dependiendo de tu necesidad
PORT = 5000   # O el puerto que estés utilizando
MONGO_URI = 'mongodb+srv://gomex6798:Uus98shCNltSknNc@cluster0.8tw2v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
SECRET_KEY = '&i!6!5JgU7hakaj6Cj4DzH6LNUAjDC'
# # GEMINI_API_KEY = config('keyGeminis')
# # GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'