from credentials import *
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import json


class listener(StreamListener):

    def on_data(self, data):

        try:
            parsed = json.loads(data)
            ID = parsed['id']
            list = []
            strID = str(parsed['user']['id'])

            if type(ID) == int:

                if strID in follow and parsed['id'] not in list:

                    # print(json.dumps(parsed, indent=4))
                    api.retweet(ID)
                    list.append(parsed['id'])

                # return(True)
            pass
        except Exception as identifier:
            print(identifier)

    def on_error(self, status):
        print(status)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

twitterStream = Stream(auth, listener())
follow = ['7557352', '3075666954', '69620713', '15296897', '2313837474', '17882258', '2320755170', '39801292',
          '1333467482', '928759224599040001', '902282851499917312', '2398137084', '499993648', '19407053', '17810254', '745273', '3108351', '105353526', '1033127171298975744', '34713362', '252751061', '19847181', '28571999', '1413027896', '361289499', '23374799', '43587624', '443292881', '2715646770', '2416349538', '443292881', '1248994556961587207', '1144984532', '816653', '49637104', '2890961', '275686563', '2347049341', '972651', '238174807', '1079768789582004224', '2361631088', '21328656', '20449296', '1636759074', '43775786', '56562803', '111988112', '1374131382', '1144984532', '970994516357472257']
twitterStream.filter(
    follow=follow)
