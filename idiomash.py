"""
********* IDIOMASH *********

Create idioms by mashing up old ones! Nothing new under the weather.

Input: text file with each candidate on a separate line

Output: `mashups_for_seq_with_lines` returns a set

Usage:
`lines = lines_from_path('some/save/path/here.txt')`
`mashups = mashups_for_seq_with_lines('and', lines)`

You can run `prompt_loop(9)` to start a user input loop
in which you select a candidate sequence and see up to 9 (or
any #) randomly chosen mashups pivoting on that sequence.


"""

import random

# recursively find the start and end indices
# of all occurrences of a sequence in a line of text
def seq_indices_in_text(seq, text, offset=0):
	if seq in text:
		start = text.index(seq) + offset	# start of 1st occurrence
		end = start + len(seq)				# start of 2nd occurrence
		return [(start, end)] + seq_indices_in_text(seq, text[start+1:], offset=offset+start+1)
	else:
		return []

# given a sequence and a list of lines, find all novel
# mashups between two lines that pivot on the sequence
# returns a set
def mashups_for_seq_with_lines(seq, lines):
	
	befores = set([])
	afters = set([])

	for line in lines:
		seq_indices = seq_indices_in_text(seq, line)
		for start, end in seq_indices:
			befores.add(line[:start])
			afters.add(line[end:])

	# insert seq between all (before, after) combinations
	mashups = set([before + seq + after for before in befores for after in afters])

	return mashups - set(lines)		# exclude reconstructed originals


################ UTILS ################

def lines_from_path(path):
	with open(path) as f:
		lines = [line.strip().lower() for line in f.readlines()]
		return [line for line in lines if len(line) > 0]

def print_random_n(mashups, n=10):
	mashups_list = list(mashups)
	random.shuffle(mashups_list)
	print('\n' +' \n'.join(mashups_list[:n]) + '\n') 

################ UX ################

def prompt_loop(n=20):
	lines = lines_from_path('text/idioms.txt')
	while True:
		choice = input('Enter a sequence:\n')
		if choice in ['q','x']:
			break
		mashups = mashups_for_seq_with_lines(choice, lines)
		print_random_n(mashups, n)


################ TESTS ################

def fruit_test():
	lines = lines_from_path('text/idioms.txt')
	fruit_mashups = mashups_for_seq_with_lines('fruit', lines)
	print(fruit_mashups)

def favorites_test():
	lines = lines_from_path('text/idioms.txt')
	favorites = ['you can', 'of the']
	for fav in favorites:
		mashups = mashups_for_seq_with_lines(fav, lines)
		print_random_n(mashups, 10)

################XXXXXXXXX################

if __name__ == '__main__':
	
	lines = lines_from_path('text/idioms.txt')
	fruit_test()
	prompt_loop(20)
	
	

	