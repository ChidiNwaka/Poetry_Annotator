#The main module - need to import so that window code works correctly
import annotate_poetry
import re

NO_STRESS_SYMBOL = 'x'
PRIMARY_STRESS_SYMBOL = '/'
SECONDARY_STRESS_SYMBOL = '\\'  # note: len('\\') == 1 due to special character

"""
A pronouncing table: a nested list, [list of str, list of list of str]
  o a two item list, contains two parallel lists
  o the first item is a list of words (each item in this sublist is a str
    for which str.isupper() is True)
  o the second item is a list of pronunciations, where a pronunciation is a 
    list of phonemes (each item in this sublist is a list of str) 
  o the pronunciation for the word at index i in the list of words is at index
    i in the list of pronunciations
"""

# A small pronouncing table that can be used in docstring examples.
SMALL_TABLE = [['A', 'BOX', 'CONSISTENT', 'DON\'T', 'FOX', 'IN', 'SOCKS'],
               [['AH0'],
                ['B', 'AA1', 'K', 'S'],
                ['K', 'AH0', 'N', 'S', 'IH1', 'S', 'T', 'AH0', 'N', 'T'],
                ['D', 'OW1', 'N', 'T'],
                ['F', 'AA1', 'K', 'S'],
                ['IH0', 'N'],
                ['S', 'AA1', 'K', 'S']]]

# A small poem that can be used in docstring examples.
SMALL_POEM = "\nI'll sit here instead,\n\n\n\nA cloud on my head\n\n"

"""
A pronouncing dictionary is a list of pronouncing lines, where a pronouncing
line is a line in the CMU Pronouncing Dictionary format: 
  a word followed by the phonemes describing how to pronounce the word.
  o example:
    BOX  B AA1 K S
"""

# A small pronouncing dictionary that can be used in docstring examples.
SMALL_PRONOUNCING_DICT = [
    'A AH0',
    'BOX B AA1 K S',
    'CONSISTENT K AH0 N S IH1 S T AH0 N T',
    'DON\'T D OW1 N T',
    'FOX F AA1 K S',
    'IN IH0 N',
    'SOCKS S AA1 K S']
      

# ===================== Provided Helper Functions =============================

