##  Aurthor: Yujia(BoBo) Wang
##  Date: 2017-09-06

##  Description:

This program takes the name of the folder containing the text files as an input parameter. It mainly consists of three parts: calculate the number of words and classify in a single text file; determine the sentiment and subjectivity of the text file; calculate the total number of words and unique words contained all text files.

In addition, there's a block to sort the dictionary by value.

##  Function:

def word_count(lines): Calculate the number of words and classify
parameter type: list
return: dictionary of words(key) and their number(value) in a single file,
        dictionary of words and their number in all files,
        total number of words in a single file

def sentiment_subjectivity(contents): Determine the sentiment and the subjectivity 
parameter type: string

def total_number(f_counts): Calculate the total number of words
parameter type: dictionary
return: total number of words