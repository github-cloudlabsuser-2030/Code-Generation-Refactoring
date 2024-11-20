import requests

def obtener_datos_meteorologicos(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        return None

def mostrar_datos(datos):
    if datos:
        print(f"Ciudad: {datos['name']}")
        print(f"Temperatura: {datos['main']['temp']}°C")
        print(f"Clima: {datos['weather'][0]['description']}")
        print(f"Humedad: {datos['main']['humidity']}%")
    else:
        print("No se pudieron obtener los datos meteorológicos.")

# Reemplaza 'tu_api_key' con tu clave API de OpenWeatherMap
api_key = 'tu_api_key'
ciudad = 'Madrid'

datos = obtener_datos_meteorologicos(ciudad, api_key)
mostrar_datos(datos)