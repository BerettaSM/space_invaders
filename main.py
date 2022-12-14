from gamemanager import GameManager
from gamescreen import GameScreen
from ships import Player


player_color = (0, 1, 0)


def main():
    player = Player(player_color)
    manager = GameManager(player)
    screen = GameScreen(manager)
    manager.setup()
    manager.spawn_aliens()
    game_is_on = True
    while game_is_on:
        screen.update()
        manager.evaluate_hits()
        if manager.player_lives == 0:
            manager.scoreboard.print_game_over_message("GAME OVER")
            game_is_on = False
        elif manager.all_aliens_defeated():
            manager.scoreboard.print_game_over_message("ALL ALIENS DEFEATED!")
            game_is_on = False
        manager.move_aliens()
        manager.make_aliens_shoot(probability=.02)
    screen.exitonclick()


if __name__ == '__main__':
    main()
