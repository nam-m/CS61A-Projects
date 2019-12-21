from utils import *
from typing import autocorrect, lines_from_file, word_time, word, elapsed_time
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

# user_word = 'wrod'
# valid_words = ["word", "rod"]
# limit = 1
# diff_function = lambda w1, w2, limit: w1[0] != w2[0]
# d = {v : diff_function(user_word, v, limit) for v in valid_words}
# print(d)
# print(min(d, key=d.get))
# print(autocorrect("wrod", ["word", "rod"], diff_function, 1))

def word_time(word, elapsed_time):
    """A data abstraction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]

p0 = [word_time('START', 0), word_time('What', 0.2), word_time('great', 0.4), word_time('luck', 0.8)]
p1 = [word_time('START', 0), word_time('What', 0.6), word_time('great', 0.8), word_time('luck', 1.19)]
p2 = [word_time('START', 0), word_time('What', 0.2), word_time('great', 0.3), word_time('luck', 0.6)]

word_times = [p0, p1]

n_players = len(word_times) # number of players
n_words = len(word_times[0]) - 1 # number of words
margin = 0.1

total_time = []
for p in word_times:
    total_time.append([(elapsed_time(p[i]) - elapsed_time(p[i-1])) for i in range(1, len(p))])
print(total_time)

min_time_words = []
for i in range(n_players):
    min_time_words += [[]]
for p in range(n_players):
    for i in range(0, n_words):
        if total_time[p][i] <= min([total_time[j][i] for j in range(n_players)]) + margin:
            min_time_words[p] += [word(word_times[p][i+1])]
print(min_time_words)
        
