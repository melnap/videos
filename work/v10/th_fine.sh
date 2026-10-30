#!/bin/bash
# fine hand strip: th_fine.sh NAME START END  (5 fps)
cd /home/user/stockedandready/work/v9; n=$1; s=$2; e=$3
ffmpeg -v error -y -ss $s -to $e -i media/heygen/$n.mp4 -vf "fps=5,crop=1000:340:460:720,scale=400:136,drawtext=text='%{eif\:t+$s\:d}.%{eif\:mod((t+$s)*10\,10)\:d}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black,tile=5x$(python3 -c "import math;print(math.ceil(($e-$s)*5/5))")" -frames:v 1 th_sheets/${n}_fine_${s}.jpg
