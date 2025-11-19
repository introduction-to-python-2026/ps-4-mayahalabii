def split_at_first_digit(formula):
    digit_location = 1
    for char in formula[1:]:
      if char.isdigit():
        break
      digit_location += 1
    
    if digit_location == len(formula):
      return formula, 1
    else:
      prefix = formula[:digit_location]
      number = int(formula[digit_location:])
      return prefix, number





def split_before_each_uppercases(formula):
    # Initialize start, end, and the result list
    split_formula = []
    start = 0
   
    

    # Loop from the second character onward
    for i in range(1, len(formula)):
        # If an uppercase letter is found, slice and update
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i
        

    # Append the final piece after the loop
    split_formula.append(formula[start:len(formula)])
    return split_formula
