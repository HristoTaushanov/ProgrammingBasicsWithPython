chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())
delivery_price = 2.50
total_price_chicken = chicken_menu_count * 10.35
total_price_fish = fish_menu_count * 12.40
total_price_vegetarian = vegetarian_menu_count * 8.15
total_sum = total_price_chicken + total_price_fish + total_price_vegetarian
desert_price = total_sum * 0.20
final_sum = delivery_price + desert_price + total_price_chicken + total_price_fish + total_price_vegetarian
print(final_sum)
