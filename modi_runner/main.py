from random import choice, randint

from sys import exit

import pygame
import json


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk = plr_frames
        self.player_index = 0

        self.player_jump = self.player_walk[2]

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(160, 475))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.3)

    def apply_gravity(self):
        self.gravity += 1.1
        self.rect.y += self.gravity
        if self.rect.bottom >= 475:
            self.rect.bottom = 475
            self.gravity = 0

    def animation_state(self):
        if self.rect.bottom < 475:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

    def update(self):
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type
        if self.type == "fly":
            self.frames = fly_frames
            y_pos = 335
            self.base_y = y_pos
            self.speed = 7
        else:
            self.frames = snail_frames
            y_pos = 475
            self.base_y = y_pos
            self.speed = 5

        self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        self.rect = self.image.get_rect(bottomright=(randint(1050, 1250), y_pos))

    def animation_state(self):
        if self.type == "fly":
            self.animation_index += 0.24
        else:
            self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

    def destroy(self):
        if self.rect.right <= 0:
            self.kill()

    def update(self):
        self.rect.x -= self.speed
        if self.type == "fly":
            self.rect.bottom = self.base_y
        self.animation_state()
        self.destroy()


def collided_hitbox(sprite1, sprite2):
    return sprite1.rect.inflate(-60, -60).colliderect(sprite2.rect.inflate(-30, -30))


def collision_sprite():
    if pygame.sprite.spritecollide(
        player.sprite, obstacle_group, False, collided_hitbox
    ):
        collision_sound.play()
        obstacle_group.empty()
        return False
    return True


def display_score():
    global last_score, score_surf, score_rect
    current_time = pygame.time.get_ticks() // 1000 - start_time

    if current_time != last_score:
        last_score = current_time

        score_surf = txt_font.render(f"Score: {(last_score)}", False, "#1E293B")
        score_rect = score_surf.get_rect(center=(512, 50))
    screen.blit(score_surf, score_rect)
    return last_score


def high_score_update():
    global high_score
    with open("highscore.json", "r") as f:
        data = json.load(f)

    if data["high_score"] < last_score:
        high_score = last_score
        with open("highscore.json", "w") as f:
            data["high_score"] = last_score
            json.dump(data, f)
    high_score = data["high_score"]
    return high_score


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
collision_sound = pygame.mixer.Sound("audio/game_over.mp3")
collision_sound.set_volume(0.5)
screen = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("Modi Runner")

start_time = 0
clock = pygame.time.Clock()

pygame.mixer.music.load("audio/song.mp3")
pygame.mixer.music.play(loops=-1)

game_active = False

# Loading Frames
plr_frames = []
snail_frames = []
fly_frames = []
for i in range(1, 9):
    plr_img = pygame.image.load(
        f"assets/characters/player/player_walk_0{i}.png"
    ).convert_alpha()
    plr_img = pygame.transform.smoothscale(plr_img, (104, 147))
    plr_frames.append(plr_img)
for i in range(1, 5):
    snail_img = pygame.image.load(
        f"assets/characters/enemies/snail/snail_frame_{i}.png"
    ).convert_alpha()
    fly_img = pygame.image.load(
        f"assets/characters/enemies/fly/fly_frame_{i}.png"
    ).convert_alpha()
    snail_img = pygame.transform.smoothscale(snail_img, (75, 75))
    fly_img = pygame.transform.smoothscale(fly_img, (70, 70))
    snail_frames.append(snail_img)
    fly_frames.append(fly_img)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Text
txt_font = pygame.font.Font("font/PixeloidSans.ttf", 30)

last_score = 0
score_surf = txt_font.render("Score: 0", False, "#1E293B")
score_rect = score_surf.get_rect(center=(512, 50))
high_score = 0


# Environment
sky_surf = pygame.image.load("assets/environment/sky.png").convert()
sky_surf = pygame.transform.scale(sky_surf, (1024, 576))

ground_surf = pygame.image.load("assets/environment/road.png").convert_alpha()
ground_surf = pygame.transform.scale(ground_surf, (1024, 559))


# INTRO screen
intro_image = pygame.image.load("assets/intro/intro.png").convert_alpha()
intro_image = pygame.transform.scale(intro_image, (1024, 576))

player_stand = pygame.image.load("assets/intro/player.png")
player_stand = pygame.transform.scale_by(player_stand, factor=0.35)
player_stand_rect = player_stand.get_rect(center=(512, 280))

game_message = txt_font.render("* Press SPACE To Run *", False, "#C8FF9A")
game_message_rect = game_message.get_rect(center=(512, 465))

sky_x_pos = 0
ground_x_pos = 0


# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and player.sprite.rect.collidepoint(event.pos)
                and player.sprite.rect.bottom == 475
            ):
                player.sprite.gravity = -17

            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
                and player.sprite.rect.bottom >= 475
            ):
                player.sprite.gravity = -17
                player.sprite.jump_sound.play()

            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["fly", "snail", "snail", "snail"])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks() // 1000

    if game_active:
        # Parallax Sky
        sky_x_pos -= 0.75
        if sky_x_pos <= -1024:
            sky_x_pos = 0

        # Parallax Ground
        ground_x_pos -= 3
        if ground_x_pos <= -1024:
            ground_x_pos = 0

        # Update
        player.update()
        obstacle_group.update()

        # Collision
        game_active = collision_sprite()

        # Draw
        screen.blit(sky_surf, (sky_x_pos, -160))
        screen.blit(sky_surf, (sky_x_pos + 1024, -160))

        screen.blit(ground_surf, (ground_x_pos, 250))
        screen.blit(ground_surf, (ground_x_pos + 1024, 250))

        player.draw(screen)
        obstacle_group.draw(screen)

        score = display_score()

    # Game Over
    else:
        player.sprite.rect.midbottom = (160, 475)
        player.sprite.gravity = 0

        # Score
        score_message = txt_font.render(
            f"* Your Score : {last_score} *", False, "#FFE84A"
        )
        score_message_rect = score_message.get_rect(center=(512, 465))

        # High Score
        high_score = high_score_update()
        high_score_message = txt_font.render(
            f"* High Score : {high_score} *", False, "#FFC52E"
        )
        high_score_message_rect = high_score_message.get_rect(center=(512, 530))

        screen.blit(intro_image, (0, 0))
        screen.blit(player_stand, player_stand_rect)
        if high_score != 0:
            screen.blit(high_score_message, high_score_message_rect)
        if last_score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    pygame.display.update()
    clock.tick(60)
