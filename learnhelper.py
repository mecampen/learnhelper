import json

class LearnHelper:
	def __init__(self):
		self.learnObjects = []

	def save(self):
		with open('amoptikThemen.json', 'w') as f:
			json.dump(self.learnObjects, f)

	def load(self):
		with open("amoptikThemen.json", "r") as r:
			self.learnObjects = json.load(r)

	def register(self, newObjectName, difficulty=0):
		self.learnObjects.append({
			"name": newObjectName,
			"repetitions": 0,
			"difficulty": difficulty
		})
		self.sortObjects()
		self.save()
		#print("registered:", newObjectName, difficulty)
	
	def sortObjects(self):
		self.learnObjects.sort(
			key=lambda learnObject: learnObject["difficulty"]
		)

	def learn(self):
		print(chr(27) + "[2J")
		currentObjectName = self.learnObjects[0]["name"]
		
		self.learnObjects[0]["repetitions"] += 1
		
		#decrease each object by one
		for i in range(len(self.learnObjects)):
			self.learnObjects[i]["difficulty"]-=1

		print(f"📚 please review topic: \n \t {currentObjectName} \n")
		print("(ENTER TO CONTINUE)")
		input()
		print(chr(27) + "[2J")
		print(
			f"""rate the difficulty of the topic {currentObjectName}: \t
			(VERY HARD 🤯 1 2 3 4 5 6 7 8 9 10 VERY EASY 🥳) \n"""
		)
		self.learnObjects[0]["difficulty"] = int(input())

		self.sortObjects()
		self.save()

	def printState(self):
		print(chr(27) + "[2J")
		print("📋 current State:")
		for element in myLearnHelper.learnObjects:
			print("\t", element["name"], element["difficulty"])


if __name__ == '__main__':
	print("Welcome to learnHelper! 😄\n")
	myLearnHelper = LearnHelper()
	myLearnHelper.load()
	#myLearnHelper.register("Wasserstoffatom", difficulty=3)
	#myLearnHelper.register("Feinstruktur", difficulty=3)
	#myLearnHelper.register("Hyperfeinstruktur", difficulty=3)
	#myLearnHelper.register("Einstein Modell", difficulty=4)
	inp = ""
	while(inp!="q"):
		print("""Choose your action: \n
		\t status - gives the current status of the queue \n
		\t learn - start learning the next element in the queue \n
		\t register - register a new topic to learn \n
		\t q - quit program""")
		inp = input()
		if inp=="status":
			myLearnHelper.printState()
			print("(ENTER TO CONTINUE)")
			input()
		if inp=="learn":
			myLearnHelper.learn()
		if inp=="register":
			print("✍️  enter name:")
			name = input()
			print("enter initial difficulty:")
			difficulty = input()
			myLearnHelper.register(name, difficulty=int(difficulty))
		print(chr(27) + "[2J")
	print(chr(27) + "[2J")
	print("Bye! 👋")
	
