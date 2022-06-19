import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((720,480))
pygame.display.set_caption('GameName')
clock = pygame.time.Clock()

# Variables
FPS = 60
score = 10
score_fix = 1 #évite le décallage du score dû aux décimales
pps = 0 #points par seconde
ppc = 0 #points par click

# Prix
ppc1_prix = 1
ppc10_prix = 200
pps1_prix = 10
pps10_prix = 1000

# Timers
pas = 1
loop=1
pps_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pps_timer, pas*1000) #délai pas seconde

fixer_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fixer_timer, 1000) #délai 1 seconde

# Fonts
general_font = pygame.font.Font('fonts\epyval\Epyval.ttf',50)
medium_font = pygame.font.Font('fonts\epyval\Epyval.ttf',35)
small_font = pygame.font.Font('fonts\epyval\Epyval.ttf',20)
tiny_font = pygame.font.Font('fonts\epyval\Epyval.ttf',10)


# Textes
restart_surf = small_font.render('Recommencer : [Espace]', False,'Purple')
restart_rect = restart_surf.get_rect(bottomright = (720, 480))

text_ppc1_surf = small_font.render('PPC + 1', False,'Black')
text_ppc1_rect = text_ppc1_surf.get_rect(center = (100,170))

text_ppc10_surf = small_font.render('PPC + 10', False,'Black')
text_ppc10_rect = text_ppc10_surf.get_rect(center = (200,170))

text_pps1_surf = small_font.render('PPS + 1', False,'Black')
text_pps1_rect = text_pps1_surf.get_rect(center = (100,270))

text_pps10_surf = small_font.render('PPS + 10', False,'Black')
text_pps10_rect = text_pps10_surf.get_rect(center = (200,270))

