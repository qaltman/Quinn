# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
def counting_vowels(paragraph):
	vowels = "aeiouAEIOU"
	v=0
	c=0
	for ch in paragraph:
		if ch.isalpha():
			if ch in vowels:
				v += 1 
			else: 	
				c += 1
	return (v,c)

def average_v_and_c(paragraph):
	total_vowels = 0 
	total_consonants = 0 
	for sentence in paragraph:
		v, c = counting_vowels(sentence)
		total_vowels += v 
		total_consonants += c 
	num_sentences = len(paragraph)

	if num_sentences == 0:
		return (0,0.0,0.0)
	
	avg_vowels = total_vowels/num_sentences
	avg_consonants = total_consonants/num_sentences

	return (num_sentences, avg_vowels, avg_consonants)

print (counting_vowels(paragraph))
print (average_v_and_c(paragraph))