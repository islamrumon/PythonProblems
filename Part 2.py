# Function that takes a sequence of numbers and determines if all are different from each othe

def test_distinct(data):
    if len(data) == len(set(data)):
        print(len(data))
        print(len(set(data)))
        return True
    else:
        print(len(data))
        print(len(set(data)))
        return False;
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))


# Create all possible strings by using a, e, i, o, u

import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))


# Remove and print every third number from a list of numbers until the list becomes empty
def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)



numbers = []
for num in range(1000):
  num=str(num).zfill(3)
print(num)
numbers.append(num)


string_words = '''United States Declaration of Independence
From Wikipedia, the free encyclopedia
The United States Declaration of Independence is the statement
adopted by the Second Continental Congress meeting at the Pennsylvania State
House (Independence Hall) in Philadelphia on July 4, 1776, which announced
that the thirteen American colonies, then at war with the Kingdom of Great
Britain, regarded themselves as thirteen independent sovereign states, no longer
under British rule. These states would found a new nation – the United States of
America. John Adams was a leader in pushing for independence, which was passed
on July 2 with no opposing vote cast. A committee of five had already drafted the
formal declaration, to be ready when Congress voted on independence.

John Adams persuaded the committee to select Thomas Jefferson to compose the original
draft of the document, which Congress would edit to produce the final version.
The Declaration was ultimately a formal explanation of why Congress had voted on July
2 to declare independence from Great Britain, more than a year after the outbreak of
the American Revolutionary War. The next day, Adams wrote to his wife Abigail: "The
Second Day of July 1776, will be the most memorable Epocha, in the History of America."
But Independence Day is actually celebrated on July 4, the date that the Declaration of
Independence was approved.

After ratifying the text on July 4, Congress issued the Declaration of Independence in
several forms. It was initially published as the printed Dunlap broadside that was widely
distributed and read to the public. The source copy used for this printing has been lost,
and may have been a copy in Thomas Jefferson's hand.[5] Jefferson's original draft, complete
with changes made by John Adams and Benjamin Franklin, and Jefferson's notes of changes made
by Congress, are preserved at the Library of Congress. The best-known version of the Declaration
is a signed copy that is displayed at the National Archives in Washington, D.C., and which is
popularly regarded as the official document. This engrossed copy was ordered by Congress on
July 19 and signed primarily on August 2.

The sources and interpretation of the Declaration have been the subject of much scholarly inquiry.
The Declaration justified the independence of the United States by listing colonial grievances against
King George III, and by asserting certain natural and legal rights, including a right of revolution.
Having served its original purpose in announcing independence, references to the text of the
Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
(as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
on human rights, particularly its second sentence:

We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.

This has been called "one of the best-known sentences in the English language", containing "the most potent
and consequential words in American history". The passage came to represent a moral standard to which
the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
through which the United States Constitution should be interpreted.

The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
(modern-day Belgium). It also served as the primary model for numerous declarations of independence across
Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
19th century.'''

word_list = string_words.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))



# Get the top stories from Google news

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)