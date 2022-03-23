import random
import arcade
import constants
from game.casting.target import Target
 
class Bonus_Target( Target ):
    """A circular, moveable target that participates in the game and gives extra points if gets hit. 
    
    The responsibility of Bonus_Target is to draw itself, keep track of its position, velocity and points.

    Attributes:
        velocity.dx( Point ): The random speed and direction for x.
        point (int): The number of points the Bonus_Target is worth.
        radius( int ): The radius of the object.
    """

    def __init__( self ):
        """Constructs a new Bonus_Target."""
        super().__init__()
        self.velocity.dx = random.uniform( 3, 5 )
        self.point = constants.BONUS_TARGET_POINTS
        self.radius = 15

    def draw( self ):
        """Draw the object itself on screen."""

        # Load the image.
        image = arcade.load_texture( constants.BONUS_TARGET_IMAGE )

        # State the scale.
        scale = .05

        # Draw the object on screen.
        arcade.draw_texture_rectangle( self.center._x, self.center._y, scale * image.width, scale * image.height, image, 0 )