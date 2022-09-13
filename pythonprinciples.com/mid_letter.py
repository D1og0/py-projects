'''
Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''

def mid(s):
  result = ''
  length = len(s)
  if length % 2 != 0:
    result = s[length // 2]
  else:
    result = ''
  return result

print(mid('ao'))