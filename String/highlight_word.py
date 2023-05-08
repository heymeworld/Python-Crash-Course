def highlight_word(sentence, word):
	new = sentence.replace(word, word.upper())
	return new

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
