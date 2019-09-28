from utils import *
from typing import autocorrect, lines_from_file
# print(remove_punctuation('A school, of fish'))
# print(lower('A school, of fish'))
# print(split('A school, of fish'))

# s = 'A school ! , of fish'
# s = remove_punctuation(s)
# s = lower(s)
# s = split(s)
# print(s)

# diff_function = lambda w1, w2, limit: abs(len(w2) - len(w1))
# user_word = "cul"
# valid_words = ["culture", "cult", "cultivate"]
# limit = 10 
# d = {v : diff_function(user_word, v, limit) for v in valid_words}

# print(d)

# # Get key with min value
# print(min(d, key=d.get))

# # Get min key
# print(min(d.keys())

# # Get min value
# print(min(d.values()))

user_word = 'wrod'
valid_words = ["word", "rod"]
limit = 1
diff_function = lambda w1, w2, limit: w1[0] != w2[0]
d = {v : diff_function(user_word, v, limit) for v in valid_words}
print(d)
print(min(d, key=d.get))
print(autocorrect("wrod", ["word", "rod"], diff_function, 1))
