'''Numbers'''

a = 1
b = 2
c = 3

dict = { a:b,b:c }
dict2 = { c:b,b:a }

'''Prints value for 'one' key'''
print( dict[1] )
'''Prints value for 2 key'''
print( dict[2] )
'''Prints complete dictionary'''
print( dict )
'''Prints all the keys'''
print( dict.keys() )
'''Prints all the values''' 
print( dict.values() )
'''Print the dictionary concatenate with an another dictionary'''
dict.update( dict2 )
print( dict )
dict2.update( dict2 )
print( dict2 )
'''Print the value of dictionary concatenation method'''
print( dict.update( dict2 ) )
print( dict2.update( dict2 ) )