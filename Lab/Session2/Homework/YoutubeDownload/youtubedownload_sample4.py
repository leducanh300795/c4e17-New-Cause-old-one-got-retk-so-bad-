from youtube_dl import YoutubeDL
# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 2 # Tell downloader to download only the second entry (video)
}
dl = YoutubeDL(options)
dl.download(['Giáng sing TAMKA pkl'])
