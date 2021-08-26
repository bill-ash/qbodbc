from dataclasses import dataclass

# @dataclass
# class Bill: 
#     TxnDate: str
#     RefNum: str
#     Memo: str


class Bill: 
    # def __init__(self, date=None, ref_num=None, memo=None, bill_class=None): 
    def __init__(self, **kwargs): 
        # self.date = date
        # self.ref_num = ref_num 
        # self.memo = memo 
        # self.bill_class = bill_class
        self.header = kwargs
        self.line_item = [] 
        self.line_expense = [] 

    def add_item(self, data = []): 
        self.line_item.append(data)

    def add_expense(self, data = []): 
        self.line_expense.append(data)

    def _create(self, connection):
        # Add the bill line 
        # Add the bill header
        # Add the expense line 

        b_line = "INSERT INTO BillExpenseLine (ExpenseLineAccountRefFullName, ExpenseLineAmount) "

    def __repr__(self):
        return f"""Bill: {self.header["ref_num"]}
        Line Items: {len(self.line_item)} Expense Items: {len(self.line_expense)}
        """ 
