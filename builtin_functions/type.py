#encoding:utf-8
'''
D:/project/python_stdlib/builtin_functions/type.py

Created on 2014年7月22日

@author: Administrator
'''



'''
complex([real[, imag]])   复数
Create a complex number with the value real + imag*j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the function serves as a numeric conversion function like int(), long() and float(). If both arguments are omitted, returns 0j.

Note
When converting from a string, the string must not contain whitespace around the central + or - operator. For example, complex('1+2j') is fine, but complex('1 + 2j') raises ValueError.

'''



'''
bytearray([source[, encoding[, errors]]]) 返回bytearray


Return a new array of bytes. The bytearray type is a mutable(可变) sequence of integers in the range 0 <= x < 256. It has most
 of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods that the str 
 type has, see String Methods.

The optional source parameter can be used to initialize the array in a few different ways:

If it is a string, you must also give the encoding (and optionally, errors) parameters; bytearray() then converts the 
string to bytes using str.encode().
If it is an integer, the array will have that size and will be initialized with null bytes.
If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.
If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial 
contents of the array.
Without an argument, an array of size 0 is created.
'''

# bytearray(('a','b')) #返回bytearray(b'abc')
# bytearray('宋')






'''
bool([x])


Convert a value to a Boolean, using the standard truth testing procedure. If x is false or omitted(省略), this returns False;
 otherwise it returns True. bool is also a class, which is a subclass of int. Class bool cannot be subclassed further. 
 Its only instances are False and True.

New in version 2.2.1.

Changed in version 2.3: If no argument is given, this function returns False.
'''
#返回假的几种情况
# print bool(0)
# print bool(False)
# print bool()



'''
bin(x)   int=>bin    若不是int　需要__index__返回一个int


Convert an integer number to a binary string. The result is a valid Python expression. If x is not a Python int object,
 it has to define an __index__() method that returns an integer.
'''
# print bin(8)#结果0b1000
# print bin(258)#结果0b100000010

# print bin('123')#报错

# class a:
#     def __index__(self):
#         return 23
# print bin(a())#定义index后可以用bin()



'''
dict(**kwarg) 
dict(mapping, **kwarg) 
dict(iterable, **kwarg) 
Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types — dict for documentation about this class.

For other containers see the built-in list, set, and tuple classes, as well as the collections module
'''




'''
enumerate(sequence, start=0) 

Return an enumerate object. sequence must be a sequence, an iterator, or some other object which supports iteration. The next() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over sequence:

>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
Equivalent to:

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
'''
'''
file(name[, mode[, buffering]]) 
Constructor function for the file type, described further in section File Objects. The constructor’s arguments are the same as those of the open() built-in function described below.

When opening a file, it’s preferable to use open() instead of invoking this constructor directly. file is more suited to type testing (for example, writing isinstance(f, file)).

'''
'''
float([x]) 
Convert a string or a number to floating point. If the argument is a string, it must contain a possibly signed decimal or floating point number, possibly embedded in whitespace. The argument may also be [+|-]nan or [+|-]inf. Otherwise, the argument may be a plain or long integer or a floating point number, and a floating point number with the same value (within Python’s floating point precision) is returned. If no argument is given, returns 0.0.

Note
When passing in a string, values for NaN and Infinity may be returned, depending on the underlying C library. Float accepts the strings nan, inf and -inf for NaN and positive or negative infinity. The case and a leading + are ignored as well as a leading - is ignored for NaN. Float always represents NaN and infinity as nan, inf or -inf.

'''

'''
frozenset([iterable]) 
Return a new frozenset object, optionally with elements taken from iterable. frozenset is a built-in class. See frozenset and Set Types — set, frozenset for documentation about this class.

For other containers see the built-in set, list, tuple, and dict classes, as well as the collections module.

'''



































