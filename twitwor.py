import tweepy
import twitworConfig

#  To use this script, you need to create a twitworConfig.py file with the following variables:
#  bearerToken = "your bearer token"
auth = tweepy.Client(twitworConfig.bearerToken)

search = str(input("Tulis username sini ngab >> "))
total = int(input("Berapa jumlah tweet yang mau diambil? [10-100] >> "))

try:
    user = auth.get_user(username=search)
    tweet = auth.get_users_tweets(id=user.data.id, max_results=total)
    print(f"mengambil {total} tweets from {user.data.name} \n")
    cnt = 1
    for xz in tweet.data:
        print("---------------------------------------------")
        print(f"Tweet ke-{cnt} ::\n {xz.text}\n")
        cnt += 1
    print("---------------------------------------------")
    
except BaseException as e:
    print('Status Failed On,',str(e))