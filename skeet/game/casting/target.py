import random
import constants
from game.casting.fly_object import Fly_Object

class Target( Fly_Object ):
    """A thing, moveable target that participates in the game. 
    
    The responsibility of Target is to draw itself, keep track of its position, velocity and points.

    Attributes:
        center._y( Point ): The random position for y.
        velocity.dx( Point ): The random speed and direction for x.
        velocity.dy( Point ): The random speed and direction for y.
        radius( int ): The radius of the target.
        color( str ): The color of the target.
        point (int): The number of points the target is worth.
    """

    def __init__(self):
        """Constructs a new Target."""
        super().__init__()
        self.center._y = random.uniform( constants.SCREEN_HEIGHT / 2, constants.SCREEN_HEIGHT )
        self.velocity.dx = random.uniform( 1, 5 )
        self.velocity.dy = random.uniform( -2, 2 )
        self.radius = constants.TARGET_RADIUS
        self.color = constants.TARGET_COLOR
        self.point = 0

    def hit( self ):
        """Represents the target being hit and should kill the target.
        
        Return
            points( int) : The points scored for that hit."""
        self.alive = False
        return self.point