# main.py (Provided for Testing)

from class_static_methods_demo import Calculator

def main():
    # Using the static method (@staticmethod)
    # The method runs like a regular function, independent of the class state.
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method (@classmethod)
    # The method automatically receives the class itself as 'cls', 
    # allowing it to print the class attribute.
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()