import arcade
import constants
from game.casting.target import Target

class Safe_Target( Target ):
    """A rectangular, moveable target that participates in the game and should be protected. 
    
    The responsibility of Safe_Target is to draw itself, keep track of its position, velocity and points.

    Attributes:
        point (int): The number of points the Safe_Target is worth.
    """

    def __init__( self ):
        """Constructs a new Safe_Target."""
        super().__init__()
        self.point = constants.SAFE_TARGET_POINTS

    def draw( self ):
        """Draw the object itself on screen."""

        # Load the image.
        image = arcade.load_texture( constants.SAFE_TARGET_IMAGE )

        # State the scale.
        scale = .07

        # Draw the object on screen.
        arcade.draw_texture_rectangle( self.center._x, self.center._y, scale * image.width, scale * image.height, image, 0 )