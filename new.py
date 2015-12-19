import tweepy
import csv

access_token = "2885728704-AKdFf5yzVjyhXnVumdzniULLEBAabCCO9N3Z0cw"
access_token_secret = "BrqkdxS8eTaHWDSKSfTqEd5J2BCcA8MG3DRrKMP5nOT0S"
consumer_key = "Hzqk2Y0aE9VcADR1OpK4WCFjO"
consumer_secret = "N4MkVtQnAjZua0tMda1NyTVvuDHsBla1aTtlHpclSwqrVEo0wl"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('yoyo.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="#analytics#machinelearning",count=100,\
                           lang="en",\
                           since_id=2015-12-16).items():
    #print tweet.created_at, tweet.text
    print tweet	
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
