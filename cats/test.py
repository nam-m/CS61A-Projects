from utils import *
# print(remove_punctuation('A school, of fish'))
# print(lower('A school, of fish'))
# print(split('A school, of fish'))

s = 'A school ! , of fish'
s = remove_punctuation(s)
s = lower(s)
s = split(s)
print(s)