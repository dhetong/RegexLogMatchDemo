from templateCluster import ClusterTemplate
from RegexTransformer import RegexMatch
from templateCluster import AdjustTmpRank
from ContentExtractor import ContentExtractor
from RegexTransformer import Templates2Regex

import csv
import pandas as pd

HDFS_part_num = 56

temple_df = ClusterTemplate('Templates/HDFS_templates.csv')
template_list = temple_df["Templates"]

template_list_rank = AdjustTmpRank(template_list)

for tmp in template_list_rank:
    regex = Templates2Regex(tmp)
    print(regex)

n_match = 0

# for f_index in range(HDFS_part_num):
#     matched_file = 'Datasets/HDFS.log.part' + str(f_index)
#     print(matched_file)
#
#     unmatchedlogs = RegexMatch(template_list_rank, matched_file)
#     unmatchedata = pd.DataFrame({"Unmathed logs": unmatchedlogs})
#     unmatchedata.to_csv('Results/HDFS_unmatched.part' + str(f_index) + '.csv')


unmatchedlogs = RegexMatch(template_list_rank,'HDFS_unmatched_1.log')

#unmatchedcontent = ContentExtractor(unmatchedlogs)
unmatchedata = pd.DataFrame({"Unmathed logs" : unmatchedlogs})
unmatchedata.to_csv("HDFS_unmatched.csv")


# template = ""
# tmp_new = Templates2Regex(template)
# print(tmp_new)
# RegexMatch(tmp_new, 'Templates/Hadoop_sample0.log')