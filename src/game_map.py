import game_settings;
import numpy as np;


MAP_EMPTY_SPACE = 0; #Empty space in a map is 0
class Map:
    def __init__(self, map: np.array, tileSize: float) -> None:
        self.map = map;
        self.tileSize = tileSize;
        self.width = self.map.shape[1];
        self.height = self.map.shape[0];

    #Check if a position is in a wall (collision)
    def is_collision(self, xPos: float, yPos: float) -> bool:

        xCoord = int(np.round(xPos / self.tileSize));
        yCoord = int(np.round(yPos / self.tileSize));

        if self.map[xCoord, yCoord] == MAP_EMPTY_SPACE:
            return False;

        return True;




