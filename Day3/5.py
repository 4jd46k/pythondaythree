# Generate a list of square numbers between 1 and 30 (both included)
squares = [x**2 for x in range(1, 6)] + [x**2 for x in range(5, 0, -1)]

print("First 5 elements:", squares[:5])
print("Last 5 elements:", squares[-5:])
