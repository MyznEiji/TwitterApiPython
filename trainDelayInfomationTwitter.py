import config
import tweepy
import codecs
import datetime
from time import sleep


# キーをセット
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

# APIインスタンスを作成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 検索内容
keywords = ["遅延", "遅れ"]
query = ' OR '.join(keywords)

# 鉄道路線遅延情報クラス


class Train:
    def __init__(self, name, word):
        self.name = name
        self.word = word
        self.count = 0
        self.tweeted = False

    def update(self, tweets):
        """検索単語出現回数をカウントする"""
        self.count = sum(self.word in line for line in tweets)
        print("{0.name}：{0.count} counts".format(self))

    def tweet(self, now):
        """遅延ツイートが5個位上あれば遅延情報をツイートする"""
        if self.count > 5 and not self.tweeted:
            message = "{now.hour}時{now.minute}分情報取得 {self.word}遅延の可能性".format(
                **locals())
            api.update_status(status=message)
            self.tweeted = True
        else:
            self.tweeted = False


# 各鉄道路線
trains = (
    Train("田園都市線　　", "田都"),
    Train("東横線　　　　", "東横"),
    Train("大井町線　　　", "大井"),
    Train("目黒線　　　　", "目黒"),
    Train("半蔵門線　　　", "半蔵門"),
    Train("東武伊勢崎線　", "東武スカイツリー"),
    Train("副都心線　　　", "副都心"),
    Train("東武東上線　　", "東上"),
    Train("西武池袋線　　", "西武池袋"),
    Train("都営三田線　　", "三田"),)

while 1:
    print("--------------------------------------------------------------------------------")
    # 現在時刻の取得
    now = datetime.datetime.today()

    # 現在時刻の表示
    print("{0.hour}時{0.minute}分{0.second}秒情報取得".format(now))

    # 検索単語についての直近ツイートを100個取得
    tweets = [tweet.text for tweet in api.search(q=query, count=100)]

    # 路線毎にツイート内容を確認し、遅延情報をツイート
    for train in trains:
        train.update(tweets)
        train.tweet(now)

    print("--------------------------------------------------------------------------------")
    sleep(300)
print("finish.")
