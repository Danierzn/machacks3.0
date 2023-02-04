from twitter_scraper import get_tweets
import csv



user = input("Enter your User: ")

data = get_tweets(f'{user}', pages = 1)
dict_data = dict()
i = 0

for tweet in data:
    dict_data[i] = tweet['text'] 
    i+=1

csv_columns = dict_data.keys()

csv = f"{user}.csv"
with open(csv, 'w') as fh:
    w = csv.DictWriter(fh, fieldnames = csv_columns)
    w.writeheader()

    for j in dict_data:
        w.writerow(j)