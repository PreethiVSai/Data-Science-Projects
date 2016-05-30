import pandas as pd


def load_data():
    hn_stories = pd.read_csv("/home/dq/scripts/hn_stories.csv")
    hn_stories.columns = ['submission_time','upvotes','url','headline']
    return hn_stories


    
    