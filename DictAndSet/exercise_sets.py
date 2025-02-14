scorpion = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spider = {"tarantula", "black widow", "wolf spider", "crab spider"}
wasps = {"yellow jacket", "hornet", "paper wasp"}

bite = set()

for biting_animals in spider, snakes:
    bite = bite.union(biting_animals)

print(bite)
