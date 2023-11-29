# Storing patient names and insurance costs
medical_costs = {}

medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0
medical_costs.update({"Connie": 8886.0, "Isaac":16444.0, "Valentina": 6420.0})
medical_costs["Vinay"] = 3325.0

# print(medical_costs)
# print(medical_costs.keys())
# print(medical_costs.values())

total_costs = 0

for cost in medical_costs.values():
  total_costs += cost
print(total_costs)

average_cost = total_costs / len(medical_costs)
print(average_cost)

# List Comprehension to Dictionary
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27,24,43,35,52]

zipped_ages = zip(names, ages)
# print(*zipped_ages)

names_to_ages = {name: age for name, age in zipped_ages}
print(names_to_ages, '\n')

mariana_age = names_to_ages.get('Marina')
print(f'Mariana\'s age is {mariana_age}')
print()

# Using Dictionary to create a medical database
medical_records = {}

medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

medical_records['Vinay'] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}

medical_records['Isaac'] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}

medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

print(medical_records, '\n')

print('Connie\'s insurance cost is {} dollars'.format(medical_records['Connie'].get('Insurance_cost')))

medical_records.pop('Vinay')
# print(medical_records.keys())
print()

for name, record in medical_records.items():
  print("{Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}".format(Name= name, Age= record['Age'], Sex= record['Sex'], BMI= record['BMI'], Smoker= record['Smoker'], Insurance_cost= record['Insurance_cost']))


# Further coding: function
"""
# Create a function called update_medical_records() that takes in the name of an individual 
as well as their medical data, and then updates the medical_records dictionary accordingly.
# Create a new dictionary of your choice – feel free to get creative!
"""