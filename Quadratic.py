import cmath  # for complex number support

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = (b**2) - (4*a*c)

# Find two solutions
sol1 = (-b + cmath.sqrt(d)) / (2*a)
sol2 = (-b - cmath.sqrt(d)) / (2*a)

print(f"The solutions are: {sol1} and {sol2}")
