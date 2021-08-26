import datetime 
from decimal import Decimal 

# Don't need to format date!!! Will accept date time attribute! 

# def format_date(date): 
#     if type(date) == datetime.date:
#         return "d{" + f"'{date.strftime('%Y-%m-%d')}'" + "}"
#     else:
#         return "d{" + f"'{date}'" + "}"
    
def format_decimal(vals): 
    rsp = []
    for i in vals:
        try: 
            rsp.append(Decimal(i))
        except: 
            rsp.append("?")
    return rsp 

# def update_date(vals):
#     return [format_date(i).encode("utf-8") if type(i) == datetime.date else '?' for i in vals]

def process_insert(header, table): 
    """Turn dictionary into SQL insert"""
    names = header.keys()
    values = format_decimal(header.values())
    return (
        f"""INSERT INTO {table} ({', '.join(names)}) VALUES ({ ', '.join(values)})"""
    )



