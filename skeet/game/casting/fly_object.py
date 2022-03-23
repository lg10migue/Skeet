from game.shared.point import Point
from game.shared.velocity import Velocity

class Fly_Object():
    """A thing that participates flying in the game.
    
    Attributes:
        center( Point ): The center screen coordinates.
        velocity( Point ): The speed and direction.
        radius( int ): The radius of the object.
        alive( bool ): If the object is alive or not.
    """

    def __init__( self ):
        """Constructs a new Fly_Object."""
        self.center = Point( 0, 0 )
        self.velocity = Velocity()
        self.radius = 0
        self.alive = True
    
    def draw( self ):
        """Draw the object itself on screen. This method should be overriden by 
        derived classes.
        """
        pass

    def advance( self ):
        """Moves the fly object to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            center._x( int ): The maximum x value.
            center._y( int ): The maximum y value.
        """
        # Move the flying object forward.  
        self.center._x += self.velocity.dx
        self.center._y += self.velocity.dy
    
    def is_off_screen( self, screen_width, screen_height ):
        """Check if the fly object is still present on the screen.

        Args:
            screen_width( int ): The screen width.
            screen_height( int ): The screen height.
        """
        # Check whether the flying object is on screen or not.
        if ( self.center._x > screen_width  or self.center._y > screen_height ):
            return True
        else:
            return False