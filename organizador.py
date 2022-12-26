import os 
import tkinter as tk
import tkinter.filedialog as filedialog

root = tk.Tk()
root.withdraw()

ORIGEM=filedialog.askdirectory(parent=root, title="Escolhe a pasta que tu quer arrumar ai chefe")

# Define a pasta de destino
DESTINO=ORIGEM

for nome_arquivo in os.listdir(ORIGEM):
    arquivo = os.path.join(ORIGEM, nome_arquivo)

    if os.path.isfile(arquivo):
        extensao = os.path.splitext(arquivo)[1][1:]

        os.makedirs(os.path.join(DESTINO, extensao),exist_ok=True)

        os.rename(arquivo,os.path.join(DESTINO,extensao,nome_arquivo))