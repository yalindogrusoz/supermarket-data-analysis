# Generated from: final_final_final (1).ipynb
# Converted at: 2025-12-30T13:51:33.050Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# **This is what you'll need to submit on Gradescope:**
# 
# 1. This notebook, completed.
# 2. Your data in csv form (as noted in the Data Cleaning section below).
# 3. Any other code you have written for your project.


# Yalin and Julian


# # Data cleaning
# 


# The first step to data analysis is ensuring that you are focussing on the subset of the data that you have complete information about.
# 
# 1. Having taken a look at your dataset, what columns and rows have you decided to drop from it? Why?
# 
# *A valid reason for dropping a column could be lack of information about the column, lack of a clear understanding of the units of measurement, a general feeling that it does not contain any useful information etc*
# 
# If you decided to focus on just a subset of your data please describe why you chose that subset and why you feel the other rows do not matter.


# ## Exploring the data


# Using sorting, groupby etc find out some interesting aspects of the data. Even a short fact counts. For instance, if you were working with population data, you could say that 25% of the world lives in South Asia after you do some group by commands.
# 
# In this section of your project try to find as many interesting facts as possible.


# # Visualizations


# Make at least 6 visualizations (if this number is unreasonable please talk to your mentoring TA before reducing it) that reveal something interesting about the data. Try to include at least one scatterplot and one histogram/bar graph (again, if the data does not lend itself to these plots do let us know


# Make sure that your visualizations
# 1. Have things like the axes, titles, units etc
# 2. Are telling a slightly interesting story. Interesting = something a person who has not seen this data might not be able to just guess.


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns



# **Euro Data**
# 
# 


euro_supermarket = pd.read_csv ("https://docs.google.com/spreadsheets/d/e/2PACX-1vRScR-0TO_hKlm4wRniG6BEqWvUvMwCV23sPJVSxn1Z0IlbdDWOmwSjaV9sk9b_k6Ot42qHfdt7HnC4/pub?output=csv")

# Deifining Functions


def date_seperator_month(date):
  lst = []
  lst = date.split("/")
  return lst[0]
def date_seperator_day(date):
  lst = []
  lst = date.split("/")
  return lst[1]
def date_seperator_year(date):
  lst = []
  lst = date.split("/")
  return lst[2][0:4]
def date_seperator_time(date):
  lst = []
  lst = date.split(" ")
  return lst[1]
def hour(time):
  if time[0:2].isnumeric() == True:
    return str(time[0:2])
  else:
    return str(time[0:1])
def rounder(number):
  number = str(number)
  lst = []
  lst = number.split(".")
  return int(lst[0])
weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
weekday_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
def week_dec(day, year):
  if year == 2010:
    return weeks[day % 7 + 1]
  else:
    return weeks[day % 7 + 2]
def week_jan(day):
  return weeks[day % 7 + 4]
def week_feb(day):
  return weeks[day % 7]
def week_mar(day):
  return weeks[day % 7]
def week_apr(day):
  return weeks[day % 7 + 3]
def week_may(day):
  return weeks[day % 7 + 5]
def week_jun(day):
  return weeks[day % 7 + 1]
def week_jul(day):
  return weeks[day % 7 + 3]
def week_aug(day):
  return weeks[day % 7 + 6]
def week_sep(day):
  return weeks[day % 7 + 2]
def week_oct(day):
  return weeks[day % 7 + 4]
def week_nov(day):
  return weeks[day % 7]
def week_decider(day, month, year):
  day = int(day)
  month = int(month)
  year = int(year)
  if month == 12:
    return week_dec(day, year)
  elif month == 11:
    return week_nov(day)
  elif month == 10:
    return week_oct(day)
  elif month == 9:
    return week_sep(day)
  elif month == 8:
    return week_aug(day)
  elif month == 7:
    return week_jul(day)
  elif month == 6:
    return week_jun(day)
  elif month == 5:
    return week_may(day)
  elif month == 4:
    return week_apr(day)
  elif month == 3:
    return week_mar(day)
  elif month == 2:
    return week_feb(day)
  elif month == 1:
    return week_jan(day)


# Data Cleaning


