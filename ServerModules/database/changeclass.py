import csv
with open ('twitter-suicidal_data.csv', 'r') as fh:
    w = csv.DictReader(fh)
    up_dt = []
    for r in w:
        if r['intention'] == '1':
            r['intention'] = "suicide"
        elif r['intention'] == '0':
            r['intention'] = "non-suicide"

        row = {'text': r['tweet'],
               'class': r['intention']}
        up_dt.append(row)

headers = ['text', 'class']
with open("twitter_dataset.csv", 'w') as fh:
    w = csv.DictWriter(fh, fieldnames= headers)
    w.writerow(dict((h, h)for h in headers))
    w.writerows(up_dt)