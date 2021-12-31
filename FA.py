class DFA:
	"""Defines Deterministic Finite Automata"""
	
    #Attempting to Overload,
	'''def makeFA(self, Q, Sig, Del):
		super(FA, self).__init__()
		self.states = Q
		self.alphabet = Sig
		self.initState = Q[0]
		self.finalStates = Q[-1]
		self.Trans = Del'''
	
	def __init__(self, Q, Sig, iniQ, F,Del):
		super(DFA, self).__init__()
		self.states = Q
		self.alphabet = Sig
		self.initState = iniQ
		self.finalStates = F
		self.Trans = Del
	def path(self, X):
		nxt = self.initState
		path = ""
		path+=nxt
		for i in str(X):
			nxt = self.Trans[nxt][int(i)]
			path+='->'+nxt
		return path
	def step(self, y):
		nxt = self.initState
		for i in str(y):
			nxt = self.Trans[nxt][int(i)]
		return nxt
	def eval(self, x):
		final = self.step(x)
		path = self.path(x)
		if final in self.finalStates:
			print(path+"\nExecution Successful")
		else:
			print(path+"\nInvalid String -- String is not in language")

#An Example for class FA
if __name__ == "__main__":
        q = ['A','B','C']
        a = [0,1]
        i = 'A'
        f = 'C'
        T = {'A':{0:'B',1:'A'},'B':{0:'B',1:'C'},'C':{0:'B',1:'A'}}
        print("you are here")
        example_dfa = DFA(q,a,i,f,T)

