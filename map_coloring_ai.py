import pygame
import random
import numpy as np
import time
from scipy.spatial import Voronoi

WIDTH, HEIGHT = 1200, 750
POINTS = 50

COLORS = [
    (255,0,0),
    (0,200,0),
    (0,120,255),
    (255,200,0)
]

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("AI Map Coloring")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None,24)
bigfont = pygame.font.SysFont(None,40)

zoom=1
offset_x=0
offset_y=0
dragging=False

steps=0
ai_time=0
human_time=0

solved=False
ai_mode=False
current_region=None

difficulty={}
human_start=None

# ---------- MAP GENERATION ----------

def generate_map():

    global regions, neighbors, region_color, difficulty

    points=np.array([
        (random.randint(50,900),
         random.randint(50,650))
        for _ in range(POINTS)
    ])

    vor=Voronoi(points)

    regions=[]
    region_map={}

    for i,reg in enumerate(vor.point_region):

        region=vor.regions[reg]

        if -1 in region or len(region)==0:
            continue

        poly=[tuple(vor.vertices[v]) for v in region]

        region_map[i]=len(regions)
        regions.append(poly)

    REGION_COUNT=len(regions)

    neighbors={i:set() for i in range(REGION_COUNT)}

    for (p1,p2) in vor.ridge_points:

        if p1 in region_map and p2 in region_map:

            r1=region_map[p1]
            r2=region_map[p2]

            neighbors[r1].add(r2)
            neighbors[r2].add(r1)

    difficulty={i:len(neighbors[i]) for i in neighbors}

    region_color={}

    return REGION_COUNT


REGION_COUNT=generate_map()

# ---------- POINT IN POLYGON ----------

def point_in_poly(point,poly):

    x,y=point
    inside=False

    for i in range(len(poly)):

        x1,y1=poly[i]
        x2,y2=poly[(i+1)%len(poly)]

        if ((y1>y)!=(y2>y)) and (x<(x2-x1)*(y-y1)/(y2-y1)+x1):
            inside=not inside

    return inside


# ---------- COLOR RULE ----------

def valid(region,color):

    for n in neighbors[region]:

        if region_color.get(n)==color:
            return False

    return True


# ---------- CHECK SOLVED ----------

def check_solved():

    if len(region_color)!=REGION_COUNT:
        return False

    for r in neighbors:
        for n in neighbors[r]:

            if region_color.get(r)==region_color.get(n):
                return False

    return True


# ---------- MRV HEURISTIC ----------

def select_region():

    best=None
    best_opt=10

    for r in range(REGION_COUNT):

        if r not in region_color:

            options=0

            for c in range(4):
                if valid(r,c):
                    options+=1

            if options<best_opt:

                best_opt=options
                best=r

    return best


# ---------- AI SOLVER ----------

def solve():

    global steps,current_region

    if len(region_color)==REGION_COUNT:
        return True

    r=select_region()

    current_region=r

    for c in range(4):

        if valid(r,c):

            region_color[r]=c
            steps+=1

            draw()
            pygame.display.flip()
            pygame.time.delay(10)

            if solve():
                return True

            del region_color[r]

    return False


# ---------- DRAW ----------

def draw():

    screen.fill((240,240,240))

    for r in neighbors:
        for n in neighbors[r]:

            x1,y1=np.mean(regions[r],axis=0)
            x2,y2=np.mean(regions[n],axis=0)

            x1=(x1*zoom)+offset_x
            y1=(y1*zoom)+offset_y
            x2=(x2*zoom)+offset_x
            y2=(y2*zoom)+offset_y

            pygame.draw.line(screen,(180,180,180),(x1,y1),(x2,y2),1)

    for i,poly in enumerate(regions):

        if i in region_color:
            color=COLORS[region_color[i]]
        else:

            d=difficulty.get(i,0)
            shade=240-(d*10)
            shade=max(180,shade)

            color=(shade,shade,shade)

        scaled=[((x*zoom)+offset_x,(y*zoom)+offset_y) for x,y in poly]

        pygame.draw.polygon(screen,color,scaled)
        pygame.draw.polygon(screen,(0,0,0),scaled,1)

        if i==current_region:
            pygame.draw.polygon(screen,(255,0,255),scaled,3)

    draw_ui()


