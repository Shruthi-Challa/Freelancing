import csv

with open("customers.csv", "r", newline = "") as file:
    reader = csv.reader(file)
    next(reader, None)

    seen = set()
    valid_customers = []
    for row in reader:
        with open("cleaned_customers.csv", "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["name", "email", "city"])
            writer.writerows(valid_customers)
        if row[1] == "":
            continue

        if row[1] in seen:
            continue
        
        seen.add(row[1])
        valid_customers.append(row)
        print(row)