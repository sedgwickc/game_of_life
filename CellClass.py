import pygame

class cellSprite( pygame.sprite.Sprite ):
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    
    COLOUR_DEAD = BLACK
    COLOUR_ALIVE = GREEN
    
    HEIGHT = 10
    WIDTH = 10
    FONT_DEBUG = 10

    DEAD = 0
    ALIVE = 1

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.state = self.DEAD
        self.x_pos = x
        self.y_pos = y
        self.num_nbrs = 0
        
        self.image = pygame.Surface( (self.WIDTH, self.HEIGHT) )
        self.image.fill( self.COLOUR_DEAD )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def revive( self ):
        self.state = self.ALIVE
        self.image.fill( self.COLOUR_ALIVE )

    def is_alive( self ):
        if self.state == self.ALIVE:
            return True
        else:
            return False

    def kill( self ):
        self.state = self.DEAD
        self.image.fill( self.COLOUR_DEAD )

    def get_rect( self ):
        return self.rect

    def count_nbrs(self, neighbors):
        self.num_nbrs = 0
        for cell in neighbors:
            if cell.is_alive():
                self.num_nbrs += 1

    def update( self ):
        # game rules
        if self.state == self.ALIVE:
            if self.num_nbrs < 2:
                    self.state = self.DEAD
            elif self.num_nbrs > 3:
                    self.state = self.DEAD
        else:
            if self.num_nbrs == 3:
                    self.state = self.ALIVE
        # update cell image     
        if self.state == self.DEAD:
            self.image.fill( self.COLOUR_DEAD )
        else:
            self.image.fill( self.COLOUR_ALIVE )
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
