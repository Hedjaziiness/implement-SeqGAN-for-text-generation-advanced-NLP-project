import re
from collections import Counter
import numpy as np



# Read the file
with open("pride_and_prejudice.txt", "r", encoding="utf-8") as file:
    text = file.read()


    # Preprocess the text 
def normalize_data(text):
    text = text.lower()  
    text = re.sub(r'[^a-zA-Z0-9\s.,!?;\'"-]', '',text) #to keep punctuanion+deleting special chars 
    text = re.sub(r'\s+', ' ', text) #replace les espaces with only one space
    return text

#apply function to our file 
cleaned_data = []
with open("pride_and_prejudice.txt",'r', encoding='utf-8') as file:
    text = file.read()
    textc = normalize_data(text)
    cleaned_data.append(textc)



    #write the result in another file
with open('GAN_data.txt', 'w') as output_file:
    for text in cleaned_data:
        output_file.write(text + '\n')




#with open('GAN_data.txt', 'r') as file:
 #   print(text)


#TOKEN TO INTEGER
#tokenization

tokens = text.split()

#create vocabularyy
token_num = Counter(tokens)
vocabulary = {word : i for i, (word,_) in enumerate(token_num.items(), start = 1)}
vocabulary['<PAD>'] = 0
vocabulary_size = len(vocabulary)


#convert sentences to a sequence of ID

def sentence_to_ids(sentence,vocabulary):
    return [vocabulary.get(word, vocabulary['<PAD>']) for word in sentence.split()]


# Split by sentence (derna the end of sentence hwa '.' )
sentences = text.split('. ')  
sequences = [sentence_to_ids(sentence, vocabulary) for sentence in sentences]


# Print some of the vocabulary
for word, index in list(vocabulary.items())[:10]:
    print(f'{word}: {index}')

#vocabulary size
print('vocabulary size :', len(vocabulary))



for i in range(4):
    print(i,':  ',sequences[i])




print([word for word, index in vocabulary.items() if index == 4150])
