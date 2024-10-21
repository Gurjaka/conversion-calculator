"""
A simple unit conversion program that allows the user to convert between different
units of length, temperature, area, volume, and weight. The user selects a conversion
type, chooses the units to convert from and to, enters the value, and receives the
converted result.

Supports:
- Length conversion (e.g., meters, kilometers)
- Temperature conversion (Celsius, Fahrenheit, Kelvin)
- Area conversion (e.g., square meters, acres)
- Volume conversion (e.g., liters, gallons)
- Weight conversion (e.g., kilograms, pounds)

Main Features:
- Menu-driven interface
- Supports multiple types of unit conversions
- Error handling for invalid inputs
"""

def conversion_menu():
    """
    Displays a menu of available conversion types (e.g., length, temperature) and 
    prompts the user to choose one. Returns the selected conversion type.

    Returns:
        str: The chosen conversion type (e.g., 'length', 'temperature').
    """
    menu_size = len(max(conversion_type, key=len)) + 4
    print('_'*menu_size)
    for index, elem in enumerate(conversion_type):
        print(f'{index}) {elem.title()}')
    print('-'*menu_size)

    while True:
        from_dict = input('--> ').lower()
        if from_dict.isdigit() and int(from_dict) in range(len(conversion_type)):
            return conversion_type[int(from_dict)]
        if from_dict in conversion_type:
            return from_dict
        print('404 Not found!')

def from_dict_items():
    """
    Prints the available units for the selected conversion type (e.g., for length, 
    it might display millimeter, meter, kilometer, etc.).
    """
    menu_size = len(max(unit_conversions, key=len)) + 4
    print('_'*menu_size)
    for i in unit_conversions:
        print(i)
    print('-'*menu_size)

def convert_temperature(val, unit1, unit2):
    """
    Converts a temperature value from one unit to another. Supports Celsius, Kelvin, and Fahrenheit.

    Args:
        val (float): The temperature value to convert.
        from_unit (str): The current unit of the temperature ('celsius', 'kelvin', 'fahrenheit').
        to_unit (str): The target unit to convert to ('celsius', 'kelvin', 'fahrenheit').

    Returns:
        float: The converted temperature value.

    Raises:
        ValueError: If the from_unit or to_unit is not a valid temperature unit.
    """
    # First convert to Celsius
    if unit1 == 'celsius':
        celsius = val
    elif unit1 == 'kelvin':
        celsius = val - 273.15
    elif unit1 == 'fahrenheit':
        celsius = (val - 32) * 5/9
    else:
        raise ValueError("Invalid from_unit. Choose 'celsius', 'kelvin', or 'fahrenheit'.")

    # Now convert from Celsius to the target unit
    if unit2 == 'celsius':
        return celsius
    if unit2 == 'kelvin':
        return celsius + 273.15
    if unit2 == 'fahrenheit':
        return (celsius * 9/5) + 32
    raise ValueError("Invalid to_unit. Choose 'celsius', 'kelvin', or 'fahrenheit'.")

conversion_type = ['exit', 'length', 'temperature', 'area', 'volume', 'weight']

conversion = {
    'length': {
        'nanometer': 1,
        'micrometer': 10**-3,
        'millimeter': 10**-6,
        'centimeter': 10**-7,
        'inch': 3.93701*10**-8,
        'foot': 3.28084*10**-9,
        'yard': 1.09361*10**-9,
        'meter': 10**-9,
        'mile': 6.21371*10**-13,
        'kilometer': 10**-12,
        'light year': 1.057*10**-25
    },
    'temperature': ['celsius', 'kelvin', 'fahrenheit'],
    'area': {
        'square millimeter': 1,
        'square centimeter': 0.01,
        'square meter': 0.000001,
        'acre': 0.000000247105,
        'hectare': 0.0000001,
        'square kilometer': 0.000000000001,
        'square mile': 0.000000000386102,
    },
    'volume': {
        'milliliter': 1,
        'liter': 0.001,
        'us gallon': 0.0002641722,
        'us quart': 0.0010566887,
        'us pint': 0.0021133774,
        'us cup': 0.0042267548,
        'us fluid ounce': 0.0338140386,
        'us table spoon': 0.0676280773,
        'us tea spoon': 0.2028842318,
        'imperial gallon': 0.0002199692,
        'imperial quart': 0.000879877,
        'imperial pint': 0.001759754,
        'imperial fluid ounce': 0.0351950797,
        'imperial table spoon': 0.0563121276,
        'imperial tea spoon': 0.1689363827,
        'cubic meter': 0.000001,
        'cubic kilometer': 9.999999999E-16,
        'cubic centimeter': 1,
        'cubic millimeter': 1000,
        'cubic mile': 2.399128636E-16,
        'cubic inch': 0.0610237441,
        'cubic foot': 0.0000353147,
        'cubic yard': 0.000001308,
    },
    'weight': {
        'atomic mass unit': 1,
        'milligram': 1.660540199E-21,
        'carrat': 8.302700999E-24,
        'gram': 1.660540199E-24,
        'ounce': 5.85738796E-26,
        'pound': 3.660867475E-27,
        'kilogram': 1.660540199E-27,
        'short ton': 1.830433737E-30,
        'metric ton': 1.660540199E-30,
        'long ton': 1.634315837E-30,
    }
}

selected_conversion = conversion_menu()
unit_conversions = conversion[selected_conversion]
from_dict_items()

while True:
    print('Choose "from" unit:')
    from_unit = input('--> ').lower()
    if from_unit in unit_conversions:
        break
    print('Unit not found!')

while True:
    print('Choose "to" unit:')
    to_unit = input('--> ').lower()
    if to_unit in unit_conversions:
        break
    print('Unit not found!')

while True:
    print('Choose value:')
    value = input('--> ')
    try:
        value = float(value)
        break
    except ValueError:
        print('Must be a number!')

match selected_conversion:
    case 'temperature':
        converted = convert_temperature(value, from_unit, to_unit)
    case _:
        converted = value * (unit_conversions[from_unit]/unit_conversions[to_unit])
print('Converted value:', converted)
