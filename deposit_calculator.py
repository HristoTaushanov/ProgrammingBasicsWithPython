deposit_sum = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())
increased_sum = deposit_sum + (deposit_term * ((deposit_sum * annual_interest_rate / 100) / 12))

print(increased_sum)
