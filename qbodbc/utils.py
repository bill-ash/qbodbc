import datetime 
from decimal import Decimal 
import random 
import secrets

# Don't need to format date!!! Will accept date time attribute! 
# def format_date(date): 
#     if type(date) == datetime.date:
#         return "d{" + f"'{date.strftime('%Y-%m-%d')}'" + "}"
#     else:
#         return "d{" + f"'{date}'" + "}"


# def update_date(vals):
#     return [format_date(i).encode("utf-8") if type(i) == datetime.date else '?' for i in vals]

def format_decimal(vals): 
    """Encoding needs to be supplied for floats and integers."""
    rsp = []
    for i in vals:
        try: 
            rsp.append(Decimal(i))
        except: 
            rsp.append("?")
    return rsp 


def as_decimal(x):
    """
    Decimal rounded two places
    """
    return Decimal(x).__round__(2)

def as_date(x, format='%m/%d/%Y'):
    """
    Convert date string to datetime object
    """
    return datetime.strptime(x, format)


def name_generator(): 
    """
    Create random names in tests
    """
    first_name = [
        'bob', 'marty', 'marsha', 'rasham', 'greg', 'gregory',
        'steve', 'mary', 'bill', 'suf', 'ashley', 'bently',
        'vicky', 'neria', 'moo', 'cow', 'dog', 'hary', 'fenti'
    ]
    last_name = [
        'meek', 'bills', 'type', 'popcorn', 'wordsss', 'blake'
        'blane', 'ash', 'blaire', 'world', 'fair', 'yarn', 'plow', 
        'rank', 'rafiki', 'reynolds', 'bear'
        ]

    return f"{random.choice(first_name)} {random.choice(last_name)}"


def account_generator(): 
    """
    Create random accounts in tests 
    """
    return str(secrets.randbits(29))


class Ref: 
    """
    Reference for parent child tables
    """
    def __init__(self): 
        self.Name = ""
        self.Value = ""
        
