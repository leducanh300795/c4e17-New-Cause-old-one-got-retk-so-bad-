from youtube_dl import YoutubeDL
# Sample 2: Download multiple youtube videos
dl = YoutubeDL()
# Put list of song urls in download function to download them, one by one
dl.download(['https://www.youtube.com/watch?v=5YHhFmhBkKI','https://www.youtube.com/watch?v=2K8cpVQ4WLA'])
