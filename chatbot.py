# Sentences we'll respond with if the user greeted us
from numpy import *
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greetingresponse"""
    #a=sentence.split
    #print "abc"
    for word in sentence.split():
        print word
        if word.lower() in GREETING_KEYWORDS:
            a=''.join(random.choice(GREETING_RESPONSES))
            return a
        
