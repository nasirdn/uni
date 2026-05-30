#отделение корней
import numpy as np

def f(x):
  return x**4+2*x-30

def proiz_f(x):
  return 4*x**3+2

def lev_gran(C):
  i = -1
  while f(i) > C:
    i *= 2
  return i

def prv_gran(C):
  i = 1
  while f(i) < C:
    i *= 2
  return i

def monoton(a, b, step = 1e-6):
  x = a
  sign = np.sign(proiz_f(x))
  while x<b:
    if sign == np.sign(proiz_f(x+step)):
      x += step
    else:
      return False
  return True

def otd_korn(a, b):
  while True:
    mon = monoton(a, b, step=1e-6)
    if (f(a)*f(b) < 0) and (mon == True):
      print(f'Функция непрерывна, монотанна на отрезке ({a}, {b}) и принимает на концах отрезка значения разных знаков.')
      return a, b
    else:
      mid = (b-a)*0.5
      if f(mid) < 0:
        a = mid
      else:
        b = mid

print(otd_korn(lev_gran(0), prv_gran(0)))

