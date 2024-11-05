import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')



#read file
with open('GAN_data.txt','r') as file:
    text = file.read()


#number of words
words = text.split()
num_words = len(words)

print('number of words :', num_words)


#number of sentences

sentences = sent_tokenize(text)
num_sent = len(sentences)
print('number of sentences :', num_sent)

