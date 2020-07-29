# from pyspark import SparkConf,SparkContext
tweet="Hello #sports"
tweets=tweet.split()
print(tweets)           #output >> ['Hello', '#sports']
tweets=tweet.split('#')[-1] 
print(tweets) #output >>sports >>as -1 gets the last value in the list