euro_supermarket["Time"] = euro_supermarket["InvoiceDate"].apply(date_seperator_time)
euro_supermarket["Day"] = euro_supermarket["InvoiceDate"].apply(date_seperator_day)
euro_supermarket["Month"] = euro_supermarket["InvoiceDate"].apply(date_seperator_month)
euro_supermarket["Year"] = euro_supermarket["InvoiceDate"].apply(date_seperator_year)
euro_supermarket["TotalPrice"] = euro_supermarket["Quantity"] * euro_supermarket["UnitPrice"]
euro_supermarket["Hour"] = euro_supermarket["Time"].apply(hour)
euro_supermarket["Weekday"] = euro_supermarket.apply(lambda row: week_decider(row['Day'], row['Month'], row['Year']), axis=1)
euro_supermarket = euro_supermarket.drop(columns = ["InvoiceDate", "Description", "StockCode", "CustomerID"])
euro_supermarket.columns
x = ['InvoiceNo', 'Quantity', 'UnitPrice', 'TotalPrice', 'Country', 'Time', 'Day', 'Month', 'Year', 'Hour', 'Weekday']
euro_supermarket = euro_supermarket[x]
euro_supermarket

# Arranging Cleaned Data for Usage


weekdays = []
for i in range (0,7):
  weekdays.append(len(euro_supermarket[euro_supermarket['Weekday'] == weeks[i]]))
weekdays_revenue = []
for i in range(0,7):
  weekdays_revenue.append(rounder(np.sum(euro_supermarket['TotalPrice'][euro_supermarket['Weekday'] == weeks[i]])))
print(weekdays)
print(weekdays_revenue)

lst = {}
countries = (euro_supermarket["Country"].unique())
for country in countries:
  lst[country] = len(euro_supermarket[euro_supermarket["Country"] == country])
list1 = lst.values()
print(sorted(lst.items(), key=lambda kv: (kv[1], kv[0]), reverse = True))



dec2010 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "12") & (euro_supermarket["Year"] == "2010")])
dec2010 = round(dec2010,-2)
jan2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "1") & (euro_supermarket["Year"] == "2011")])
jan2011 = round(jan2011,-2)
feb2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "2") & (euro_supermarket["Year"] == "2011")])
feb2011 = round(feb2011,-2)
mar2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "3") & (euro_supermarket["Year"] == "2011")])
mar2011 = round(mar2011,-2)
apr2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "4") & (euro_supermarket["Year"] == "2011")])
apr2011 = round(apr2011,-2)
may2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "5") & (euro_supermarket["Year"] == "2011")])
may2011 = round(may2011,-2)
jun2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "6") & (euro_supermarket["Year"] == "2011")])
jun2011 = round(jun2011,-2)
jul2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "7") & (euro_supermarket["Year"] == "2011")])
jul2011 = round(jul2011,-2)
aug2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "8") & (euro_supermarket["Year"] == "2011")])
aug2011 = round(aug2011,-2)
sep2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "9") & (euro_supermarket["Year"] == "2011")])
sep2011 = round(sep2011,-2)
oct2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "10") & (euro_supermarket["Year"] == "2011")])
oct2011 = round(oct2011,-2)
nov2011 = np.sum(euro_supermarket["TotalPrice"][(euro_supermarket["Month"] == "11") & (euro_supermarket["Year"] == "2011")])
nov2011 = round(nov2011,-2)
month_sales = [jan2011,feb2011,mar2011,apr2011,may2011,jun2011,jul2011,aug2011,sep2011,oct2011,nov2011,dec2010]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

len(euro_supermarket[euro_supermarket["Hour"] == "12"])
hours = []
for i in range(0,24):
  hours.append(len(euro_supermarket[euro_supermarket['Hour'] == str(i)]))
print(hours)
hours_prices = []
for i in range(0,24):
  hours_prices.append(rounder(round(np.sum(euro_supermarket['TotalPrice'][euro_supermarket['Hour'] == str(i)]),0)))
#for some reason the data for hour 6 shows that all of the purchases are negative?? I turned the number back positive.
hours_prices[6] = -hours_prices[6]
hours_prices.reverse()
print(hours_prices)
list_hours = []
for i in range (0,24):
  if i // 12 == 0:
    if i % 12 != 0 and i % 12 != 11:
      list_hours.append(str(i) + "AM - " + str(i + 1) + "AM")
    elif i % 12 == 0:
      list_hours.append("12AM - 1AM")
    else:
      list_hours.append("11AM - 12PM")
  else:
    if i % 12 != 0 and i % 12 != 11:
      list_hours.append(str(i%12) + "PM - " + str(i%12 + 1) + "PM")
    elif i % 12 == 0:
      list_hours.append("12PM - 1PM")
    else:
      list_hours.append("11PM - 12AM")
list_hours.reverse()

# ####Myanmar Data:


