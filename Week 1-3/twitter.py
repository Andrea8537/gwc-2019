'''
In this program, we print out all the text data from our twitter JSON file.

Please explain the comments to students as you code.
'''

from wordcloud import WordCloud
import json
from textblob import TextBlob
import matplotlib.pyplot as plt

# # # Next we want to open the JSON file. We tag this file as
# # "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
#
texts = [] # creating empty list
#
for i in range(0,len(tweetData)):
	texts.append(tweetData[i]["text"])

#countLetter(tweetstring, "a")

def wordCount(stringOfTweet, string1):
	counter=0
	string1=string1.lower()
	wordList = stringOfTweet.split(" ")
	for item in wordList:
		if item == string1:
			counter += 1
	return counter

wordCountList=[]
for item in texts:
	wordoccurrence = wordCount(item, "the")
	wordCountList.append(wordoccurrence)
print(wordCountList)
print(min(wordCountList), max(wordCountList))
plt.hist(wordCountList)
plt.axis([min(wordCountList), max(wordCountList), 0, 10])
plt.show()


def countLetter(string, letter):
	counter=0
	for let in string:
		if let.lower() == letter:
			counter+= 1
		else:
			counter+=0
	return counter

# print(countLetter("A"*8,"a"))


tweetstring =""
for tweet in texts:
	tweetstring += tweet+" "
	#tweetstring = tweetstring + tweet + " "
# print(tweetstring)

countLetter(tweetstring, "a")
alpha = "qwertyuiopasdfghjklzxcvbnm"
letters =set(sorted(alpha))
print(len(letters))


for letter in letters:
	print (f"letter:{letter} occurrences:{countLetter(tweetstring, letter)}")

occurrences=[]
for letter in letters:
	occurrences.append(countLetter(tweetstring, letter))
	# print (f"letter:{letter} occurences:{countLetter(tweetstring, letter)}")

print(occurrences)
print(min(occurrences), max(occurrences))
plt.hist(occurrences)
plt.axis([min(occurrences), max(occurrences), 0, 10])
plt.show()

#tb=TextBlob("You are a brilliant computer scientists")



wordcloud = WordCloud(height=1000, width=1000).generate(tweetstring)
plt. figure(figsize= (10,10), facecolor= None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('alischart.png')


#histogram
polarity_list=[]
for item in texts:
	blob1=TextBlob(item)
	polar1=blob1.polarity
	polarity_list.append(polar1)
print(polarity_list)


print(polarity_list)
print(min(polarity_list), max(polarity_list))
n, bins, patches=plt.hist(polarity_list)
plt.axis([-0.55, 1.05, 0, 50])
#plt.grid(True)
plt.show()

n, bins, patches = plt.hist(polarity_list, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
# # tb=TextBlob("You are a brilliant computer scientists")
# # print (tb.polarity)
# # print(type(tweetData))
# # print((tweetData[0]))
# #
# #s
# #
# # # print(list(tweetData[0]))
# # print(tweetData["favorite_count"])
# #
# # sum=0
# # num=0
# # for i in range(len(tweetdata)):
# # 	tweet=tweetData[i]
# # 	if["favorite_count"] not in tweet:
# # 		# print(len(tweet.keys()))
# # 		# print(tweet.keys())
# 	else:
# 		# print("this is working")
# 		num+=1
# 		sum+=tweetData[i]["favorite count"]
# avg=sum/num
# # print("Here is avg")
# print(avg)
#


# print(texts)
# print(texts[0])

# polarity_list=[]
# for item in texts:
# 	blob1=TextBlob(item)
# 	polar1=blob1.polarity
# 	polarity_list.append(polar1)
# print(polarity_list)
#
# least=[]
for i in range(len(tweetData)):
	dictionary={}
	dictionary["id"]=tweetData[i]["id"]
	dictionary["polarity"]=polarityList[i]
	dictionary["tweet"]=tweetList[i]
	least.append(dictionary)
# # print(least)
# #









# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
#
# # Encourage students to think about how there are
# # often multiple solutions for each problem, and
# # how each solution might have strenghts and drawbacks.
