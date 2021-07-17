import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text = """NLP is the use of psychology with sound strategies and techniques a person can use to create results they desire. Neuro (neurology) and Linguistic (language) program (patterns, themes) is about the language of the brain and knowing NLP gives an individual the power to reprogram thinking using the many techniques of NLP. This brings effective changes to transform lives.
The use of NLP has created astounding results in the lives of all. NLP brings in a tremendous change in the way a coach works with the self and the client. A coach learns winning tactics that bring greater coaching success. A successful coach with the knowledge of NLP is equipped to create a business module for self while serving the world at large. To understand this better, we list 5 techniques among the many NLP techniques you can use to elevate your coaching practice."""
stopwords = list(STOP_WORDS)
print(text)
print("")
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
tokens = [token.text for token in doc]
#print(tokens)
punctuation = punctuation + '\n'
#print(punctuation)
word_frequencies ={}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
#print(word_frequencies)
max_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency
#print(word_frequencies)
sentence_tokens = [sent for sent in doc.sents]
#print(sentence_tokens)
sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]
#print(sentence_scores)

from heapq import nlargest
select_length1 = int(len(sentence_tokens)*0.4)
select_length2 = int(len(sentence_tokens)*0.3)
summary1 = nlargest(select_length1, sentence_scores, key = sentence_scores.get)
summary2 = nlargest(select_length2, sentence_scores, key = sentence_scores.get)
print("\n","Summarized paragraph (40%) is as follows")
print(summary1)

print("\n","Summarized paragraph (30%) is as follows",)
print(summary2)
