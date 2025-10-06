import numpy as np
customer_name = np.array(['Danish', 'Aysha', 'Noman', 'Shoaib', 'Haseeb', 'Abuzar'])
balances = np.array ([12000, 23000, 34888, 123990, 990000, 450000])

avg_balance = np.mean (balances)
max_balance = np.max (balances)
min_balance = np.min (balances)

print ('Average Balance:', avg_balance)
print ("Highest Balance:", max_balance)
print ('Lowest Balance:', min_balance)

rechist_index = np.argmax(balances)
print ('\nRichest Customer:', customer_name[rechist_index])
print ('Balance:', balances[rechist_index])

low_balance = customer_name[balances < 10000]
print ('\ncustomer with blew balance 10,000:')
print (low_balance)

abov_average = customer_name[balances > avg_balance]
print ('\ncustomer with above average balance:')
print (abov_average)


