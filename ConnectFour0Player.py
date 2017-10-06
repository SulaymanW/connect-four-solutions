import ConnectFourRandomAI
import ConnectFourMinimaxAI
import ConnectFourAlphabetaAI

import ConnectFourEngine

if __name__ == '__main__':
    # Initialise the game engine
    # Modify these parameters to tweak the game
    app = ConnectFourEngine.ConnectFour(
        ai_delay=10,
        red_player=ConnectFourMinimaxAI.AIcheck,
        blue_player=ConnectFourMinimaxAI.AIcheck,
    )
    # start the game engine
    app.game_loop()
