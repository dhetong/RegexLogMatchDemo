from pyspark import SparkContext, SparkConf

from RegexTransformer import Templates2Regex
from SparkRegexFilter import IsMatched
from templateCluster import ClusterTemplate, AdjustTmpRank

temple_df = ClusterTemplate('Templates/HDFS_5k.log_templates.csv')
template_list = temple_df["Templates"]

template_list_rank = AdjustTmpRank(template_list)

print(len(template_list_rank))

regex_list = []

for tmp in template_list_rank:
    regex = Templates2Regex(tmp)
    regex_list.append(regex)

sc = SparkContext.getOrCreate(SparkConf())
rddlog = sc.textFile('HDFS_unmatched.log')
warn_lines = rddlog.filter(lambda line: IsMatched(regex_list, line))
print(warn_lines.count())