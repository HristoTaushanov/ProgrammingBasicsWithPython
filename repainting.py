nylon_quantity = int(input())
paint_quantity = int(input())
thinner_quantity = int(input())
hours_needed = int(input())
total_nylon_quantity = nylon_quantity + 2
total_paint_quantity = paint_quantity + (paint_quantity * 0.10)
bags_cost = 0.40
total_materials_cost = (total_nylon_quantity * 1.50) + (total_paint_quantity * 14.50) + (thinner_quantity * 5.00) + bags_cost
labour_hourly_rate = total_materials_cost * 0.30
labour_total_cost = hours_needed * labour_hourly_rate
total_for_paining = total_materials_cost + labour_total_cost
print(total_for_paining)