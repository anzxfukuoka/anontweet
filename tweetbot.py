import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)



def sendtweet(msg):
    try:
        api.update_status(msg)
        return "отправлен твит: \n " + msg
    except tweepy.TweepError as e:
        return "error: " + e.reason

botname = "@penayongbumi "
max = 280 - len(botname)

def startthread(txt):
    thread = []

    while 1:
        if len(txt) > max:
            thread.append(txt[:max])
            txt = txt[max:]
        else:
            thread.append(txt)
            break

    last_tweet = api.update_status(thread[0])
    thread.pop(0)

    try:
        for t in thread:
            print(t)
            last_tweet = api.update_status(botname + t, last_tweet.id)
            #last_tweet = api.user_timeline(screen_name='penayongbumi', count=1, trimuser=1)
    except tweepy.TweepError as e:
        return "error: " + e.reason

    return "отправлена ветка твитов: \n " + "..." + thread.pop()



def sendmsgtouser(user,msg):
    api.send_direct_message(screen_name=user, text=msg)
    return "отправленo сообщение пользоватнлю " + user + ": \n " + msg

def follow_all():
    for follower in tweepy.Cursor(api.followers).items():
        print(follower.screen_name)
        follower.follow()


def like_replys():
    for result in api.search(q="@penayongbumi", count=100):
            print(str(result.id) + " [" + result.user.name + "]: " +  result.text)
            try:
                api.create_favorite(result.id)
            except:
                pass
