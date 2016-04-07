#Just for the sake of time, I assume the broken multiplication in the modules of 0.9.1 works.
def eq(a,b):
  return (a<=b and b<=a)
def ne(a,b):
  return (not eq(a,b))
def mul(a,b):
  r = 0
  i = 0
  while ne(i,b):
    r = r + a
    i = i + 1
  return r
#Python 0.9.1 does not allow int + float!
def float_div(a,b):
  return float(a)/float(b)

