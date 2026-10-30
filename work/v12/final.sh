#!/bin/bash
# concat precut shots -> grade, grain, vignette, burned captions -> mux mix
set -e
cd "$(dirname "$0")"
python3 build.py concat
ffmpeg -v error -y -i out/video_raw.mp4 -i out/mix.m4a -filter_complex \
 "[0:v]colorbalance=rs=-0.02:bs=0.03:rh=0.035:gh=0.01:bh=-0.035,eq=contrast=1.04:saturation=0.97,vignette=angle=PI/5,noise=alls=3:allf=t,ass=subs.ass:fontsdir=fonts[v]" \
 -map "[v]" -map 1:a -c:v libx264 -preset medium -crf 20 -maxrate 10M -bufsize 20M -pix_fmt yuv420p -c:a copy -movflags +faststart -shortest \
 out/Stocked-and-Ready_Video12.mp4
echo FINALDONE
