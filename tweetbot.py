import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

def sendtweet(msg):
    try:
        api.update_status(msg)
        return "отправлен твит: \n " + msg
    except tweepy.TweepError as e:
        return "error: " + e.reason

def sendmsgtouser(user,msg):
    api.send_direct_message(screen_name=user, text=msg)
    return "отправленo сообщение пользоватнлю " + user + ": \n " + msg
