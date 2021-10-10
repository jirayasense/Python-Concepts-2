def f():
    print('HAhA')

e = compile('from __main__ import f as f2', filename='sample', mode='exec')
exec(e)
f2()

from __main__ import f2 as f22

f22()