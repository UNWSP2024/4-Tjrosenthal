# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.


#Tanner Rosenthal
#2/13/2025
def main():

total_months = 0
total_rainfall = 0.0

years = int(input("How many years of rainfall are you measuring?"))
for year in range(1,years+1):
    for month in range(1,13):
       rainfall = float(input(f"What is the rainfall in month {month} of year {year}"))
       total_rainfall += rainfall


print(f"In {years} years, which is {years * 12} months, it rained {total_rainfall:.2f} inches") 


if __name__ == '__main__':
    main()
