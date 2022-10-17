import tweepy
import twitworConfig

# DONT DELETE ALL CODE ABOVE :3

auth = tweepy.Client(twitworConfig.bearer)

search = str(input("Tulis username sini ngab >> "))
# search = "vestiazeta"
# total = 10
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