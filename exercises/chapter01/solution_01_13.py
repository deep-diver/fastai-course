from fastcore.all import *

@typedispatch
def happy_newyear(name:str): 
  return f'happy new year, {name}!'

@typedispatch
def happy_newyear(year:int): 
  return f'happy new year, it\'s {year} now!'

@typedispatch
def happy_newyear(name:str, year:int): 
  return f'happy new year, {name}. It\'s {year} now!'

print('등록된 함수 목록')
print(happy_newyear)

print(happy_newyear('chansung'))
print(happy_newyear(2022))
print(happy_newyear('chansung', 10))
