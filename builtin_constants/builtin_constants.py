#encoding:utf-8
'''
Created on 2014年7月22日

@author: Administrator
'''
# print __builtins__.NotImplemented
import subprocess



print True

print False

print None

'''
the comparison is not implemented with respect to the other type
'''
print NotImplemented

'''
Special value used in conjunction with extended slicing syntax.
'''
print Ellipsis 

'''
true if Python was not started with an -O option
'''
print __debug__

'''
imported automatically  site module

useful for the interactive interpreter shell and should not be used in programs.
'''
# quit()
# exit()

print subprocess.check_output('cmd',stdin=subprocess.PIPE,stderr=subprocess.PIPE).decode('gbk').encode('utf-8')
