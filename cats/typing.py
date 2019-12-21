"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    para_list = [p for p in paragraphs if select(p)]
    return para_list[k] if k + 1 <= len(para_list) else ''
    # END PROBLEM 1

def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select (paragraph):
        para = remove_punctuation(paragraph).lower().split()
        for t in topic:
            for p in para:
                if t == p:
                    return True
        return False
    return select
    # END PROBLEM 2

def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    num_correct = 0
    if len(typed_words) == 0 or len(reference_words) == 0:
        return 0.0
    elif len(typed_words) == 1:
        return 100.0 if typed_words[0] == reference_words[0] else 0.0
    else:
        for k in range(len(typed_words)):
            while k <= len(reference_words) - 1:
                if typed_words[k] == reference_words[k]:
                    num_correct += 1
    return num_correct / len(typed_words) * 100
    # END PROBLEM 3

def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # words per minute is the ratio of the number of characters typed
    # divided by 5 (a typical word length) to the elapsed time in minutes
    return (len(typed) / 5) * 60.0 / elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    # Create dictionary with keys as iterables in valid_words list
    # and values as difference between them and user_word
    d = {v : diff_function(user_word, v, limit) for v in valid_words}
    return min(d, key=d.get) if min(d.values()) <= limit else user_word
    # END PROBLEM 5

def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    if start == goal:
        return 0
    if limit == 0:
        return 1
    # return (limit == 0) 
    if min(len(start), len(goal)) == 0:
        return max(len(start), len(goal))
    diff = start[0] != goal[0] 
    # diff = 1 if start and goal have identical initial letter, else 0
    return diff + swap_diff(start[1:], goal[1:], limit-diff)
    # compare two reduced strings and decrease limit by diff
    # END PROBLEM 6

# print(swap_diff("awful", "awesome", 3) > 3)
# big_limit = 10
# swap_diff("awe", "awesome", big_limit)
# swap_diff("from", "form", big_limit)
# limit = 4
# print(swap_diff("roses", "arose", limit) > limit)
# print(swap_diff("rosesabcdefghijklm", "arosenopqrstuvwxyz", limit) > limit)
# print(swap_diff("tesng", "testing", 10))

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'
    if limit < 0:
        return 1
    elif start == goal: 
        return 0
    elif min(len(start), len(goal)) == 0:
        return max(len(start), len(goal))
    else:
        diff = start[0] != goal[0]
        add_diff = 1 + edit_diff(start, goal[1:], limit-1)
        remove_diff = 1 + edit_diff(start[1:], goal, limit-1)
        substitute_diff = diff + edit_diff(start[1:], goal[1:], limit-diff)
    return min(add_diff, remove_diff, substitute_diff)

sum([edit_diff('hyper', 'yhbpexr', k) > k for k in range(7)])
def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'

###########
# Phase 3 #
###########

def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    num_correct = 0
    for k in range(len(typed)):
        if typed[k] == prompt[k]:
            num_correct += 1
        else:
            break
    progress = num_correct / len(prompt)
    send({'id': id, 'progress': progress})
    return progress
    # END PROBLEM 8

def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report

def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times) # number of players
    n_words = len(word_times[0]) - 1 # number of words
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # Get total elapsed time of each word for each player
    total_elapsed_time = []
    for p in word_times:
        total_elapsed_time.append([(elapsed_time(p[i]) - elapsed_time(p[i-1])) for i in range(1, len(p))])
    # print(total_elapsed_time)

    # Get word from word_times list for words with min elapsed time
    min_time_words = []
    for i in range(n_players):
        min_time_words += [[]] # create empty lists corresponding to number of players
    for p in range(n_players):
        for i in range(0, n_words):
            if total_elapsed_time[p][i] <= min([total_elapsed_time[j][i] for j in range(n_players)]) + margin:
                min_time_words[p] += [word(word_times[p][i+1])]
    return min_time_words
    # END PROBLEM 9

def word_time(word, elapsed_time):
    """A data abstraction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)