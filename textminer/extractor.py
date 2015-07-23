#from validator.py import *
import re

def phone_numbers(expression):
    """ ["(454) 999-1212", "(919) 123-4569"""
    regex = re.findall(r"\(\d{3}\) \d{3}-\d{4}", expression)
    print(regex)
    return regex
## HARD MODE BEGINS


def emails(expression):
    # from emailregex.com
    # regex = re.findall("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", expression)
    regex = re.findall("^[A-z]+[.A-z]*\@[A-z]+.[A-z]{3}$", expression)
    print(regex)
    return regex
    pass

if __name__ == '__main__':
    text = """
        I got to know of your company through our mutual friend Fiona Williams and the
        training you offer to graduate students in Advertising.

        If you would like a reference, my advisor can be reached at (454) 999-1212.
        You can contact me at (919) 123-4569 at your convenience.
        amaranth@gmail.com tatsoi tomatillo azuki bean garlic.

        Gumbo beet greens corn soko endive gumbo gourd. Parsley shallot courgette
        tatsoi pea@sprouts.org fava bean collard greens dandelion okra wakame
        tomato. Dandelion cucumber.earthnut@pea.net"""
    print(phone_numbers(text))
    print(emails(text))
