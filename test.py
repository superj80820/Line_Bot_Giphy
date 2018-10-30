import moviepy.editor as mp
import json
import requests
import random, string

name = ''.join(random.choice(string.ascii_letters) for x in range(10))

resp = requests.get("http://api.giphy.com/v1/gifs/search?api_key=V5pYPSB0TKF00sZUnt7feN8cjbikI1UF&limit=1&q=%s" %('cat'))
resp_json = resp.json()

with open('%s.gif' %name, 'wb') as f:
    f.write(requests.get(resp_json['data'][0]['images']['fixed_height_still']['url']).content)
clip = mp.VideoFileClip("%s.gif" %name)
clip.write_videofile("%s.mp4" %name)
