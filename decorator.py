class Trace:
	def __init__(self):
		self.enabled = True
	
	def __call__(self,f):
		def wrap(*args,**kwargs):
			if self.enabled:
				print "calling {}".format(f)
				print args,kwargs, f(*args,**kwargs)
			return f(*args,**kwargs)
		return wrap
		
		
tracer = Trace()

@tracer
def rotate_list(l):
	print "rotate_list li",l[1:] + [l[0]]
	return l[1:] + [l[0]]