class Player:
    score = 0
    best_score = 0
    game_field = []
    game_restarted = False
    game_over = False


    @classmethod
    def save_best_score(cls):
        cls.load_best_score()
        if Player.score > int(Player.best_score):
            with open('best_result.txt', 'w') as file:
                file.write(str(Player.score))


    @staticmethod
    def load_best_score():
        with open('best_result.txt') as file:
            Player.best_score = file.read()


    @classmethod
    def end_game(cls):
        Player.save_best_score()
        Player.load_best_score()
        Player.game_over = True