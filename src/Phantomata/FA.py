class DFA:
	"""Defines Deterministic Finite Automata"""
	
	def __init__(self, Q, Sig, iniQ, F,Del):
		super(DFA, self).__init__()
		self.states = Q
		self.alphabet = Sig
		self.initState = iniQ
		self.finalStates = F
		self.Trans = Del
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
		final = self.step(ip_str)
		path = self.path(ip_str)
		if final in self.finalStates:
			print(path+"\nExecution Successful")
		else:
			print(path+"\nInvalid String -- String is not in language")

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
        T = {'A':{0:'B',1:'A'},'B':{0:'B',1:'C'},'C':{0:'B',1:'A'}}
        print("you are here")
        example_dfa = DFA(q,a,i,f,T)