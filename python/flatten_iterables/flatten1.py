# from reportlab lib

def isSeq(v, _st=(tuple,list)):
    return isinstance(v, _st)

def _flatten(L, a):
    for x in L:
        if isSeq(x): _flatten(x,a)
        else: a(x)

def flatten(L):
    '''recursively flatten the list or tuple L'''
    R = []
    _flatten(L, R.append)
    return R


in_data = [1,2,3,[4,[5,[6,[7]]]]]
flatten_data = flatten(in_data)
print(flatten_data)
