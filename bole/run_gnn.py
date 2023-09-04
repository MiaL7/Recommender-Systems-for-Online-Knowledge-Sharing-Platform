import argparse

import sys
sys.path.append("/content/drive/Shareddrives/SI650_Final_Project/RecBole-GNN-main")

from recbole_gnn.quick_start import run_recbole_gnn
import pandas as pd
import os

import sys
import csv

csv.field_size_limit(sys.maxsize)

DATA_DIR = "/content/drive/Shareddrives/SI650_Final_Project/RecBole/dataset/ZhihuRec-1M"
DIR = "/content/drive/Shareddrives/SI650_Final_Project/RecBole"
SOURCE_DIR = "/content/drive/Shareddrives/SI650_Final_Project/ZhihuRec-1M"

# user_col = ['userID', 'gender', 'n_followers',
#                  'n_topics_followed', 'n_questions_followed', 'n_answers', 'n_questions',
#                  'n_comments', 'n_thanks_recv', 'n_comments_recv', 'n_likes_recv',
#                  'n_dislikes_recv', 'province']
# item_col = ['answerID', 'is_anonymous', 'is_hi_val',
#                 'is_editor_recom', 'has_pic', 'has_vid', 'n_thanks',
#                 'n_likes', 'n_comments', 'n_collections', 'n_dislikes', 'n_reports',
#                 'n_helpless']
inter_col = ['userID', 'answerID', 'imp_ts',
       'is_clicked']

# test_df = pd.read_csv(os.path.join(SOURCE_DIR, "test-1M.csv"), index_col=0)
# inter_col = test_df.columns


if __name__ == '__main__':
  parameter_dict = {
    'data_path': "/content/drive/Shareddrives/SI650_Final_Project/RecBole/dataset",
    'load_col': {'inter': inter_col, 'net': ['user1', 'user2']}, # ,'inter': inter_col 'user': user_col, 'item': item_col
    'USER_ID_FIELD': 'userID',
    'benchmark_filename': ['train', 'val', 'test'],
    'field_separator': ",",
    'ITEM_ID_FIELD': 'answerID',
    'RATING_FIELD': 'is_clicked',
    'LABEL_FIELD': 'is_clicked',
    'TIME_FIELD': 'imp_ts',
    # social network config
    'NET_SOURCE_ID_FIELD': 'user1',
    'NET_TARGET_ID_FIELD': 'user2',
    #'NET_WEIGHT_FIELD': 'n_common_topics',
    'filter_net_by_inter': True,
    'undirected_net': True,

    'metrics': ["Recall","MRR","NDCG","Hit","Precision","MAP"] 
    # 'metrics': ["RMSE", "AUC"] 
  }

  parser = argparse.ArgumentParser()
  parser.add_argument('--model', '-m', type=str, default='BPR', help='name of models')

  args, _ = parser.parse_known_args()

# run_recbole(dataset=dataset, model=model, config_file_list=config_file_list, config_dict=config_dict)
run_recbole_gnn(model=args.model, dataset='ZhihuRec-1M', config_dict=parameter_dict)