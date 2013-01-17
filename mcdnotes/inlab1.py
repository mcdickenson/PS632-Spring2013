def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  while num: 
    digits.append(str(num % 2))
    num /= 2
  digits.reverse()
  return ''.join(digits)