def prepare_word(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been converted to 
    uppercase and punctuation characters have been stripped from both ends. 
    Inner punctuation is left unchanged.
    
    This function prepares a word for looking up in a pronouncing table.

    >>> prepare_word('Birthday!!!')
    'BIRTHDAY'
    >>> prepare_word('"Quoted?"')
    'QUOTED'
    >>> prepare_word("Don't!")
    "DON'T"
    """

    # punctuation = """!"`@$%^&_+-={}|\\/—,;:'.-?)([]<>*#\n\t\r"""
    # result = s.upper().strip(punctuation)
    # return result


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


# ======== Students: Add Any Helper Functions Below This Line ================


# ======== Students: Add Any Helper Functions Above This Line ================

# ======== Students: Add One Docstring Example And Function ===================
# ========           Body Code To Each Function Below       ===================

def get_word(pronouncing_line):
    """ (str) -> str

    Precondition: pronouncing_line has the form:
                  WORD  PHONEME_1 PHONEME_2 ... PHONEME_LAST

    Return the word in pronouncing_line.

    >>> get_word('ABALONE  AE2 B AH0 L OW1 N IY0')
    'ABALONE'
    >>> get_word ('FOX F AA1 K S')
    'FOX'
    """
    
    
       # RETURN the first index of the string
       #return all the chracters before there is a whitespace
       # a word is a number of consecutive characters followed by a whitespace
       # return characters until not ch.isspace    
    word = pronouncing_line.split(' ')[0]
    
    #str = "'"+ word + "' get_word"
    
    return word



    # To do: Add one docstring example above and fill in this function's
    #        body to meet its specification.


def get_pronunciation(pronouncing_line):
    """ (str) -> list of str

    Precondition: pronouncing_line has the form:
                  WORD  PHONEME_1 PHONEME_2 ... PHONEME_LAST

    Return a list containing the phonemes in pronouncing_line.

    >>> get_pronunciation('ABALONE AE2 B AH0 L OW1 N IY0')
    ['AE2', 'B', 'AH0', 'L', 'OW1', 'N', 'IY0']
    >>> get_pronunciation('FOX F AA1 K S')
    ['F', 'AA1', 'K', 'S']
    """
    
    # To do: Add one docstring example above and fill in this function's
    #        body to meet its specification.
    # skip the first word, list at index [0]
    #return all the words after the first word

    return pronouncing_line.split(" ") [1:]

def make_pronouncing_table(pronouncing_list):
    """ (list of str) -> pronouncing table

    Precondition: pronouncing_list is a list of pronouncing lines.  
                  Each pronuncing line has the form:
                  WORD  PHONEME_1 PHONEME_2 ... PHONEME_LAST

    Return a pronouncing table for the data in pronouncing_list.

    >>> SMALL_TABLE == make_pronouncing_table(SMALL_PRONOUNCING_DICT)
    True
    >>> make_pronouncing_table(['A AHO', 'BOX B AA1 K S'])
    [['A', 'BOX'], [['AHO'], ['B', 'AA1', 'K', 'S']]]
    """
    
    #make two lists
    # the first list is a list of words
    #the seconding list is a list of pronouncing lines
    # i in words corresponds to i in pronouncing lines
    # open the pronouncing list at the same index as word from [i:]
    
    ## make a list of the form 

    # To do: Add one docstring example above and fill in this function's
    #        body to meet its specification.
    list_of_words = []
    word_phoneme = []
    table = []
    
    for word in pronouncing_list:
        split_word_into_a_list = word.split(" ")
        list_of_words.append(split_word_into_a_list[0])
        word_phoneme.append(split_word_into_a_list[1:])
       
    
    table.append(list_of_words)
    table.append(word_phoneme)
    
    return table
        


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
    #word= word.upper()
    
    #CHANGE TO upper case and alphanumeric
    
    #new_word = ''
    
    #for ch in word: 
        #if (ch.isalpha() or (ch == "'")): 
            #new_word += ch
         
    #if position > -1:
            #return pronouncing_table[1][position + 1]
    #else:
        #return 0
   
        
        #pronouncing_table= make_pronouncing_table(pronouncing_table)
        
        #for word in pronouncing_table:
            #if word in make_pronouncing_table(pronouncing_table):
                
                #return pronouncing_line
    
 

def is_vowel_phoneme(s):
    """ (str) -> bool

    Return True if and only if s is a vowel phoneme.  Vowel phonemes are three 
    character strings that start with two uppercase letters and end with a 
    single digit of 0, 1 or 2.  The first uppercase letter must be one of 
    A, E, I, O or U.

    >>> is_vowel_phoneme("AE0")
    True
    >>> is vowel_phoneme("AA1")
    True
    >>> is_vowel_phoneme("AE0t")
    False
    """
    
    if len(s) != 3:
        return False
    
    else:
               
        if ((s[0] in "AEIOU") and (s[1].isupper()) and (s[2].isdigit())):
                       
            return True

    return False
            
         
            
        

    # To do: Add one docstring example above and fill in this function's
    #        body to meet its specification.


def last_syllable(phoneme_list):
    """ (list of str) -> list of str

    Return the last vowel phoneme and any subsequent consonant phoneme(s) from
    phoneme_list, in the same order as they appear in phoneme_list.

    >>> last_syllable(['K', 'AH0', 'N', 'S', 'IH1', 'S', 'T', 'AH0', 'N', 'T'])
    ['AH0', 'N', 'T']
    
    last_syllable(['B', 'AA1', 'K', 'S'])
    ['AA1', 'K', 'S']
    
    >>> last_syllable(['B', 'K', 'S'])   # without a vowel phoneme
    []
    """

    # To do: Add one docstring example above and fill in this function's
    #        body to meet its specification.
        
    index = len(phoneme_list) - 1
    
    
    while (not is_vowel_phoneme(phoneme_list[index])) and index >= 0:
        index -= 1
        
    # if there are no vowels in phoneme list, return []    
    if index < 0:
        return []
    
    
    return phoneme_list[index:]   

      
           
    #the second code needs to return the rest of the characters in the string        
       #for get_last_char in get_last_vowel:
           #if get_last_char[-1] in phoneme_list:
               #get_last_char.append    
        
  
# Interested in why the next docstring starts with an r?
# See section 2.4.1:
# 3

def convert_to_lines(poem):
    r""" (str) -> list of str

    Return a list of the lines in poem, with leading and trailing whitespace
    removed from each poem line, and leading and trailing blank lines removed.
    Blank lines between stanzas are reduced to a single blank line.

    >>> convert_to_lines(SMALL_POEM)
    ["I'll sit here instead,", '', 'A cloud on my head']
     
    """
    
    divided_poem= []
    output = poem.split("\n")
    
    for word in output:
        if word: 
            divided_poem.append(word)
            divided_poem.append('')
                
    return divided_poem[:-1]

#fix quotation issue

# To do: Add one docstring example above and fill in this function's
#        body to meet its specification.


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
    
      
    rhyme_scheme_pattern= []
    annotate_poem= [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
                     'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
                     'X','Y', 'Z' ]
    line= 0
    
    # this code gets each individual poem line for example ['cats','are','evil']
    # it will return cats
    
    for line in poem_lines:
        line= poem_lines[line][:]
        line +=1
             
    # this code is to get the last word of the line
    last_word=[]
 
    for ch in line:
        if not ch.isspace():
            last_word = ch.append(last_word)
        
    #this is the code to get the last word of every poem line and its value
    #in the pronounciation_table 
    
    for last_word in line:
        if last_word in pronouncing_table[0]:
            index_last_word = pronouncing_table[0][last_word.index]
                           
     #this is the code to get the pronounciation scheme of the last word
  
    for phoneme_last_word in pronouncing_table:
                
                phoneme_last_word == index_last_word
                
              
    # this is the code to get the rhyme scheme, appended into a list
    
    for rhyme_pattern in poem_lines:
        for alpha in annotate_poem:
            if last_word == last_word[1]:
                
                rhyme_scheme.append(alpha)
              
    return rhyme_scheme_pattern   
    
 
 
def get_stress_pattern(word, pronouncing_table):
    """ (str, pronouncing table) -> str

    Return the stress pattern for pronouncing word using the pronouncing table 
    pronouncing_table.  Separate each stress symbol in the stress pattern by a
    single space, and pad the end of the stress pattern with spaces to make
    the length of the stress pattern the same as the length of word. 

    The stress symbols are given by the defined constants NO_STRESS_SYMBOL,
    PRIMARY_STRESS_SYMBOL, and SECONDARY_STRESS_SYMBOL, which correspond to
    the lexical stress markers 0, 1 and 2, respectively.

    The docstring examples assume NO_STRESS_SYMBOL = 'x', 
    PRIMARY_STRESS_SYMBOL = '/' and SECONDARY_STRESS_SYMBOL = '\\'.

    >>> pronouncing_table = SMALL_TABLE
    >>> get_stress_pattern('consistent', pronouncing_table)
    'x / x     '
    """

    # To do: Add one docstring example above and fill in this function's
    #        body to meet its specification.


if __name__ == '__main__':
    import doctest
    doctest.testmod()
