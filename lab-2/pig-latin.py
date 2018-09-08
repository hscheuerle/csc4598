import re
import logging


def ruleOf(word):  # rule
    if re.match(r"^[b-df-hj-np-tv-z]{2,}", word, re.I):
        return 'CC'
    if re.match(r"^[b-df-hj-np-tv-z]{1,}", word, re.I):
        return 'C'
    if re.match(r"^[aeiou]{1,}", word, re.I):
        return 'V'
    return ''

# does python even optimize this?


def transformOf(rule):  # piglatin
    if rule == 'CC':
        return lambda word: word[2:] + word[:2] + "ay"
    if rule == 'C':
        return lambda word: word[1:] + word[:1] + "ay"
    if rule == 'V':
        return lambda word: word + "way"
    return lambda word: "(" + word + ")"


def apply(transform, word):
    return transform(word)


input = original = "How much wood could a woodchuck chuck"

words = input.split(" ")

output = map(lambda word: apply(transformOf(ruleOf(word)), word), words)

actual = " ".join(output).lower()

# input = input.split(" ")

# input = map(lambda x: mapPigLatin(x), input)
# input = (" ".join(input)).lower()

# actual = input
# print(actual)
expected = "owhay uchmay oodway ouldcay away oodchuckway uckchay"
assert actual == expected, "no match"
