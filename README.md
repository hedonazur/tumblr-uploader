#Uploader for Tumblr

Uploads pictures and text from a dropbox file to Tumblr using the console. 

##Requirements

* python wrapper [pytumblr](https://github.com/tumblr/pytumblr) v0.0.6
* pafy
* Python 2.7

##Usage

You need to add two paramenters to script `uploader.py`. For a text post it would be:

```shell
python uploader.py "title" "body of the text"
```
and for pictures:

```shell
python uploader.py "caption of foto" "foto.jpg"
```