import random
import arcade
import constants
from game.casting.target import Target

class Strong_Target( Target ):
    """A circular, moveable target that participates in the game and gives points if gets hit. 
    
    The responsibility of Strong_Target is to draw itself, keep track of its position, velocity and points.

    Attributes:
        velocity.dx( Point ): The random speed and direction for x.
        point (int): The number of points the Strong_Target is worth.
        lives( int ): The quantity of lives that the object has.
    """

    def __init__( self ):
        """Constructs a Strong_Target."""
        super().__init__()
        self.velocity.dx = random.uniform( 1, 3 )
        self.lives = 3

    def draw( self ):
        """Draw the object itself on screen."""

        # Load the image.
        image = arcade.load_texture( constants.STRONG_TARGET_IMAGE )

        # State the scale.
        scale = .2

        # Draw the object on screen.
        arcade.draw_texture_rectangle( self.center._x, self.center._y, scale * image.width, scale * image.height, image, 0 )
        
        # Draw the number of lives for the object.
        text_x = self.center._x - ( self.radius * 1.2 )
        text_y = self.center._y - ( self.radius / 500 )
        arcade.draw_text( repr( self.lives ), text_x, text_y, self.color, font_size = 15 )

    def hit( self ):
        """Represents the target being hit and should decrement the number of hits remaining for the strong target.
        
        Return
            points( int) : The points scored for that hit."""
        self.lives -= 1
        if self.lives > 0:
            self.alive = True
            self.point = 1
            return self.point
        else:
            self.alive = False
            self.point = 5
            return self.point
