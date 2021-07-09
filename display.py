import pygame 
from pygame.locals import DOUBLEBUF


class Display2D(object):
    def __init__(self,w,h):
        pygame.init()
        self.movie_screen = pygame.display.set_mode((w,h),DOUBLEBUF)
        self.movie_surface= pygame.Surface(self.movie_screen.get_size()).convert()

    
    def draw(self,frame):
        
        for event in pygame.event.get():
            pass
        
        # surfarry.plot_array: Blit directly from a array values

        pygame.surfarray.blit_array(self.movie_surface,frame.swapaxes(0,1)[:, :, [0,1,2]])
        self.movie_screen.blit(self.movie_surface,(0,0))

        pygame.display.flip()


