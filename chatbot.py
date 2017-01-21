# Sentences we'll respond with if the user greeted us
from __future__ import print_function, unicode_literals
from numpy import *
from textblob import *
import logging
import os

os.environ['NLTK_DATA'] = os.getcwd() + '/nltk_data'

from textblob import TextBlob
#from config import FILTER_WORDS

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
GREETING_KEYWORDS = ("hello", "hi,", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["Sup ", "Hey ", "Howdy ", "Hey, how you doin "]

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greetingresponse"""
    #a=sentence.split
    #print "abc"
    cleaned = preprocess_text(sentence)
    parsed = TextBlob(cleaned)
    pronoun, noun, adjective, verb = find_candidate_parts_of_speech(parsed)
    for word in sentence.split():
        #print(word)
        if word.lower() in GREETING_KEYWORDS:
             print(random.choice(GREETING_RESPONSES)+noun)
            #return a

def find_pronoun(sent):
    """Given a sentence, find a preferred pronoun to respond with. Returns None if no candidate
    pronoun is found in the input"""
    pronoun = None

    for word, part_of_speech in sent.pos_tags:
        # Disambiguate pronouns
        if part_of_speech == 'PRP' and word.lower() == 'you':
            pronoun = 'I'
        elif part_of_speech == 'PRP' and word == 'I':
            # If the user mentioned themselves, then they will definitely be the pronoun
            pronoun = 'You'
    return pronoun
# end

def find_verb(sent):
    """Pick a candidate verb for the sentence."""
    verb = None
    pos = None
    for word, part_of_speech in sent.pos_tags:
        if part_of_speech.startswith('VB'):  # This is a verb
            verb = word
            pos = part_of_speech
            break
    return verb, pos


def find_noun(sent):
    """Given a sentence, find the best candidate noun."""
    noun = None

    if not noun:
        for w, p in sent.pos_tags:
            if p == 'NNP':  # This is a noun
                noun = w
                break

    if noun==None:
        #print('abc')
        for name in sent.split():
            #print('xyz')
            if (any(l.isupper() for l in name) and name!='I'):
                #print('Name found')
                noun=name
    
    if noun:
        logger.info("Found noun: %s", noun)

    return noun

def find_adjective(sent):
    """Given a sentence, find the best candidate adjective."""
    adj = None
    for w, p in sent.pos_tags:
        if p == 'JJ':  # This is an adjective
            adj = w
            break
    return adj

"""def find_code(sent):
    key=None
    for w,p in sent.pos_tags:
        if p=="""

def find_candidate_parts_of_speech(parsed):
    """Given a parsed input, find the best pronoun, direct noun, adjective, and verb to match their input.
    Returns a tuple of pronoun, noun, adjective, verb any of which may be None if there was no good match"""
    pronoun = None
    noun = None
    adjective = None
    verb = None
    for sent in parsed.sentences:
        pronoun = find_pronoun(sent)
        noun = find_noun(sent)
        adjective = find_adjective(sent)
        verb = find_verb(sent)
    logger.info("Pronoun=%s, noun=%s, adjective=%s, verb=%s", pronoun, noun, adjective, verb)
    return pronoun, noun, adjective, verb

def preprocess_text(sentence):
    """Handle some weird edge cases in parsing, like 'i' needing to be capitalized
    to be correctly identified as a pronoun"""
    cleaned = []
    words = sentence.split(' ')
    for w in words:
        if w == 'i':
            w = 'I'
        if w == "i'm":
            w = "I'm"
        cleaned.append(w)

    return ' '.join(cleaned)

def test(sentence):
    cleaned = preprocess_text(sentence)
    parsed = TextBlob(cleaned)
    pronoun, noun, adjective, verb = find_candidate_parts_of_speech(parsed)
    return pronoun, noun, adjective, verb

def start(sentence):
    check_for_greeting(sentence)
    querry = 'Hey'
    while querry.lower()!='bye':
        querry = raw_input('How can I help you?\n')
        if querry.lower()=='bye':
            print('Okay Bye')
        else:
            print('I will help you')
            cleaned = preprocess_text(querry)
            parsed = TextBlob(cleaned)
            pronoun, noun, adjective, verb = find_candidate_parts_of_speech(parsed)
            if (noun=='hackathon' and any(l.equals('time') for l in querry)):
                datafile=file('Data.txt')
                for line in datafile:
                    for a in line.split():
                        if a=='time':
                            print(line)
    print(var)
        
