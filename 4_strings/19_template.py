# string.Template(string_with_variables) is a simpler, less error prone to string formatting
# values are indicated with $variable_name
# to set values we use template_name.substitute(key_value_pair)
import string  # necessary to import string library

template = string.Template('$x + $y = $result')
print(template.substitute(x = 3, y = 6, result = 3 + 6))
# print(template.substitute(x = 3, y = 6))  # Error if there is one value to substitute missing
print(template.safe_substitute(x = 3, y = 6))  # Avoids error promt and puts $variable_name if some value is missing

# We can also set the values to substitute in a dictionary, a data structure formed by key:value pairs
dictionary = dict(x = 30, y = 60, result = 30 + 60)
print(template.substitute(dictionary))

# '$$' prints '$', this is known as escaping a control character
template = string.Template('$x + $y = $result $$')
print(template.substitute(x = 3000, y = 6000, result = 3000 + 6000))