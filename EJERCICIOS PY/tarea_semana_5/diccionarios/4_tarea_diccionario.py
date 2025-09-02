# Given a list of sales with the following information:

# date

# customer_email

# items

# And each item having the following information:

# name

# upc

# unit_price

# Create a dictionary that stores the total sales for each UPC.

sales=[
    {
        "date":"07/01/2025",
        "costumer_email":"pedropablo@gmail.com",
        "items":[
            {
                "name":"book",
                "upc":"ITEM-01",
                "unit_price": 10.00,
            },
            {
                "name":"notebook",
                "upc":"ITEM-02",
                "unit_price":5.00,
            },
            {
                "name":"pencil",
                "upc":"ITEN-03",
                "unit_price":1.00,
            }
        ]   
    },
    {
        "date":"07/01/2025",
        "costumer_email":"juanlopez@hotmail.com",
        "items":[
            {
                "name":"pen",
                "upc":"ITEM-04",
                "unit_price": 2.00,
            },
            {
                "name":"backpack",
                "upc":"ITEM-05",
                "unit_price": 30.00,
            },
            {
                "name":"computer_mouse",
                "upc":"ITEM-110",
                "unit_price": 20,
            },
            {
                "name":"keyboard",
                "upc":"ITEM-120",
                "unit_price": 25,
            }
        ]
    },
    {
        "date":"07/01/2025",
        "costumer_email":"mariasanchez@yahoo.com",
        "items":[
            {
                "name":"plates",
                "upc":"ITEM-320",
                "unit_price": 12.00,
            },
            {
                "name":"glass_cup",
                "upc":"ITEM-330",
                "unit_price": 12.00
            },
            {
                "name":"book",
                "upc":"ITEM-01",
                "unit_price": 10.00,
            },
            {
                "name":"backpack",
                "upc":"ITEM-05",
                "unit_price":30.00,
            },
        ],
    },
]


result={}

for sale in sales:
    for item in sale["items"]:
        upc=item["upc"]
        unit_price=item["unit_price"]
        if upc in result:
            result[upc]+=unit_price
        else:
            result[upc]=unit_price
print(result)