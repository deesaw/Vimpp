#custom exceptions
class DeloitteMath(Exception):
	def __init__(self,args):
		super().__init__(args)

e = DeloitteMath("I do not know math")

#raise e

myexp = ValueError("pl. check the values")

raise myexp