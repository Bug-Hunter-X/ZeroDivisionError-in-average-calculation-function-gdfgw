def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage (will now return 0):
result = calculate_average([]) 
print(result) # Output: 0

# Example with numbers
result2 = calculate_average([10,20,30])
print(result2) #Output: 20.0