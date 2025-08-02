import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here

print(financial_data.head())

month = financial_data['Month']
revenue = financial_data['Revenue']

plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')

plt.show()

expenses = financial_data['Expenses']

plt.clf()
plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()


expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head(7))


# expense_categories = expense_overview['Expense']
# proportions = expense_overview['Proportion']

# plt.clf()
# plt.pie(proportions, labels = expense_categories)
# plt.title('Expense Categories')
# plt.axis('Equal')
# plt.tight_layout()

# plt.show()
expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()


employees = pd.read_csv('employees.csv')
print(employees.head())

sorted_productivity = employees.sort_values(by=['Productivity'])

print(sorted_productivity)

employees_cut = sorted_productivity.head(100)
print(employees_cut)

transformation = 'standardization'

commute_times = employees['Commute Time']
commute_times_log = np.log(commute_times)

print(commute_times.describe())

plt.clf()
# plt.hist(commute_times)
plt.hist(commute_times_log)

plt.title("Employee Commute Times")
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show()


