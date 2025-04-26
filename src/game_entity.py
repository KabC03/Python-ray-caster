import game_map;
import numpy as np;


class Entity:
    def __init__(self, moveSpeed: float, turnSpeed: float, xPos: float, yPos: float, angle: float) -> None:
        self.moveSpeed = moveSpeed;
        self.turnSpeed = turnSpeed;
        self.xPos = xPos;
        self.yPos = yPos;
        self.angle = angle;
        return None;


    #Turn left
    def turn_left(self) -> None:
        self.angle -= self.turnSpeed;
        return None;

    #Turn right
    def turn_right(self) -> None:
        self.angle += self.turnSpeed;
        return None;

    #Move forward
    def move_forward(self, map: np.array) -> None:
        newX = self.xPos + self.moveSpeed * np.cos(self.angle);
        newY = self.yPos + self.moveSpeed * np.sin(self.angle);

        if map.is_collision(newX, self.yPos) == False:
            self.xPos = newX;

        if map.is_collision(self.xPos, newY) == False:
            self.yPos = newY;
        
        return None;

    #Move backward
    def move_backward(self, map: np.array) -> None:
        newX = self.xPos - self.moveSpeed * np.cos(self.angle);
        newY = self.yPos - self.moveSpeed * np.sin(self.angle);

        if map.is_collision(newX, self.yPos) == False:
            self.xPos = newX;

        if map.is_collision(self.xPos, newY) == False:
            self.yPos = newY;

        return None;



























