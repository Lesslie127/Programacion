def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit
def celsius_to_kelvin(celsius):
    kelvin = (celsius)+273.15
    return kelvin

celsius=30
fahrenheit=celsius_to_fahrenheit(celsius)
kelvin=celsius_to_kelvin(celsius)

print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit y {kelvin} grados Kelvin")
