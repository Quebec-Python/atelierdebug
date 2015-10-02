import dis
func = """
g = 5
print(globals().keys())
[g for i in range(5)]
"""


func2 = """
g = 5
def otherfunc():
	w = g+2
"""

def f2():
	g = 5
	[g for i in range(5)]

def f():
	a  = compile(func, "blop", "exec")

	#dis.dis(func)
	print("###")
	dis.dis(a.co_consts[1])
	exec(func, {})

f()
print("###")
dis.dis(f2)
print("###")
dis.dis(f2.__code__.co_consts[2])

import pdb; pdb.set_trace()


def f():
	k = 2
	def g():
		w = k+2

	g()