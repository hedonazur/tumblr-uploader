import pytumblr
import sys
from tumblr_keys import consumer_key
from tumblr_keys import consumer_secret
from tumblr_keys import token_key
from tumblr_keys import token_secret 

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)
print (sys.argv)
titulo= sys.argv[1]
cuerpofoto=sys.argv[2]

if cuerpofoto.endswith(".jpg"):
	resultado= client.create_photo('perunalainen', state="published", data="/home/carol/uploader/"+ cuerpofoto, caption=titulo)
else:
	resultado= client.create_text("perunalainen", state="published", slug="testing-text-posts", title=titulo, body=cuerpofoto)

	
#Posts an image to your tumblr.
#Make sure you point an image in your hard drive. Here, 'image.jpg' must be in the 
#same folder where your script is saved.
#From yourBlogName.tumblr.com should just use 'yourBlogName'
#The default state is set to "queue", to publish use "published"
print (resultado)
