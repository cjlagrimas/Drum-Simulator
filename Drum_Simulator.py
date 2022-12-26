# Created using the guidance of FCC Drum Beat maker Tutorial

# Import needed modules
import pygame
from pygame import mixer

# Start pygame
pygame.init()

# setting windows dimension
height = 400
width = 700

# setting colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = (50, 50, 50)
green = (0, 255,0)
gold = (212, 175, 55)
blue = (0, 255, 255)

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Drum simulator")
label_font = pygame.font.Font("Roboto-Bold.ttf", 16)
medium_font = pygame.font.Font("Roboto-Bold.ttf", 14)

fps = 60
bpm = 240
playing = True
active_length = 0
active_beat = 0
beat_changed = True
beats = 8
instrument = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instrument)]
active_list = [1 for _ in range(instrument)]
timer = pygame.time.Clock()
screen = pygame.display.set_mode([width, height])

#Sounds
hi_hat = mixer.Sound("Sounds\hi hat.WAV")
snare = mixer.Sound("Sounds\snare.WAV")
kick = mixer.Sound("Sounds\kick.WAV")
crash = mixer.Sound("Sounds\crash.WAV")
clap = mixer.Sound("Sounds\clap.WAV")
tom = mixer.Sound("Sounds\\tom.WAV")
pygame.mixer.set_num_channels(instrument * 3)

def play_notes():
    for i in range(len(clicked)):
        if (clicked[i][active_beat] == 1) and (active_list[i] == 1):
            if i == 0:
                hi_hat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                crash.play()
            if i == 4:
                clap.play()
            if i == 5:
                tom.play()

def draw_grid(clicks, beat, actives):
    left_box = pygame.draw.rect(screen, gray, [0,0,100,height-100],3)
    bottom_box = pygame.draw.rect(screen, #Surface
                                  gray, #Color
                                  [0, height-100, width, 100], #x, y, len, wid
                                  3, #Border Thickness
                                  5) #Border Radius
    boxes = []
    colors = [gray, white, gray]

    #Instrument's labels
    hi_hat_text = label_font.render("Hi Hat",True,colors[actives[0]])
    screen.blit(hi_hat_text, (10, 20))
    snare_text = label_font.render("Snare",True,colors[actives[1]])
    screen.blit(snare_text, (10, 70))
    kick_text = label_font.render("Kick",True,colors[actives[2]])
    screen.blit(kick_text, (10, 120))
    crash_text = label_font.render("Crash",True,colors[actives[3]])
    screen.blit(crash_text, (10, 170))
    clap_text = label_font.render("Clap",True,colors[actives[4]])
    screen.blit(clap_text, (10, 220))
    floor_tom_text = label_font.render("Floor Tom",True,colors[actives[5]])
    screen.blit(floor_tom_text, (10, 270))

    #Draw line after each label
    for i in range(instrument):
        pygame.draw.line(screen, gray, [0, (i*50) +50], [100, (i*50)+50],3)

    for i in range(beats):
        for j in range(instrument):
            if clicks[j][i] == -1:
                color = gray
            else:
                color = green
            rect = pygame.draw.rect(screen, color, 
                                    [i * ((width-100)//beats) + 100, 
                                     (j*50 + 5), 
                                     ((width-100) // beats) - 5, 
                                     ((height-100)//instrument)-5],
                                     0,
                                     5)
            pygame.draw.rect(screen, gold, 
                                    [i * ((width-100)//beats) + 100, 
                                     (j*50), 
                                     ((width-100) // beats), 
                                     ((height-100)//instrument)],
                                     5,
                                     5)
            pygame.draw.rect(screen, black, 
                                    [i * ((width-100)//beats) + 100, 
                                     (j*50), 
                                     ((width-100) // beats), 
                                     ((height-100)//instrument)],
                                     2,
                                     5)
            boxes.append((rect, (i,j)))

            #Moving indicator that indicates what is active
            active = pygame.draw.rect(screen,
                                      blue,
                                      [beat * ((width-100)//beats)+100,0,((width-100)//beats), instrument * 50],5,3)
    return boxes


run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat, active_list)

    #Lower menus buttons
    play_pause = pygame.draw.rect(screen, gray, [15, height-75, 100, 50],0,5)
    play_text = label_font.render("Play/Pause", True, white)
    screen.blit(play_text, (25, height-70))

    if playing:
        play_text2 = medium_font.render("Play", True, dark_gray)
    else:
        play_text2 = medium_font.render("Pause", True, dark_gray)
    screen.blit(play_text2, (40, height-45))
    
    # bpm settings
    bpm_rect = pygame.draw.rect(screen, gray, [120, height-75, 100, 50], 0, 5)
    bpm_text = medium_font.render("BPM", True, white)
    screen.blit(bpm_text, (155, height-70))
    bpm_text2 = label_font.render(str(bpm), True, white)
    screen.blit(bpm_text2, (155, height-45))
    bpm_add_rect = pygame.draw.rect(screen, gray, [224, height-75, 24,24], 0, 5)
    bpm_add_text = medium_font.render("+", True, white)
    screen.blit(bpm_add_text, (233, height-70))
    bpm_minus_rect = pygame.draw.rect(screen, gray, [224, height-50, 24, 24], 0, 5)
    bpm_minus_text = medium_font.render("-", True, white)
    screen.blit(bpm_minus_text, (233, height-45))

    #beats settings
    beats_rect = pygame.draw.rect(screen, gray, [253, height-75, 100, 50], 0, 5)
    beats_text = medium_font.render("Beats", True, white)
    screen.blit(beats_text, (285, height-70))
    beats_text2 = label_font.render(str(beats), True, white)
    screen.blit(beats_text2, (300, height-45))
    beats_add_rect = pygame.draw.rect(screen, gray, [357, height-75, 24,24], 0, 5)
    beats_add_text2 = medium_font.render("+", True, white)
    screen.blit(beats_add_text2, (365, height-70))
    beats_minus_rect = pygame.draw.rect(screen, gray, [357, height-50, 24, 24], 0, 5)
    beats_minus_text2 = medium_font.render("-", True, white)
    screen.blit(beats_minus_text2, (365, height-45))

    #Instruments rect
    instrument_rect = []
    for i in range(instrument):
        rect = pygame.rect.Rect((0, i*50), (100, 50))
        instrument_rect.append(rect)

    if beat_changed:
        play_notes()
        beat_changed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
        if event.type == pygame.MOUSEBUTTONUP:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing =True
            elif bpm_add_rect.collidepoint(event.pos):
                    bpm += 5
            elif bpm_minus_rect.collidepoint(event.pos):
                    bpm -= 5
            elif beats_add_rect.collidepoint(event.pos):
                    beats += 1
                    for i in range(len(clicked)):
                        clicked[i].append(-1)
            elif beats_minus_rect.collidepoint(event.pos):
                    beats -= 1
                    for i in range(len(clicked)):
                        clicked[i].pop(-1)
            for i in range(len(instrument_rect)):
                if instrument_rect[i].collidepoint(event.pos):
                    active_list[i] *= -1


    beat_length = 3600 // bpm
    
    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

    pygame.display.flip()
pygame.quit()