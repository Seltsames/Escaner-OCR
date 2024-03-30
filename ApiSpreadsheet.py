import requests

url = "https://script.google.com/macros/s/AKfycbyOWl8_-HfeIeHYBtfVSkcOGnXlN9Kn9KfjIE0dyAF2EPCURwgyBeU1Fth5QRkb0ofYQw/exec"

def send_asset_data(serial, estacion, piso):
    answer = requests.post(url+"?serialn="+serial+"&estacionn="+estacion+"&piso="+piso)

    if answer.status_code == 200:
        print("Registro existoso Estación "+estacion+" SN = "+serial)
        return estacion+" S/N"+serial
    else:
        print("Error en el registro")
        return "Error en conexion a la API"

