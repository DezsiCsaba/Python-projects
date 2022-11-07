import pygame; pygame.init()
from Tile import Tile_C
from Cell import Cell_C
from random import randint
import random



pygame.display.set_caption("Wave_Function_Collapse")
def DontClose():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
            pygame.display.update()

h = 400
w = h
canvas = pygame.display.set_mode((h,w))
DIM_of_canvas = 2  # 10 -> 10 x 10 tiles
DIM_of_img = int(h/DIM_of_canvas)
SIZE_of_IMG = (DIM_of_img, DIM_of_img)

path1 = "Python\WaveFunc_Collapse\Coding_Train_Circuit/"
path2 = "Python\WaveFunc_Collapse\Demo_Tiles/blank.png"
def _import_all_images_(dir): #given a directory, lists all the files within
    tileImages = []           # and appends all the files to a list
    
    for i in range(13):
        tileImages.append(pygame.image.load(str(dir) + str(i) + ".png"))
    return tileImages
def load_demo_tiles():
    tiles=[]
    tiles.append(pygame.image.load("Python\WaveFunc_Collapse\Demo_Tiles/blank.png"))
    tiles.append(pygame.image.load("Python\WaveFunc_Collapse\Demo_Tiles/up.png"))
    #tiles.append(pygame.transform.rotate(tiles[0], pi/2 * 1))
    return tiles
def displayIMG():
    x = 0
    for tile in tiles:
        tile = pygame.transform.scale(tile.image, (SIZE_of_IMG))
        canvas.blit(tile, (0, x))
        x +=  DIM_of_img
def DrawAllTiles(tileList):
    index = 0
    y = 0
    x = 0
    for i in range(len(tileList)):
        tileList[index]._ShowTile(canvas, x,y)
        index += 1
        if (x == w-DIM_of_img): x = 0; y += DIM_of_img
        x += DIM_of_img
#tileImages = _import_all_images_(path1)
tileImages = load_demo_tiles()


def CheckValid(list, valid):
    for i in range(len(list)-1):
        element = list[i]
        if (element not in valid):
            slice(i, 1)
#displayIMG()


tiles = []
#Tiles_C takes no argument -> mindegyiket meg kell csinalni kulon es meghivni egyesevel a constructor functciont
def DemoTiles():
    tile1 = Tile_C()
    tile2 = Tile_C()
    tile3 = Tile_C()
    tile4 = Tile_C()
    tile5 = Tile_C()

    tile1._TileInit(tileImages[0], [0,0,0,0], DIM_of_img)
    tile2._TileInit(tileImages[1], [1,1,0,1], DIM_of_img)
    tile3 = tile2.rotate_tile(1)
    tile4 = tile2.rotate_tile(2)
    tile5 = tile2.rotate_tile(3)

    tiles.append(tile1)
    tiles.append(tile2)
    tiles.append(tile3)
    tiles.append(tile4)
    tiles.append(tile5)
    for i in range(len(tiles)):
        tiles[i].index = i
DemoTiles()

grid = []
for i in range(DIM_of_canvas*DIM_of_canvas):
    gridi = Cell_C()
    gridi._CellInit(len(tiles))
    gridi.collapsed = False
    gridi.options = [tiles[0], tiles[1], tiles[2],tiles[3], tiles[4]]
    grid.append(gridi)
    # -----Hardcoded values for debugging
    #grid[0].collapsed = True
    #grid[10].options = [tiles[1], tiles[4]]
    #grid[0].options = [tiles[0], tiles[2]]
    #grid[2].options = [tiles[1], tiles[4]]
print(len(grid))
def _WCF():
    #print("iterated")
    pygame.display.update()
    for i in range(len(tiles)):
        tiles[i]._analyze(tiles)

    
    
    # -----Pick cell with the lowest entropy
    copyOfGrid = grid.copy()
    copyOfGrid.sort(key = lambda x: len(x.options))
    
    for i in range(len(copyOfGrid)):
        if (len(copyOfGrid[i].options) == len(copyOfGrid[0].options)):
            filtered.append(copyOfGrid[i])
    
    
    cell = random.choice(filtered)
    cell.collapsed = True
    pick = random.choice(cell.options)
    cell.options = [pick]
    #print(pick.image)

    x,y = 0,0
    index = 0
    for i in range(DIM_of_canvas):
        x=0
        for j in range(DIM_of_canvas):
            if (grid[index].collapsed == True):
                grid[index].options[0]._ShowTile(canvas, x*DIM_of_img, y*DIM_of_img)
            else:
                pygame.draw.rect(canvas, (0,0,0), (j*DIM_of_img, i*DIM_of_img, DIM_of_img, DIM_of_img))
                
            index += 1
            x += 1
        y += 1
    
    
    nextTiles = []
    for k in range(DIM_of_canvas * DIM_of_canvas):
        nextTiles.append(i)


    for j in range(DIM_of_canvas):
        for i in range(DIM_of_canvas):
            index = i + j * DIM_of_canvas
            if (grid[index].collapsed):
                nextTiles[index] = (grid[index])
            else:
                options = []
                for i in range(len(tiles)):
                    options.append(i)
                #up
                if (j > 0):
                    up = grid[i + (j-1) * DIM_of_canvas]
                    ValidOptions =  []
                    insideindex = 0
                    for z in range(len(up.options)):
                        valid = tiles[z].up
                        ValidOptions.append(valid)
                        insideindex += 1
                    CheckValid(options, ValidOptions)
                #right
                if (i < DIM_of_canvas - 1):
                    right = grid[i + 1 + j *DIM_of_canvas]
                    ValidOptions =  []
                    insideindex = 0
                    for z in range(len(right.options)):
                        valid = tiles[z].right
                        ValidOptions.append(valid)
                        insideindex += 1
                    CheckValid(options, ValidOptions)
                #down
                if (j < DIM_of_canvas - 1):
                    down = grid[i + (j + 1) * DIM_of_canvas]
                    ValidOptions =  []
                    insideindex = 0
                    for z in range(len(down.options)):
                        valid = tiles[z].down
                        ValidOptions.append(valid)
                        insideindex += 1
                    CheckValid(options, ValidOptions)

                #left
                if (j > 0):
                    left = grid[i - 1 + j *DIM_of_canvas]
                    ValidOptions =  []
                    insideindex = 0
                    for z in range(len(left.options)):
                        valid = tiles[z].left
                        ValidOptions.append(valid)
                        insideindex += 1
                    CheckValid(options, ValidOptions)

                next = Cell_C()
                next._CellInit(options)
                #nextTiles[index] = next
                nextTiles.append(next)

    #for i in range(len(grid)):
    #    if grid[i].collapsed == false: return True


filtered = []


while(True):_WCF()

#print(len(filtered))
#DrawAllTiles(tiles)
DontClose()