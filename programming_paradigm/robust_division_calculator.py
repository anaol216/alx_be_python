def safe_divide(numerator, denominator):
    """Safely divide two values with error handling."""
    try:
        # convert inputs → float
        num = float(numerator)
        den = float(denominator)

        # division by zero check
        if den == 0:
            return "Error: Cannot divide by zero."

        # return result
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # non-numeric input
        return "Error: Please enter numeric values only."
