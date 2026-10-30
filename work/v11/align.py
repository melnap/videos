"""Merge the 3 Scribe word lists (offsets from vo/ concat), map onto exact script words -> words_cap.json, sent.json"""
import json,re,difflib,subprocess,numpy as np
def pcm(f,ss,t):
    b=subprocess.check_output(['ffmpeg','-v','error','-ss',str(ss),'-t',str(t),'-i',f,'-ac','1','-ar','8000','-f','s16le','-'])
    return np.frombuffer(b,np.int16).astype(float)
# nominal offsets, then refine by cross-correlation against vo.mp3
d=[float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'vo/p{i}.mp3'])) for i in (1,2,3)]
OFF=[0.0,d[0]+0.6,d[0]+d[1]+1.2]
for i in (1,2):
    a=pcm(f'vo/p{i+1}.mp3',1,6); b=pcm('vo.mp3',OFF[i]+1-0.5,7)
    c=np.correlate(b,a,'valid'); lag=(np.argmax(c))/8000-0.5; OFF[i]+=lag; print('part',i+1,'lag',round(lag,3))
W=[]
for i in (1,2,3):
    for x in json.load(open(f'asr/w{i}.json'))['words']:
        if x['type']=='word': W.append(dict(w=x['text'],s=round(x['start']+OFF[i-1],3),e=round(x['end']+OFF[i-1],3)))
T=open('script.txt').read().split()
norm=lambda s:re.sub(r'[^a-z0-9]','',s.lower())
sm=difflib.SequenceMatcher(None,[norm(x) for x in T],[norm(x['w']) for x in W],autojunk=False)
out=[None]*len(T)
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag=='equal':
        for k in range(i2-i1): out[i1+k]=dict(w=T[i1+k],s=W[j1+k]['s'],e=W[j1+k]['e'])
    else:
        print(tag,T[i1:i2],[x['w'] for x in W[j1:j2]])
        if j2>j1:
            s,e=W[j1]['s'],W[j2-1]['e']; n=i2-i1
            for k in range(n): out[i1+k]=dict(w=T[i1+k],s=round(s+(e-s)*k/n,3),e=round(s+(e-s)*(k+1)/n,3))
for k in range(len(out)):  # fill gaps by interpolation
    if out[k] is None:
        p=out[k-1]; out[k]=dict(w=T[k],s=p['e'],e=p['e']+0.2)
json.dump(out,open('words_cap.json','w'))
S=[];w0=0
for k,x in enumerate(out):
    if re.search(r'[.!?]["”]?$',x['w']):
        S.append(dict(i=len(S),w0=w0,w1=k+1,s=out[w0]['s'],e=x['e'],t=' '.join(y['w'] for y in out[w0:k+1]))); w0=k+1
json.dump(S,open('sent.json','w'),indent=0)
print(len(out),'words',len(S),'sentences, last end',out[-1]['e'])
