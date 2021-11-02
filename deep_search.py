import itertools
from nltk.metrics import distance
import numpy as np


# this code basically gets a sentence and computes the diference between both sentences
# by words only.  It does not matter if one word has 3 errors inside of it, it will call
# back 1 because the word is already an error and we are looking wordwise here, not char
# wise.
def wer(decode, target):
    """Computes the Word Error Rate (WER).
    WER is defined as the edit distance between the two provided sentences after
    tokenizing to words.
    Args:
      decode: string of the decoded output.
      target: a string for the ground truth label.
    Returns:
      A float number for the WER of the current decode-target pair.
    """
    # Map each word to a new char.
    words = set(decode.split() + target.split())
    word2char = dict(zip(words, range(len(words))))

    new_decode = [chr(word2char[w]) for w in decode.split()]
    new_target = [chr(word2char[w]) for w in target.split()]

    return distance.edit_distance(''.join(new_decode), ''.join(new_target))


v = wer('hello how are you', 'vello how ae yu')  # should be 3
b = wer('I love you', 'I lv you')  # should be 1
print(f'v = {v} and b = {b}')


# This one computes the character, not the word as a whole.


def cer(decode, target):
    """ Computes the Character Errror Rate (CER).
    CER is defined as the edit distance between two given strings.

    :param decode: a string of the decoded output
    :param target: a string for the ground truth label.
    :return: a float number denoting the CER for the current sentence pair.
    """
    return distance.edit_distance(decode, target)


w = cer('hello', 'velo')  # should be 2

x = cer('Miguel', 'Migel')  # should be 1
print(f'w = {w} and x = {x}')



