"""PUT the files listed in heygen_batch.json to HeyGen's presigned S3 URLs (only network target: heygen-resources-prod S3)."""
import json, pathlib, sys, urllib.request

HERE = pathlib.Path(__file__).parent
B = json.loads((HERE / (sys.argv[1] if len(sys.argv) > 1 else 'heygen_batch.json')).read_text())
for it in B['items']:
    data = (HERE / 'media' / 'th' / it['file']).read_bytes()
    req = urllib.request.Request(it['url'], data=data, method='PUT', headers={
        'content-type': it['ct'], 'x-amz-checksum-sha256': it['sha'], 'x-amz-server-side-encryption': 'AES256'})
    with urllib.request.urlopen(req) as r:
        print(it['file'], r.status)
print('UPLOAD DONE')
