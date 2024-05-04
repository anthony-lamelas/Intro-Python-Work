days = int(input("How many days do you have?"))
hours= int(input("How many hours do you have?"))
minutes = int(input("How many minutes do you have?"))
seconds = int(input("How many seconds do you have?"))

total_seconds = days*(86400) + hours*(3600) + minutes*(60) + seconds

print(days, "Days", hours, "Hours", minutes, "Minutes and", seconds, "Seconds results in a total of", total_seconds, "Seconds")


