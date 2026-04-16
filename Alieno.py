import g2d

LARGEUR = 600
HAUTEUR = 400
dx = 3          # déplacement horizontal par frame
dy = 30         # descente à chaque rebord
x = 0
y = 0
descente = 0    # pixels restants à descendre

def tick():
    global x, y, dx, descente

    # Fond noir
    g2d.set_color((0, 0, 0))
    g2d.draw_rect((0, 0), (LARGEUR, HAUTEUR))

    if descente > 0:
        # Mode descente : on descend, on ne bouge PAS en horizontal
        x += 0
        y += 1
        descente -= 1
    else:
        # Mode horizontal : on avance, on ne descend PAS
        x += dx

        # Arrivée au bord droit
        if x >= LARGEUR - 20:
            x = LARGEUR - 20
            dx = -dx
            descente = dy

        # Arrivée au bord gauche
        elif x <= 0:
            x = 0
            dx = -dx
            descente = dy

    # Affichage de l'alien (fantôme) découpé depuis le sprite
    g2d.draw_image("sprites.png", (x, y), (20, 0), (20, 20))

def main():
    g2d.init_canvas((LARGEUR, HAUTEUR))
    g2d.main_loop(tick)

main()