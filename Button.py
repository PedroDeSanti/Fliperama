import pygame

class Button:
    def __init__(self, topic, x, y, image, screen, key):
        self.screen = screen
        self.button_surface = pygame.image.load(image).convert_alpha()
        self.previous_state = False
        self.current_state = False
        self.topic = topic
        self.position = (x, y)
        self.key = key

    def update(self):
        self.screen.blit(self.button_surface, self.position)

    def has_changed(self):
        self.previous_state = self.current_state

    def get_topic(self):
        return self.topic
        



    # private:
    #     int GPIO_pin;
    #     bool previous_state;
    #     bool current_state;

    #     // std::string topic;
    #     char* topic;