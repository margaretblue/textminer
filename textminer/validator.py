import re

def hello():
    print("hello")
    return True

def binary(expression):
    # PASSED
    regex = re.findall(r"^[0-1]+$", expression)
    print(regex)
    if len(regex) >= 1:
        return True
    else:
        return False

def binary_even(expression):
    # PASSED
    regex = re.findall(r"^[0-1]+0$", expression)
    if len(regex) >= 1:
        return True
    else:
        return False

def hex(expression):
    # PASSED
    regex = re.findall(r"^([A-F]|[a-f]|[0-9])+$", expression)
    if len(regex) >= 1:
        return True
    else:
        return False

def word(expression):
    # PASSED
    regex = re.findall(r"(^[A-z0-9\-]+)[0-9]*$", expression)
    #regex = re.findall(r"^([0-9]|[a-z])*-*([A-Z]|[a-z])+$", expression)
    print(regex)
    if len(regex) >= 1:
        return True
    else:
        return False

def words(expression, count=False):
    # print("{}, {}".format(expression, count))
    # PASSED. The secret is to add an allowable space character to your
    # word() regex, then just count the number of spaces later.
    regex = re.findall(r"(^[A-z0-9\- ]+)[0-9]*$", expression)
    spaces = expression.count(' ')
    print(regex)
    if len(regex) >= 1:
        if count:
            if (spaces+1) == count:
                return True
            else:
                return False
        return True
    else:
        return False

def phone_number(expression):
    regex = re.findall(r"^((\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4})|\d{10}$", expression)
    #regex = re.findall(r"^\$  ([0-9]+,*)  (.[0-9][0-9]{2}) {0,1} $", expression)
    print(regex)
    if len(regex) >= 1:
        return True
    else:
        return False

def money(expression):
    # regex = re.findall(r"^\$[0-9]+[,]*(.\d{2})*$", expression)
    #                    r"  [   ([0-9]+,*)(.[0-9][0-9]{2}){0,1}$", expression)
    # source: http://stackoverflow.com/questions/11954280/regex-for-us-currency-format-and-length-limitation
    #regex = re.findall(r"^\$([1-9][0-9]{0,2}(?:(?:,[0-9]{3}){0,5})|\d{,15})?(?:\.[0-9]{0,10})?$", expression)
    regex = re.findall(r"^\$\d+(?:\,\d{3})?(?:\,\d{3})?(?:\.\d{2})?$", expression)
    print(regex)
    if len(regex) >= 1:
        return True
    else:
        return False
    pass

def zipcode(expression):
    regex = re.findall(r"(^\d{5})+(-\d{4})*$", expression)
    if len(regex) >= 1:
        return True
    else:
        return False

def date(expression):
    regex = re.findall(r"^\d{1,4}[\-/]{1}\d{1,2}[\-/]{1}\d{2,4}$", expression)
    print(regex)
    if len(regex) >= 1:
        return True
    else:
        return False

# ******HARD
def test_hard_date():
    pass

def test_email():
    pass

def test_address():
    pass

if __name__ == '__main__':

    # print("*** ONE WORD BELOW ***")
    # print(word("zyggon"))
    # print(word("horse-dagger"))
    # print(word("18-wheeler"))
    # print(word(""))
    # print(word("12"))
    # print(word("!!!"))
    # print(word("bar*us"))
    #
    #
    # print("***** WORDS BELOW *****")
    #
    # print(words("raggggg hammer dog"))
    # print(words("18-wheeler tarbox"))
    # print(words("hello", count=1))
    # print(words("hello world", count=2))
    # print(words("raggggg hammer dog", count=3))
    # print(words("18-wheeler tarbox", count=2))
    # print(words(""))
    # print(words("12"))
    # print(words("hey !!!", count=2))
    # print(words("bar*us w!zard", count=2))
    # print(words("hello", count=2))
    # print(words("hello world", count=3))
    # print(words("raggggg hammer dog", count=1))
    # print(words("18-wheeler tarbox", count=3))

    # print("**** Phone Number Below ***")
    # print(phone_number("919-555-1212"))
    # print(phone_number("(919) 555-1212"))
    # print(phone_number("9195551212"))
    # print(phone_number("919.555.1212"))
    # print(phone_number("919 555-1212"))
    # print(phone_number(""))
    # print(phone_number("555-121"))
    # print(phone_number("1212"))
    # print(phone_number("mobile"))

    print("****** MONEY BELOW *****")
    print(money("$4"))
    print(money("$19"))
    print(money("$19.00"))
    print(money("$3.58"))
    print(money("$1000"))
    print(money("$1000.00"))
    print(money("$1,000"))
    print(money("$1,000.00"))
    print(money("$5,555,555"))
    print(money("$5,555,555.55"))
    print(money("$45,555,555.55"))
    print(money("$456,555,555.55"))
    print(money("$1234567.89"))
    print(money(""))
    print(money("$12,34"))
    print(money("$1234.9"))
    print(money("$1234.999"))
    print(money("$"))
    print(money("31"))
    print(money("$$31"))

    # print("****ZIP***")
    # print(zipcode("63936"))
    # print(zipcode("50583"))
    # print(zipcode("48418"))
    # print(zipcode("06399"))
    # print(zipcode("26433-3235"))
    # print(zipcode("64100-6308"))
    # print(zipcode(""))
    # print(zipcode("7952"))
    # print(zipcode("115761"))
    # print(zipcode("60377-331"))
    # print(zipcode("8029-3924"))
    #
    # print(date("9/4/1976"))
    # print(date("1976-09-04"))
    # print(date("2015-01-01"))
    # print(date("02/15/2004"))
    # print(date("9/4"))
    # print(date("2015"))