medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hudson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# replace "#" with "$"
updated_medical_data = medical_data.replace('#', "$")

print(updated_medical_data)

num_records = 0
for character in updated_medical_data:
    if character == "$":
        num_records += 1

print(f'\nThere are {num_records} medical records in the data.')

# Separating individual record
medical_data_split = updated_medical_data.split(';')

print('\n', medical_data_split)

# Splitting single item in each record
medical_records = []
for i in medical_data_split:
    medical_records.append(i.split(","))

print('\n', medical_records)

# Clean white spaces of each item of records using nested loops
medical_records_clean = []
for record in medical_records:
    record_clean = []
    for item in record:
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)

print('\n', medical_records_clean)
print()
# Print the names of each individual medical record
for record in medical_records_clean:
    # print(record)
    print(record[0].upper())

# Store data in independent variables
names = []
ages = []
bmis = []
insurance_costs = []
for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])

print(f'\nNames: {names}', f'Ages: {ages}', f'BMI: {bmis}', f'Insurance Costs: {insurance_costs}', sep="\n")

# Calculate average BMI
total_bmi = 0
for bmi in bmis:
    total_bmi += float(bmi)

avg_bmi = total_bmi / len(bmis)

print(f"\nAverage BMI: {round(avg_bmi, 2)}")

# Calculate the average insurance cost
total_insurance_cost = 0
for cost in insurance_costs:
    total_insurance_cost += float(cost.strip("$"))

avg_insurance_cost = total_insurance_cost / len(insurance_costs)

print('Average Insurance Cost: {avg_cost}'.format(avg_cost=round(total_insurance_cost, 2)), '\n')

# Summary records print
for i in range(len(medical_records_clean)):
    print("{0}. {name} is {age} years old with a BMI of {bmi} and an insurance cost of {insurance_cost}.".format(
        i + 1, name=names[i], age=ages[i], bmi=bmis[i], insurance_cost=insurance_costs[i])
    )
