import requests
import pygame
from PIL import Image
import re

while True:
    try:
        URL = "https://pokeapi.co/api/v2/pokemon/"
        number = input("What number pokemon? ")
        URL = URL+number

        r = requests.get(url = URL)
        data = r.json()
        name = data["species"]["name"]
        sprite_info_back = data['sprites']['back_default']
        sprite_info_front = data['sprites']['front_default']
        sprite_info_shiny = data['sprites']['front_shiny']



        back_image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/{number}.png"
        front_image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png"
        shiny_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{number}.png"
        


        #inital
        img_data = requests.get(front_image_url).content
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
        imp = pygame.image.load("/home/maeve/VSCode/scaled.jpg").convert_alpha()

        display_surface.blit(imp, (0, 0))
        pygame.display.flip()
        status = True
        x = False



        while (status):
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    status = False
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_SPACE:
                        if x:
                            img_data = requests.get(front_image_url).content
                            with open('image.jpg', 'wb') as handler:
                                handler.write(img_data)
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
                            imp = pygame.image.load("/home/maeve/VSCode/scaled.jpg").convert()

                            display_surface.blit(imp, (0, 0))
                            pygame.display.flip()
                            status = True
                            x = False

                        else:
                            img_data = requests.get(back_image_url).content
                            with open('image.jpg', 'wb') as handler:
                                handler.write(img_data)
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
                            imp = pygame.image.load("/home/maeve/VSCode/scaled.jpg").convert_alpha()

                            display_surface.blit(imp, (0, 0))
                            pygame.display.flip()
                            status = True
                            x = True
        pygame.quit()





    except requests.JSONDecodeError:
        print("invalid input")
    except Image.UnidentifiedImageError:
        print("There is no back to this pokemon")