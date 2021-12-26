import pygame as pg
import game.definitions as definitions

pg.init()
pg.font.init()

COLOR_INACTIVE = pg.Color(127,127,127)
COLOR_ACTIVE = pg.Color(255,255,255)
FONT = pg.font.SysFont('arial', 20)


class Chat:

    def __init__(self, resource_manager, x, y, w, h, text=''):
        self.resource_manager = resource_manager
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the chat rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    if self.text == "NINJALUI":
                        self.resource_manager.resources["wood"] += 10000
                        self.resource_manager.resources["stone"] += 10000
                    elif self.text == "minimap":
                        if definitions.afficher_minimap == "oui" :
                            definitions.afficher_minimap = "non"
                        else : definitions.afficher_minimap = "oui"
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
