
class Point:
	cer=0
	a=0
	b=0
	def __init__(self,a,b,cer):
		self.a=a
		self.b=b
		self.cer=cer
	def Mult(self):
		self.cer = self.a * self.b
	def Sub(self):
		self.cer = self.a - self.b
	def Add(self):
		self.cer = self.a + self.b
	def Div(self):
		self.cer = self.a / self.b
	def Mod(self):
		self.cer = self.a % self.b
	def Exp(self):
		self.cer = self.a ** self.b
	def printState(self):
		print("A = " + str(self.a))
		print("B = " + str(self.b))
		print("C = " + str(self.cer))

print("1st set of variables")
Pointer1=Point(5, 5, 1)
Pointer1.printState()
print("2nd set of variables")
Pointer2=Point(4, 4, 2)
Pointer2.printState()
print("Now moving onto multiplication for 1st set of variables")
Pointer1.Mult()
Pointer1.printState()
print("Multiplication for 2nd set of variables")
Pointer2.Mult()
Pointer2.printState()
print("Now moving onto Division for 1st set of variables")
Pointer1.Div()
Pointer1.printState()
print("Now moving onto Division for 2nd set of variables")
Pointer2.Div()
Pointer2.printState()
print("Now moving onto Exponent for 1st set of variables")
Pointer1.Exp()
Pointer1.printState()
print("Now moving onto Exponent for 2nd set of variables")
Pointer2.Exp()
Pointer2.printState()