class Settings:
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (217,177,102)
        self.bullet_allowed = 30
        self.alien_speed = 10.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3
        self.speed_up = 1.1
        self.score_scale = 1.5
        self.alien_points = 50
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speed_up
        self.bullet_speed *= self.speed_up
        self.alien_speed *= self.speed_up

        self.alien_points = int(self.alien_points * self.score_scale)
        



