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
def get_raw():
  try:
    r=raw_input()
  except NameError:
    r=input()
  return r
#As for evaling code, give up!
#Oh god, python 0.9.1 does not have global
def modify_global(name,val):
  import __main__
  __main__.__dict__[name] = val
def delete_global(name):
  import __main__
  del __main__.__dict__[name]
