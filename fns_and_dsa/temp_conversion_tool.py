FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    while True:
        temperature = int(input("Enter the temperature to convert: "))
        temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
        if temp_type == "C":
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
            break
        elif temp_type == "F":
            print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
            break
        else:
            print("Invalid temperature. Please enter a numeric value.")