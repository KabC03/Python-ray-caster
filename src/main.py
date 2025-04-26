import sys;
import pygame as pg;
import numpy as np;
import settings;


def internal_clock_frame(clock: pg.time.Clock) -> None:
    clock.tick(60);






def main() -> int:
    pg.init();
    clock = pg.time.Clock();

    running = True;
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False;



        keys = pg.key.get_pressed();
        




        internal_clock_frame(clock);


    return 0;



if __name__ == "__main__":
    sys.exit(main());







