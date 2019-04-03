from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("Assigment1")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    id = int(fields[0])
    price = float(fields[2])
    return (id, price)

orders = sc.textFile("customer-orders.csv")

prices = orders.map(parseLine)

sum = prices.reduceByKey(lambda x, y: x + y).map(lambda x: (x[1], x[0])).sortByKey()

results = sum.collect()

for result in results:
    print(str(result[0]) + "\t" + str(result[1]))
