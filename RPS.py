def player(prev_play, opponent_history=[]):
    import random
    
    if not hasattr(player, "my_history"):
        player.my_history = []
    
    if prev_play:
        opponent_history.append(prev_play)

    moves = ["R", "P", "S"]

    def beats(move):
        return {"R": "P", "P": "S", "S": "R"}[move]

    def loses_to(move):
        return {"R": "S", "P": "R", "S": "P"}[move]

    if not opponent_history:
        choice = "R"
        player.my_history.append(choice)
        return choice

    count_R = opponent_history.count("R")
    count_P = opponent_history.count("P")
    count_S = opponent_history.count("S")

    freq_moves = {"R": count_R, "P": count_P, "S": count_S}
    most_common = max(freq_moves, key=freq_moves.get)
    counter_most_common = beats(most_common)

    transitions = {"R": [], "P": [], "S": []}
    for i in range(len(opponent_history) - 1):
        transitions[opponent_history[i]].append(opponent_history[i + 1])
    last_move = opponent_history[-1]

    if transitions[last_move]:
        next_move_guess = max(set(transitions[last_move]), key=transitions[last_move].count)
        markov_choice = beats(next_move_guess)
    else:
        markov_choice = random.choice(moves)

    if len(player.my_history) >= 1:
        my_last = player.my_history[-1]
        counter_move = beats(my_last)
        reaction_count = 0
        reaction_total = 0
        for i in range(len(opponent_history) - 1):
            if i < len(player.my_history) - 1:
                if player.my_history[i] == my_last:
                    reaction_total += 1
                    if opponent_history[i + 1] == counter_move:
                        reaction_count += 1
        if reaction_total > 5 and (reaction_count / reaction_total) > 0.6:
            react_choice = beats(counter_move)
        else:
            react_choice = None
    else:
        react_choice = None

    choices = [counter_most_common, markov_choice]
    if react_choice:
        choices.append(react_choice)

    final_choice = random.choices(
        choices + [random.choice(moves)],
        weights=[3, 3, 4 if react_choice else 0, 1],
        k=1
    )[0]

    player.my_history.append(final_choice)

    return final_choice