myanmar_supermarket = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRpzpaKqLmHmJNcL0nfOpvJPFVl5i1Qf1Wqi7uS4L4ZDeJvQ0gYaUAytBP5Qw90fgblK-IbGsNGKkCM/pub?output=csv")
myanmar_supermarket.columns

myanmar_supermarket = myanmar_supermarket.rename(columns={'Customer type': 'Membered?'})

x = ['City', 'Membered?', 'Gender', 'Product line', 'Unit price', 'Quantity', 'Total', 'Date', 'Time', 'Payment', 'Rating']

myanmar_supermarket = myanmar_supermarket[x]

def date_seperator_month(date):
  lst = []
  lst = date.split("/")
  return lst[0]
def date_seperator_day(date):
  lst = []
  lst = date.split("/")
  return lst[1]
def date_seperator_year(date):
  lst = []
  lst = date.split("/")
  return lst[2]

myanmar_supermarket["Month"] = myanmar_supermarket["Date"].apply(date_seperator_month)
myanmar_supermarket["Day"] = myanmar_supermarket["Date"].apply(date_seperator_day)
myanmar_supermarket["Year"] = myanmar_supermarket["Date"].apply(date_seperator_year)


def price_paid_rounded(price):
    return round(price)

#myanmar_supermarket_graphed = myanmar_supermarket['Total'].apply(round_to_dollars)
myanmar_supermarket['price_paid_rounded'] = myanmar_supermarket['Total'].apply(price_paid_rounded)
myanmar_supermarket

x = ['City', 'Membered?', 'Gender', 'Product line', 'Unit price', 'Quantity', 'Total', 'Time', 'Day', 'Month', 'Year', 'Payment', 'Rating']
myanmar_supermarket = myanmar_supermarket[x]

