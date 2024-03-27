import requests

url = "https://script.google.com/macros/s/AKfycbwUTSdkejcSIb-v3suXch799eyJGjurK5_h9m9WWs9JcdMbLSus6NDlpqAVTPWCbfWs/exec"

def send_asset_data(serial, estacion, piso):
    answer = requests.post(url+"?serialn="+serial+"&estacionn="+estacion+"&piso="+piso)

    if answer.status_code == 200:
        print("Registro existoso")
    else:
        print("Error en el registro")

