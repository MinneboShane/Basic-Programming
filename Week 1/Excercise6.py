seconds = int(input("Enter the number of seconds:"))
days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print(f"d:h:m:s -> {days}:{hours}:{minutes}:{seconds}")