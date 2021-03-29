import json
import requests
from elasticsearch import Elasticsearch

# Display page 'http://localhost:9200' content.
# Just unnecessary information, no longer used.
res = requests.get('http://localhost:9200')
print(res.json())

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

# open the file with outputs and read it
f = open("output_Lab2.json")
data = f.read()

i = 1
# Send the data into es
for body in json.loads(data):
    es.index(index='Yarosav', id=i, body=body, ignore=400)

    i += 1
