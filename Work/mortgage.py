# mortgage.py
#
# Exercise 1.7
month = 0
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

amplifying_percent = 1 + rate/12

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
	month += 1
	principal_with_new_percent = principal * amplifying_percent
	principal = principal_with_new_percent - payment
	if(principal < 0):
		principal = 0
		total_paid += principal_with_new_percent 
	else:
		total_paid += payment
	if month >= extra_payment_start_month and month <= extra_payment_end_month:
		principal_with_new_percent = principal
		principal -= extra_payment
		if(principal < 0):
			principal = 0
			total_paid += principal_with_new_percent
		else:
			total_paid += extra_payment
	print(f'Month {month} - Paid ${total_paid:0.2f}, Left: ${principal:0.2f}')

print(f'Total paid: ${total_paid:0.2f}')
print(f'Months: {month}')
