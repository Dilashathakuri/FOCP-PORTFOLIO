
to_seconds = lambda hours, minutes=0: (hours * 3600) + (minutes * 60)


print("Total seconds for 1 hour:", to_seconds(1))  
print("Total seconds for 2 hours:", to_seconds(2)) 
print("Total seconds for 1 hour and 30 minutes:", to_seconds(1, 30))  
print("Total seconds for 3 hours and 15 minutes:", to_seconds(3, 15)) 
