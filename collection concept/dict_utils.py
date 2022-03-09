import operator as op

def dict_equal_sensative(d1, d2):
    ''' Compare 2 Dictionary (order wise))'''
    # 1. Check First if both dictionary have same items
    if d1 == d2: 
        # 2. check if all keys in both dict are in same order
        return all(map(op.eq, d1, d2))
    else:
        return False

def inverse_mapping(f):  # Assuming the {f} is dict
    return f.__class__(map(reversed, f.items()))
    # dict(((v, k) for k, v in f.items()))

