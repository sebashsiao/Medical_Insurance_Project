# Lists of medical data
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Appending new data
names.append("Priscilla")
insurance_costs.append(8320.0)

# Combining  lists
medical_records = list(zip(names, insurance_costs))
print(medical_records)

# Print number of records
num_medical_records = len(medical_records)
print("- There are " + str(num_medical_records) + " medical records.")

# selecting list elements
first_medical_record = medical_records[0]
print("- Here is the first medical record: {}.".format(first_medical_record))

# Sort medical records by insurence cost
medical_records.sort(key= lambda medical_records: medical_records[1], reverse=False)
print("- Here are the medical records sorted ny insurance cost: {}.".format(medical_records))

# Slicing three cheapest 3 insurence records
cheapest_three = medical_records[:3]
print("- Here are the three cheapest insurance costs in our medical records: {}".format(cheapest_three))

# Slicing three most expensive 3 insurence records
priciest_three = medical_records[-3:]
print("- Here are the three most expensive insurance costs in our medical records: {}".format(priciest_three))

# Counting elements in a list
ocurrences_paul = names.count("Paul")
print("- There are {} individuals withe name Paul in our medical records.".format(ocurrences_paul))


# Sorting medical records by name
med_records_names = list(zip(names, insurance_costs))
sorted_med_records = sorted(med_records_names, reverse=False)
print("- Here are the medical records sorted by names: {}".format(sorted_med_records))

#slicing meddle five records
middle_five_records = sorted_med_records[3:8]
print("- Here are the middle five medical records: {}".format(middle_five_records))