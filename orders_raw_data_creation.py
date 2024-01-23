import pandas as pd
import datetime
import names
from random import choice, choices, randint, sample, uniform

'''CREATION OF THE CUSTOMERS TABLE'''
# define the list of unique segments and the number of customers to be generated
segment_choices = ['Consumer', 'Corporate', 'Small Business']
num_customers = 400

# initialize the remaining lists that will be used as columns in the product table
customer_ids, customer_names, segments = ([] for i in range(3))

# for the number of customers defined above, generate the data required to populate the Customer table
for i in range(0, num_customers):
    customer_ids.append(10000 + i)
    name = names.get_full_name()
    # allow a 1/15 chance for white-spaces to be added in front of the customer's name
    rand_num = randint(1, 15)
    if rand_num == 1:
        name = "        " + name
    customer_names.append(name)
    segments.append(choice(segment_choices))

# the Customers table is created using the generated data
customer_info = {'Customer ID': customer_ids, 'Customer Name': customer_names, 'Segment': segments}
customer_df = pd.DataFrame(customer_info)


'''CREATION OF THE LOCATIONS TABLE'''
# define the lists of unique cities, states and countries (note the values across these lists are associated by index)
cities = ['Toronto', 'Brampton', 'Guelph', 'Montreal', 'New York', 'Los Angeles', 'Chicago', 'Houston', 'Paris', 'Madrid', 'London', 'Cambridge', 'Berlin', 'Milan', 'Mexico City', 'Melbourne', 'Sydney', 'Bangkok', 'Kuantan', 'Mumbai']
states = ['Ontario', 'Ontario', 'Ontario', 'Quebec', 'New York', 'California', 'Illinois', 'Texas', 'Ile-de-France', 'Madrid', 'England', 'England',' Berlin', 'Lombardy', 'Distrito Federal', 'Victoria', 'New South Wales', 'Bangkok', 'Pahang', 'Konkan']
countries = ['Canada', '     Canada', 'Canada',  'Canada', 'United States', 'United Staates', 'United States', 'United States', 'France', 'Spain', 'United Kingdom', 'United   Kingdom', 'Germany', 'Italy', 'Mexico', 'Australia', 'Australia', '   Thailand', 'Malaysia', 'India']

# define a dictionary which maps each country to its corresponding shipping multiplier and prefix respectively
additional_country_info = {'Canada': [1.00, 'CA'], '     Canada': [1.00, 'CA'], 'United States': [1.05, 'US'], 'United Staates': [1.05, 'US'], 'France': [1.10, 'FR'], 'Spain': [1.10, 'SP'], 'United Kingdom': [1.10, 'UK'], 'United   Kingdom': [1.10, 'UK'],
                            'Germany': [1.10, 'GE'], 'Italy': [1.10, 'IT'], 'Mexico': [1.05, 'MX'], 'Australia': [1.20, 'AU'], 'Thailand': [1.15, 'TH'], '   Thailand': [1.15, 'TH'],'Malaysia': [1.15, 'ML'], 'India': [1.15, 'IN']}

# for each location, retrieve and store its shipping multiplier
shipping_multipliers = []
for i in range(len(cities)):
    shipping_multipliers.append(additional_country_info.get(countries[i])[0])

# the Locations table is created using the generated data
city_info = {'City': cities, 'State': states, 'Country': countries, 'Shipping Multiplier': shipping_multipliers}
location_df = pd.DataFrame(city_info)


