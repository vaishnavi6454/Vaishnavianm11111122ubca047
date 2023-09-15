class player:
    def play(self):
     print("The player is playing cricket.")
class Batsman(player):
  def play(self):
    print("The Batsman is Bating.")
class Bowler(player):
    def play(self):
      print("The Bowler is Bowling.")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()