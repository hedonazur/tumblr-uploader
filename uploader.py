import pytumblr
import pafy
import sys
import json
from tumblr_keys import consumer_key
from tumblr_keys import consumer_secret
from tumblr_keys import token_key
from tumblr_keys import token_secret
from tumblr_keys import youtube_key

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

print (sys.argv)
titulo = sys.argv[1]
cuerpofoto = sys.argv[2]

if titulo == "sync" and cuerpofoto == "videos":
    # videos

    videos = client.posts("perunalainen", type="video", limit=20)
    videos_list = videos['posts']
    last_10 = []
    for video in videos_list:
        last_10.append(video["permalink_url"][-11:])

    pafy.set_api_key(youtube_key)
    v = "https://www.youtube.com/playlist?list=PL7rxKO9f1bIguuo1dPQRFu7bIr3eqFcij"
    playlist = pafy.get_playlist(v)
    tot = len(playlist['items'])
    count = 0
    ids = []
    while count < tot:
        objeto = playlist['items'][count]['playlist_meta']['encrypted_id']
        ids.append(objeto)
        count = count + 1

    for v in ids:
        if v in last_10:
            print "all sync"
        else:
            client.create_video('perunalainen', embed="https://www.youtube.com/watch?v="+v)

elif cuerpofoto.endswith(".jpg"):
    resultado = client.create_photo('perunalainen', state="published", data="/home/carol/Dropbox/tumblr/" + cuerpofoto, caption=titulo)
    print (resultado)

else:
    resultado = client.create_text("perunalainen", state="published", slug="testing-text-posts", title=titulo, body=cuerpofoto)
    print (resultado)
