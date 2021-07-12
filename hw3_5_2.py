
#___5_____________________________________________________________________________________

from collections import Counter
import re


# while True:

#     found_word = (input('write the word:\n(russian here)\n')).lower()
#     words = re.findall(r'\w+', open('./3-5.txt', 'r', encoding="utf8").read().lower())
#     # print (words)
#     if found_word in words:
#         с = Counter(w for w in words if w == found_word)
#         #print(c)
#         print (с[found_word])
#     else:
#         print('not in text')


#     if input('any othere?(y/n)') == 'n':
#         break



#___6__________________________________________________________________________________________



with open ('./3-5.txt','r', encoding="utf8") as f:
  old_data = f.read()
found_word = (input('write the word:\n(russian here)\n'))
new_word = (input('write the new word:\n(russian here)\n'))

if found_word.lower() in old_data.lower():
    new_data = old_data.replace(found_word, new_word)
    with open ('./file_nr.txt', 'w') as f:
        f.write(new_data)

else:
    print('not in text')


# в VSC пишет такую ошибку :

# Traceback (most recent call last):
#   File "g:\hw\hw3_5_2.py", line 38, in <module>
#     f.write(new_data)
#   File "C:\Users\il_li\AppData\Local\Programs\Python\Python39\lib\encodings\cp1251.py", line 19, in encode
#     return codecs.charmap_encode(input,self.errors,encoding_table)[0]
# UnicodeEncodeError: 'charmap' codec can't encode character '\u25a0' in position 274: character maps to <undefined>


# через убунту работает вроде нормально

