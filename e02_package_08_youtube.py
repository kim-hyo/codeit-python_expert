import youtube_dl

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(['https://www.youtube.com/watch?v=4cY4Q1CN49k'])