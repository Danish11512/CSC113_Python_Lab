import math

# Write a function to convert minutes to miliseconds.
def milconvert(min):
  print (min*60000, "milliseconds")

milconvert(60)

# Define a function to find the average of two exam scores.
def average(one, two):
  print((one+two)/2, 'is the average')

average(3, 3)


# Use math module import to use square root and compute the roots of a quatratic equation

def quad_eq(a, b, c):
  delta = (b**2) - 4*a*c;

  if delta >= 0 and a>0:
    one = ((-1*b) + math.sqrt(delta))/2*a
    two = ((-1*b) - math.sqrt(delta))/2*a
    print(' the roots are', one,'and', two)

  else:
    print (' wrong inputs')


quad_eq(1,0,1)

#Define a function to convert Kelvin to Réaumur, then Réaumur to Celsius. Use different
#functions, and call one inside the other, if necessary

def K2reaumur(kelvin):
  R = ((kelvin- 273.15) * 0.8)
  return R

def reaumer2C(R):
  C = R *(5/4)
  return C


print (K2reaumur(10))
print (reaumer2C(K2reaumur(10)))

#5
def area( cube_n):
  sphere = (4/3)*math.pi*((cube_n/4)**3)
  cube_a = cube_n**3
  return int(cube_a/sphere)

print(area(20))

# Write a function to give the following output
def print_output():
  print ('^-^-^^-^-^^-^-^^-^-^^')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('^-^-^^-^-^^-^-^^-^-^^')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('^-^-^^-^-^^-^-^^-^-^^')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('^-^-^^-^-^^-^-^^-^-^^')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('i    i    i    i    i')
  print ('^-^-^^-^-^^-^-^^-^-^^')




print_output()
