# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    return f"The estimated insurance cost for {name} is {estimated_cost} dollars."

# Func2: Difference of insurance cost
def calculate_cost_difference(person1, person2):
    cost_person1 = calculate_insurance_cost(*person1).split(" ")[-2]
    cost_person2 = calculate_insurance_cost(*person2).split(" ")[-2]
    difference = float(cost_person1) - float(cost_person2)
    return f"The difference in insurance cost between the given two people is {difference} dollars."

# Maria & Omar data
maria_data = ('Maria', 28, 0, 26.2, 3, 0)
omar_data = ('Omar', 35, 1, 22.2, 0, 1)

# Calculate Maria's insurance cost
maria_cost = calculate_insurance_cost(*maria_data)
print(maria_cost)

# Calculate Omar's insurance cost
omar_cost = calculate_insurance_cost(*omar_data)
print(omar_cost)

# Calculate difference of insurance cost between 2 people
diff_cost = calculate_cost_difference(maria_data, omar_data)
print(diff_cost)


# # Initial variables for Maria 
# age = 28
# sex = 0  
# bmi = 26.2
# num_of_children = 3
# smoker = 0  

# # Estimate Maria's insurance cost
# insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

# print("The estimated insurance cost for Maria is " + str(insurance_cost) + " dollars.")

# # Initial variables for Omar
# age = 35
# sex = 1 
# bmi = 22.2
# num_of_children = 0
# smoker = 1  

# # Estimate Omar's insurance cost 
# insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

# print("The estimated insurance cost for Omar is " + str(insurance_cost) + " dollars.")