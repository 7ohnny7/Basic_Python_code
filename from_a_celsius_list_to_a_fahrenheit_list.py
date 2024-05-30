def fahrenheit(celsius):
    """Convert degrees Celsius to Fahrenheit"""
    return ((9 * celsius) / 5) + 32



def fahrenheit_list(celsius_list):
    """Convert a list of temperatures in degrees Celsius to degrees Fahrenheit"""
    for i in range(0, len(celsius_list)):
        celsius_list[i] = fahrenheit(celsius_list[i])
    return celsius_list
