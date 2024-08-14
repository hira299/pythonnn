def add_car_record(car,car_id):
    print('enter details for {car_id}')
    
    
    
    
stri = ['haha','hehe','hoho','keke']
enu = list(enumerate(stri))
print(enu)

name = '\n     hhhira       '
oo = 'mm'
lstr = name.lstrip() 
rstr = name.rstrip()
strp = name.strip()

print(lstr + oo)
print(rstr  + oo)
print(strp  + oo)

color = input('put color of 4 words: ' )

print(color*10)
print(color + " "*32 + color)
print(color*10)

import random

a = []

for i in range(10):
    tt =(random.randint(1, 100))
    a.append(tt)
    
print(a)


strr = 'hellloooo'
tt = 'kitttttttttttt'

print(tt.replace('t', 'o'))






disco = {}

disco['oo'] = 'heehe'
disco[90000] = 'greOEEEE'
disco['me'] = 'cute'

print(disco)

disco.pop('oo')

    
print(disco)


import random
ques = {'pak': 'islamabad', 'japan': 'tokyo', 'korea':'seoul','hehe' :'hihi'}

coco =list(ques.keys())



correct = 0
incorrect = 0 

while True: 
    qq= random.choice(coco)
    ans = input(f'what is cap of {qq}?: ').lower()
    
    if ans == ques[qq]:
      correct+=1 
    else:
      incorrect+=1
      
    ag = input("play again? enter yes: ").lower()
    
    if ag != 'yes':
        break
    
print(correct, incorrect)



fav_places = {'Alice' :['oo', 'ppp', 'lll'], 'bob' :['jj', 'pp' , 'yy'], 'SAnd': ['gg', 'ee', 'qq']}

for k,v in fav_places.items():
    print(k)
    for i in v:
        print(i)
    

oo = ()

pp = list(oo)
for i in range(4): 
    aa = input("enter no: ")
    pp.append(aa)
tuple(pp)
    
y = input("give no: ")

if y in pp:
    print('yes')
    
    
else: 
    print('no')





def add_car(cars , car_no):
    
    print(f'car no {car_no} info:')
    
    model = input('model no: ')
    clr = input('color of car : ')
    trans = input('auto/manual: ')
    brand = 'toyota'
    cars[car_no] = {'model': model, 'color': clr ,'transmission': trans}
    
    
    
def print_car(cars, car_no):
    if car_no in cars:
        print(f'the {car_no}  of {cars[car_no]}')
    else:
        print(f'the {car_no} doesnt exist')
        
def update_car(cars, car_no):
    if car_no in cars:
        print(f'car no {car_no} info updating now:')
        
        model = input('model no: ')
        clr = input('color of car : ')
        trans = input('auto/manual: ')
        brand = 'toyota'
        cars[car_no] = {'model': model, 'color': clr ,'transmission': trans}
    else:
            print(f'the {car_no} doesnt exist')
            
def main():
    
    cars = {}
    
    for i in range(1,4):
        add_car(cars, i)
        
    (print_car(cars, 2))
    update_car(cars, 2)
    
    add_car(cars, 4)
    for h in range(1,5):
      print_car(cars, h)
    cars.pop(3)
    for z in range(1,4):
      print_car(cars, z)
    
    
main()
        
    
        
    
    
    







try : 
    list1 = ['rr','tt','jj']
    print(list1[5])
except:
    print('error index se bhair h')



tup1 = ()

for i in range(4):
    
    a = int(input('enter no: '))
    
    tup1 += (a,)
    
print(tup1)
    

dic1 = {}

for i in range(4):
    
    x = (input('enter no k: '))
    
    a = int(input('enter no v: '))
    
    
    dic1[x]= a
    
print(dic1)
    

def seee(list1 ,list2):
    
    for x in list1:
        if x in list2:
            print('uuuuu')
            
        print('oooooooo')
    
    
list1 = [1,3,5,7,9,]
list2 = [3,0,66,78,99]

seee(list1, list2)


balance = int(input("Enter your balance: "))
while True:
  if balance <= 9000: 
      
      balance = balance + 999.99
      break
     
print("Balance is",balance)

def multiply_list(elements):
      q = 1
      for x in elements:
            q*= x
      return q
print(multiply_list([2,5,8]))

tuple1 = ("green", "red", "blue")
tuple2 = tuple([7, 1, 2, 23, 4, 5])
tuple3 = tuple1 + tuple2 
print(tuple3)
tuple3 = 2 * tuple1 
print(tuple3)
print(tuple2[2 : 4]) 
print(tuple1[-1])

list1 = [22,55,76,89,344446,23]

def max_min(list1):

    maxval = list1[0]
    minval = list1[0]

    for num in list1[1:]:
        if num > maxval:
            maxval = num
        if num < minval:
            minval = num

    return maxval, minval

print(max_min(list1))
















































































































































































































































































































