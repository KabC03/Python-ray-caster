import game_settings;
import numpy as np;


#world_map = [
#    [1,1,1,1,1,1,1,1],
#    [1,0,0,0,0,0,0,1],
#    [1,0,1,0,1,0,0,1],
#    [1,0,1,0,1,0,0,1],
#    [1,0,0,0,0,1,0,1],
#    [1,1,1,1,1,1,1,1]
#]


MAP_EMPTY_SPACE = 0; #Empty space in a map is 0
class Map:
    def __init__(self, map: np.array, tileSize: float) -> None:
        self.map = map;
        self.tileSize = tileSize;
        self.width = self.map.shape[0];
        self.height = self.map.shape[1];

    #Check if a position is in a wall (collision)
    def is_collision(self, xPos: float, yPos: float) -> bool:

        xCoord = np.round(xPos / self.tileSize);
        yCoord = np.round(yPos / self.tileSize);

        if self.map[xCoord, yCoord] == MAP_EMPTY_SPACE:
            return True;

        return False;




