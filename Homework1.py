from textblob import TextBlob
import string
import os
import math

def word_count(lines):  # Calculate the number of words and classify
	counts = dict()
	total_words = 0
	for line in lines:
		line = line.translate(None, string.punctuation)
		line = line.lower()
		words = line.split()
		total_words = total_words + len(words)
		for word in words:
			if word not in counts:
				counts[word] = 1
			else:
				counts[word] += 1
			if word not in f_counts:
				f_counts[word] = 1
			else:
				f_counts[word] += 1
	total_words = float(total_words)
	return counts, f_counts, total_words

def sentiment_subjectivity(contents):  # Determine the sentiment and the subjectivity 
	analysis = TextBlob(contents)
	result = analysis.sentiment
	# Sentiment
	if result[0] >= 0.5:
		term_sentiment = "STRONGLY POSITIVE"
	elif result[0] >= 0 and result[0] < 0.5:
		term_sentiment = "MILDLY POSTIVE"
	elif result[0] >= -0.5 and result[0] < 0:
		term_sentiment = "MILDLY NEGTIVE"
	else:
		term_sentiment = "STRONGLY NEGTIVE"
	print "Sentiment is %s (%s)" % (term_sentiment, str(result[0]))
	# Subjectivity
	if result[1] >= 0.75:
		term_subjectivity = "STRONGLY SUBJECTIVE"
	elif result[1] >= 0.5 and result[1] < 0.75:
		term_subjectivity = "MILDLY SUBJECTIVE"
	elif result[1] >= 0.25 and result[1] < 0.5:
		term_subjectivity = "MILDLY OBJECTIVE"
	else:
		term_subjectivity = "STRONGLY OBJECTIVE"
	print "Subjectivity is %s (%s)" % (term_subjectivity, str(result[1]))

def total_number(f_counts):  # Calculate the total number of words
	f_total_words = 0
	for f_key in f_counts:
		f_total_words = f_total_words + f_counts[f_key]
	return f_total_words

f_counts = dict()
try:
	foldername = raw_input("Enter a foldername: ")
	filelist = os.listdir(foldername)
	for filename in filelist:
		if filename.endswith('.txt'):
			thefile = foldername + "/" + filename
			file = open(thefile, "r")
			lines = file.readlines()

			(counts, f_counts, total_words) = word_count(lines)
			
			# Sort the dictionary by value
			lst = list()
			for key, val in counts.items():
				lst.append( (val, key) )
			lst.sort(reverse=True)
			print "File: ", filename
			for val, key in lst[:]:
				percentage = val / total_words
				percentage = "%.2f%%" % (percentage * 100)
				print "%s: %d (%s of total words)" % (key, val, percentage)
            
            # Read again
			file.seek(0)
			contents = file.read()
			file.close()

			sentiment_subjectivity(contents)
			print "\n"

	f_total_words = total_number(f_counts)
	print "Document corpus contains %s total words (%s unique words)" % (f_total_words, len(f_counts))	
except:
	print "No such folder!"

						

