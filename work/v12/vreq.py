import json,sys,assets_m as a
J=json.load(open('hf_jobs_img.json')); M={x[0]:x[4] for x in a.A if x[1]=='V'}
print(json.dumps([{'index':i,'params':{'model':'cinematic_studio_video_v2','duration':5,'aspect_ratio':'16:9','sound':'off','speedramp':'linear','declined_preset_id':'24bae836-2c4a-48e0-89b6-49fcc0b21612','prompt':M[k]+a.CALM,'medias':[{'value':J[k],'role':'image'}]}} for i,k in enumerate(sys.argv[1:])]))
