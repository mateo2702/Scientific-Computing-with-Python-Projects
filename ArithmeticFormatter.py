def arithmetic_arranger(problems, solve=False):
  top = ""
  bottom = ""
  dashes = ""
  solution=""
  # Check problems does not exceed the given max(5)
  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    for item in problems:
      problem = item.split()

      number1 = problem[0]
      OP = problem[1]
      number2 = problem[2]

      # Handle errors for input:
      if OP != "+" and OP != "-":
        return "Error: OP must be '+' or '-'."
      if type(int(number1)) != int or type(int(number2)) != int:
        return "Error: Numbers must only contain digits."
      elif len(number1) > 4 or len(number2) > 4:
        return "Error: Numbers cannot be more than four digits."

      # Get total of correct function
      if OP == "+":
        result = int(number1) + int(number2)
      else:
        result = int(number1) - int(number2)

      # Format lines
      longest = max(number1, number2)
      width = len(str(longest))

      if item != problems[0]:
        top += f'{"" :{" "}<{4}}'
        bottom += f'{"" :{" "}<{4}}'
        dashes += f'{"" :{" "}<{4}}'
        solution += f'{"" :{" "}<{4}}'
  
      top += f'{number1:>{width + 2}}'
      bottom += f'{OP} {number2:>{width}}'
      dashes += f'{"":->{width+2}}'
      solution += f'{result:>{width+2}}'
      
    if solve:
      arranged_problems = '\n'.join((top, bottom, dashes, solution))
    else:
      arranged_problems = '\n'.join((top, bottom, dashes))

    return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))