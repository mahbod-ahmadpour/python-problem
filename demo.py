#problem1
s = 'lexicon'
print((s[0].upper()))
print((s[-1:]))
print(s[:4])
print(s[-3:])
print(s[-2:])

#problem 2
my_list=[3,7,[1,4,'hello']]
my_list[2].pop(2)
my_list[2].append('goodbye')
print(my_list)

#problem3
d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1])

#problem4
my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(my_list))

#problem5
age = 4
name = "Sammy"
print("Hello my dog's name is "+ name + " he is "+ str(age)+"years old")


