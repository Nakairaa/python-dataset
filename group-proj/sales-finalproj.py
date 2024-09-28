import csv


'''
author @nakaira
this function is an extension of the read_data function, 
allowing the user to choose between two data sets and further options tailored to each dataset
due to different columns. Provides various user inputs and if-else statements
most difficult part was mapping the functions to numbers in a dictionary to allow the selection
of a function, ran into a loop problem read_data instead of sales_data
'''


def read_data():
    userinput = input("Do you want to view the 'sales' or the 'car' dataset?: ")

    # sales options:
    if userinput == "sales":
        sales_data = []

        # open/read file
        with open('sales.csv', 'r') as csv_file:
            salessheet = csv.DictReader(csv_file)

            # loop through the data and put it all in a list, 'sales_data'
            for row in salessheet:
                sales_data.append(row)

            print("Available options are:\n1 The sales dataset\n2 The total sales for each month\n3 The total sales in that year")
            uinput = input("Select 1, 2 or 3: ")

            # created a dictionary to map the function to an integer, so the user can pick them in selection process
            function_map = {
                '1': sales_data,
                '2': run_sales_by_month,
                '3': run_total_sales
            }
            # retrieving the value from the dict 'function_map'
            if uinput in function_map:
                result = function_map[uinput]
                if callable(result):
                    result = result(sales_data)
                print(result)

        return sales_data

    # car prices options:
    elif userinput == "car":
        car_data = []
        with (open('car_prices.csv', 'r') as car_csv):
            spreadsheet = csv.DictReader(car_csv)
            for row in spreadsheet:
                car_data.append(row)

            print("Available functions are:\n1 The car dataset\n2 The top most expensive cars")
            uinput = input("Select 1 or 2: ")

            function_map = {
                '1': car_data,
                '2': top_n_expensive_cars,
                '3': run_total_sales
            }
            # retrieving the value from the dict 'function_map', checking if it's a callable function 2 and 3 are
            if uinput in function_map:
                result = function_map[uinput]
                if callable(result):
                    result = result(car_data)
                print(result)

            return uinput
    else:
        print("Unfortunately we have no records of that dataset, try again")
        return read_data()


def run_sales_by_month(sales_data):
    data = sales_data
    sales = []
    months = []
    for row in data:
        month = row['month']
        sale = int(row['sales'])
        months.append(month)
        sales.append(sale)
        combination = list(zip(months, sales))
    print(f'The sales for each month are as follows:\n{combination}')


# Returning total sales amount
def run_total_sales(sales_data):
    data = sales_data
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    total = sum(sales)
    print(f'Total sales: {total}')


'''
these parameters take in a user input to be able to specify how much top ££ cars they want to view
sorting and putting the prices into nlist, using sellingprice variable
'''


def top_n_expensive_cars(car_data):
    data = car_data  # getting the dat from the car spreadsheet
    n = int(input("How many do you want to view?: "))
    nlist = []  # creating an empty list to be able to populate it
    for row in data:
        # Only append rows that have a valid 'sellingprice'
        if row['sellingprice'].isdigit():  # Check if sellingprice is a valid number
            nlist.append(row)

    #sort list highest to lowest
    #lambda function is a small, anonymous function that can have any number
    # of arguments, but only one expression
    nlist.sort(key=lambda x: int(x['sellingprice']), reverse=True)

    # Get the top 'n' most expensive cars
    top_cars = nlist[:n]

    for car in top_cars:
        print(f"{car['make']} {car['model']} - £{car['sellingprice']}")
    return None


read_data()
