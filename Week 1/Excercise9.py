celcius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15

print(f"{celcius:.2f}°C = {fahrenheit:.2f}F = {kelvin:.2f}K")