import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_p, K_s, K_n, K_b

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Music Player with Buttons")

playlist = [
    "Lab_7\\musics\\Can't tell me nothing - Kanye West.mp3",
    "Lab_7\\musics\\Darkhan Juzz-Erikpe.mp3",
    "Lab_7\\musics\\Стыцамен - Иван Дорн.mp3"
]
photos = [
    "Lab_7\\images\\image1.jpg",
    "Lab_7\\images\\image2.jpg",
    "Lab_7\\images\\image3.jpg"
]
buttons = [
    "Lab_7\\images\\previous.png",
    "Lab_7\\images\\next.png",
    "Lab_7\\images\\play.png",
    "Lab_7\\images\\stop.png"
]

# Class to manage the music player
class MusicPlayer:
    def __init__(self):
        self.current_index = 0
        self.is_playing = True

        # Load button images
        self.previous_button = pygame.image.load(buttons[0])
        self.next_button = pygame.image.load(buttons[1])
        self.play_button = pygame.image.load(buttons[2])
        self.stop_button = pygame.image.load(buttons[3])

    def display_photo(self, index):
        screen.fill((255, 255, 255))  # Белый фон
        photo = pygame.image.load(photos[index])
        photo = pygame.transform.scale(photo, (384, 288))  # Масштабируем фото
        x_offset = (400 - 384) // 2
        y_offset = (400 - 384) // 2
        screen.blit(photo, (x_offset, y_offset))
        self.display_buttons()  # Отображаем кнопки
        pygame.display.flip()

    def display_buttons(self):
        screen.blit(self.previous_button, (50, 325))  # Кнопка Previous
        if self.is_playing:
            screen.blit(self.stop_button, (176, 325))  # Кнопка Stop
        elif not self.is_playing:
            screen.blit(self.play_button, (176, 325))  # Кнопка Play
        screen.blit(self.next_button, (302, 325))  # Кнопка Next

    def play_song(self):
        pygame.mixer.music.load(playlist[self.current_index])
        pygame.mixer.music.play()
        self.display_photo(self.current_index)

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_song(self):
        self.stop_music()
        self.current_index = (self.current_index + 1) % len(playlist)
        self.play_song()

    def previous_song(self):
        self.stop_music()
        self.current_index = (self.current_index - 1) % len(playlist)
        self.play_song()

# Initialize the music player
player = MusicPlayer()

# Start playing the first song
player.play_song()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            # Определяем, какая кнопка была нажата
            if 50 <= x <= 50 + 48 and 325 <= y <= 325 + 48:  # Кнопка Previous
                player.previous_song()
            elif 302 <= x <= 302 + 48 and 325 <= y <= 325 + 48:  # Кнопка Next
                player.next_song()
            elif 176 <= x <= 176 + 48 and 325 <= y <= 325 + 48:  # Кнопка Play/Stop
                if player.is_playing:
                    player.stop_music()
                    player.is_playing = False
                else:
                    player.play_song()
                    player.is_playing = True
                player.display_buttons()  # Обновляем кнопки сразу после изменения состояния
        elif event.type == KEYDOWN:  # Управление клавишами
            if event.key == K_p:  # Клавиша Play
                player.play_song()
            elif event.key == K_s:  # Клавиша Stop
                player.stop_music()
            elif event.key == K_n:  # Клавиша Next
                player.next_song()
            elif event.key == K_b:  # Клавиша Previous
                player.previous_song()

    # Обновляем кнопки для отображения корректного состояния
    player.display_buttons()
    pygame.display.flip()
