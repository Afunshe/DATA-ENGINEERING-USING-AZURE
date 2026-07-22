# IMPORT DATA AND READ FILE
#Import library pandas

import pandas as pd
#Reading the CSV file
df = pd.read_csv("C:/Users/Admin/Documents/AI DATA ENGINEER HAPPINESS/Data Sets/cleaned_sales.csv")

#Confirm file was found and read successfully
#print(df.head())

#Understanding the dataset
#print(df.info())

#Import Data Viz library
import matplotlib

#Import Package
import matplotlib.pyplot as plt

#impoort numpy for mathematical calculation
import numpy as np


#Which region has the region has the highest number of transaction
#Bar chart Question
region_sale = df['Region'].value_counts()
#print(region_sale)

region_sale.plot(kind="bar")
plt.title("Number of Transaction by Region")
plt.xlabel("Region")
plt.ylabel("Transaction")
plt.show()
 
#LINE CHART
#How do sales change over time by calculating the monthly sales
df["OrderDate"] = pd.to_datetime(df["OrderDate"]) #converting the date column data type.
monthly_sales = df.groupby(df["OrderDate"].dt.month)["SalesAmount"].sum()
print(monthly_sales)
monthly_sales.plot(kind = "line", marker = "o" )
plt.title("Monthly Sales")
plt.xlabel("Month Sales")
plt.ylabel("Sales")
plt.grid()
plt.show()


#Which payment method are used often
#Pie chart is used to show proportion of large chart
#which payment methods are used often
payment = df["PaymentMethod"].value_counts()
payment.plot(kind = "pie", autopct = "%1.1f%%")
plt.title("Payment Method")
plt.ylabel("Pie Chart")
plt.show()


##Exercise 1
#Create a bar chart showing the number of products sold by Category.
product_sales = df["Product"].value_counts()
#print (product_sales)
product_sales.plot(kind= "bar")
plt.title("Product Sold by Category")
plt.xlabel("Product")
plt.ylabel("Category")
plt.show()

##Exercise 2
##Create a pie chart showing the percentage of transactions by Region.
region = df["Region"].value_counts()
region.plot(kind="pie",autopct="%1.1f%%")
plt.title("Regional Transaction Percentages")
plt.ylabel("")
plt.show()

##Exercise 3
##Create a histogram of the Quantity column.
plt.hist(df["Quantity"], bins=5)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

#CREATING ALL THREE VISUALISATION AND DISPLAYING AT THESAME TIME
# Bar Chart
# -------------------------------
category_count = df["Category"].value_counts()
category_count.plot(kind="bar")
plt.title("Products Sold by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products Sold")
plt.show()

# Pie Chart
# -------------------------------
region_count = df["Region"].value_counts()
region_count.plot(kind="pie", autopct="%1.1f%%", startangle=90)

plt.title("Percentage of Transactions by Region")
plt.ylabel("")
plt.show()

# -------------------------------
# Histogram
# -------------------------------
plt.hist(df["Quantity"], bins=10)
plt.title("Distribution of Quantity Sold")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()
