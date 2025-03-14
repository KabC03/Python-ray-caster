import sys;
import pygame as pg;
import numpy as np;
import map;
import player;
import settings;

xRes = 800;
yRes = 600;


def main():
    pg.init();

    screen = pg.display.set_mode((xRes, yRes));
    pg.display.set_caption("Raycaster");

    running = True;
    while running:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False;
            
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False;






    pg.quit();
    return 0;





if __name__ == "__main__":
    sys.exit(main());



