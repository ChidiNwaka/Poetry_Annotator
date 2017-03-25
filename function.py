
# A small pronouncing table that can be used in docstring examples.
SMALL_TABLE = [['A', 'BOX', 'CONSISTENT', 'DON\'T', 'FOX', 'IN', 'SOCKS'],
               [['AH0'],
                ['B', 'AA1', 'K', 'S'],
                ['K', 'AH0', 'N', 'S', 'IH1', 'S', 'T', 'AH0', 'N', 'T'],
                ['D', 'OW1', 'N', 'T'],
                ['F', 'AA1', 'K', 'S'],
                ['IH0', 'N'],
                ['S', 'AA1', 'K', 'S']]]



def get_rhyme_scheme_letter(offset):
    """ (int) -> str

    Precondition: 0 <= offset <= 25

    Return the letter corresponding to the offset from 'A'.  Helpful when 
    labelling a poem with its rhyme scheme.

    >>> get_rhyme_scheme_letter(0)
    'A'
    >>> get_rhyme_scheme_letter(25)
    'Z'
    """

    return chr(ord('A') + offset)

def look_up_pronunciation(word, pronouncing_table):
    """ (str, pronouncing table) -> list of str

    Return the list of phonemes for pronouncing word, as found in
    pronouncing_table.  Ignore the leading and trailing punctuation in word
    as well as the case of any letters in word.

    >>> pronouncing_table = SMALL_TABLE
    >>> look_up_pronunciation("Don't!", pronouncing_table)
    ['D', 'OW1', 'N', 'T']
    >>> look_up_pronunciation("!CONSISTENT!", pronouncing_table)
    ['K', 'AH0', 'N', 'S', 'IH1', 'S', 'T', 'AH0', 'N', 'T']
    """
    # To do: Add one docstring example above and fill in this function's
        #        body to meet its specification.
        
        
        #print "firstList: ", pronouncing_table[0][0]
        #for  word in pronouncing_table[0]:
            #print(word)
        #position = first_list[0].index(word)
        
        #if position > -1:
            #return pronouncing_table[1][position + 1]
        #else:
            #return 0
            
    word = word.upper() # Converts word to upper case.
    #word = re.sub('[!]', '', word) # Ignores any punchation in word.
    word = word.strip('!')
    
    if (word in pronouncing_table[0]):
        
        position = pronouncing_table[0].index(word)
        
        return pronouncing_table[1][position]
    else:
        return []


def detect_rhyme_scheme(poem_lines, pronouncing_table):
    """ (list of str, pronouncing table) -> list of str

    Return a list of single characters indicating the rhyme scheme for 
    poem_lines, with blank lines that separate stanzas given the rhyme scheme 
    marker ' '.  The marker for the first line in the poem is 'A'. When 
    annotating the rhyme scheme in a poem, consecutive uppercase letters are 
    used, starting with the letters A, B, C, etc

    >>> pronouncing_table = SMALL_TABLE
    >>> poem_lines = ["Don't, in box!", '', 'Fox in socks.', 'Consistent.']
    >>> detect_rhyme_scheme(poem_lines, pronouncing_table)
    ['A', ' ', 'A', 'B']
    """

    # To do: Add one docstring example above and fill in this function's
    #        body to meet its specification.
    
    rhyme_scheme_pattern = []
    list_of_word_phoneme = []

    offset = 0;

    for line in poem_lines:

    	line = ' '.join(line.split())

    	if line != '':
    		print(line)
    		last_word = line.split()[-1]
    		# last_word = prepare_word(last_word)
    		last_word = last_word.upper() # Converts word to upper case.
    		last_word = last_word.strip('.')

    		
    		word_phoneme = look_up_pronunciation(last_word, pronouncing_table) 
    		print(word_phoneme)
    		# print(offset)
    		# print(word_phoneme)
    		if len(word_phoneme) > 0:

    			# if (len(rhyme_scheme_pattern) > 0) and (rhyme_scheme_pattern[offset - 1] == get_rhyme_scheme_letter(offset)):
    			# 	rhyme_scheme_pattern.append('')
    			# 	rhyme_scheme_pattern.append(get_rhyme_scheme_letter(offset))
    			# 	offset += 1
    			# else:  
    			# print(word_phoneme)
    			if word_phoneme in pronouncing_table[1]:
	    			if word_phoneme in list_of_word_phoneme: 
	    				# print('yes')
	    				# offset -= 1
		    			prev_index = list_of_word_phoneme.index(word_phoneme)
		    			# print(word_phoneme)
		    			# print(prev_index)
		    			ch = rhyme_scheme_pattern[prev_index]
		    			print('here')
		    			print(ch)
		   		    	list_of_word_phoneme.append(ch)
		    			# rhyme_scheme_pattern.append(ch)
		    			# print(rhyme_scheme_pattern)
		    			# print('here')
		    		else: 
		    			# print('yes')
		    			# offset += 1
		    			# offset -= 1
		    			rhyme_scheme_pattern.append(get_rhyme_scheme_letter(offset))
		    			list_of_word_phoneme.append(word_phoneme)
		    			offset += 1
		    	else:
		    		rhyme_scheme_pattern.append(get_rhyme_scheme_letter(offset))
		    		list_of_word_phoneme.append(word_phoneme)
		    		offset += 1
	    		
        else: 
        	rhyme_scheme_pattern.append(' ')
        	offset -= 1


    return rhyme_scheme_pattern   


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # poem = "\nI'll sit here instead,\n\n\n\nA cloud on my head\n\n"
    # x = convert_to_lines(poem)
    # print(x)

    pronouncing_table = SMALL_TABLE
    print(pronouncing_table)
    poem_lines = ["Don't, in box!", '', 'Fox in socks.', 'Consistent.']
    # listAns = detect_rhyme_scheme(poem_lines, pronouncing_table)
    # print(listAns)

    poem_lines2 = ['DON\'T', 'JAMES', ' ', 'DON\'T', '    ']


    poem_lines2 = ['Jane is CONSISTENT', 'why CONSISTENT', 'NONE']
    listAns2 = detect_rhyme_scheme(poem_lines2, pronouncing_table)
    print(listAns2)



