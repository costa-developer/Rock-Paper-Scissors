from RPS import player
from RPS_game import play, quincy, opponent_bot2, opponent_bot3, opponent_bot4  # replace bot names accordingly

def test_all_bots():
    bots = [quincy, opponent_bot2, opponent_bot3, opponent_bot4]
    for bot in bots:
        print(f"Testing against {bot.__name__}...")
        results = play(player, bot, 1000, verbose=False)
        print(results)

if __name__ == "__main__":
    test_all_bots()
