from urllib.requst import urlopen

with urlopen('http://sixty-north.com/c.t.txt') as story:
    story_words = []
    for line in story:
        line_words = lin.decode('urf-8').split()
	for words in line_words:
	    story_words.append(word)
