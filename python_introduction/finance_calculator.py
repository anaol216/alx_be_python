# calculate finance related values
monthly_income = float(input("Enter your monthly income: "))
total_mExpenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_mExpenses 

# annual savings
annual_Irate = 0.05
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * annual_Irate))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")