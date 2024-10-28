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

class Menu:
    """
    Handles the user interface, displaying menus and getting user input for unit conversions.
    """

    def __init__(self, conversion_type, conversion):
        """
        Initializes the Menu object.

        Args:
            conversion_type: A list of available conversion types.
            conversion: A dictionary mapping conversion types to their corresponding units.
        """
        self.conversion_type = conversion_type
        self.selected_conversion = self.conversion_menu()
        self.unit_conversions = conversion[self.selected_conversion]
        self.display_units()
        self.unit1, self.unit2, self.value = self.get_units()

    def conversion_menu(self):
        """
        Displays a menu of conversion types and prompts the user to select one.

        Returns:
            The selected conversion type.
        """
        menu_size = len(max(self.conversion_type, key=len)) + 4
        print('_' * menu_size)
        for index, elem in enumerate(self.conversion_type):
            print(f'{index}) {elem.title()}')
        print('-' * menu_size)
        return self.dictionary_type()

    def dictionary_type(self):
        """
        Prompts the user to select a specific conversion type from the available options.

        Returns:
            The selected conversion type.
        """
        while True:
            try:
                from_dict = int(input('--> ').lower())
                if from_dict < 0 or from_dict >= len(self.conversion_type):
                    raise IndexError('Error: Please select a valid option!')
                return self.conversion_type[from_dict]
            except ValueError as e:
                print(f'Error: {e}. Please enter valid numeric value!')

    def display_units(self):
        """
        Displays a menu of available units for the selected conversion type.
        """
        menu_size = len(max(self.unit_conversions, key=len)) + 4
        print('_' * menu_size)
        for i, j in enumerate(self.unit_conversions):
            print(f'{i}) {j}')
        print('-' * menu_size)

    def get_units(self):
        """
        Prompts the user to select the "from" and "to" units, as well as the value to be converted.

        Returns:
            A tuple containing the "from" unit, "to" unit, and the value to be converted.
        """
        while True:
            try:
                print('Choose "from" unit:')
                from_unit = int(input('--> '))
                if from_unit < 0 or from_unit >= len(self.unit_conversions):
                    raise IndexError('Error: Please select a valid numeric value!')
                print(f'Choose [{self.unit_conversions[from_unit]}] to unit:')
                to_unit = int(input('--> '))
                if to_unit < 0 or to_unit >= len(self.unit_conversions):
                    raise IndexError('Error: Please select a valid numeric value!')
                print('Choose value:')
                value = float(input('--> '))
                return self.unit_conversions[from_unit], self.unit_conversions[to_unit], value
            except ValueError as e:
                print(f"Error: {e}. Please enter valid value.")
            except IndexError as e:
                print(e)


class Calculation:
    """
    Performs unit conversions for various categories (temperature, length, area, volume, weight).
    """

    def __init__(self, conversion_type, unit1, unit2, value):
        """
        Initializes the Calculation object.

        Args:
            conversion_type: The type of conversion (e.g., 'temperature', 'length').
            unit1: The "from" unit.
            unit2: The "to" unit.
            value: The value to be converted.
        """
        self.unit1 = unit1
        self.unit2 = unit2
        self.value = value
        match conversion_type:
            case 'temperature':
                self.result = self.temperature()
            case 'length':
                self.result = self.length()
            case 'area':
                self.result = self.area()
            case 'volume':
                self.result = self.volume()
            case 'weight':
                self.result = self.weight()

    def convert(self, factors):
        """
        Performs the actual conversion using the provided conversion factors.

        Args:
            factors: A dictionary mapping units to their conversion factors.

        Returns:
            The converted value.
        """
        value_in_base = self.value / factors[self.unit1]
        converted_value = value_in_base * factors[self.unit2]
        return converted_value

    def temperature(self):
        """
        Converts temperatures between Celsius, Fahrenheit, and Kelvin.

        Returns:
            The converted temperature.
        """
        match self.unit1, self.unit2:
            case 'celsius', 'fahrenheit':
                return self.value * (9 / 5) + 32
            case 'fahrenheit', 'celsius':
                return (self.value - 32) * 5 / 9
            case 'celsius', 'kelvin':
                return self.value + 273.15
            case 'kelvin', 'celsius':
                return self.value - 273.15
            case _:
                raise ValueError(f"Unsupported conversion from {self.unit1} to {self.unit2}")

    def length(self):
        """
        Converts lengths between various units.

        Returns:
            The converted length.
        """
        conversion_factors = {
            'nanometer': 1,
            'micrometer': 10**-3,
            'millimeter': 10**-6,
            'centimeter': 10**-7,
            'inch': 3.93701 * 10**-8,
            'foot': 3.28084 * 10**-9,
            'yard': 1.09361 * 10**-9,
            'meter': 10**-9,
            'mile': 6.21371 * 10**-13,
            'kilometer': 10**-12,
            'light year': 1.057 * 10**-25
        }

        return self.convert(conversion_factors)

    def area(self):
        """
        Converts area between various units.

        Returns:
            The converted area.
        """
        conversion_factors = {
            'square millimeter': 1,
            'square centimeter': 0.01,
            'square meter': 0.000001,
            'acre': 0.000000247105,
            'hectare': 0.0000001,
            'square kilometer': 0.000000000001,
            'square mile': 0.000000000386102,
        }

        return self.convert(conversion_factors)

    def volume(self):
        """
        Converts volume between various units.

        Returns:
            The converted volume.
        """
        conversion_factors = {
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
        }

        return self.convert(conversion_factors)

    def weight(self):
        """
        Converts weight between various units.

        Returns:
            The converted weight.
        """
        conversion_factors = {
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

        return self.convert(conversion_factors)

conversion_type = ['exit', 'length', 'temperature', 'area', 'volume', 'weight']

conversion = {
    'length': [
        'nanometer', 'micrometer', 'millimeter', 
        'centimeter', 'inch', 'foot', 'yard', 'meter', 
        'mile', 'kilometer', 'light year'
    ],
    'temperature': [ 'celsius', 'kelvin', 'fahrenheit' ],
    'area': [ 
        'square millimeter', 'square centimeter', 'square meter', 
        'acre', 'hectare', 'square kilometer', 'square mile'
    ],
    'volume': [
        'milliliter', 'liter', 'us gallon', 'us quart', 'us pint', 'us cup', 'us fluid ounce', 
        'us table spoon', 'us tea spoon', 'imperial gallon', 'imperial quart', 'imperial pint', 
        'imperial fluid ounce', 'imperial table spoon', 'imperial tea spoon', 'cubic meter', 
        'cubic kilometer', 'cubic centimeter', 'cubic millimeter', 'cubic mile', 'cubic inch', 
        'cubic foot', 'cubic yard'
    ],
    'weight': [
        'atomic mass unit', 'milligram', 'carrat', 'gram', 'ounce', 
        'pound', 'kilogram', 'short ton', 'metric ton', 'long ton'
    ]

}

menu = Menu(conversion_type, conversion)
calculation = Calculation(menu.selected_conversion, menu.unit1, menu.unit2, menu.value)

print(f'Value {menu.value} from {menu.unit1} to {menu.unit2} is {calculation.result}')
