annual_tax = int(input())
sneakers_price = annual_tax - (annual_tax * 0.40)
basketball_equipment_price = sneakers_price - (sneakers_price * 0.20)
ball_price = basketball_equipment_price / 4
accessories_price = ball_price / 5
total_price = annual_tax + sneakers_price + basketball_equipment_price + ball_price + accessories_price
print(total_price)
