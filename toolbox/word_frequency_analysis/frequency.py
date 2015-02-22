""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
import re
from collections import Counter

def turn_line_into_list(str):
	'''This function takes each line and returns a list of the words in that line

	>>> turn_line_into_list("one two three four five")
	['one', 'two', 'three', 'four', 'five']
	>>> turn_line_into_list('')
	[]
	'''
	return re.findall(r"[a-z']+", str.lower())

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]
	words = []
	for line in lines:
		fixed_line = turn_line_into_list(line)
		for word in fixed_line:
			if not word == "'":
				words.append(word)
	return words

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	word_counts = Counter(word_list)
	ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
	return ordered_by_frequency[0:n]

def main():
	print get_top_n_words(get_word_list('alice.txt'),100)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	main()