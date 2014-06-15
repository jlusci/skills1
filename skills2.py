string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]
words_joined = " ".join(words)

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
	my_dict = {}
	my_list = string1.split()
	for word in my_list:
		if word in my_dict:
			my_dict[word] += 1
		else:
			my_dict[word] = 1
	return my_dict

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
	common_list=[]
	# for word in list1:
	# 	if word in list2:
	# 		common_list.append(word)

	# return common_list
	i = 0
	j = 0
	while i < len(list1):
		while j < len(list2):
			if list2[j] == list1[i]:
				common_list.append(list2[j])	
				# print common_list
			j += 1	
		# print list1[i]
		j = 0
		i += 1

	return common_list

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
	my_dict = {}
	my_list = []

	#works, but uses in!
	# for word in list1:
	# 	if word in my_dict:
	# 		my_dict[word] += 1
	# 	else:
	# 		my_dict[word] = 1

	# for word in list2:
	# 	if word in my_dict:
	# 		my_dict[word] += 1
	# 	else:
	# 		my_dict[word] = 1

	#doesn't work!
	# i = 0
	# j = 0
	# while i < len(list1):
	# 	while j < len(list2):
	# 		my_dict[list2[j]] += 1
	# 		j += 1
	# 	j = 0
	# 	i += 1

	# for word in my_dict:
	# 	if my_dict[word] >= 2:
	# 		my_list.append(word)

	return my_list			


"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
	my_list = []
	for i in range(len(list1)):
		for j in range(len(list1)):
			if list1[i] + list1[j] == 0:
				if (list1[i],list1[j]) in my_list:
					continue
				else:
					my_list.append((list1[i],list1[j]))

	return my_list



"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    pass

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    pass

"""
Here's a table of English to Pirate translations
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

def main():
	#first test
	# test1 = count_unique(string1)
	# print test1
	# testwords1 = count_unique(words_joined)
	# print testwords1

	#second test
	# common_list = common_items(list1,list2)
	# print common_list

	my_list = common_items2(list1,list2)
	print my_list

	my_list = sum_zero(list1)
	print my_list

if __name__ == '__main__':
	main()