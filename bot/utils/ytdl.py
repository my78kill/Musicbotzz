from yt_dlp import YoutubeDL

def search(query):
    ydl_opts = {"format": "bestaudio[abr<=128]"}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        return info['url'], info['title']