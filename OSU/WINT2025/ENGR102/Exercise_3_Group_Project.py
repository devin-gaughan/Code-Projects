
def celsius_to_fahrenheit(celsius_temp):
    """
    Converts a temperature from Celsius to Fahrenheit.
    
    Parameters:
        celsius_temp (float): Temperature in Celsius.
        
    Returns:
        float: Temperature in Fahrenheit.
    """
    return 32 + (celsius_temp * (9 / 5))

print(celsius_to_fahrenheit(-2))
