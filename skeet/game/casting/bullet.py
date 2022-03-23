import constants
import arcade
import math
from game.casting.fly_object import Fly_Object

class Bullet( Fly_Object ):
    """
    A circular object shot by the rifle.
    
    The responsibility of Bullet is to move itself.

    Attributes:
        radius( int ): The radius of the bullet.
        color( str ): The color of the bullet.
    """
    def __init__( self ):
        """Constructs a new Bullet."""
        super().__init__()
        self.radius = constants.BULLET_RADIUS
        self.color = constants.BULLET_COLOR
    
    def draw( self, angle ):
        """Draw the object itself on screen."""

        # Load the image.
        image = arcade.load_texture( constants.BULLET_IMAGE )

        # State the scale.
        scale = .03

        # Draw the object on screen.
        arcade.draw_texture_rectangle( self.center._x, self.center._y, scale * image.width, scale * image.height, image, angle - 90  )
    
    def fire( self, angle ):
        """Shoot the bullet at the indicated angle.

        Args:
            angle( int ): The angle at which the bullet will move.
        """
        # Fire the bullet.
        self.velocity.dx = math.cos( math.radians( angle ) ) * constants.BULLET_SPEED
        self.velocity.dy = math.sin( math.radians( angle ) ) * constants.BULLET_SPEED