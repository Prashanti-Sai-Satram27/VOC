def convert_temperature(temp, unit):
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        celsius = (temp - 32) * 5 / 9
        return round(celsius, 2)
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        fahrenheit = (temp * 9 / 5) + 32
        return round(fahrenheit, 2)
    else:
        return "Invalid unit. Please use 'F' for Fahrenheit or 'C' for Celsius."


print(convert_temperature(100, 'F'))  


print(convert_temperature(37.78, 'C')) 
