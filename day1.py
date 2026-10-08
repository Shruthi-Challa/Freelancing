customers = [
    ["Tharun","tharun143@gmail.com","hyderebad"],
    ["Shruthi","Shruthi94@gmail.com","Eturnagaram"],
    ["Tharun","tharun143@gmail.com","hyderebad"],
    ["charan","Rajpet"],
    ["Shravani","Sravs123@gmail.com","Eturnagaram"]
]

valid_customers = []
seen = set()

for customer in customers:
    if len(customer)==3:
        if customer[1] not in seen:
            seen.add(customer[1])
            valid_customers.append(customer)

print(valid_customers)