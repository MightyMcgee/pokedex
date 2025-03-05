import requests
import pygame
from PIL import Image

URL = "https://pokeapi.co/api/v2/pokemon/"
number = input("What number or name? ")
URL = URL+number

r = requests.get(url = URL)
data = r.json()
name = data['species']['name']

image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png"

img_data = requests.get(image_url).content
with open('image.jpg', 'wb') as handler:
    handler.write(img_data)

pygame.init()
display_surface = pygame.display.set_mode((600, 700))

white = (255, 255, 255)
black = (0,0,0)
font = pygame.font.Font('pokemon.ttf',50)
text = font.render(name, True, white)
width = text.get_rect().width
display_surface.blit(text, (300-(width/2),600))

Image.open('image.jpg').convert('RGB').save('image.jpg')
image = Image.open('image.jpg')
new_image = image.resize((600, 600))
new_image.save('scaled.jpg')
imp = pygame.image.load("/home/sean/Documents/vscode/scaled.jpg").convert()

display_surface.blit(imp, (0, 0))
pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

pygame.quit()