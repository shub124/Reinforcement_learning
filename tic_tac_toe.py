#This is an example of reinforcement learning.


import numpy as np 
import matplotlib.pyplot as plt 


l=3
#WE design three classes for agent,environment and 

class Agent:
	def __init__(self,epsilon=0.1,alpha=0.5):
		#defining the parameters
		self.epsilon=epsilon
		self.alpha=alpha
		self.statehistory=[]
		self.verbose=False

	def setV(self,V):
		self.V=V
	def setverbose(self,V):#provides additional information if we choose to print more
		self.verbose=V
	def resethistory(self):
		self.statehistory=[]

	def takeaction(self,env):
		#Here we shall be using epsilon greedy technique to resolve explore-exploit dilemma
		r=np.random.rand()
		beststate=None
		if r<self.epsilon:
			if self.verbose:
				print("Taking action randomly:")
			all_moves=[]
			for i in range(l):
				for j in range(l):
					if env.isempty(i,j):
						all_moves.append((i,j))
					id=np.random.choice(len(all_moves))
					next=all_moves[id]


		else:
					#otherwise take the best suiable option
			pos2v={}
			next=None
			best=-1

			for i in range(l):
				for j in range(l):
					if env.isempty(i,j):
						env.board[i,j]=self.sym
						state=env.get_state()
						#changing it back
						env.board[i,j]=0
						pos2v[(i,j)]=self.V[state]
						#choosing the best

						if best<self.V[state]:
							best=self.V[state]
							beststate=state
							next=(i,j)
					
			if self.verbose:

				print("Taking a greedy action")
				for i in range(l):
					print("------------------")
					for j in range(l):
						if env.isempty(i, j):
							print(" %.2f|" % pos2value[(i,j)], end="")
						else:
							print("  ", end="")
						if env.board[i,j] == env.x:
							print("x  |", end="")
						elif env.board[i,j] == env.o:
							print("o  |", end="")
						else:
							print("   |", end="")
						print("")
				print("------------------")

			env.board[next[0],next[1]]=self.sym

		
              	
              			
              				
              			
              		
              			

              				

              				


              				



            			





							

        		
          			
          			
            			
              			
              			
              			
                			
              			
                			
              			
                			
          		
			


	def updatestatehistory(self,s):
		self.statehistory.append(s)
	def update(self,env):
		#updating rewards from the final state back to the first state
		reward=env.reward(self.sym)
		answer=reward
		for prev in reversed(self.statehistory):
			self.V[prev]=self.V[prev] + self.alpha*(answer - self.V[prev])
			answer=self.V[prev]
		self.resethistory()


class Environment:
	def __init__(self,s):
		self.board=np.zeros((l,l))
		self.x=-1
		self.o=1
		self.winner=None
		self.game_ended=False
		self.num_state=3**(l*l)

	def isempty(self,i,j):
		return self.board[i,j]==0

	def reward(self,sym):
		if not self.isgame_over():
			return 0
		if self.winner==sym:
			return 1
		else:
			return 0
	def game_over():

		#check rows
		for i in range(l):
			for player in (self.x,self.o):
				if self.board[i].sum()==player*l:
					self.winner=player
					self.game_ended=True
					return  True
		for i in range(l):
			for player in (self.x,self.o):
				if self.board[:,j].sum()==player*l:
					self.winner=player
					self.game_ended=True
					return True

		#checking the diagonals

		for player in (self.x,self.o):
			if self.board.trace()==player*l:
				self.winner=player
				self.game_ended=True
				return True
			if np.fliplr(self.board).trace()==player*l :
				self.winner=player
				self.game_ended=True
				return True

		#for draw		
		if np.all((self.board==0)==False):
			self.winner=None
			self.game_ended=True
			return True
		self.winner=None
		return False

	def get_state(self):
		k=0
		h=0
		for i in range(l):
			for j in range(l):
				if self.board[i,j]==0:
					v=0
				elif self.board[i,j]==self.x:
					v=1
				elif self.board[i,j]==self.o:
					v=2
				h+=(3**k)*v
				k+=1
		return h


	def draw(self):
		for i in range(l):
			print("------------------")
			for j in range(l):
				if env.isempty(i, j):
					print(" %.2f|" % pos2value[(i,j)], end="")
				else:
					print("  ", end="")
				if env.board[i,j] == env.x:
					print("x  |", end="")
				elif env.board[i,j] == env.o:
					print("o  |", end="")
				else:
					print("   |", end="")
			print("")
		print("------------------")
					
          		


          	
          	

            			

#Third class human for interaction with AI

class Human:
	def __init__(self):
		pass

	def set_symbol(self,sym):
		self.sym=sym

	def update(self,env):
		pass

	def updatestatehistory(self,s):
		pass

	def takeaction(self,env):
		while True:
			x=input("Enter co-ordinates of i and j")
			i,j=x.split(',')
			i=int(i)
			j=int(j)
			if env.isempty(i,j):
				env[i,j]=self.sym
				break


#This is a helper function that returns state,winner at that state and if game has ended
def utility(env,i=0,j=0):
	results=[]
	for p in (0,self.x,self.o):
		env.board[i,j]=p
		if(j==2):
			if(i==2):
				#implies board is full
				state=env.get_state()
				ended=env.game_over()
				winner=env.winner
				results.append((state,winner,ended))
			else:
				results+=utility(env,i+1,0)
		else:
			results+=utility(env,i,j+1)
	return results


def initial_Vx(env,triple):
	V=np.zeros(env.num_state)
	for state,winner,ended in triple:
		if ended:
			if winner==env.x:
				v=1
			else:
				v=0
		else:
			v=0.5
		V[state]=0.5
	return V

def initial_Vo(env,triple):

	V=np.zeros(env.num_state)
	for state,winner,ended in triple:
		if ended:
			if winner==env.o:
				v=1
			else:
				v=0
		else:
			v=0.5
		V[state]=0.5
	return V

def play_the_game(p1,p2,env,draw=False):
	c1=None
	while not env.game_over():
		if c1==p1:
			c1==p2
		else:
			c1=p1

		if draw:
			if draw==1 and c1==p1:
				env.draw()
			else:
				env.draw()
		c1.takeaction(env)
		state=env.get_state()
		p1.updatestatehistory(state)
		p2.updatestatehistory(state)

	if draw:
		env.draw()

	p1.update(env)
	p2.update(env)



if __name__=='__main__':
	p1=	Agent()
	p2=Agent()

	env=Environment()
	triples=utility(env)
	Vx=initial_Vx(env,triples)
	p1.setV(Vx)
	Vo=initial_Vo(env,triples)
	p2.setV(Vo)

	p1.set_symbol(env.x)
	p2.set_symbol(env.o)

	n=10000
	for i in range(10000):
		play_the_game(p1,p2,Environment())


	#playing humanvs agent
	human=Human()
	human.set_symbol(env.o)
	while True:
		p1.setverbose(True)
		play_the_game(p1,human,Environment(),draw=2)
		answer = input("Play again? [Y/n]: ")
		if answer and answer.lower()[0] == 'n':
			break
    		







		




