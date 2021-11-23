Python Version - 3.9.5
Spark Version - 3.1.2

We created a SparkContext to connect connect the Driver that runs locally.

sc = SparkContext("local","PySpark Word Count Exmaple")

Next, we read the input text file using SparkContext variable and created a flatmap of words. words is of type PythonRDD.

words = sc.textFile("WordCountVideo(Hadoop directory)input.txt").flatMap(lambda line: line.split(" "))

we have split the words using single space as separator.

Then we will map each word to a key:value pair of word:1, 1 being the number of occurrences.

words.map(lambda word: (word, 1))

The result is then reduced by key, which is the word, and the values are added.

reduceByKey(lambda a,b:a +b)

The result is saved to a text file.

wordCounts.saveAsTextFile("spark(Hadoop Directory)/output/")

