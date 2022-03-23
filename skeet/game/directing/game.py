import arcade
import random
import constants
import math
from game.casting.rifle import Rifle
from game.casting.bullet import Bullet
from game.casting.standart_target import Standart_Target
from game.casting.bonus_target import Bonus_Target
from game.casting.safe_target import Safe_Target
from game.casting.strong_target import Strong_Target

class Game( arcade.Window ):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__( self, width, height ):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__( width, height )

        self.rifle = Rifle()
        self.score = 0
        self.background = arcade.load_texture( constants.BACKGROUND_IMAGE )

        self.bullets = []

        # TODO: Create a list for your targets (similar to the above bullets)
        self.targets = []

        # arcade.set_background_color( arcade.color.WHITE )

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # Draw the background.
        arcade.draw_texture_rectangle( constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background )

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            # bullet.draw()
            bullet.draw( self.angle )

        # TODO: iterate through your targets and draw them...
        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format( self.score )
        start_x = 10
        start_y = constants.SCREEN_HEIGHT - 20
        # arcade.draw_text( score_text, start_x = start_x, start_y = start_y, font_size = 12, color = arcade.color.NAVY_BLUE )

        # Change score color.
        arcade.draw_text( score_text, start_x = start_x, start_y = start_y, font_size = 12, color = arcade.color.WHITE )

    def update( self, delta_time ):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        # if random.randint( 1, 50 ) == 1:
        if random.randint( 1, 20 ) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()

    def create_target( self ):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # TODO: Decide what type of target to create and append it to the list
        if random.randint( 1, 4 ) == 1:
            target = Standart_Target()
            self.targets.append( target )
        elif random.randint( 1, 4 ) == 2:
            target = Strong_Target()
            self.targets.append( target )
        elif random.randint( 1, 4 ) == 3:
            target = Safe_Target()
            self.targets.append( target )
        elif random.randint( 1, 4 ) == 4:
            target = Bonus_Target()
            self.targets.append( target )

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if ( abs( bullet.center._x - target.center._x ) < too_close and
                                abs( bullet.center._y - target.center._y ) < too_close ):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies( self ):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove( bullet )

        for target in self.targets:
            if not target.alive:
                self.targets.remove( target )

    def check_off_screen( self ):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen( constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT ):
                self.bullets.remove( bullet )

        for target in self.targets:
            if target.is_off_screen( constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT ):
                self.targets.remove( target )

    def on_mouse_motion( self, x: float, y: float, dx: float, dy: float ):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees( x, y )

    def on_mouse_press( self, x: float, y: float, button: int, modifiers: int ):
        # Fire!
        self.angle = self._get_angle_degrees( x, y )
        # angle = self._get_angle_degrees( x, y )

        bullet = Bullet()
        bullet.fire( self.angle )
        # bullet.fire( angle )

        self.bullets.append( bullet )

    def _get_angle_degrees( self, x, y ):
        """
        Gets the value of an angle ( in degrees ) defined
        by the provided x and y.

        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2( y, x )

        # convert to degrees
        angle_degrees = math.degrees( angle_radians )

        return angle_degrees