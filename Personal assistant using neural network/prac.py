import nltk
from nltk import word_tokenize, pos_tag, sent_tokenize

inp = "tell me weather of indore. And can you also tell me about mumbai"
sent = list(w for w in sent_tokenize(inp))
word = list(w for w in word_tokenize(inp))
print("word : " , word)
print("sentence : " , sent)
pos_tags_word = pos_tag(word)
# pos_tags_sent = nltk.pos_tag_sents(sent)
print("tag word : " , pos_tags_word)
# print("tag sentence : " , pos_tags_sent)