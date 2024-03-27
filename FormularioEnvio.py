import customtkinter
import tkinter
from ApiSpreadsheet import send_asset_data

customtkinter.set_ctk_parent_class(tkinter.Tk)
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Cargar Serial")

print(type(app), isinstance(app, tkinter.Tk))

def button_callback():
    serial = entry_0.get()
    estacion = entry_1.get()
    piso = optionmenu_1.get()
    send_asset_data(serial, estacion, piso)


def SetSerial(serial):
    entry_0.delete(0,1000)
    entry_0.insert(0,serial)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Serial recibido")
label_1.pack(pady=10, padx=10)

entry_0 = customtkinter.CTkEntry(master=frame_1, placeholder_text="SERIAL")
entry_0.pack(pady=10, padx=2)
entry_0.insert(0,"TEST")

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Estación de trabajo")
entry_1.pack(pady=10, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["17", "13", "7"])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Piso")


button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Enviar")
button_1.pack(pady=10, padx=10)

