pen_pack_count = int(input())
marker_pack_count = int(input())
litters_count = int(input())
discount = int(input())
discount_rate = float(discount / 100)
total_for_pens = pen_pack_count * 5.80
total_for_markers = marker_pack_count * 7.20
total_for_liquid = litters_count * 1.20
total_sum = total_for_pens + total_for_markers + total_for_liquid
final_sum = total_sum - (total_sum * discount_rate)
print(final_sum)
