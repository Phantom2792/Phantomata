class DFA:
	"""Defines Deterministic Finite Automata"""
	
	def __init__(self, Q, Sig, iniQ, F,Del):
		super(DFA, self).__init__()
		self.states = Q
		self.alphabet = Sig
		self.initState = iniQ
		self.finalStates = F
		self.Trans = Del
	def ip_valid(self,ip_str):
		for i in str(ip_str):
			if int(i) in self.alphabet:
				continue
			else:
				return i
		return True
	def path(self, ip_str):
		nxt = self.initState
		path = ""
		path+=nxt
		for i in str(ip_str):
			nxt = self.Trans[nxt][int(i)]
			path+='->'+nxt
		return path
	def step(self, ip_str):
		nxt = self.initState
		for i in str(ip_str):
			nxt = self.Trans[nxt][int(i)]
		return nxt
	def eval(self, ip_str):
		if self.ip_valid(ip_str) != True:
			print("Invalid inputs")
		else:
			final = self.step(ip_str)
			path = self.path(ip_str)
			if final in self.finalStates:
				print(path+"\nExecution Successful")
			else:
				print(path+"\nInvalid String -- String is not in language")
class Mealy:
	"""Defines Mealy Machine"""
	
	def __init__(self, Q, Sig, iniQ, O,Del):
		super(Mealy, self).__init__()
		self.states = Q
		self.ip_alphabet = Sig
		self.initState = iniQ
		self.op_alphabet = O
		self.Trans = Del
	def ip_valid(self,ip_str):
		for i in str(ip_str):
			if int(i) in self.ip_alphabet:
				continue
			else:
				return i
		return True
	def path(self, ip_str):
		nxt = self.initState
		path = ""
		out = ""
		path+=nxt
		for i in str(ip_str):
			nxt,op = self.Trans[nxt][int(i)]
			path+='->'+nxt
			out+=op
		return path,out
	def step(self, ip_str):
		nxt = self.initState
		for i in str(ip_str):
			nxt,op = self.Trans[nxt][int(i)]
		return nxt
	def op_valid(self, out):
		for i in out:
			if i in self.op_alphabet:
				continue
			else:
				return i
		return True
	def eval(self, ip_str):
		if self.ip_valid(ip_str) != True:
			print("Invalid inputs")
		else:
			path,out = self.path(ip_str)
			if self.op_valid(out) == True:
				print(path+"\n"+out)
			else:
				print("~ERROR IN TRANSITION FUNCTION~\n'"+self.op_valid(out)+"' Is not in output alphabet")
	
def make_dfa(Del,iniQ="*",finalStates="*",fa_type="DFA"):
	q = list(Del.keys())
	if iniQ == '*':
		q0 = q[0]
	else:
		q0 = iniQ
	if finalStates == '*':
		F = q[-1]
	else:
		F = finalStates
	Sig = list(Del[q0].keys())

	args = (q,Sig,q0,F,Del)
	if fa_type == 'DFA':
		return DFA(q,Sig,q0,F,Del)
	else:
		return args

#An Example for class FA
if __name__ == "__main__":
        q = ['A','B','C']
        a = [0,1]
        i = 'A'
        f = 'C'
        T1 = {'A':{0:'B',1:'A'},'B':{0:'B',1:'C'},'C':{0:'B',1:'A'}}
        print("you are here")
        example_dfa = DFA(q,a,i,f,T1)
        T2 = {'A':{0:('B','b'),1:('A','a')},'B':{0:('B','b'),1:('A','a')}}
        example_mealy = Mealy(q,a,i,['a','b'],T2)