'''CREATION OF THE PRODUCTS TABLE'''
# define the list of unique product names
product_names = ['Nokia Smart Phone', 'Samsung Smart Phone', 'Apple Smart Phone', 'Cisco Smart Phone', 'OnePlus Smart Phone', 'Sony Smart Phone', 'LG Smart Phone', 'Motorola Smart Phone', 'Huawei Smart Phone', 'BlackBerry Smart Phone',
                'Brother Wireless Fax Machine', 'Brother Copy     Machine', 'HP Wireless Fax', 'HP Inkjet Printer', 'StarTech Printer', 'Epson Printer', 'Canon Printer', 'Sharp Printer', 'Xerox Printer', 'Lexmark Printer',
                'Hoover Microwave', 'KitchenAid Microwave', 'Hamilton Beach Microwave', 'Breville Microwave', '  Samsung Microwave', 'LG Microwave', 'Cuisinart Microwave', 'Panasonic Microwave', 'Whirlpook Microwave', 'Toshiba Microwave',
                'Samsung Television', 'Panasonic Television', 'LG Television', 'Sony Television', 'Toshiba Television', 'Philips Television', 'Insignia Television      ', 'Supersonic Television', 'Sharp Television', 'TCL Television',
                '      Cuisinart Stove', 'Breville Stove', 'KitchenAid Stove', 'Hoover Stove', 'Hamilton Beach Stove', 'Whirlpool Stove', 'LG Stove', 'HiSense Stove', 'Samsung Stove', 'Maytag Stove']

# generate a list of randomly selected numbers to be used as part of each product id
product_id_nums = sample(range(10000000, 10009999), len(product_names))

# initialize the remaining lists that will be used as columns in the product table
product_ids, sale_prices, base_profits, local_shipping_costs = ([] for i in range(4))

# for each product, dependent on its type, set the associated prefix, sale price, local shipping cost and base profit 
for product in product_names:
    if 'Phone' in product:
        prefix = 'PH'
        sale_price = round(uniform(500.00, 1000.00), 2)
        local_shipping_cost = round(sale_price * uniform(0.03, 0.07), 2)
        base_profit = round(sale_price * 0.20, 2)
    elif 'Copy' in product or 'Fax' in product or 'Printer' in product:
        prefix = 'PR'
        sale_price = round(uniform(80.00, 280.00), 2)
        local_shipping_cost = round(sale_price * uniform(0.07, 0.12), 2)
        base_profit = round(sale_price * 0.15, 2)
    elif 'Microwave' in product:
        prefix = 'MI'
        sale_price = round(uniform(140.00, 310.00), 2)
        local_shipping_cost = round(sale_price * uniform(0.07, 0.12), 2)
        base_profit = round(sale_price * 0.12, 2)
    elif 'Television' in product:
        prefix = 'TV'
        sale_price = round(uniform(700.00, 1400.00), 2)
        local_shipping_cost = round(sale_price * uniform(0.15, 0.20), 2)
        base_profit = round(sale_price * 0.22, 2)
    elif 'Stove' in product:
        prefix = 'ST'
        sale_price = round(uniform(600.00, 1300.00), 2)
        local_shipping_cost = round(sale_price * uniform(0.20, 0.30), 2)
        base_profit = round(sale_price * 0.25, 2)

    # append each value determined above to its corresponding list
    product_ids.append(prefix + '-' + str(product_id_nums[0]))
    product_id_nums.pop(0)
    sale_prices.append(sale_price)
    base_profits.append(base_profit)
    local_shipping_costs.append(local_shipping_cost)

# the Products table is created using the generated data
product_info = {'Product ID': product_ids, 'Product Name': product_names, 'Sale Price': sale_prices, 'Base Profit': base_profits, 'Local Shipping Cost': local_shipping_costs}
product_df = pd.DataFrame(product_info)


'''CREATION OF THE ORDERS TABLE'''
# define a start date, end date and calculate the number of days between the two (all order dates will be between these start and end dates)
start_date = datetime.date(2018, 1, 1)
end_date = datetime.date(2022, 12, 31)
num_days = (end_date - start_date).days

# initialize the lists that will hold the data for each column of the Orders table
order_ids, order_dates, customer_ids, customer_names, customer_segments, cities, states, countries, product_ids, product_names, quantities, discounts, sale_prices, shipping_costs, profits = ([] for i in range(15))

# define the last index for each of the Products, Locations and Customers tables
last_product_df_index = product_df.shape[0] - 1
last_location_df_index = location_df.shape[0] - 1
last_customer_df_index = customer_df.shape[0] - 1

# set the number of orders and create a list of randomly generated numbers to be used as part of each order id
num_orders = 1000
order_id_nums = sample(range(1000000, 1999999), num_orders)

