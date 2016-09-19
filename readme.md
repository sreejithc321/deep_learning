
## Word2vec

– Word Embedding Model
– Created by a team of researchers led by Tomas Mikolov at Google


– Contains two distinct models
	- continuous bag-of-words (CBOW) : predicting the word given
its context ,ie predicts the current word w, given the neighboring
words in the window.
	- continuous skip-gram : predicting the context given a word, ie
given a window size of n words around a word w, the skip-gram
model predicts the neighboring words given the current word

- Convert words to vectors in a high dimensional space. Each dimension denotes an aspect like gender, type of object / word.
- By converting words to vectors we build relations between words. More similar the words in a dimension, more closer their scores are.


