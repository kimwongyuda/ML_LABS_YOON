import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

file = codecs.open("2BEXXX01.txt", "r", encoding="utf-16")
soup = BeautifulSoup(file, "html.parser")
body = soup.select_one("text > body")
text = body.getText()

twitter = Twitter()
word_dic = {}
lines = text.split("\r\n")
#명사 빈도 찾기
for line in lines:
    malist = twitter.pos(line)
    for taeso, pumsa in malist:
        if pumsa =="Noun":
            if not (taeso in word_dic):
                word_dic[taeso]=0
            word_dic[taeso] +=1

keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1})".format(word,count),end="")
print()
