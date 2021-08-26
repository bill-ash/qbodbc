import datetime 

def format_date(date): 
    if type(date) == datetime.date:
        return "d{" + f"'{date.strftime('%Y-%m-%d')}'" + "}"
    else:
        return "d{" + f"'{date}'" + "}"
    
def update_date(vals):
    return [format_date(i).encode("utf-8") if type(i) == datetime.date else '?' for i in vals]

def process_insert(header, table): 
    """Turn dictionary into SQL insert"""
    names = header.keys()
    values = update_date(header.values())
    return (
        f"""INSERT INTO {table} ({', '.join(names)}) VALUES ({ ', '.join(values)})"""
    )



def test_list(one, two, three): 
    print(one)
    print(two)
    print(three)


test_list(*[1, 2, 3])