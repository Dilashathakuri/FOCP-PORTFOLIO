
to_seconds = lambda hours, minutes: (hours * 3600) + (minutes * 60)


print("Total seconds for 1 hour and 30 minutes:", to_seconds(1, 30))
print("Total seconds for 2 hours and 45 minutes:", to_seconds(2, 45))
print("Total seconds for 0 hours and 5 minutes:", to_seconds(0, 5))
print("Total seconds for 0 hours and 0 minutes:", to_seconds(0, 0))
print("Total seconds for 3 hours and 0 minutes:", to_seconds(3, 0))