# Fonctions
def format_nombre(n):
    suffixes = ['k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    size = [1e3, 1e6, 1e9, 1e12, 1e15, 1e18, 1e21, 1e24]
    if n < size[0]:
        return  str(n)
    if size[0] <= n < size[1]:
        return str(int(n/size[0]))+' '+str(suffixes[0])

game_active = True

while True:
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:

            if event.type == pygame.MOUSEBUTTONDOWN:

                if click_rect.collidepoint(event.pos):
                    score_fix += ppc
                if bonus_ppc1_rect.collidepoint(event.pos) and score >= ppc1_prix:
                    ppc += 1
                    score_fix -= ppc1_prix
                    ppc1_prix *= 10
                if bonus_ppc10_rect.collidepoint(event.pos) and score >= ppc10_prix:
                    ppc += 10
                    score_fix -= ppc10_prix
                    ppc10_prix *= 10
                if bonus_pps1_rect.collidepoint(event.pos) and score >= pps1_prix:
                    pps += 1
                    score_fix -= pps1_prix
                    pps1_prix *= 10
                if bonus_pps10_rect.collidepoint(event.pos) and score >= pps10_prix:
                    pps += 10
                    score_fix -= pps10_prix
                    pps10_prix *= 10
                score = score_fix

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                score = 1
                score_fix = 1
                pps = 0
                ppc = 0
                ppc1_prix = 1
                ppc10_prix = 200
                pps1_prix = 10
                pps10_prix = 1000

            # if event.type == pps_timer :
            #     print('score =' + str(score))
            #     print(str(loop*pas)+' secondes')
            #     loop += 1

            if event.type == fixer_timer :
            #if event.type == fixer_timer:
                score_fix += pps #car 1s est passée depuis le dernier fix
                score = score_fix

# écran de jeu
    if game_active :


        # Interface
            # Background
        bg_surf = pygame.Surface((720,480))
        bg_surf.fill('Grey')
        bg_rect = bg_surf.get_rect()
        screen.blit(bg_surf,bg_rect)

            # Zone_click
        click_surf = pygame.Surface((300,400))
        click_surf.fill('Pink')
        click_rect = click_surf.get_rect(center = (460,240))
        screen.blit(click_surf,click_rect)

        score_surf = general_font.render('Score : '+format_nombre(int(score)), False,'Red')
        score_rect = score_surf.get_rect(center = (460,100))
        screen.blit(score_surf, score_rect)

        tiny_score_surf = tiny_font.render('Score : '+str(int(score)), False,'Red')
        tiny_score_rect = tiny_score_surf.get_rect(center = (460,150))
        screen.blit(tiny_score_surf, tiny_score_rect)
            # Texte PPC
        ppc_surf = medium_font.render('Points/click : '+str(ppc), False,'Red')
        ppc_rect = ppc_surf.get_rect(center = (460,200))
        screen.blit(ppc_surf, ppc_rect)
            # Texte PPS
        pps_surf = medium_font.render('Points/s : '+str(pps), False,'Red')
        pps_rect = pps_surf.get_rect(center = (460,300))
        screen.blit(pps_surf, pps_rect)

            # Zone_bonus_ppc_1
        bonus_ppc1_surf = pygame.Surface((100,100))
        bonus_ppc1_surf.fill('Gold')
        bonus_ppc1_rect = bonus_ppc1_surf.get_rect(center = (100,200))
        screen.blit(bonus_ppc1_surf,bonus_ppc1_rect)

        text_ppc1_prix_surf = small_font.render('Coût : ' + format_nombre(ppc1_prix), False,'Black')
        text_ppc1_prix_rect = text_ppc1_prix_surf.get_rect(center = (100,210))
        screen.blit(text_ppc1_surf,text_ppc1_rect)
        screen.blit(text_ppc1_prix_surf,text_ppc1_prix_rect)
            # Zone_bonus_ppc_10
        bonus_ppc10_surf = pygame.Surface((100,100))
        bonus_ppc10_surf.fill('Green')
        bonus_ppc10_rect = bonus_ppc10_surf.get_rect(center = (200,200))
        screen.blit(bonus_ppc10_surf,bonus_ppc10_rect)

        text_ppc10_prix_surf = small_font.render('Coût : ' + format_nombre(ppc10_prix), False,'Black')
        text_ppc10_prix_rect = text_ppc10_prix_surf.get_rect(center = (200,210))
        screen.blit(text_ppc10_surf,text_ppc10_rect)
        screen.blit(text_ppc10_prix_surf,text_ppc10_prix_rect)
        screen.blit(text_ppc10_surf,text_ppc10_rect)

            # Zone_Bonus_pps_1
        bonus_pps1_surf = pygame.Surface((100,100))
        bonus_pps1_surf.fill('LightBlue')
        bonus_pps1_rect = bonus_pps1_surf.get_rect(center = (100,300))
        screen.blit(bonus_pps1_surf,bonus_pps1_rect)
        screen.blit(text_pps1_surf,text_pps1_rect)


        text_pps1_prix_surf = small_font.render('Coût : ' + format_nombre(pps1_prix), False,'Black')
        text_pps1_prix_rect = text_pps1_prix_surf.get_rect(center = (100,310))
        screen.blit(text_pps1_prix_surf,text_pps1_prix_rect)

            # Zone_bonus_pps_10
        bonus_pps10_surf = pygame.Surface((100,100))
        bonus_pps10_surf.fill('brown')
        bonus_pps10_rect = bonus_pps10_surf.get_rect(center = (200,300))
        screen.blit(bonus_pps10_surf,bonus_pps10_rect)
        screen.blit(text_pps10_surf,text_pps10_rect)

        text_pps10_prix_surf = small_font.render('Coût : ' + format_nombre(pps10_prix), False,'Black')
        text_pps10_prix_rect = text_pps10_prix_surf.get_rect(center = (200,310))
        screen.blit(text_pps10_prix_surf,text_pps10_prix_rect)

        score = score + pps/FPS

            # Texte Recommencer
        screen.blit(restart_surf, restart_rect)

    pygame.display.update()
    clock.tick(FPS) #FPS
