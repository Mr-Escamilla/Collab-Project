class Player():
    name = None
    score = 0

    def set_name(self, name_):
        self.name = name_

    def add_score(self, points):
        self.score += points
    
    def lose_score(self, points):
        self.score -= points


def create_player(player_name, player_score):
    temporary = Player()
    temporary.set_name(player_name)
    temporary.add_score(player_score)
    return temporary

players = []
for nothing in range(10):
    players.append(create_player("Julia", 100))

# players = []
# player_names = ["Sid", "Nalin", "Mela", "Maddie", "Annelise", "Allie", "Lucas", "Aaron", "Hieu", "Parker"]
# for name in player_names:
#     players.append(create_player(name, 100))


print(players)
print(players[0])
print(players[0].name)
print(players[0].score)
