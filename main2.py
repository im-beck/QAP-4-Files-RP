# Program Description: This program will allow the user to enter the total amount of sales for each month and then
#                      plot it onto a graph.
# Written by: Rebecca Pond
# Written on: July 22, 2023

# IMPORTED LIBRARIES
import matplotlib.pyplot as plt
import FormatValues as FV

# MAIN PROGRAM

MonthsLst = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SalesLst = []

for Month in MonthsLst:
    Sales = float(input(f"Enter the total sales for {Month}: "))
    SalesLst.append(Sales)


plt.plot(MonthsLst, SalesLst)

plt.xlabel("Months")
plt.ylabel("Sales")

plt.title("Graph of Total Sales per Month")


plt.show()

