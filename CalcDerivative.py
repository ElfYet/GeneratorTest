import sympy as sp

def derivative_of_function(expression, variable):
    x = sp.symbols(variable)  # Define the variable
    function = sp.sympify(expression)  # Convert string to symbolic expression
    derivative = sp.diff(function, x)  # Compute the derivative
    return derivative

# Example usage:
expr = "x**2 + 3*x + 5"  # Define the function
variable = "x"
result = derivative_of_function(expr, variable)
print(f"The derivative of {expr} with respect to {variable} is: {result}")
