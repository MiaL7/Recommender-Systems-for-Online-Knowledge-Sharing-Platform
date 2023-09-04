from recbole.quick_start import run_recbole
from recbole.config import Config
import pandas as pd
import os

import sys
import csv

csv.field_size_limit(sys.maxsize)

DATA_DIR = "/content/drive/Shareddrives/SI650_Final_Project/RecBole/dataset/ZhihuRec-1M"
DIR = "/content/drive/Shareddrives/SI650_Final_Project/RecBole"
SOURCE_DIR = "/content/drive/Shareddrives/SI650_Final_Project/ZhihuRec-1M"

user_col = ['userID', 'gender', 'n_followers',
                 'n_topics_followed', 'n_questions_followed', 'n_answers', 'n_questions',
                 'n_comments', 'n_thanks_recv', 'n_comments_recv', 'n_likes_recv',
                 'n_dislikes_recv', 'province']
item_col = ['answerID', 'is_anonymous', 'is_hi_val',
                'is_editor_recom', 'has_pic', 'has_vid', 'n_thanks',
                'n_likes', 'n_comments', 'n_collections', 'n_dislikes', 'n_reports',
                'n_helpless']
inter_col = ['userID', 'answerID', 'imp_ts',
       'is_clicked']

# test_df = pd.read_csv(os.path.join(SOURCE_DIR, "test-1M.csv"), index_col=0)
# inter_col = test_df.columns


if __name__ == '__main__':
  parameter_dict = {
    'data_path': "/content/drive/Shareddrives/SI650_Final_Project/RecBole/dataset",
    'load_col': {'inter': inter_col, 'item': item_col}, # ,'inter': inter_col 'user': user_col, 'item': item_col
    'USER_ID_FIELD': 'userID',
    'benchmark_filename': ['train', 'val', 'test'],
    'field_separator': ",",
    'ITEM_ID_FIELD': 'answerID',
    'RATING_FIELD': 'is_clicked',
    'LABEL_FIELD': 'is_clicked',
    'TIME_FIELD': 'imp_ts',
    'metrics': ["Recall","MRR","NDCG","Hit","Precision","MAP"] 
    # 'metrics': ["RMSE", "AUC"] 
  }

# run_recbole(dataset=dataset, model=model, config_file_list=config_file_list, config_dict=config_dict)
  run_recbole(dataset='ZhihuRec-1M', config_dict=parameter_dict)