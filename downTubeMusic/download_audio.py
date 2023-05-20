import sys
import os
import concurrent.futures
from pytube import YouTube

def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_file = audio_stream.download(output_path="musicas", filename_prefix="audio_")
        print(f"Áudio baixado com sucesso: {yt.title}")
    except Exception as e:
        print(f"Erro ao baixar áudio: {url}. Erro: {e}")

def download_audios(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_audio, urls)

if __name__ == "__main__":
    # Criar a pasta "musicas" se ela não existir
    if not os.path.exists('musicas'):
        os.makedirs('musicas')

    urls = [
        "Aqui vai a(s) url(s)"
    ]

    download_audios(urls)
