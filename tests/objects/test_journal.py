# from qbodbc import QuickBooks
# from qbodbc.objects import Journal, journal
# import datetime 
# from decimal import Decimal

# quickbooks = QuickBooks(DSN='qbtest')

# # Creates a cursor to be passed as a argument 
# qb = quickbooks.connect()

# journal_entry = Journal()

# credit = {
#     'TxnDate': datetime.date(2021,1, 1),
#     'JournalCreditLineAccountRefListID': None,
#     'JournalCreditLineAccountRefFullName': 'Accounts Payable',
#     'JournalCreditLineAmount': Decimal('10.99'),
#     'JournalCreditLineMemo': 'MyCreditMemo\'s Here',
#     'JournalCreditLineEntityRefListID': None,
#     'JournalCreditLineEntityRefFullName': 'Locksmith',
#     'JournalCreditLineEntityClassRefListID': None,
#     'JournalCreditLineEntityClassRefFullName': None,
#     }

# journal_entry.add_credit_line(**credit)
# journal_entry.credit_line

# debit = {
#     'TxnDate': datetime.date(2021,1, 1),
#     # 'JournalDebitLineAccountRefListID': None,
#     'JournalDebitLineAccountRefFullName': 'Other Expense',
#     'JournalDebitLineAmount': Decimal('10.99'),
#     'JournalDebitLineMemo': 'MyCreditMemo',
#     # 'JournalDebitLineEntityRefListID': None,
#     # 'JournalDebitLineEntityRefFullName': None,
#     # 'JournalDebitLineEntityClassRefListID': None,
#     # 'JournalDebitLineEntityClassRefFullName': None,
#     }

# journal_entry.add_debit_line(**debit)
# journal_entry.debit_line


# # qb.execute("sp_batchclear JournalEntryCreditLine")
# # qb.execute("sp_batchclear JournalEntryDebitLine")
# # qb.execute("sp_lastinsertid JournalEntryDebitLine")
# # qb.fetchone()

# resp = journal_entry.create(qb=qb).fetchval()