def main():
  x = input("""What data would you like to analyze?
  a) Global supermarket chain, all purchases
  b) Myanmar supermarket chain, select purchases
  c) See all
  """)
  while x != "a" and x != "b" and x!= "c":
    print("your only options are a and b, please re-enter")
    x = input("Input a,b and c?")
  if x == "a":
    z = input(""" What graph would you like to look at?
  a) Total revenue made for each month of the year
  b) Total revenue made for each day of the week
  c) Total revenue made for each hour of the day
  d) Total prices of each purchase made

  """)
    while z != "a" and z != "b" and z!="c" and z!="d":
      print("your only valid options are a,b,c and d.")
      z = input("please enter again")
    if z == "a":
      plt.barh(months, month_sales, color = "darkblue");
      plt.xlabel("Revenue made in that month, in dollars")
      plt.ylabel("Months")
      plt.title("Total revenue made in each month of the year, in million dollars")
      plt.show()
      print("""  Ways to improve:

        a) More stock during peak months -- discounts for buying in stock, no need to store stock during offpeak
        b) hire more staff during peak, less during offpeak
        c) have more seasonal items (fall months have more sales)



      """)

    elif z == "b":
      plt.bar(weekday_list, weekdays_revenue, color = "Cyan");
      plt.xlabel("Days of the week")
      plt.ylabel("Total revenue made in millions of dollars")
      plt.title("Total revenue made in each day of the week, in millions of dollars")
      plt.show()
      print("""
        a- Special deals on specific days such as Thursday
        b- Less/more employees in specific days according to activity
      """)
    elif z == "c":
      plt.figure(figsize = (7,7))
      plt.barh(list_hours, hours_prices, edgecolor = "black", color = "olive");
      plt.xlabel("Total Revenue made in hour");
      plt.ylabel("hour");
      plt.title("Total revenue(in million dollars) made in each hour of the day for one entire year's data");
      plt.show()
      print("""
        a- More/less employees in specific hours
        b- Store's active hours may be adjusted accordingly
      """)
    elif z == "d":
      sns.histplot(data = euro_supermarket, x = euro_supermarket["TotalPrice"], color = "gold", bins = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,125,150,175,200]).set_title("Prices paid by customers in dollars");
      plt.show()
      print("""  Ways to improve:

        a) Discount offers for bigger purchases
        b) Cash-back for members in store credit to insentivise making bigger purchases at this store instead of buying in fragments.
        c) Have express checkout lane in peak purchasing hours to encourage smaller purchases as-well.



      """)
  elif x == "b":
    y = input (""" What graph would you like to look at?
    a) Average Price Paid by Membered vs. Non-Membered Shoppers
    b) Customer Ratings vs. Price Paid
    c) Average Price Paid by Male vs. Female Shoppers
    d) Total Payment per Product Line
    """)
    while y != "a" and y != "b" and y!="c" and y!="d":
      print("your only valid options are a,b,c and d.")
      y = input("please enter again")
    if y == "a":
      mean_of_shoppers = myanmar_supermarket.groupby("Membered?")["Total"].mean()

      plt.figure(figsize=(5, 6))
      mean_of_shoppers.plot(kind="bar", color=['blue', 'green']) #without error bars
      std_of_shoppers = myanmar_supermarket.groupby("Membered?")["Total"].std()
      # mean_of_shoppers.plot(kind="bar", color=['blue', 'green'], yerr=std_of_shoppers, capsize = 5) # with error bars


      plt.title('Average Price Paid by Membered vs. Non-Membered Shoppers')
      plt.xlabel('Membered?')
      plt.ylabel('Average Price Paid')
      plt.xticks(rotation=360)


      plt.tight_layout()
      plt.show()

      print("""  Applications:

        a) Discounts for members
        b) Member exclusive deals, encourage those who spend more, to spend even more.
        c) Special perks for members such as faster checkout, or delivery service for groceries.



      """)
    elif y == "b":
      plt.figure(figsize=(6, 4))
      plt.scatter(myanmar_supermarket['Total'], myanmar_supermarket['Rating']);

      plt.xlabel('Price Paid (rounded to dollars)');
      plt.ylabel("Rating");
      plt.grid(True);
      plt.title('Customer Ratings vs. Price Paid')

      coefficients = np.polyfit(myanmar_supermarket['Total'], myanmar_supermarket['Rating'], 1 );
      slope = coefficients[0];
      intercept = coefficients[1];

      line_of_best_fit = slope * myanmar_supermarket['Total'] + intercept;
      plt.plot(myanmar_supermarket['Total'], line_of_best_fit, color='red', label='Line of best fit');
      plt.show()

      print("""  Applications:

        a) More expensive items should be very high quality, those who buy it are left happy.
        b) Less deals on higher priced items, people dont mind spending more.
        c) Create a paid - VIP experience for shoppers, higher spenders have a better shopping experience.


      """)
    elif y == "c":
      gender_means = myanmar_supermarket.groupby('Gender')['Total'].mean()

      plt.figure(figsize=(5, 6))
      gender_means.plot(kind="bar", color=['hotpink', 'blue'])

      plt.title('Average Price Paid by Male vs. Female Shoppers')
      plt.xlabel('Gender')
      plt.ylabel('Average Price Paid')
      plt.xticks(rotation=360)


      plt.tight_layout()
      plt.show()
      print("""  Applications:

        a) Higher quality and more expensive products for females -- they appreciate the quality and don't mind spending.
        b) Cheaper products for male oriented products, -- they would rather have less quality and spend a bit less.
        c) Deal for higher qualtity male targeted products, the deal makes them beleive their saving money and getting higher quality products.


      """)
    elif y == "d":
      total_payment_per_product = myanmar_supermarket.groupby('Product line')['Total'].sum()

      plt.figure(figsize=(8, 6))
      total_payment_per_product.plot(kind='barh', color='skyblue')
      plt.title('Total Payment per Product Line')
      plt.xlabel('Total Income ($)')
      plt.ylabel('Product Line ')
      plt.xticks(rotation=0)
      plt.tight_layout()

      plt.show()
      print("""  Applications:

        a) Higher prices foods and beverages which are also higher quality
        b) Deals on health and beauty products -- allowing people to get good products for less
        c) Staff tech experts for the tech area encouraging customers to buy higher quality products and pay more.


      """)
  elif x == "c":
    # a a
    plt.barh(months, month_sales, color = "darkblue");
    plt.xlabel("Revenue made in that month, in dollars")
    plt.ylabel("Months")
    plt.title("Total revenue made in each month of the year, in million dollars")
    plt.show()
    print("""  Ways to improve:
      a) More stock during peak months -- discounts for buying in stock, no need to store stock during offpeak
      b) hire more staff during peak, less during offpeak
      c) have more seasonal items (fall months have more sales)
    """)
    # a b
    plt.bar(weekday_list, weekdays_revenue, color = "Cyan");
    plt.xlabel("Days of the week")
    plt.ylabel("Total revenue made in millions of dollars")
    plt.title("Total revenue made in each day of the week, in millions of dollars")
    plt.show()
    print("""
      a- Special deals on specific days such as Thursday
      b- Less/more employees in specific days according to activity
    """)
    # a c
    plt.figure(figsize = (7,7))
    plt.barh(list_hours, hours_prices, edgecolor = "black", color = "olive");
    plt.xlabel("Total Revenue made in hour");
    plt.ylabel("hour");
    plt.title("Total revenue(in million dollars) made in each hour of the day for one entire year's data");
    plt.show()
    print("""
      a- More/less employees in specific hours
      b- Store's active hours may be adjusted accordingly
    """)
    #a d
    sns.histplot(data = euro_supermarket, x = euro_supermarket["TotalPrice"], color = "gold", bins = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,125,150,175,200]).set_title("Prices paid by customers in dollars");
    plt.show()
    print("""  Ways to improve:
      a) Discount offers for bigger purchases
      b) Cash-back for members in store credit to insentivise making bigger purchases at this store instead of buying in fragments.
      c) Have express checkout lane in peak purchasing hours to encourage smaller purchases as-well.
    """)
    #b a
    mean_of_shoppers = myanmar_supermarket.groupby("Membered?")["Total"].mean()
    plt.figure(figsize=(5, 6))
    mean_of_shoppers.plot(kind="bar", color=['blue', 'green']) #without error bars
    std_of_shoppers = myanmar_supermarket.groupby("Membered?")["Total"].std()
    # mean_of_shoppers.plot(kind="bar", color=['blue', 'green'], yerr=std_of_shoppers, capsize = 5) # with error bars
    plt.title('Average Price Paid by Membered vs. Non-Membered Shoppers')
    plt.xlabel('Membered?')
    plt.ylabel('Average Price Paid')
    plt.xticks(rotation=360)
    plt.tight_layout()
    plt.show()
    print("""  Applications:
      a) Discounts for members
      b) Member exclusive deals, encourage those who spend more, to spend even more.
      c) Special perks for members such as faster checkout, or delivery service for groceries.
    """)
    #b b
    plt.figure(figsize=(6, 4))
    plt.scatter(myanmar_supermarket['Total'], myanmar_supermarket['Rating']);
    plt.xlabel('Price Paid (rounded to dollars)');
    plt.ylabel("Rating");
    plt.grid(True);
    plt.title('Customer Ratings vs. Price Paid')
    coefficients = np.polyfit(myanmar_supermarket['Total'], myanmar_supermarket['Rating'], 1 );
    slope = coefficients[0];
    intercept = coefficients[1];
    line_of_best_fit = slope * myanmar_supermarket['Total'] + intercept;
    plt.plot(myanmar_supermarket['Total'], line_of_best_fit, color='red', label='Line of best fit');
    plt.show()
    print("""  Applications:

      a) More expensive items should be very high quality, those who buy it are left happy.
      b) Less deals on higher priced items, people dont mind spending more.
      c) Create a paid - VIP experience for shoppers, higher spenders have a better shopping experience.


    """)
    #b c
    gender_means = myanmar_supermarket.groupby('Gender')['Total'].mean()
    plt.figure(figsize=(5, 6))
    gender_means.plot(kind="bar", color=['hotpink', 'blue'])
    plt.title('Average Price Paid by Male vs. Female Shoppers')
    plt.xlabel('Gender')
    plt.ylabel('Average Price Paid')
    plt.xticks(rotation=360)
    plt.tight_layout()
    plt.show()
    print("""  Applications:

      a) Higher quality and more expensive products for females -- they appreciate the quality and don't mind spending.
      b) Cheaper products for male oriented products, -- they would rather have less quality and spend a bit less.
      c) Deal for higher qualtity male targeted products, the deal makes them beleive their saving money and getting higher quality products.
    """)
    #b d
    total_payment_per_product = myanmar_supermarket.groupby('Product line')['Total'].sum()
    plt.figure(figsize=(8, 6))
    total_payment_per_product.plot(kind='barh', color='skyblue')
    plt.title('Total Payment per Product Line')
    plt.xlabel('Total Income ($)')
    plt.ylabel('Product Line ')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
    print("""  Applications:
      a) Higher prices foods and beverages which are also higher quality
      b) Deals on health and beauty products -- allowing people to get good products for less
      c) Staff tech experts for the tech area encouraging customers to buy higher quality products and pay more.
    """)
main()
choice = "no"
if x == "c":
  quit()
while choice == "yes":
  main()
  choice = input("Would you like to view another graph, yes or no ")
while choice != "no":
  choice = input("That's an invalid input. Enter yes or no ")
if choice == "yes":
  main()



#