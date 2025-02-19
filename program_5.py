# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.


#Tanner Rosenthal
#02/13/2025
def main():

expenses = 0.0
total_cost = 0.0
budget = float(input("What is your budget?"))

while True:
    cost = input("How much did your next item cost? (type 'done' to finish)")
    if cost == "done":
       break
    else:
        total_cost += float(cost)

over_under = budget - total_cost

if over_under<0:
    print(f"You were ${abs(over_under):.2f} over budget!")

elif over_under == 0:
    print(f"You spent your budget of ${total_cost:.2f}")

else:
    print(f"You still have ${over_under:.2f} left of your budget")


if __name__ == '__main__':
    main()
