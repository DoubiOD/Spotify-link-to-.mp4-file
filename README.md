**Drag&drop a song from spotify to download it as mp4.**

# Usage

1. Get your spotify API access [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token)
2. Use API credentials in the script:
`client_id, client_secret = 'client_id', 'client_secret'`
3. Place the 'getNoise.bat' to desktop and open it or `python spotify_link_to_m4a.py <spotify_track_link>`

# Install

## 1. ffmpeg

**Linux**

Debian/Ubuntu-based:

`sudo apt install ffmpeg`

Fedora/CentOS/RHEL:

`sudo dnf install ffmpeg`

Arch Linux:

`sudo pacman -S ffmpeg`

**Windows**

1. Download [here](https://ffmpeg.org/download.html)
2. Add to path - [guide](https://github.com/ytdl-org/youtube-dl#on-windows-how-should-i-set-up-ffmpeg-and-youtube-dl-where-should-i-put-the-exe-files)

## 2. python modules

pip install -r requirements.txt
