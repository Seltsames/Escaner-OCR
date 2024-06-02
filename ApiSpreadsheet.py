import requests

url = "https://script.google.com/macros/s/AKfycbxkzjyVgWnnMncs_oD8qrYu73i5NoMVDtPDOrbtLoVVWx8W9vlMYBFuICAZdyjT2ggM/exec"

def send_asset_data(serial, estacion):
    answer = requests.post(url+"?serialn="+serial+"&estacionn="+estacion)

    if answer.status_code == 200:
        print("Registro existoso Estación "+estacion+" SN = "+serial)
        return estacion+" S/N"+serial
    else:
        print("Error en el registro")
        return "Error en conexion a la API"

