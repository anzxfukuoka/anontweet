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
