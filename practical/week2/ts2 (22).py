###TASK: Work out in your head what the contents of the ‘nums’ list would be, then check this using the Python interpreter.

nums = [1, 2, 3, 4, 5]
nums = [num * 2 for num in nums]  # Multiply each element by 2
nums.extend([6, 7])  # Append 6 and 7
nums = nums[2:]  # Remove the first two elements

print(nums)