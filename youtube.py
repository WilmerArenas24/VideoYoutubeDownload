import flet as ft
from pytube import YouTube
import os

#Creando una interfaz basica en flet
def main(page):
    url = ft.TextField(label='URL',
                       autofocus=True)

    submit = ft.ElevatedButton('Descarga')

    def btn_click(e):
        current_folder = os.getcwd()
        yt = YouTube(url.value)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=current_folder)

    submit.on_click = btn_click
    page.add(
        url,
        submit
    )
#Llamando la interfaz grafica flet
ft.app(target=main)



