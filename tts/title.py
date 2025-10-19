from config import *

background_colour = (15, 106, 112)
(width, height) = (500, 500)
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.NOFRAME)

pygame.display.set_caption('Shindo')

screen.fill(background_colour)
pygame.display.flip()


def add_to_tindex(tuple, index, amount): # add to tuple index unsafe asf cus lazy coding
    new_tup_changed_index = tuple[index] + amount
    if index == 1:
        new_tup = (tuple[0], new_tup_changed_index)
    else: 
        new_tup = (new_tup_changed_index, tuple[1])

    return new_tup
    
def gen_debug_txt(text):
    text = font.render(text, True, (255, 255, 255))  
    return text

def fetch_true_center(ints):
    center = (info.current_w / 2, info.current_h / 2)

    try:
        if not ints:
            return center
        else: 
            return center[0], center[1]
    except:
        return 0,0 # handle crashes

def switchScene():
    print('switched')
    showTitle = False
    return True    


# fonts & stuff
play = font.render("play", True, (255, 255, 255))  
saves = font.render("saves", True, (255, 255, 255))  

pax, pay = fetch_true_center(True)

play_area = pygame.Rect(pax, pay, play.get_width(), play.get_height())
saves_area = pygame.Rect(pax, pay+savesMargin, saves.get_width(), saves.get_height())

print(f"play button area: {play_area}")
print(f"save button area {saves_area}")

cloud1floor = pygame.image.load("tts\\background\\clouds_mg_1.png") 
cloud2lonely = pygame.image.load("tts\\background\\cloud_lonely.png") 

# Base positions
baseX, baseY = 0, 0

# Get image width/height
cloud_w, cloud_h = cloud1floor.get_size()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if play_area.collidepoint(event.pos):
                Playing = switchScene()
            elif saves_area.collidepoint(event.pos):
                Saves = switchScene()

    center = fetch_true_center(False)

    if showTitle:
        screen.fill(background_colour)
        screen.blit(play, center)
        screen.blit(saves, add_to_tindex(center, 1, savesMargin))
        
        # Scroll cloud
        screen.blit(pygame.transform.scale(cloud1floor, (info.current_w, info.current_h)), (baseX * 0.3, baseY))
        # Duplicate for wrapping
        screen.blit(pygame.transform.scale(cloud1floor, (info.current_w, info.current_h)), (baseX * 0.3 - info.current_w, baseY))
        

        # smol cloud :D 
        screen.blit(pygame.transform.scale(cloud2lonely, (info.current_w, info.current_h)), (baseX, baseY))
        screen.blit(pygame.transform.scale(cloud2lonely, (info.current_w, info.current_h)), (baseX - info.current_w, baseY))


        baseX += 3  # scroll speed

        # Wrap around
        if baseX >= info.current_w:
            baseX -= info.current_w

        

    if Playing:
        screen.fill((0,0,0))
        playing = gen_debug_txt("playing")
        screen.blit(playing, fetch_true_center(False))
    if Saves:
        screen.fill((0,0,0))
        saves = gen_debug_txt("saves")
        screen.blit(saves, fetch_true_center(False))

    pygame.display.flip()