# ---------- UI ----------

def draw_ui():

    # Right UI panel
    pygame.draw.rect(screen,(30,30,30),(950,0,250,750))

    # Title
    title = bigfont.render("MAP AI",True,(255,255,255))
    screen.blit(title,(1020,20))

    texts = [
        f"Mode: {'AI' if ai_mode else 'Human'}",
        f"Regions: {REGION_COUNT}",
        f"AI Steps: {steps}",
        f"AI Time: {round(ai_time,2)}s",
        f"Human Time: {round(human_time,2)}s",
        "",
        "Controls:",
        "1-4 Color",
        "1 Red",
        "2 Green",
        "3 Blue",
        "4 Yellow",
        "SPACE AI Solve",
        "H Human Mode",
        "A AI Mode",
        "5 Easy (10 to 15)",
        "6 Medium (35 to 40)",
        "7 Hard (65 to 70)",
        "R Reset",
        "N New Map",
        "Wheel Zoom",
        "Right Drag"
    ]

    y = 100

    for t in texts:
        txt = font.render(t,True,(255,255,255))
        screen.blit(txt,(970,y))
        y += 25


    # SOLVED message at bottom
    if solved:

        # background box
        pygame.draw.rect(screen,(20,120,20),(970,680,210,50))

        done = bigfont.render("SOLVED!",True,(255,255,255))

        # center text in the box
        done_rect = done.get_rect(center=(1075,705))

        screen.blit(done,done_rect)

selected_color=0 

# ---------- MAIN LOOP ----------

running=True

while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_1: selected_color=0
            if event.key==pygame.K_2: selected_color=1
            if event.key==pygame.K_3: selected_color=2
            if event.key==pygame.K_4: selected_color=3

            if event.key==pygame.K_r:

                region_color.clear()
                steps=0
                solved=False
                ai_time=0
                human_time=0
                human_start=None

            if event.key==pygame.K_h:

                ai_mode=False
                human_start=time.time()

            if event.key==pygame.K_a:

                ai_mode=True

            if event.key==pygame.K_n:

                REGION_COUNT=generate_map()
                steps=0
                solved=False

            # difficulty control

            if event.key==pygame.K_5:

                POINTS=20
                REGION_COUNT=generate_map()

            if event.key==pygame.K_6:

                POINTS=50
                REGION_COUNT=generate_map()

            if event.key==pygame.K_7:

                POINTS=80
                REGION_COUNT=generate_map()

            if event.key==pygame.K_SPACE:

                region_color.clear()
                steps=0

                start=time.time()
                solve()
                ai_time=time.time()-start

                solved=True

        if event.type==pygame.MOUSEWHEEL:

            mouse_x,mouse_y=pygame.mouse.get_pos()

            old_zoom=zoom
            zoom+=event.y*0.1
            zoom=max(0.5,min(zoom,3))

            offset_x = mouse_x - (mouse_x-offset_x)*(zoom/old_zoom)
            offset_y = mouse_y - (mouse_y-offset_y)*(zoom/old_zoom)

        if event.type==pygame.MOUSEBUTTONDOWN:

            if event.button==1 and not ai_mode:

                pos=pygame.mouse.get_pos()

                for i,poly in enumerate(regions):

                    scaled=[((x*zoom)+offset_x,(y*zoom)+offset_y) for x,y in poly]

                    if point_in_poly(pos,scaled):

                        if valid(i,selected_color):

                            region_color[i]=selected_color

                            if check_solved():

                                solved=True

                                if human_start:
                                    human_time=time.time()-human_start

            if event.button==2 or event.button==3:
                dragging=True

        if event.type==pygame.MOUSEBUTTONUP:

            if event.button==2 or event.button==3:
                dragging=False

        if event.type==pygame.MOUSEMOTION:

            if dragging:

                dx,dy=event.rel
                offset_x+=dx
                offset_y+=dy

    draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()