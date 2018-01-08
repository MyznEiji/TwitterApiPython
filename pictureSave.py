import sys
import tweepy as tp
import urllib.request
import os
import config

CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_SECRET = config.ACCESS_TOKEN_SECRET
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tp.API(auth)


# バリューにアカウントのurl
account_names = {
    # "mimura": "mimu_vo"
    # "iwahashi": "mikichosuuuuuuu"
    # "mirin": "FurukawaMirin",
    # "risa": "RISA_memesama",
    # "nemu": "yumeminemu",
    # "ei": "eitaso",
    # "moga": "mogatanpe",
    # "pinky": "PINKY_neko"
    }

for name, twi_id in account_names.items():
    maxid = api.user_timeline(twi_id).max_id
    # ディレクトリ作成
    # if os.path.exists("./twitter-images/" + name) == False:
    #     os.makedirs("./twitter-images/" + name)
    for l in range(16):
        for twi in api.user_timeline(twi_id, count=200, max_id=maxid):
            if hasattr(twi, "extended_entities"):
                if "media" in twi.extended_entities:
                    for index, media in enumerate(twi.extended_entities["media"]):
                        img_url = media["media_url_https"]
                        print(name + " image " + str(img_url) +
                              " save to ./twitter-images/" + name)
                        # with urllib.request.urlopen(img_url) as url:
                        #     img = url
                        #     tmp_path = open("./dempa-images/" + name +
                        #                     "/" + os.path.basename(img_url), "wb")
                        # tmp_path.write(img.read())
                        # img.close()
                        # tmp_path.close()
            maxid = twi.id

num = 1
print("hoge"+str(num))
