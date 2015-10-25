#Uploader for Tumblr

Uploads to Tumblr videos, text and photos using the console. Videos are uploaded from a playlist in youtube and
pictures  from a file in your computer.

##Usage

Add two paramenters to script `uploader.py`.

For a text post it would be:

```shell
python uploader.py "title" "body of the text"
```

For pictures:

```shell
python uploader.py "caption of foto" "foto.jpg"
```
For videos:

```shell
python uploader.py "sync" "videos"
```

It will compare the permalinks of the youtube playlist with the permalinks of the videos post and create 
a new video post if needed. 


