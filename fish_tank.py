tank_length = int(input())
tank_width = int(input())
tank_height = int(input())
percent = float(input())
percent_rate = percent / 100
tank_volume = tank_length * tank_width * tank_height
tank_volume_litters = tank_volume * 0.001
sand_volume = tank_volume_litters * percent_rate
water_volume = tank_volume_litters - sand_volume
print(water_volume)
