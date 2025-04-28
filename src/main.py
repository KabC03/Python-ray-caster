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
    pg.display.set_caption("Process");


    map_array = game_map.Map(
        np.array([
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1],
            [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1],
            [1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1],
            [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1],
            [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
            [1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1],
            [1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1],
            [1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1],
            [1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1],
            [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1],
            [1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1],
            [1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
            [1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1],
            [1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1],
            [1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1],
            [1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
            [1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]),
        50
    );
    player = game_player.Player(0.5, 1, 0.1,50, 50, 0);
    DELTA_ANGLE = game_settings.PLAYER_FOV / game_settings.NUM_RAYS;
    DIST_TO_PLANE = (game_settings.SCREEN_WIDTH // 2) / np.tan(game_settings.PLAYER_FOV / 2);
    SLICE_SIZE = game_settings.SCREEN_WIDTH // game_settings.NUM_RAYS;





    running = True;
    pg.mouse.set_visible(False);
    pg.event.set_grab(True);

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False;

        mouse_dx, mouse_dy = pg.mouse.get_rel();
        player.set_angle(player.angle + mouse_dx * game_settings.PLAYER_SENSITIVITY);
        keys = pg.key.get_pressed();
        if keys[pg.K_ESCAPE]:
            running = False;
        if keys[pg.K_LEFT]:
            player.turn_left();
        if keys[pg.K_RIGHT]:
            player.turn_right();
        


        if keys[pg.K_a]:
            player.strafe_left(map_array);
        if keys[pg.K_d]:
            player.strafe_right(map_array);
        
        if keys[pg.K_w]:
            player.move_forward(map_array);
        if keys[pg.K_LSHIFT]:
            player.sprint_forward(map_array);
        if keys[pg.K_s]:
            player.move_backward(map_array);


        screen.fill(game_settings.BLACK);


        startAngle = player.angle - (game_settings.PLAYER_FOV / 2);
        for ray in range(game_settings.NUM_RAYS):
            rayAngle = startAngle + ray * DELTA_ANGLE;


            for depth in range(game_settings.RAY_DEPTH):

                rayX = int((player.xPos + depth * np.cos(rayAngle)) / map_array.tileSize);
                rayY = int((player.yPos + depth * np.sin(rayAngle)) / map_array.tileSize);

                if 0 <= rayX <= map_array.width and 0 <= rayY <= map_array.height:
                    if map_array.map_array[rayY, rayX] != game_map.MAP_EMPTY_SPACE:
                        depth *= np.cos(player.angle - rayAngle); #Correct fisheye
        
                        wallHeight = (map_array.tileSize / (depth + 0.0001)) * DIST_TO_PLANE; #0.0001 avoids zero division

                        color = 100 / (1 + (depth ** 2) * 0.0001);
                        color = min(255, max(0, int(color)));

                        pg.draw.rect(screen, (color, color, color), (ray * SLICE_SIZE, (game_settings.SCREEN_HEIGHT / 2) - wallHeight / 2, SLICE_SIZE, wallHeight));
                        break;




        clock.tick(game_settings.FPS);
        pg.display.flip();

    return 0;



if __name__ == "__main__":
    sys.exit(main());







