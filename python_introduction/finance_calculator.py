income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = income - expenses
projection = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are",monthly_savings)
print("Projected savings after one year, with interest, is:",int(projection))