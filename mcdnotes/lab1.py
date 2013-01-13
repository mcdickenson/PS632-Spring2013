def binarify(num): 
  """convert positive integer to base 2"""
  # if num==0:
  #   return 0 
  digits = []
  while num: 
    digits.append(str(num % 2))
    num /= 2
  digits.reverse()
  return ''.join(digits)

def int_to_base(num, base):
  if num==0: return '0'
  digits = []
  while num:
    digits.append(str(num % base))
    num /= base
  if num < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

def roman_numify(num):
  if not 0 < num< 4000:
    return "out of range"
  ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
  nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
  result = ""
  for i in range(len(ints)):
    count = int(num / ints[i])
    result += nums[i] * count 
    num -= ints[i] * count 
  return result
  # might be better once they know dicts!  

x10 = 16
x2 = int_to_base(16, 2)
print x2

print int_to_base(123, 2)

print roman_numify(3)
print roman_numify(9)


# TODO: put these tests in separate file