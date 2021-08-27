import datetime 
from decimal import Decimal 

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
    return Decimal(x).__round__(2)

def as_date(y, m, d):
    return datetime.date(y, m, d)


def format_qs(vals):
    return ",".join("?" * len(vals)) 
    

def process_insert(header, table): 
    """Turn dictionary into SQL insert. Integers will 
    need to be handled on runtime."""
    names = header.keys()
    values = format_qs(header.values())
    return (
        f"""INSERT INTO {table} ({', '.join(names)}) VALUES ({values})"""
    )



