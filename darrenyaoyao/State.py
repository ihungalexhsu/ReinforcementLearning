import random

class State:
	player_value_sum = 0
	dealer_value_sum = 0
	policy = { 'hit': 0, 'stick': 0 }
	policy['hit'] = random.random()
	policy['stick'] = 1-policy['hit']
	reward = 0
	processing = 'draw'

	def __init__(self, player_value_sum=0, dealer_value_sum=0, reward=0, processing='draw'):
		self.player_value_sum = player_value_sum
		self.dealer_value_sum = dealer_value_sum
		self.reward = reward
		self.processing = processing
		
	def getaction(self):
		if random.random() < self.policy['hit']:
			return 'hit'
		else:
			return 'stick'

	def  getplayer_value(self):
		return self.player_value_sum;