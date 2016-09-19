
from gensim.models import word2vec
from gensim.models.word2vec import Word2Vec
import os
import pickle


# Read Data
male_posts = []
female_post = []
with open("male_blog_list.txt","rb") as male_file:
    male_posts= pickle.load(male_file)
with open("female_blog_list.txt","rb") as female_file:
    female_posts = pickle.load(female_file)
print len(female_posts)
print len(male_posts)


# Filter Data
filtered_male_posts = []
filtered_female_posts = []
for post_male in male_posts:
    if len(post_male) == 0:
        continue
    filtered_male_posts.append(post_male)
for post_female in female_posts:
    if len(post_female) == 0:
        continue
    filtered_female_posts.append(post_female)
print len(filtered_female_posts)
print len(filtered_male_posts)
filtered_female_posts = map(lambda x:unicode(x), filtered_female_posts)
filtered_male_posts = map(lambda x: unicode(x), filtered_male_posts)
posts = filtered_female_posts + filtered_male_posts    
type(posts[0])
print len(posts)
print type(posts[100])


# Word2vec
w2v = Word2Vec(size=1000, min_count=1)
w2v.build_vocab(map(lambda x: x.split(), posts), )
#print w2v.vocab
print w2v.similarity('I', 'My')
print w2v.similarity('husband', 'male')



