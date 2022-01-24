#!/usr/bin/env python3
import time
resources = {
	"Water": 1000,
	"Milk": 1000,
	"Coffee": 1000,
	"Money": 0
}
coffee_cost = {
	"espresso": 1,
	"latte": 2.5,
	"cappuccino": 3
}
while True:
	coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

	if coffee_choice == 'report':
		print(resources)

	if coffee_choice == 'off':
		exit()

	if coffee_choice == 'espresso':
		if resources['Water'] < 50:
			print("We don't have enough water for an espresso")
		elif resources['Coffee'] < 50:
			print("We don't have enough coffee for an espresso")
		else:
			quarters = int(input("How many quarters do you have? Please insert amount:"))/4
			dimes = int(input("How many dimes do you have? Please insert amount:"))/10
			nickles = int(input("How many nickles do you have? Please insert amount:"))/20
			pennies = int(input("How many pennies do you have? Please insert amount:"))/100
			paid_amount_dollars = quarters + dimes + nickles + pennies
			change_back = paid_amount_dollars - coffee_cost["espresso"]
			if change_back < 0:
				print("Sorry that's not enough money. Money refunded.")
			else:
				print("Your total is: " + str(coffee_cost["espresso"]) + " dollar" + " and your change is " + str(change_back) + " dollar(s).")
				print("Making " + coffee_choice + "...")
				time.sleep(5)
				resources["Money"] = resources["Money"] + coffee_cost["espresso"]
				resources["Water"] = resources["Water"] - 50
				resources['Coffee'] = resources['Coffee'] - 50
				print("Here you go, one " + coffee_choice)


	if coffee_choice == ('latte'):
		if resources['Water'] < 200:
			print("We don't have enough water for a latte")
		elif resources['Milk'] < 100:
			print("We don't have enough milk for a latte")
		elif resources['Coffee'] < 50:
			print("We don't have enough coffee for a latte")
		else:
			quarters = int(input("How many quarters do you have? Please insert amount:"))/4
			dimes = int(input("How many dimes do you have? Please insert amount:"))/10
			nickles = int(input("How many nickles do you have? Please insert amount:"))/20
			pennies = int(input("How many pennies do you have? Please insert amount:"))/100
			paid_amount_dollars = quarters + dimes + nickles + pennies
			change_back = paid_amount_dollars - coffee_cost["latte"]
			if change_back < 0:
				print("Sorry thats not enough money. Money refunded.​")
			else:
				print("Your total is: " + str(coffee_cost["latte"]) + " dollar" + " and your change is " + str(change_back) + " dollar(s).")
				print("Making " + coffee_choice + "...")
				time.sleep(5)
				resources["Money"] = resources["Money"] + coffee_cost["latte"]
				resources["Water"] = resources["Water"] - 200
				resources["Milk"] = resources["Milk"] - 100
				resources['Coffee'] = resources['Coffee'] - 50
				print("Here you go, one " + coffee_choice)

	if coffee_choice == ('cappuccino'):
		if resources['Water'] < 200:
			print("We don't have enough water for a cappuccino")
		elif resources['Milk'] < 100:
			print("We don't have enough milk for a cappuccino")
		elif resources['Coffee'] < 50:
			print("We don't have enough coffee for a cappuccino")
		else:
			quarters = int(input("How many quarters do you have? Please insert amount:"))/4
			dimes = int(input("How many dimes do you have? Please insert amount:"))/10
			nickles = int(input("How many nickles do you have? Please insert amount:"))/20
			pennies = int(input("How many pennies do you have? Please insert amount:"))/100
			paid_amount_dollars = quarters + dimes + nickles + pennies
			change_back = paid_amount_dollars - coffee_cost["cappuccino"]
			if change_back < 0:
				print("Sorry thats not enough money. Money refunded.")
			else:
				print("Your total is: " + str(coffee_cost["cappuccino"]) + " dollar" + " and your change is " + str(change_back) + " dollar(s).")
				print("Making " + coffee_choice + "...")
				time.sleep(5)
				resources["Money"] = resources["Money"] + coffee_cost["cappuccino"]
				resources["Water"] = resources["Water"] - 200
				resources["Milk"] = resources["Milk"] - 100
				resources['Coffee'] = resources['Coffee'] - 50
				print("Here you go, one " + coffee_choice)
