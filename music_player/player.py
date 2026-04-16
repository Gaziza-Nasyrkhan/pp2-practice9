import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

# экран
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()
done = False

BASE_DIR = os.path.dirname(__file__)

volume = 0.5
pygame.mixer.music.set_volume(volume)

# ---------------- TRACKS ----------------
tracks = [
    {
        "music": os.path.join(BASE_DIR, "music", "song1.mp3"),
    },
    {
        "music": os.path.join(BASE_DIR, "music", "song2.mp3"),
    }
]

current_track = 0

# ---------------- LOAD FUNCTION ----------------
def load_track(index):
    pygame.mixer.music.load(tracks[index]["music"])
    pygame.mixer.music.play()

    # image жоқ болса — қара экран
    img = pygame.Surface((400, 300))
    img.fill((200, 200, 200))

    return img

current_image = load_track(current_track)

# auto next event
MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

# ---------------- MAIN LOOP ----------------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                pygame.mixer.music.unpause()

            if event.key == pygame.K_s:
                pygame.mixer.music.pause()

            if event.key == pygame.K_n:
                current_track = (current_track + 1) % len(tracks)
                current_image = load_track(current_track)

            if event.key == pygame.K_b:
                current_track = (current_track - 1) % len(tracks)
                current_image = load_track(current_track)

            if event.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1)
                pygame.mixer.music.set_volume(volume)

            if event.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)

            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        if event.type == MUSIC_END:
            current_track = (current_track + 1) % len(tracks)
            current_image = load_track(current_track)

    # draw
    screen.fill((255, 255, 255))

    rect = current_image.get_rect(center=(400, 300))
    screen.blit(current_image, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()