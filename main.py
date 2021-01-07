import praw
import requests
import random
from wallpaper import set_wallpaper
import threading
image=[]
reddit = praw.Reddit(client_id = 'PhST7A4huxJkjQ', 
                    client_secret = 'T1dyyvg6VChuqOH2vxQZmudIeRKOpA', 
                    user_agent = 'Meme Bot')
def wall():
    subreddit =reddit.subreddit('CityPorn') 
    posts = subreddit.hot(limit=50)
    for post in posts:
        mem= post.url.encode('utf-8')
        image.append(mem)
    num= random.randint(1,200)
    val="wall"+str(num)+str(random.randint(1,200))+str(random.randint(1,200))
    memes= random.choice(image)
    meme= requests.get(memes).content
    open(r"{}.jpg".format(val), 'wb').write(meme)
    set_wallpaper(r"{}.jpg".format(val))
    print("done")
    t= threading.Timer(300,wall)
    t.start()
wall()
