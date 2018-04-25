import pygame, sys, os
import numpy as np
'''
This class presents a visualization of the board
'''
class SlidePuzzle:
       #  gs = grid size
       #  ts = size of the tiles
       #  ms = size of the margin
    def __init__(self, gs, ts, ms):
        self.gs = gs
        self.ts = ts
        self.ms = ms

        # create board of size nxn
        self.tiles_len = len(gs[0])*len(gs[1])

        # array that will mimic the tiles on the board
        self.tiles = [(x, y) for y in range(len(gs[1])) for x in range(len(gs[0]))]
        # print(self.tiles)

        # positions of the tiles on the board
        self.tilespos = {(x, y):(x*(ts+ms), y*(ts+ms)+ms) for y in range(len(gs[1])) for x in range(len(gs[0]))}

        # size of the font 
        self.font = pygame.font.Font(None, 120)

        # flatten the permutation array to display on the board
        display_arr = gs.flatten()

        self.images = []
        for i in range(self.tiles_len):
            image = pygame.Surface((ts, ts))
            if display_arr[i] != 0:
                image.fill((0, 255, 0))
                text = self.font.render(str(display_arr[i]), 1, (0, 0, 0))
                w, h = text.get_size()
                image.blit(text, ((ts-w)/2, (ts-h)/2))
            self.images += [image]
        
    def update(self, dt, moves_list):
        x,y = self.opentile

        if moves_list[0] == 'R':
            self.switch((x+1, y))
        elif moves_list[0] == 'L':
            self.switch((x-1, y))
        elif moves_list[0] == 'U':
            self.switch((x, y-1))
        elif moves_list[0] == 'D':
            self.switch((x, y+1))
        

    def draw(self, screen):
        for i in range(self.tiles_len):
            x, y = self.tilespos[self.tiles[i]]
            screen.blit(self.images[i], (x, y))


    def getBlank(self):
        index_0 = np.argmin(self.gs)
        # print(index_0)
        return self.tiles[index_0]
    
    def setBlank(self, pos):
        index_0 = np.argmin(self.gs)
        self.tiles[index_0] = pos

    opentile = property(getBlank, setBlank)
    # print(opentile)
    def switch(self, tile):
        
        self.tiles[self.tiles.index(tile)] = self.opentile
        self.opentile = tile

# Main methods that runs the visualization 
def main(arr, moves_list):
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('Slide Puzzle')
    screen = pygame.display.set_mode((800, 600))
    fpsclock = pygame.time.Clock()
    # arr = np.array([[1,2,3], [4,0,5], [8,6,7]])
    program = SlidePuzzle(arr, 160, 5)
    # moves_list = ['R', 'D', 'L', 'L', 'U', 'R', 'R', 'D', 'L', 'U', 'L', 'D', 'R', 'R']
    counter = 0
    while True:
        dt = fpsclock.tick(2) 


        screen.fill((0,0,0,0))
        program.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        
        if counter < len(moves_list):
            program.update(dt, moves_list[counter])
            counter += 1
