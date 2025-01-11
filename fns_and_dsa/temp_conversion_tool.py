FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def calculation():
    try:
        prompt_temp = float(input("Enter the temperature to convert: "))
        prompt_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        def unit_choice(unit):
            match unit:
                case 'C':
                    result = convert_to_fahrenheit(prompt_temp)
                    print(f"{prompt_temp}°C is {result:.2f}°F")
                case 'F':
                    result = convert_to_celsius(prompt_temp)
                    print(f"{prompt_temp}°F is {result:.2f}°C")
                case _:
                    print("Invalid temperature. Please enter a numeric value.")
        
        unit_choice(prompt_unit)
    
    except ValueError:
        print("Invalid input. Please enter a valid numeric temperature.")

calculation()

