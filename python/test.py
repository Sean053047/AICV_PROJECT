class C():
    class D():
        def  func():
            print('C.D.func has been used.')
def use(*arg,**kwarg):
    print("use function have been used")
    '''
    This is document of function.
    '''

print(use.__module__)
use.__qualname__ = 'uss'
print(use.__qualname__)
use()
alias_func =  C.D.func.__qualname__
print(alias_func)
