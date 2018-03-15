# author - Richard Liao
# Dec 26 2016
import numpy as np
import pandas as pd
#import cPickle
#from collections import defaultdict
#import re

#from bs4 import BeautifulSoup

import sys
import os
from utils import *
from rnnmath import *

# os.environ['KERAS_BACKEND']='theano'

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical

from keras.layers import Embedding
from keras.layers import Dense, Input, Flatten, Masking, dot

from keras import optimizers

from keras.layers import Conv1D, MaxPooling1D, Embedding, Merge, Dropout, LSTM, GRU, Bidirectional, SimpleRNN
from keras.models import Model

from keras import backend as K
from keras.engine.topology import Layer, InputSpec
from keras import initializers

MAX_SEQUENCE_LENGTH = 50
#MAX_NB_WORDS = 2000
#EMBEDDING_DIM = 100
#VALIDATION_SPLIT = 0.2

'''def clean_str(string):
    """
    Tokenization/string cleaning for dataset
    Every dataset is lower cased except
    """
    string = re.sub(r"\\", "", string)    
    string = re.sub(r"\'", "", string)    
    string = re.sub(r"\"", "", string)    
    return string.strip().lower()

data_train = pd.read_csv('~/Testground/data/imdb/labeledTrainData.tsv', sep='\t')
print data_train.shape

texts = []
labels = []

for idx in range(data_train.review.shape[0]):
    text = BeautifulSoup(data_train.review[idx])
    texts.append(clean_str(text.get_text().encode('ascii','ignore')))
    labels.append(data_train.sentiment[idx])
    

tokenizer = Tokenizer(nb_words=MAX_NB_WORDS)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

labels = to_categorical(np.asarray(labels))
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
nb_validation_samples = int(VALIDATION_SPLIT * data.shape[0])'''

train_size = 25000 #TODO
dev_size = 1000
vocab_size = 2000

data_folder = 'data'
vocab = pd.read_table(data_folder + "/vocab.wiki.txt", header=None, sep="\s+", index_col=0, names=['count', 'freq'], )
num_to_word = dict(enumerate(vocab.index[:vocab_size]))
word_to_num = invert_dict(num_to_word)

# calculate loss vocabulary words due to vocab_size
fraction_lost = fraq_loss(vocab, word_to_num, vocab_size)
print("Retained %d words from %d (%.02f%% of all tokens)\n" % (vocab_size, len(vocab), 100*(1-fraction_lost)))

# load training data
sents = load_np_dataset(data_folder + '/wiki-train.txt')
S_train = docs_to_indices(sents, word_to_num, 0, 0)
x_train, y_train = seqs_to_npXY(S_train)

x_train = x_train[:train_size]
y_train = y_train[:train_size]

# load development data
sents = load_np_dataset(data_folder + '/wiki-dev.txt')
S_dev = docs_to_indices(sents, word_to_num, 0, 0)
x_val, y_val = seqs_to_npXY(S_dev)

x_val = x_val[:dev_size]
y_val = y_val[:dev_size]

#x_train = data[:-nb_validation_samples]
#y_train = labels[:-nb_validation_samples]
#x_val = data[-nb_validation_samples:]
#y_val = labels[-nb_validation_samples:]

print('Traing and validation set number of positive and negative reviews')
print(y_train.sum(axis=0))
print(y_val.sum(axis=0))

'''GLOVE_DIR = "~/Testground/data/glove"
embeddings_index = {}
f = open(os.path.join(GLOVE_DIR, 'glove.6B.100d.txt'))
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Total %s word vectors.' % len(embeddings_index))

embedding_matrix = np.random.random((len(word_index) + 1, EMBEDDING_DIM))
for word, i in word_index.items():
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector
        
embedding_layer = Embedding(len(word_index) + 1,
                            EMBEDDING_DIM,
                            weights=[embedding_matrix],
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=True)'''

def make_onehot_array(X):
    X_one = np.zeros((len(X), MAX_SEQUENCE_LENGTH, vocab_size), dtype='float32')
    for i in range(len(X_one)):
        for j in range(len(X[i])):
            X_one[i, j, X[i][j]] = 1
        X_one[i, len(X[i]):, :] = 0.125
    return X_one 

