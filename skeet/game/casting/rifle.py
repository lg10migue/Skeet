import arcade
import constants
from game.shared.point import Point

class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.

    Attributes:
        center( Point ): The center screen coordinates.
        angle( int ): The angle at which the rifle should be aimed.
    """
    def __init__( self ):
        """Constructs a new Rifle."""
        self.center = Point( 20, 20 )
        self.center.x = 0
        self.center.y = 0
        self.angle = 45

    def draw( self ):
        """Draw the object itself on screen."""
        
        # Load the image.
        image = arcade.load_texture( constants.RIFLE_IMAGE )

        # State the scale.
        scale = .1

        # Draw the object on screen.
        arcade.draw_texture_rectangle( self.center._x, self.center._y, scale * image.width, scale * image.height, image, self.angle - 90 )