MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class Secret:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = []

for i in range(MAX_N):
    agents.append(Secret(codenames[i], scores[i]))

min_agent = agents[0]

for i in range(1, MAX_N):
    if agents[i].score < min_agent.score:
        min_agent = agents[i]

print(min_agent.codename, min_agent.score)
