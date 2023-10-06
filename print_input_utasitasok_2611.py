#print("Tell me anything...")
#anything = input()
#print("Hmm...", anything, "... Really?")
#print("\n")

#anything2 = input("Tell me anything...")
#print("Hmm...", anything2, "...Really?")
#print("\n")

#anything3 = float(input("Enter a number: "))
#something3 = anything3 ** 2.0
#print(anything3, "to the power of 2 is", something3)
#print("\n")

#leg_a = float(input("Input first leg length: "))
#leg_b = float(input("Input second leg length: "))
#hypo = (leg_a**2 + leg_b**2) ** .5
#print("Hypotenuse length is", hypo)
#print("\n")

#fnam = input("May I have your first name, please? ")
#lnam = input("May I have your last name, please? ")
#print("Thank you.")
#print("\nYour name is " + fnam + " " + lnam + ".")
#print("\n")

#print("+" + 10 * "-" + "+")
#print(("|" + " " * 10 + "|\n") * 5, end="")
#print("+" + 10 * "-" + "+")
#print("\n")

#a=float(input("adj meg egy értéket:"))# input a float value for variable a here
#b=float(input("adj meg egy másik értéket:"))# input a float value for variable b here

#print(a+b)# output the result of addition here
#print(a-b)# output the result of subtraction here
#print(a*b)# output the result of multiplication here
#print(a/b)# output the result of division here

#print("\nThat's all, folks!")
#print("\n")

# Input: Start time in hours and minutes, and duration in minutes
start_hours = int(input("Enter the start hours (0-23): "))
start_minutes = int(input("Enter the start minutes (0-59): "))
duration_minutes = int(input("Enter the duration in minutes: "))

# Calculate the end time in minutes
end_time_minutes = (start_hours * 60 + start_minutes + duration_minutes) % (24 * 60)

# Calculate the end hours and end minutes
end_hours = end_time_minutes // 60
end_minutes = end_time_minutes % 60

# Print the result in the required format
print(f"The event will end at {end_hours:02}:{end_minutes:02}")

