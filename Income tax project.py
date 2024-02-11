gross_income = float(input("Enter the gross income: "))
num_dependents = int(input("Enter the number of dependents: "))

standard_deduction = 10000
dependent_deduction = 3000 * num_dependents

total_deduction = standard_deduction + dependent_deduction
taxable_income = gross_income - total_deduction
	
if taxable_income < 0:
	taxable_income = 0

tax_rate = 0.20
income_tax = taxable_income * tax_rate
	
print(f"The income tax is: ${income_tax:.1f}")
