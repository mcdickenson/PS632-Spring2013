def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  while num: 
    digits.append(str(num % 2))
    num /= 2
  digits.reverse()
  return ''.join(digits)

def int_to_base(num, base):
  if num==0 or base <= 0 : return '0'
  digits = []
  absnum = abs(num)
  while absnum:
    digits.append(str(absnum % base))
    absnum /= base
  if num < 0: digits.append('-')
  digits.reverse()
  return ''.join(digits)

def romanify(num):
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

