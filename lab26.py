#Input the month name
Month_name = input("Enter month name: March.").lower() # Convert to lowercase for case-insensitive comparison

#Determine the number of days based on the month
if Month_name== "january" or Month_name == "march" or Month_name == "may" or \
Month_name == "july" or Month_name == "August" or Month_name == "october" or Month_name == "december":
    days = 31
elif Month_name == "april" or Month_name == "june" or Month_name =="september" or Month_name =="november":
    days=30
elif Month_name == "february":
    days =28 #Assuming it's not a leap year
else:
    days = "Invalid month name"

    # Print the result
    print(f"The number of the days in{Month_name.capitalize()} is: {days}")