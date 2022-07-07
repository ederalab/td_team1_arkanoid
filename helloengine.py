import sys
from engine.engine import Engine

engine = Engine()

engine.loadScene("startGame.json")

engine.gameloop()

sys.exit()