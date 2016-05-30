import pandas as pd
import collections as cl
hn_s = pd.read_csv("hn_stories.csv")
hn_s.columns = ['submission_time','upvotes','url','headline']
url = hn_s['url'].value_counts()
domains = url[:99]
for name, row in domains.items():
    print("{0}: {1}".format(name, row))