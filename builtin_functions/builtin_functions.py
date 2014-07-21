#encoding:utf-8
'''
Created on 2014年7月22日

@author: Administrator
'''
#encoding:utf-8
'''
Created on 2014年7月21日

@author: Administrator
'''

'''
abs绝对值
abs(x)


Return the absolute value of a number. The argument may be a plain or long integer or a floating point number. If the 
argument is a complex number, its magnitude is returned.
'''
# print abs(-12)


'''
any(iterable) 如果有一个是真 返回真 否则是假


Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
'''
# a=(False,False,False,True)
# print any(a)

'''
basestring() 不能被实例化，str和unicode的父类，用来测试是否是str或unicode的实例


This abstract type is the superclass for str and unicode. It cannot be called or instantiated, but it can be used to 
test whether an object is an instance of str or unicode. isinstance(obj, basestring) is equivalent to
 isinstance(obj, (str, unicode)).
'''
# basestring()#报错,不能实例化

# print isinstance('song', basestring)
# print isinstance(u'song', basestring)






'''
callable(object) 

Return True if the object argument appears callable, False if not. If this returns true, it is still possible that a 
call fails, but if it is false, calling object will never succeed. Note that classes are callable (calling a class 
returns a new instance); class instances are callable if they have a __call__() method.

'''
# class a:
#     print 'bbb'
# print callable(a)

'''
chr(i)    int=>ascII

Return a string of one character whose ASCII code is the integer i. For example, chr(97) returns the string 'a'. 
This is the inverse of ord(). The argument must be in the range [0..255], inclusive; ValueError will be raised if i is
 outside that range. See also unichr().
'''
# print chr(126)

'''
unichr(i)  类似chr  范围更大

Return the Unicode string of one character whose Unicode code is the integer i. For example, unichr(97) returns the 
string u'a'. This is the inverse of ord() for Unicode strings. The valid range for the argument depends how Python 
was configured – it may be either UCS2 [0..0xFFFF] or UCS4 [0..0x10FFFF]. ValueError is raised otherwise. For ASCII 
and 8-bit strings see chr().
'''
# print unichr(97)


'''
ord(c)     unicode字符=>unicode    8bitstring=>value  

Given a string of length one, return an integer representing the Unicode code point of the character when the argument 
is a unicode object, or the value of the byte when the argument is an 8-bit string. For example, ord('a') returns the 
integer 97, ord(u'\u2020') returns 8224. This is the inverse of chr() for 8-bit strings and of unichr() for unicode 
objects. If a unicode argument is given and Python was built with UCS2 Unicode, then the character’s code point must be 
in the range [0..65535] inclusive; otherwise the string length is two, and a TypeError will be raised.

'''

# print ord(u'\u2020')

'''
pow(x, y[, z])     x**y.   pow(x, y) % z


Return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently than
 pow(x, y) % z). The two-argument form pow(x, y) is equivalent to using the power operator: x**y.

'''
# print pow(2,3)
# print pow(2,3,3)


'''
??????????

property([fget[, fset[, fdel[, doc]]]]) 

如果要使用property函数，首先定义class的时候必须是object的子类。通过property的定义，当获取成员x的值时，就会调用getx函数，
当给成员x赋值时，就会调用setx函数，当删除x时，就会调用delx函数。使用属性的好处就是因为在调用函数，可以做一些检查。如果没有严
格的要求，直接使用实例属性可能更方便。

同时，还可以通过指定doc的值来为类成员定义docstring。

Return a property attribute for new-style classes (classes that derive from object).

'''

# class C(object):
#     def __init__(self):
#         self._x = None
# 
#     def getx(self):
#         return self._x
#     def setx(self, value):
#         self._x = value
#     def delx(self):
#         del self._x
# #     x = property(getx, setx, delx, "I'm the 'x' property.")


'''
range()  return a list
'''
# print range(18)


'''
classmethod(function) 


Return a class method for function.

A class method receives the class as implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:

class C(object):
    @classmethod
    def f(cls, arg1, arg2, ...):
        ...
The @classmethod form is a function decorator – see the description of function definitions in Function definitions for details.

It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class. If a class method is called for a derived class, the derived class object is passed as the implied first argument.

Class methods are different than C++ or Java static methods. If you want those, see staticmethod() in this section.


'''
# class a:
#     @classmethod
#     def a1(self):
#         pass


'''
staticmethod(function) 


Return a static method for function.

A static method does not receive an implicit first argument. To declare a static method, use this idiom:

class C(object):
    @staticmethod
    def f(arg1, arg2, ...):
        ...
The @staticmethod form is a function decorator – see the description of function definitions in Function definitions for details.

It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class.

Static methods in Python are similar to those found in Java or C++. Also see classmethod() for a variant that is useful for creating alternate class constructors.

'''

# class a:
#     @staticmethod
#     def a1(self):
#         pass

'''
cmp(x, y) 
Compare the two objects x and y and return an integer according to the outcome. The return value is negative if x < y, zero if x == y and strictly positive if x > y.

'''

# print cmp(2,4)

'''
compile(source, filename, mode[, flags[, dont_inherit]])  ????


中文说明：将source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值。
参数source：字符串或者AST（Abstract Syntax Trees）对象。
参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
参数model：指定编译代码的种类。可以指定为 ‘exec’,’eval’,’single’。
参数flag和dont_inherit：这两个参数暂不介绍，可选参数。

版本：在python2.3、2.6、2.7、3.2中均有不同，使用时要引起注意，兼容python3
'''


##操作类属性
'''
delattr(object, name) 
This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar.
'''
'''
setattr(object, name, value) 
This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
'''
'''
getattr(object, name[, default]) 
Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised
'''


'''
divmod(a, b) 
Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using long division. With mixed operand types, the rules for binary arithmetic operators apply. For plain and long integers, the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) but may be 1 less than that. In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b).

'''
# print divmod(3,2)#返回一个元组











































