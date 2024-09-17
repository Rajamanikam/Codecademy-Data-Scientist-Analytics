"""
Working with Python Lists: Medical Insurance Costs Project
"""


names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here

#adding new name & cost
names.append("Priscilla")
insurance_costs.append(8320.0)

#combining names & insurance costs using zip() function

medical_records = list(zip(names, insurance_costs))

print(medical_records)

# no of records using len()
print("\n")
num_medical_records = len(medical_records)
print(f"There are {num_medical_records} medical records.")

# first medical record
print("\n")
first_medical_record = medical_records[0]
print(f"Here is the first medical record: {first_medical_record}")


# sorting records based on insurance cost using sort() function with key parameter

medical_records.sort(key=lambda x: x[1])
print("\n")
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

# Cheapest 3 insurance costs

cheapest_three = medical_records[0:3]
print("\n")
print(f"Here are the three cheapest insurance costs in our medical records: {cheapest_three}")

# Most expensive 3 insurance costs

priciest_three = medical_records[-3:]
print("\n")
print(f"Here are the three most expensive insurance costs in our medical records: {priciest_three}")


occurrences_paul = names.count('Paul')
print("\n")
print(f"There are {occurrences_paul} individuals with the name Paul in our medical records.")



### Extra Tasks ###
print("\n")

print("*********************************************")
insurance_records = list(zip(names, insurance_costs))

print(insurance_records)
# Sort the medical records alphabetically by name
print("\n")
insurance_records.sort()
print("Insurance records sorted alphabetically by name :\n",insurance_records)

print("\n")
middle_five_records = insurance_records[3:8]

print("Middle five records :\n",middle_five_records)
