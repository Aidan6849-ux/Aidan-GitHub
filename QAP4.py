# Description: QAP4, One Stop Insurance Company.
# Author: Aidan
# Date(s): March 27

# Define required libraries.
import datetime
import os

# Define the file path. 
file_path = "Policies.dat"

# Check and be sure the file actually exists. 
##if not os.path.exists(file_path):
##    with open(file_path) as file:
##        file.write("Policy Number, Customer Name, Total Cost, Monthly Payment, Claims\n")



# Define all of the program constants.

NEXT_POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
DISCOUNT_CAR = 0.25
LIABILITY_COST = 130.00
GLASS_COST = 86.00
LOANER_COST = 58.00
HST_RATE = 0.15
PROCESSING_FEE = 39.99
PROVINCES = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland", 
             "Nova Scotia", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan"]
PAYMENT_METHODS = ["Full", "Monthly", "Down Pay"]

# I listed all provinces and added their full names.
# For the actual constants I kept the words all in caps.



# Define program functions.
# Function to calculate insurance premium
def calculate_premium(num_cars, liability, glass, loaner):
    premium = BASIC_PREMIUM
    if num_cars > 1:
        premium += (num_cars - 1) * BASIC_PREMIUM * (1 - DISCOUNT_CAR)
    
    extra_costs = 0
    if liability == 'Y':
        extra_costs += LIABILITY_COST * num_cars
    if glass == 'Y':
        extra_costs += GLASS_COST * num_cars
    if loaner == 'Y':
        extra_costs += LOANER_COST * num_cars

    total_premium = premium + extra_costs
    return total_premium


# This is the function to validate and format the input values.
def format_values(value, is_title_case=False, is_upper_case=False):
    if is_title_case:
        value = value.title()
    if is_upper_case:
        value = value.upper()
    return value





# Function to calculate HST and total cost. 
# Here I have a function that returns multiple values.
def calculate_hst_and_total_cost(premium):
    hst = premium * HST_RATE
    total_cost = premium + hst
    return hst, total_cost



# This if the function to calculate the  monthly payment
def calculate_monthly_payment(total_cost, payment_method, down_payment=0):
    if payment_method == "Full":
        return total_cost
    else:
        total_cost_with_fee = total_cost + PROCESSING_FEE
        if payment_method == "Down Pay":
            total_cost_with_fee -= down_payment
        monthly_payment = total_cost_with_fee / 8
        return monthly_payment

# Main program starts here.
while True:
    # Gather user inputs.
    print("Enter customer details  :")
    
    first_name = input("First Name: ").strip()
    if first_name == "END":
        break
    last_name = input("Last Name: ").strip()
    address = input("Address: ").strip()
    city = input("City: ").strip()
    province = input("Province: ").strip()
    
    while province not in PROVINCES:
        print("Invalid province. Please enter a valid province .")
        province = input("Province: ").strip()
    
    postal_code = input("Postal Code: ").strip()
    phone_number = input("Phone Number: ").strip()
    num_cars = int(input("Number of Cars: ").strip())

    liability = input("Extra Liability Coverage (Y/N): ").strip().upper()
    glass = input("Glass Coverage (Y/N): ").strip().upper()
    loaner = input("Loaner Car Coverage (Y/N): ").strip().upper()

#Here comes the payment section. 
    payment_method = input("Payment Method (Full, Monthly, Down Pay): ").strip().title()
    while payment_method not in PAYMENT_METHODS:
        print("Invalid payment method. Please enter Full, Monthly, or Down Pay.")
        payment_method = input("Payment Method (Full, Monthly, Down Pay): ").strip().title()

    down_payment = 0
    if payment_method == "Down Pay":
        down_payment = float(input("Enter Down Payment: ").strip())

    # This is the previous claim info for the customer.
    claims = []
    while True:
        claim_number = input("Enter Claim Number (or type 'done' to finish): ").strip()
        if claim_number.lower() == 'done':
            break
        claim_date = input("Enter Claim Date (YYYY-MM-DD): ").strip()
        claim_amount = float(input("Enter Claim Amount: ").strip())
        claims.append((claim_number, claim_date, claim_amount))

    # Perform required calculations.
    total_premium = calculate_premium(num_cars, liability, glass, loaner)
    hst, total_cost = calculate_hst_and_total_cost(total_premium)
    monthly_payment = calculate_monthly_payment(total_cost, payment_method, down_payment)





    # Display results. Keep everythibng in proper order.
    # For the second line down, i kept the customer first and last name on the same line.
    print(f"Policy Number: {NEXT_POLICY_NUMBER}")
    print(f"Customer: {format_values(first_name)} {format_values(last_name)}")
    print(f"Address: {address}")
    print(f"City: {format_values(city, is_title_case=True)}")
    print(f"Province: {format_values(province, is_title_case=True)}")
    print(f"Postal Code: {postal_code}")
    print(f"Phone Number: {phone_number}")
    print(f"Number of Cars Insured: {num_cars}")
    print(f"Liability Coverage: {liability}")
    print(f"Glass Coverage: {glass}")
    print(f"Loaner Car Coverage: {loaner}")
    print(f"Total Premium: ${total_premium:.2f}")
    print(f"HST: ${hst:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

    if payment_method == "Full":
        print(f"Total Payment: ${total_cost:.2f}")
    else:
        print(f"Monthly Payment: ${monthly_payment:.2f}")

    # Displaying all of the claims. Here is where i had to do some additional research
    # and try a few things 
    print("            Previous Claims          :")
    print("  Claim #      Claim Date       Amount")
    print("--------------------------------------------")
    for claim in claims:
        print(f"{claim[0]}   {claim[1]}   ${claim[2]:,.2f}")
    
    NEXT_POLICY_NUMBER += 1

    # Write the values to a data file for storage. 
    # Same here with the above display results section. Keep everything in proper order.
    # This is where i have had diffuculty.
    with open("Policies.dat,") as file:
        file.write(f"Policy Number: {NEXT_POLICY_NUMBER - 1} ")
        file.write(f"Customer: {first_name} {last_name} ")
        file.write(f"Address: {address} ")
        file.write(f"City: {city} ")
        file.write(f"Province: {province} ")
        file.write(f"Postal Code: {postal_code} ")
        file.write(f"Phone Number: {phone_number} ")
        file.write(f"Number of Cars: {num_cars} ")
        file.write(f"Liability: {liability} ")
        file.write(f"Glass Coverage: {glass} ")
        file.write(f"Loaner Car: {loaner} ")
        file.write(f"Total Premium: ${total_premium:.2f} ")
        file.write(f"HST: ${hst:.2f} ")
        file.write(f"Total Cost: ${total_cost:.2f} ")
        file.write(f"Monthly Payment: ${monthly_payment:.2f} ")
        file.write(f"Claims: {claims} ")

# Any housekeeping duties at the end of the program.
print("Program has finished!! The Data has been written to Policies.dat.")

# I have had difficulty with making the policies.dat file work. 
# Lines 12-15 i commented them out because for the life of me that is the only 
# thing i could not figure out and i still need the program to run.
