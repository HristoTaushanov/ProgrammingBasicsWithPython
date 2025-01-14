import math

book_pages_count = int(input())
pages_per_hour_count = int(input())
days_needed_count = int(input())
hours_to_read_the_whole_book = book_pages_count / pages_per_hour_count
hours_per_day = math.floor(hours_to_read_the_whole_book / days_needed_count)
print(hours_per_day)
