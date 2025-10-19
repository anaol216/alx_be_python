# class_static_methods_demo.py

class Calculator:
    """
    A class demonstrating the usage of static methods and class methods.
    """
    # 1. Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Performs an addition. 
        It does not require access to the class (cls) or instance (self).
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Performs a multiplication. 
        It takes 'cls' as the first argument, allowing it to access 
        class-level attributes like calculation_type.
        """
        # Accessing the class attribute using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# End of class_static_methods_demo.py