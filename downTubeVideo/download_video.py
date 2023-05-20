import os
from pytube import YouTube

# Criar a pasta "videos" se ela não existir
if not os.path.exists('videos'):
    os.makedirs('videos')

# Lista de URLs do YouTube
urls = [
    "aqui vai a(s) url(s) do(s) vídeo(s)"
]

# Para cada URL, baixar o vídeo em formato MP4
for url in urls:
    try:
        yt = YouTube(url)
        video = yt.streams.filter(file_extension='mp4').first()
        video.download(output_path='videos')
        print(f'{yt.title} baixado com sucesso!')
    except:
        print(f'Erro ao baixar {url}')
