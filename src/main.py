import sys;
import pygame as pg;
import numpy as np;
import game_settings;
import game_entity;
import game_player;
import game_map;


def internal_clock_frame(clock: pg.time.Clock) -> None:
    clock.tick(60);






def main() -> int:
    pg.init();
    clock = pg.time.Clock();
    screen = pg.display.set_mode((game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT));



    map = game_map.Map(
        np.array([
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]),
        100
    );
    player = game_player.Player(0.01, 0.01, 200, 200, 0);







    running = True;
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False;

        keys = pg.key.get_pressed();
        if keys[pg.K_ESCAPE]:
            running = False;
        if keys[pg.K_LEFT]:
            player.turn_left();
        if keys[pg.K_RIGHT]:
            player.turn_right();
        if keys[pg.K_UP]:
            player.move_forward();
        if keys[pg.K_DOWN]:
            player.move_backward()




        screen.fill(game_settings.BLACK);




        internal_clock_frame(clock);
        pg.display.flip();

    return 0;



if __name__ == "__main__":
    sys.exit(main());







