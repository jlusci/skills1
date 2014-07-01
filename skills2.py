import operator

string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]
words_joined = " ".join(words)

"""
1 - Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
	my_dict = {}
	my_list = string1.split()
	for word in my_list:
		my_dict[word] = my_dict.get(word,0) + 1
	return my_dict

"""
2 - Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
	common_list=[]

	#**************************************************
	# works, but uses keyword 'in' as part of solution
	# for word in list1:
	# 	if word in list2:
	# 		common_list.append(word)

	# return common_list

	#**************************************************
	# try using while loops and lists to avoid using 'in'?
	i = 0
	j = 0

	while i < len(list1):
		while j < len(list2):
			if list2[j] == list1[i]:
				common_list.append(list2[j])
			j += 1	
		
		j = 0
		i += 1

	new_list = list(set(common_list))

	return new_list

"""
3 - Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
	my_dict = {}
	my_list = []

#**********************************************
#Use dictionaries with counters 
#**********************************************
	# for item in list1:
	# 	if my_dict.get(item,0) == 0:
	# 		my_dict[item] = my_dict.get(item,0) + 1

	# for item in list2:
	# 	my_dict[item] = my_dict.get(item,0) + 1

#*****************************************************
#Use dictionaries with while loops to avoid using 'in'
#*****************************************************
	# i = 0
	# j = 0
	# while i < len(list1):
	# 	while j < len(list2):
	# 		if list1[i] == list2[j]:
	# 			key = list2[j]
	# 			my_dict[key] = my_dict.get(key,0) + 1
	# 		j += 1
	# 	j = 0
	# 	i += 1

	# for key in my_dict:
	# 	if my_dict[key] > 1:
	# 		my_list.append(key)
#***************************************************
#Now try without a counter - 'in' is okay in for loop
#***************************************************
	for item in list1:
		my_dict[item] = True

	for item in list2:
		if my_dict.get(item) == True:
			my_list.append(item)


	return my_list

"""
4 - Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
	
	my_list = []
	for i in range(len(list1)):
		for j in range(i,len(list1)):
			if list1[i] + list1[j] == 0:
				my_list.append((list1[i],list1[j]))

	return my_list

"""
5 - Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	my_dict = {}
	my_list = []
	for word in words:
		my_dict[word] = my_dict.get(word,0) + 1

	for key in my_dict:
		if my_dict[key] == 1:
			my_list.append(key)

	return my_list

"""
6 - Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    my_dict = {}
    for index in range(len(words)):
    	value = len(words[index])
    	my_dict[words[index]] = value
    	sorted_list = sorted(my_dict, key = my_dict.get)
    return sorted_list

"""
7 - Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
def pirate_trans(text):
	pirate_dict = {}
	word_list = []
	trans = open("pirate.txt")

	for line in trans:
		line = line.rstrip()
		line = line.split(',')
		word_list.extend(line)

	for i in range(0,len(word_list),2):
		key = word_list[i]
		value = word_list[i+1]
		pirate_dict[key] = value

	intext = text.split()
	outtext = []
	for word in intext:
		if pirate_dict.get(word):
			outtext.append(pirate_dict.get(word))
		else:
			outtext.append(word)

	print " ".join(outtext)


def main():
	#first test
	# test1 = count_unique(string1)
	# print test1
	# testwords1 = count_unique(words_joined)
	# print testwords1

	#second test
	common_list = common_items(list1,list2)
	print common_list

	#third test
	my_list = common_items2(list1,list2)
	print my_list

	#fourth test
	my_list = sum_zero(list1)
	print my_list

	#fifth test
	my_dict = find_duplicates(words)
	print my_dict

	#sixth test
	my_list = word_length(words)
	print my_list

	my_list = pirate_trans("This is my translator, man. What is your problem, madam")

if __name__ == '__main__':
	main()