#Luluh Almogbil -  temperature converte system
'''
# Bonus
##  Temperature Converter

Description: In this exercise, you will practice using Python exceptions by creating a simple temperature converter 
that accepts user input and converts temperatures between Celsius and Fahrenheit. 
You will handle various exceptions that might arise during the conversion process.

#### Instructions:

1. Write a function `celsius_to_fahrenheit(celsius)` that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit. Use the formula `fahrenheit = (celsius * 9/5) + 32`.

2. Write a function `fahrenheit_to_celsius(fahrenheit)` that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius. Use the formula `celsius = (fahrenheit - 32) * 5/9`.

3. Write a `main` function that:
    - a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F").
    - b. Splits(its a function) the input string into a temperature value and its unit.
    - c. Tries to convert the input temperature to its opposite unit using the appropriate function (e.g., if the user enters a Celsius temperature, convert it to Fahrenheit).
    - d. Riases & handles the following exceptions:
        - `ValueError`: If the user enters an invalid temperature value, display an error message and prompt the user to try again.
        - `TypeError`: raise this error  If the user enters an invalid unit, display an error message and prompt the user to try again.
    - e. If the conversion is successful, print the converted temperature and its unit.

4. Call the `main` function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.

Example Output:

```
Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100 F
Temperature in Celsius: 37.78 C

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 50 C
Temperature in Fahrenheit: 122.0 F

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 25 X
Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100.5 F
Temperature in Celsius: 38.06 C
'''

def celsius_to_fahrenheit(celsius):
   # print("this function will convert from C to F: ")
    fahrenheit = (celsius * 9/5) + 32
    return (round(fahrenheit,2))

def fahrenheit_to_celsius(fahrenheit):
   # print("this function will convert from F to C: ")
    celsius = (fahrenheit - 32) * 5/9
    return (round(celsius,2))




def main():
    
    while True:
        try:
            
            convert = input("Enter a temperature and its unit (e.g., \"25 C\" or \"77 F\") : ")
            value,unit = convert.split() # "25 F"
            value = float(value)
            #print(value)
            #unit > 'F'
            #value > '77'

            if unit.upper() == 'C':
                print("Temperature in Fahrenheit:",celsius_to_fahrenheit(value),"F" ) 
                break
            elif unit.upper() == 'F':
                print("Temperature in Celsius:",fahrenheit_to_celsius(value),"C" )
                break
            else:
                raise TypeError("An exception raised.Please enter C or F for the units")
            
        except ValueError:
            print("invalid temperature value, please try again and make sure to enter a real number")
        except TypeError as t:
            print(t)
        except Exception as e:
            print("Something went wrong!")
        else:
            print("Every thing went successfully")
        finally:
            print("Finally block")

main()










    

    