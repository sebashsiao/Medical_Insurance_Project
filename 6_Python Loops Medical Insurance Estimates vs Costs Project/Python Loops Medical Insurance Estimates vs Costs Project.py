names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Sum total actual insurance costs
total_cost = 0
# for cost in actual_insurance_costs:
#   total_cost += cost
# While loop approach
i = 0
while i < len(actual_insurance_costs):
  total_cost += actual_insurance_costs[i]
  i += 1

# Average cost of insurance
average_cost = total_cost / len(actual_insurance_costs)
print(f"Average Insurance Cost: {average_cost}")

# for loop with range on list length
# for i in range(len(names)):
# While loop approach
i = 0
while i < len(names):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("- The insurance cost for {0} is {1} dollars.".format(name, insurance_cost))
  if insurance_cost > average_cost:
    print(f"\t(+) The insurance cost for {name} is above average.")
  elif insurance_cost < average_cost:
    print(f"\t(-) The insurance cost for {name} is below average.")
  else:
    print(f"\t(=) The insurance cost for {name} is equal to the average.")
  i += 1

# creating list comprehension
updated_estimated_costs = [cost * 11/10 for cost in estimated_insurance_costs]

print(updated_estimated_costs)