# create a list of discounts and quantities ordered, each randomly generated using weighted choices
discount_choices = [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
quantity_choices = [1, 2, 3, 4, 5, 6, 7]
weights=[0.5, 0.15, 0.10, 0.10, 0.05, 0.05, 0.05]
discounts = choices(population=discount_choices, weights=weights, k=num_orders)
quantities = choices(population=quantity_choices, weights=weights, k=num_orders)

# each record in the Orders table is populated as defined below
for i in range(0, num_orders):
    # a random date between the start and end dates is selected
    random_days = randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=random_days)
    order_dates.append(random_date)

    # a random customer from the Customers table is selected and their data is added to the current record of the Orders table
    random_customer = randint(0, last_customer_df_index)
    customer_ids.append(customer_df.iloc[random_customer]['Customer ID'])
    customer_names.append(customer_df.iloc[random_customer]['Customer Name'])
    customer_segments.append(customer_df.iloc[random_customer]['Segment'])

    # a random location from the Locations table is selected and its data is added to the current record of the Orders table
    random_location = randint(0, last_location_df_index)
    cities.append(location_df.iloc[random_location]['City'])
    states.append(location_df.iloc[random_location]['State'])
    countries.append(location_df.iloc[random_location]['Country'])
    shipping_multiplier = location_df.iloc[random_location]['Shipping Multiplier']

    # a random product from the Products table is selected and its data is added to the current record of the Orders table
    random_product = randint(0, last_product_df_index)
    product_ids.append(product_df.iloc[random_product]['Product ID'])
    product_names.append(product_df.iloc[random_product]['Product Name'])
    sale_price = product_df.iloc[random_product]['Sale Price']
    base_profit = product_df.iloc[random_product]['Base Profit']
    local_shipping_cost = product_df.iloc[random_product]['Local Shipping Cost']

    # the shipping cost, final sale price and profit of the current order are then calculated and added to the current record
    shipping_costs.append(round(local_shipping_cost * shipping_multiplier, 2))
    sale_prices.append(round(sale_price*quantities[i], 2))
    profits.append(round(base_profit*quantities[i] + shipping_costs[i]*0.10, 2))

    # using the prefix and year of the randomly selected country and order date respectively, an order id is set, completing the current record
    country_prefix = additional_country_info.get(countries[i])[1]
    year_prefix = random_date.strftime('%Y')
    order_ids.append(country_prefix + '-' + year_prefix + '-' + str(order_id_nums[i]))

# the Orders table is created using the generated data
order_info = {'Order ID': order_ids, 'Order Date': order_dates, 'Customer ID': customer_ids, 'Customer Name': customer_names, 'Segment': customer_segments, 'City': cities, 'State': states, 'Country': countries,
              'Product ID': product_ids, 'Product Name': product_names, 'Quantity': quantities, 'Discount': discounts, 'Sale Price': sale_prices, 'Shipping Cost': shipping_costs, 'Profit': profits}
order_df = pd.DataFrame(order_info)


# define the last index of the Orders table, the number of rows to be duplicated and generate a list of random indices to be duplicated
last_order_df_index = order_df.shape[0] - 1
num_duplicates = randint(20, 50)
duplicate_row_indices = sample(range(0, last_order_df_index), num_duplicates)

# for each index to be duplicated, copy the data in the row
# next randomly select a row in the table to place the duplicated data
# move the data from this index to be replaced to the end of the table
# finally overwrite the data at the randomly selected index to the duplicated data
for duplicate_row_index in duplicate_row_indices:
    duplicate_row_data = order_df.iloc[duplicate_row_index]
    replacement_index = randint(0, order_df.shape[0] - 1)
    replacement_row_data = order_df.iloc[replacement_index]
    order_df.loc[order_df.shape[0]] = replacement_row_data
    order_df.loc[replacement_index] = duplicate_row_data

# write the Orders table to an excel file
order_df.to_excel('orders_raw_data.xlsx', index=False, sheet_name='Raw Data')
