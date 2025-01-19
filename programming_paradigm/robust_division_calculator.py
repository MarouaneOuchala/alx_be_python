def safe_divide(numerator, denominator):
    """
    Safely performs division between two numbers with error handling.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        str: Result message or error message
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."
            
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
        
    except ValueError:
        return "Error: Please enter numeric values only."
    
    # Error: Please enter numeric values only."
    #Error: Please enter numeric values only.
