import json
import feedparser
import pandas as pd

with open("rss.json") as json_data_file:
    data = json.load(json_data_file)

df = pd.DataFrame()
num_of_entries = 0
for link in data['links']:
    d = feedparser.parse(link)
    num_of_entries += len(d.entries)
    df = df.append(pd.DataFrame(d.entries), ignore_index=True)

with open("output.json", 'w') as outfile:
    df.to_json(outfile, orient="records")
