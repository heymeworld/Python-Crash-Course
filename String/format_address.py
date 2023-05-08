def format_address(address_string):
  # Declare variables
  address_word = address_string.split()
  # Separate the address string into parts
  house_number = address_word[0]
  street_name = ""
  # Traverse through the address parts
  for item in address_word[1:]:
    # Determine if the address part is the
    # house number or part of the street name
    if item != address_word[-1]:
      street_name += item + " "
    else:
      street_name += item


  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
