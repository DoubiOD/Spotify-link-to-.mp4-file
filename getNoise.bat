@echo off
set /p input=spotify link: 
cd /d "C:\path\spotifyLinkToMP4"
python spotify_link_to_m4a.py %input%
move "C:\path\spotifyLinkToMP4\*.m4a" "D:\Music\folder"