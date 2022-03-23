import arcade
import constants
from game.casting.target import Target

class Standart_Target( Target ):
    """A circular, moveable target that participates in the game and gives points if gets hit. 
    
    The responsibility of Standart_Target is to draw itself, keep track of its position, velocity and points.

    Attributes:
        point (int): The number of points the Safe_Target is worth.
    """

    def __init__( self ):
        """Constructs a new Standart_Target."""
        super().__init__()
        self.point = constants.STANDART_TARGET_POINTS

    def draw( self ):
        """Draw the object itself on screen."""

        # Load the image.
        image = arcade.load_texture( constants.STANDARD_TARGET_IMAGE )

        # State the scale.
        scale = .2

        # Draw the object on screen.
        arcade.draw_texture_rectangle( self.center._x, self.center._y, scale * image.width, scale * image.height, image, 0 )