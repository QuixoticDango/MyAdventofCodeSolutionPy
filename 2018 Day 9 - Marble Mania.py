# 476 players; last marble is worth 71657 points

class Marble():
    marble_count = 0
    def __init__(self, player='-'):
        self.player = player
        self.number = Marble.marble_count
        self.is_current_marble = True
        Marble.marble_count += 1
    
    def place_marble(self):
        # if Marble.marble_count - self.number > 1:
        #     self.is_current_marble = False
        return self
    
    def kept_marble(self):
        self.is_current_marble = False
        return self
    
    def f(self):
        self.is_current_marble = False
        return self
    
    def __str__(self):
        return "Marble {} placed by player {}".format(self.number, self.player)

class MarbleGame():
    def __init__(self, players=1):
        self.players = {"P" + str(i):0 for i in range(players)}
        self.circle = [Marble()]
        self.turn = 0
        self.last_player_scored = False
        self.score = 0
        self.current_marble_index = 0
    
    def place_marble(self):
        if Marble.marble_count < 2:
            self.circle.append(Marble("P" + str(self.turn % len(self.players))).place_marble())
            for i, m in enumerate(self.circle):
                if i < len(self.circle) - 1:
                    m.f()
            self.current_marble_index = [i for i in range(len(self.circle)) 
                                    if self.circle[i].is_current_marble][0]
            self.turn += 1
            return self
        
        if Marble.marble_count >= 2 and Marble.marble_count % 23 != 0:
            self.current_marble_index = [i for i in range(len(self.circle)) 
                                    if self.circle[i].is_current_marble][0]
            if self.current_marble_index == len(self.circle) - 1:
                self.circle.insert(1, Marble("P" + str(self.turn % len(self.players))).place_marble())
                for i, m in enumerate(self.circle):
                    if i != 1:
                        m.f()
            elif self.current_marble_index == len(self.circle) - 2:
                self.circle.append(Marble("P" + str(self.turn % len(self.players))).place_marble())
                for i, m in enumerate(self.circle):
                    if i < len(self.circle) - 1:
                        m.f()
            else:
                self.circle.insert(self.current_marble_index + 2, Marble("P" + str(self.turn % len(self.players))).place_marble())
                for i, m in enumerate(self.circle):
                    if i == self.current_marble_index + 2:
                        m.f()
            self.current_marble_index = [i for i in range(len(self.circle)) 
                                    if self.circle[i].is_current_marble][0]
            self.turn += 1
            return self
        
        if Marble.marble_count % 23 == 0 and Marble.marble_count > 0:
            unplaced_marble = Marble("P" + str(self.turn % len(self.players))).kept_marble()
            try:    
                self.score = unplaced_marble.number + self.circle[(self.current_marble_index - 7) % len(self.circle)].number
            except:
                print(f"{(self.current_marble_index - 7) % len(self.players)=}")
                print(f"{len(self.circle)=}")
                return 0
            self.players["P" + str(self.turn % len(self.players))] += self.score
            del self.circle[self.current_marble_index - 7]
            self.current_marble_index -= 7
            self.last_player_scored = True
            self.turn += 1
            return self
        
        if self.last_player_scored:
            self.circle.insert(self.current_marble_index, Marble("P" + str(self.turn % len(self.players))).place_marble())
            for i, m in enumerate(self.circle):
                if i != self.current_marble_index:
                    m.f()
            self.last_player_scored = False
            self.turn += 1
            return self


print(divmod(71657, 23))
game = MarbleGame(476)
players = game.players.keys()
turns = 0
while Marble.marble_count <= 71658:
    game.place_marble()
    if turns % 23 == 0:
        print(f"It is now player {turns % len(players)}'s turn")
        print(f"Score = {game.score}")
    turns += 1

print([(player, game.players[player]) for player in players if game.players[player] == max(game.players[player] for player in players)][0])

# from collections import deque, defaultdict

# def play_game(max_players, last_marble):
#     scores = defaultdict(int)
#     circle = deque([0])

#     for marble in range(1, last_marble + 1):
#         if marble % 23 == 0:
#             circle.rotate(7)
#             scores[marble % max_players] += marble + circle.pop()
#             circle.rotate(-1)
#         else:
#             circle.rotate(-1)
#             circle.append(marble)

#     return max(scores.values()) if scores else 0
# print(play_game(476, 71657))