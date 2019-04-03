from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("ml-100k/u.data")
# Each line is read as a string, thus, we need to split it and take the val we need
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
print(result)
for key, value in sortedResults.items():
    print("%s %i" % (key, value))
