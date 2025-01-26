class Calculator:
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers, referencing the class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Usage Example
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(5, 10)
    print(f"Sum: {sum_result}")  # Output: Sum: 15

    # Using the class method
    product_result = Calculator.multiply(4, 3)
    print(f"Product: {product_result}")  # Output: Calculation type: Arithmetic Operations
                                        #         Product: 12
