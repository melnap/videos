# Downloads the V13 probe sentence from ElevenLabs and makes a +8 % tempo copy.
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$ff = Join-Path $here '..\..\..\tools\ffmpeg\bin\ffmpeg.exe'
$u = (Get-Content (Join-Path $here 'probe_url.txt') -Raw).Trim()
Invoke-WebRequest -Uri $u -OutFile (Join-Path $here 'probe_1.00.mp3') -UseBasicParsing
& $ff -hide_banner -loglevel error -y -i (Join-Path $here 'probe_1.00.mp3') -filter:a atempo=1.08 (Join-Path $here 'probe_1.08.mp3')
Remove-Item (Join-Path $here 'probe_url.txt')
Get-ChildItem (Join-Path $here 'probe_*.mp3') | Select-Object Name, Length
'PROBE DONE'
