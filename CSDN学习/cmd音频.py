import subprocess

inmp4 = '无价之姐最终版2.mp4'
inmp3 = '无价.mp3'

cmd=f'ffmpeg -i {inmp4} -i {inmp3} -codec copy a.mp4'