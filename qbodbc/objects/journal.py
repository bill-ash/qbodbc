
class Journal: 
    __table__ = 'Journal'

    def __init__(self): 
        self.credit_line = []
        self.debit_line = []

    def add_credit_line(self, **kwargs): 
        self.credit_line.append(
            {
                **{k:v for k,v in kwargs.items() if v is not None},
                'FQSaveToCache': '1'
                }
            )

    def add_debit_line(self, **kwargs): 
        self.debit_line.append({**kwargs, 'FQSaveToCache': '0'})
        
    def create(self, qb, **kwargs): 
        """
        credit = {
            'TxnDate': datetime.date(2021,1, 1),
            'JournalCreditLineAccountRefListID': None,
            'JournalCreditLineAccountRefFullName': 'Accounts Payable',
            'JournalCreditLineAmount': Decimal('10.99'),
            'JournalCreditLineMemo': 'MyCreditMemo',
            'JournalCreditLineEntityRefListID': None,
            'JournalCreditLineEntityRefFullName': 'Locksmith',
            'JournalCreditLineEntityClassRefListID': None,
            'JournalCreditLineEntityClassRefFullName': None,
        }
        """
        for credit in self.credit_line:
            centry = (
                f"insert into JournalEntryCreditLine ({', '.join(credit.keys())})"
                f" values ({','.join('?' * len(credit))})"
            ) 
            qb.execute(centry, *list(credit.values()))
            print(centry)

        for debit in self.debit_line: 
            dentry = (
                f"insert into JournalEntryDebitLine ({', '.join(debit.keys())})"
                f" values ({','.join('?' * len(debit))})"
            ) 
            qb.execute(dentry, *list(debit.values()))
            print(dentry)
        
        return qb.execute('SP_LASTINSERTID JournalEntryDebitLine')

