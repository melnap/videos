#!/bin/bash
# hand-strip (2 fps) and face (1 fps) contact sheets for V9 TH clips -> th_sheets/
cd /home/user/stockedandready/work/v9; mkdir -p th_sheets
for n in "$@"; do
 f=media/heygen/$n.mp4
 d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)
 rows=$(python3 -c "import math;print(math.ceil($d*2/5))")
 ffmpeg -v error -y -i $f -vf "fps=2,crop=1000:300:460:740,scale=400:120,drawtext=text='%{pts\:hms}':x=4:y=4:fontsize=16:fontcolor=yellow:box=1:boxcolor=black,tile=5x${rows}" -frames:v 1 th_sheets/${n}_hands.jpg
 rows=$(python3 -c "import math;print(math.ceil($d/6))")
 ffmpeg -v error -y -i $f -vf "fps=1,crop=520:560:700:60,scale=208:224,drawtext=text='%{pts\:hms}':x=4:y=4:fontsize=14:fontcolor=yellow:box=1:boxcolor=black,tile=6x${rows}" -frames:v 1 th_sheets/${n}_face.jpg
done
