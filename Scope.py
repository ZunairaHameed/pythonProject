# Local scope are accessible within the function
def myfunc():
  x = 300
  print(x)
myfunc()
# Global variable are accessible in whole program
x = 300
def myfunc():
  print(x)
myfunc()
print(x)
# Global keyword
def myfunc():
  global x
  x = 300
myfunc()
print(x)
# changing the value globally
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)