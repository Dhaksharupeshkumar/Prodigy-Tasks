def temperature_converter(temperature, unit):
  """
  This function converts a temperature value between Celsius, Fahrenheit, and Kelvin scales.

  Args:
      temperature: The temperature value to be converted.
      unit: The original unit of measurement (Celsius, Fahrenheit, or Kelvin).

  Returns:
      A dictionary containing the converted temperature values in Celsius, Fahrenheit, and Kelvin.
  """

  converted_values = {}
  if unit.upper() == "C":
    converted_values["Fahrenheit"] = (temperature * 9/5) + 32
    converted_values["Kelvin"] = temperature + 273.15
  elif unit.upper() == "F":
    converted_values["Celsius"] = (temperature - 32) * 5/9
    converted_values["Kelvin"] = (temperature - 32) * 5/9 + 273.15
  elif unit.upper() == "K":
    converted_values["Celsius"] = temperature - 273.15
    converted_values["Fahrenheit"] = (temperature - 273.15) * 9/5 + 32
  else:
    print("Invalid unit of measurement. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
    return

  return converted_values

# Get user input
while True:
  try:
    temperature = float(input("Enter temperature value: "))
    unit = input("Enter unit (C, F, or K): ").upper()
    break
  except ValueError:
    print("Invalid input. Please enter a numerical temperature value.")

# Convert temperature and display results
converted_temperatures = temperature_converter(temperature, unit)

print(f"Converted temperatures:")
for unit, value in converted_temperatures.items():
  print(f"{unit}: {value:.2f}")
