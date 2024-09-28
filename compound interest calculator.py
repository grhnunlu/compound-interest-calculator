capital = int(input("enter capital:"))
interest_rate = float(input('enter yearly interest rate(with decimal number): '))
year = int(input("how many years: "))

for i in range(year):
    capital*=(1+interest_rate)
    
print(f'After {year} years, your total money is = {round(capital,2)}')