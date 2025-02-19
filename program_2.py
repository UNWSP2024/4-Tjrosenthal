# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.


#Tanner Rosenthal
#02/12/2025

def main():

total_tickets = 0

while True:
    movie_name = input("What movie would you like to see? (type 'done' to finish)")
    if movie_name == "done":
        break

    ticket_number = int(input("How many tickets would you like?"))
    total_tickets += ticket_number

print("You bought", total_tickets, "tickets")

if __name__ == '__main__':
    main()
