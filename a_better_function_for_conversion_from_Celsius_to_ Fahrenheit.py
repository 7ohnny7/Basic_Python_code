def fahrenheit(celsius):
    """Convert degrees Celsius to Fahrenheit"""
    return ((9 * celsius) / 5) + 32



def fahrenheit_list(celsius_list):
    """Convert a list of temperatures in degrees Celsius to degrees Fahrenheit"""
    fahrenheit_list = []
    for celsius_temp in celsius_list:
        fahrenheit_temp = fahreheit(celsius_temp)
        fahrenheit_list = fahrenheit_list + [fahrenheit_temp]
    return fahrenheit_list

