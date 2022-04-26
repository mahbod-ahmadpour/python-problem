#lab2
#problem1
def arrayCheck(nums):
    num =""
    for i in nums:
        num +=str(i)
    if "123" in num:
        return True
    else:
        return False
#nums = [1,1,2,3,1]
nums = [1,1,2,4,1]       
#nums=[1,1,2,1,2,3]
print(arrayCheck(nums))

#problem2      
def string_mah(str):
    return str[::2]
#st = ('Hello')
#st = ('Hi')
st = ('Heeololeo')
print(string_mah(st))
    

#problem3
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (b.endswith(a) or a.endswith(b))
#print(end_other('Hiabc', 'abc'))  
#print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

#problem4
def doubleChar(str):
  lisp = list(str)
  out = []
  string = ''
  for i in range(len(lisp)):
    out.append(lisp[i])
    out.append(lisp[i])
  for i in range(len(out)):
    string += out[i]
  return string
#print(doubleChar('The'))
#print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))



