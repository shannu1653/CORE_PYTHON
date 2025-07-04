# list=("hi","hello",'welcome')
# for x in list:
#     print(x[0])

list=("hi","hello",'welcome','hello','hiii')
for x in range(len(list)-1,-1,-1):
    print(list[x])

list={"hi","hello",'welcome','hello','hiii'}
for x in list:
    print(x)
print("==============")

list=("hi","hello",'welcome','hello','hiii')
for x in range(1,len(list)-1):
    print(list[x])

import math
sum =0
for x in range(1,11):
    x +=1
    sum +=x
print(sum)
print("=============")

list=["awesome","hi","hello",'welcome','hello',"hiii",'hiii']
for x in list:
    if len(x) & 1==0:
        print(f"{x} is having length of {len(x)}")
print("=============================")

dict={"name":"suraj","gender":"male","age":28}
for x in dict:
    print(f"{x}:{dict[x]}")
    print("===================")
    
list_of_dictionary=[{"name":"suraj","gender":"male","age":28},{"name":"satish","gender":"male","age":28},
                    {"name":"naveen","gender":"male","age":28},{"name":"tharun","gender":"male","age":28},
                    {"name":"alpha","gender":"male","age":28}

]
for x in list_of_dictionary:
    print(x["name"])
# print(list_of_dictionary[3])
print("=======================")

dict1=[
    {
        "order_id": "ORD001",
        "customer_name": "Alice Johnson",
        "product": "Wireless Mouse",
        "category": "Electronics",
        "quantity": 2,
        "price_per_unit": 599,
        "payment_method": "Credit Card",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD002",
        "customer_name": "Rajesh Kumar",
        "product": "Bluetooth Speaker",
        "category": "Electronics",
        "quantity": 1,
        "price_per_unit": 1999,
        "payment_method": "UPI",
        "delivery_status": "Shipped"
    },
    {
        "order_id": "ORD003",
        "customer_name": "Maria Fernandez",
        "product": "Leather Handbag",
        "category": "Fashion",
        "quantity": 1,
        "price_per_unit": 2499,
        "payment_method": "Cash on Delivery",
        "delivery_status": "Out for Delivery"
    },
    {
        "order_id": "ORD004",
        "customer_name": "John Smith",
        "product": "Running Shoes",
        "category": "Footwear",
        "quantity": 1,
        "price_per_unit": 3499,
        "payment_method": "Net Banking",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD005",
        "customer_name": "Anjali Mehta",
        "product": "Cotton Bedsheet Set",
        "category": "Home & Living",
        "quantity": 3,
        "price_per_unit": 899,
        "payment_method": "Credit Card",
        "delivery_status": "Cancelled"
    },
    {
        "order_id": "ORD006",
        "customer_name": "Samuel Lee",
        "product": "Smart Watch",
        "category": "Wearable Tech",
        "quantity": 1,
        "price_per_unit": 5299,
        "payment_method": "Debit Card",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD007",
        "customer_name": "Neha Sharma",
        "product": "Makeup Kit",
        "category": "Beauty",
        "quantity": 2,
        "price_per_unit": 1499,
        "payment_method": "UPI",
        "delivery_status": "Processing"
    },
    {
        "order_id": "ORD008",
        "customer_name": "David Brown",
        "product": "Office Chair",
        "category": "Furniture",
        "quantity": 1,
        "price_per_unit": 4599,
        "payment_method": "Credit Card",
        "delivery_status": "Delivered"
    }
]

for x in dict1:
    if (x["category"]=="Electronics"):
        # print(f"{x}\n")   
        print("\n",x)

print(dict1[2]["category"])