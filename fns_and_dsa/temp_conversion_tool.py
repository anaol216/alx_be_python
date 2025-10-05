# Define Global Conversion Factors
# Factors are defined as expressions to ensure float division for accurate results
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using a global conversion factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # The global factor is accessed without the 'global' keyword because we are only reading its value
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using a global conversion factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # The global factor is accessed without the 'global' keyword because we are only reading its value
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Handles user interaction for the temperature conversion tool.
    """
    try:
        # User Input: Temperature
        temp_input = input("Enter the temperature to convert: ")
        
        # Input Validation: Check if temperature is a numeric value
        try:
            temperature = float(temp_input)
        except ValueError:
            # Raise the specified error message for non-numeric input
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # User Input: Unit
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        unit = unit_input.strip().upper()

        # Conversion logic
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        # Catch and display the specific error message
        print(e)
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()