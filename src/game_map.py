import game_settings;
import numpy as np;


MAP_EMPTY_SPACE = 0; #Empty space in a map_array is 0
class Map:
    def __init__(self, map_array: np.array, tileSize: float) -> None:
        self.map_array = map_array;
        self.tileSize = tileSize;
        self.width = self.map_array.shape[1];
        self.height = self.map_array.shape[0];

    #Check if a position is in a wall (collision)
    def is_collision(self, xPos: float, yPos: float) -> bool:

        xCoord = int(np.round(xPos / self.tileSize));
        yCoord = int(np.round(yPos / self.tileSize));

        if 0 <= xCoord < self.width and 0 <= yCoord < self.height:
            if self.map_array[yCoord, xCoord] == MAP_EMPTY_SPACE:
                return False;

        return True;




