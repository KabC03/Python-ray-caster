import sys;
import pygame as pg;
import numpy as np;
import game_settings;
import game_entity;
import game_player;
import game_map;


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
    DELTA_ANGLE = game_settings.PLAYER_FOV / game_settings.NUM_RAYS;
    DIST_TO_PLANE = (game_settings.SCREEN_WIDTH // 2) / np.tan(game_settings.PLAYER_FOV / 2);
    SLICE_SIZE = game_settings.SCREEN_WIDTH // game_settings.NUM_RAYS;





    running = True;
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False;

        keys = pg.key.get_pressed();
        if keys[pg.K_ESCAPE]:
            running = False;
        if keys[pg.K_LEFT]:
            player.turn_left(map);
        if keys[pg.K_RIGHT]:
            player.turn_right(map);
        if keys[pg.K_UP]:
            player.move_forward(map);
        if keys[pg.K_DOWN]:
            player.move_backward(map)

        screen.fill(game_settings.BLACK);


        startAngle = player.angle - (game_settings.PLAYER_FOV / 2);
        for ray in range(game_settings.NUM_RAYS):
            rayAngle = startAngle + ray * DELTA_ANGLE;


            for depth in range(game_settings.RAY_DEPTH):

                rayX = np.round((player.xPos + depth * np.cos(rayAngle)) / map.tileSize);
                rayY = np.round((player.YPos + depth * np.sin(rayAngle)) / map.tileSize);

                if 0 < rayX < map.width and 0 < rayY < map.height:
                    if map.map[rayX, rayY] != game_map.MAP_EMPTY_SPACE:
                        depth *= np.cos(player.angle - rayAngle); #Correct fisheye
        
                        wallHeight = (map.tileSize / (depth + 0.0001)) * DIST_TO_PLANE; #0.0001 avoids zero division

                        color = 255 / (1 + (depth ** 2) * 0.0001);
                        color = min(255, max(0, int(color)));

                        pg.draw.rect(screen, (color, color, color), (ray * SLICE_SIZE, (game_settings.HEIGHT // 2) - wallHeight // 2, SLICE_SIZE, wallHeight));
                        break;




        clock.tick(game_settings.FPS);
        pg.display.flip();

    return 0;



if __name__ == "__main__":
    sys.exit(main());







