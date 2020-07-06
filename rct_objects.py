class PeepStatus:
	def __init__(self,thirst,hunger,nausea,happiness,angeriness,energy):
		self.thirst = thirst
		self.hunger = hunger
		self.nausea = nausea
		self.happiness = happiness
		self.angeriness = angeriness
		self.energy = energy

class Object:
	def __init__(self,width,length,peepReact,time,cost,price):
		self.size = (width,length)
		self.peepReact = peepReact #arr looks like [thirst,hunger,nausea,happiness,angeriness,energy]
		self.time = time
		self.cost = cost
		self.price = price
		self.position = None