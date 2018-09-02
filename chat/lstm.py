import codecs
from bs4 import BeautifulSoup
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys

fp = codecs.open("./2BEXXX01.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body")
text = body.getText() + " "

print(text)
print('코퍼스의 길이: ', len(text))

#문자 하나로 구분
chars = sorted(list(set(text)))

#sys.exit(0)

print('사용되고 있는 문자의 수: ', len(chars))

char2indices = dict((c, i) for i, c in enumerate(chars))
indices2char = dict((i, c) for i, c in enumerate(chars))

print(char2indices)
# 20 문자씩 짜르고 그 다음 문자를 넣어놈 그리고 그거 3칸 씩 뛰면서 반복
maxlen = 20
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i+maxlen])
    next_chars.append(text[i+maxlen])

print("학습할 구문의 수: ", len(sentences))
print('텍스트를 ID 벡터로 변환합니다.')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)

#안녕하세요 => [a,b,c,d,e]
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char2indices[char]] = 1
    y[i, char2indices[next_chars[i]]] = 1

# print(X[0][0].shape)
# print(X[0][0])