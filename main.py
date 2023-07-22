# Program Description: This is a program for One Stop Insurance Company to enter and calculate
# new insurance policy information for its customers.
# Written by: Rebecca Pond
# Written on: July 18, 2023

# REQUIRED LIBRARIES
import datetime
import FormatValues as FV

# CONSTANTS/DATA FILE
f = open("OSICDef.dat", "r")
POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
LIABILITY = float(f.readline())
GLASS_COVERAGE = float(f.readline())
LOANER_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PAYMENTS = float(f.readline())
f.close()

# MAIN PROGRAM
while True:
    CustFirst = input("Enter your first name (End to close the program): ").title()
    if CustFirst == "End":
        break
    CustLast = input("Enter your last name: ").title()
    Address = input("Enter your street address: ").title()
    City = input("Enter your city: ").title()

    while True:
        Prov = input("Enter your province (LL): ").upper()
        ProvLst = ["NL", "NS", "PE", "NB", "QB", "ON", "MB", "SK", "AB", "BC", "YT", "NT"]
        if Prov == "":
            print("Error - Province cannot be blank.")
        elif len(Prov) != 2:
            print("Error - Province must be 2 letters only.")
        elif Prov not in ProvLst:
            print("Error - Not a valid province.")
        else:
            break

    PostalCode = input("Enter your postal code: ").upper()
    PhoneNum = input("Enter your phone number (9999999999) : ")

    NumCars = int(input("Enter the number of cars being insured: "))
    ExtraLiability = input("Do you want extra liability up to $1,000,000? (Y/N): ").upper()
    Glass = input("Do you want glass coverage? (Y/N): ").upper()
    LoanerCar = input("Do you want a loaner car? (Y/N): ").upper()

    while True:
        PayMethod = input("Do you wish to pay in full or monthly installments?: ").title()
        PayMethLst = ["Full", "Monthly"]
        if PayMethod == "":
            print("Error - You must select a payment method.")
        elif PayMethod not in PayMethLst:
            print("Error - Please select either full or monthly.")
        else:
            break

# CALCULATIONS

    Premium = BASIC_PREMIUM * NumCars
    if NumCars > 1:
        Premium = (BASIC_PREMIUM * NumCars) - (BASIC_PREMIUM * NumCars * ADD_CAR_DISCOUNT)

    AddCarDisc = BASIC_PREMIUM * NumCars * ADD_CAR_DISCOUNT

    CostLiability = 0
    if ExtraLiability == "Y":
        CostLiability = NumCars * LIABILITY

    CostGlass = 0
    if Glass == "Y":
        CostGlass = NumCars * GLASS_COVERAGE

    CostLoaner = 0
    if LoanerCar == "Y":
        CostLoaner = NumCars * LOANER_COVERAGE

    TotalExtraCost = CostLiability + CostGlass + CostLoaner
    TotalInsPrem = Premium + TotalExtraCost
    HST = TotalInsPrem * HST_RATE
    TotalCost = TotalInsPrem + HST

    ProcessingFee = 0
    if PayMethod == "Monthly":
        ProcessingFee = (MONTHLY_PAYMENTS + TotalCost) / 8

    InvDate = datetime.datetime.now()
    PayDate = InvDate.replace(day=1) + datetime.timedelta(days=31)

# OUTPUT
    print()
    print("               ONE STOP INSURANCE COMPANY")
    print("              Insurance Policy Information")
    print(
        f"INVOICE DATE: {FV.FDateShort(InvDate):>10s}         NEXT PAYMENT DATE: {FV.FDateShort(PayDate):>10s}")
    print("-" * 62)
    print("Customer Information")
    print("-" * 21)
    print(f"First Name:   {CustFirst:<20s}")
    print()
    print(f"Last Name:    {CustLast:<20s}")
    print()
    print(f"Address:      {Address:>12s}")
    print(f"              {City}, {Prov}")
    print()
    print(f"Postal Code:  {PostalCode}")
    print()
    print(f"Phone Number: {FV.FPhoneNumber(PhoneNum):>12s}")
    print("-" * 62)
    print("Insurance Information")
    print("-" * 21)
    print(f"Number of Cars: {NumCars}")
    print()
    print(f"Liability: {ExtraLiability}")
    print()
    print(f"Glass Coverage: {Glass}")
    print()
    print(f"Payment Method: {PayMethod}")
    print()
    print(f"Loaner Car: {LoanerCar}")
    print("-" * 62)
    print("Total")
    print("-" * 21)
    print(f"Insurance Premium:", "-"*33, f"{FV.FDollar2(Premium):>9s}")
    print(f"Additional Car Discount:", "-"*27, f"{FV.FDollar2(AddCarDisc):>9s}")
    print(f"Extra Liability Charge:", "-"*28, f"{FV.FDollar2(CostLiability):>9s}")
    print(f"Glass Coverage Charge:", "-"*29, f"{FV.FDollar2(CostGlass):>9s}")
    print(f"Loaner Car Charge:", "-"*33, f"{FV.FDollar2(CostLoaner):>9s}")
    print("-" * 21)
    print(f"Total Extra Cost:", "-"*34, f"{FV.FDollar2(TotalExtraCost):>9s}")
    print(f"Total Insurance Premium:", "-"*27, f"{FV.FDollar2(TotalInsPrem):>9s}")
    print(f"HST:", "-"*47, f"{FV.FDollar2(HST):>9s}")
    print(f"Total:", "-"*45, f"{FV.FDollar2(TotalCost):>9s}")
    print("-" * 21)
    print(f"Processing Fee:", "-"*36, f"{FV.FDollar2(ProcessingFee):>9s}")
    print("-" * 62)


    import time
    from tqdm import tqdm
    print()
    print()
    print("Saving policy information - please wait")
    # Processing bar
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)



    # FUTURE REFERENCE FILE
    f = open("Policies.dat", "a")
    f.write(f"{POLICY_NUM}, ")
    f.write(f"{InvDate}, ")
    f.write(f"{CustFirst}, ")
    f.write(f"{CustLast}, ")
    f.write(f"{Address}, ")
    f.write(f"{City}, ")
    f.write(f"{Prov}, ")
    f.write(f"{PostalCode}, ")
    f.write(f"{PhoneNum}, ")
    f.write(f"{NumCars}, ")
    f.write(f"{ExtraLiability}, ")
    f.write(f"{Glass}, ")
    f.write(f"{LoanerCar}, ")
    f.write(f"{PayMethod}\n")
    f.close()

    print("Policy information processed and saved.")
    time.sleep(1)

    POLICY_NUM += 1