x_train = make_onehot_array(x_train)
x_val = make_onehot_array(x_val)

#print(x_train)

sequence_input = Input(shape=(MAX_SEQUENCE_LENGTH, vocab_size), dtype='float32')
#embedded_sequences = embedding_layer(sequence_input)
mask = Masking(mask_value=.125, input_shape=(MAX_SEQUENCE_LENGTH, vocab_size))(sequence_input)
l_lstm = (SimpleRNN(50, activation='sigmoid', use_bias=False))(mask)
preds = Dense(1, activation='sigmoid')(l_lstm)

model = Model(sequence_input, preds)
model.compile(loss='binary_crossentropy',
              optimizer=optimizers.SGD(lr=1.0, momentum=0.0, decay=0.2, nesterov=False),
              metrics=['acc'])

print("model fitting - simple RNN")
model.summary()
model.fit(x_train, y_train, validation_data=(x_val, y_val),
         nb_epoch=5, batch_size=50)

print(x_val[:3])
print(model.predict(x_val[:3]))

# Attention GRU network		  
# class AttLayer(Layer):
#     def __init__(self, **kwargs):
#         self.init = initializers.RandomNormal()
#         #self.input_spec = [InputSpec(ndim=3)]
#         super(AttLayer, self).__init__(**kwargs)
#
#     def build(self, input_shape):
#         assert len(input_shape)==3
#         #self.W = self.init((input_shape[-1],1))
#         self.W = self.init((input_shape[-1],))
#         #self.input_spec = [InputSpec(shape=input_shape)]
#         self.trainable_weights = [self.W]
#         super(AttLayer, self).build(input_shape)  # be sure you call this somewhere!
#
#     def call(self, x, mask=None):
#         print(x.shape, self.W.shape)
#         eij = K.tanh(K.dot(x, self.W))
#         # eij = K.tanh(dot([x, self.W], axes=(2,0)))
#
#         ai = K.exp(eij)
#         weights = ai/K.sum(ai, axis=1).dimshuffle(0,'x')
#
#         weighted_input = x*weights.dimshuffle(0,1,'x')
#         return weighted_input.sum(axis=1)
#
#     def get_output_shape_for(self, input_shape):
#         return (input_shape[0], input_shape[-1])
#
# '''embedding_matrix = np.random.random((len(word_index) + 1, EMBEDDING_DIM))
# for word, i in word_index.items():
#     embedding_vector = embeddings_index.get(word)
#     if embedding_vector is not None:
#         # words not found in embedding index will be all-zeros.
#         embedding_matrix[i] = embedding_vector
#
# embedding_layer = Embedding(len(word_index) + 1,
#                             EMBEDDING_DIM,
#                             weights=[embedding_matrix],
#                             input_length=MAX_SEQUENCE_LENGTH,
#                             trainable=True)'''
#
#
#
# '''sequence_input = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
# #embedded_sequences = embedding_layer(sequence_input)
# l_gru = Bidirectional(GRU(100, return_sequences=True))(sequence_input)
# l_att = AttLayer()(l_gru)
# preds = Dense(1, activation='softmax')(l_att)
# model = Model(sequence_input, preds)
# model.compile(loss='binary_crossentropy',
#               optimizer='rmsprop',
#               metrics=['acc'])'''
#
# sequence_input = Input(shape=(MAX_SEQUENCE_LENGTH, vocab_size), dtype='float32')
# #embedded_sequences = embedding_layer(sequence_input)
# #mask = Masking(mask_value=.125, input_shape=(MAX_SEQUENCE_LENGTH, vocab_size))(sequence_input)
# l_lstm = Bidirectional(SimpleRNN(50, activation='sigmoid', use_bias=False, return_sequences=True))(sequence_input)
# l_att = AttLayer()(l_lstm)
# preds = Dense(1, activation='sigmoid')(l_att)
#
# model = Model(sequence_input, preds)
# model.compile(loss='binary_crossentropy',
#               optimizer='rmsprop',
#               metrics=['acc'])
#
#
# #print("model fitting - attention GRU network")
# model.summary()
# model.fit(x_train, y_train, validation_data=(x_val, y_val),
#           nb_epoch=10, batch_size=50)