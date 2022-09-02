# -*- coding: utf-8 -*-
"""Menu screen

Build menu screen and auth between server and client.
"""
from src.utils.settings import WIDTH, HEIGHT
from src.game_objects.input import Input
from src.game_objects.button import Button
from src.game_objects.text_label import TextLabel
from src.utils.network import Network


class Menu:
    """Menu class

    Attribiutes:
        network: Network, Connection tools with server.
        email: Input, Interactive input object.
        password: Input, Interactive input object.
        button: Button, Clickable object.
        login_label: TextLabel, Login message label draws on screen.
        error_label: TextLabel, Response errors draws on screen.
    """

    def __init__(self):
        """Constructor

        Attribiutes:
            network: Network, Connection tools with server.
            email: Input, Interactive input object.
            password: Input, Interactive input object.
            button: Button, Clickable object.
            login_label: TextLabel, Login message label draws on screen.
            error_label: TextLabel, Response errors draws on screen.
            """
        self.network = Network()
        self.connection_successful = False

        coordiantes = [WIDTH / 4, HEIGHT / 2]

        # Interactive elements
        self.password = Input(coordiantes, True)
        coordiantes[1] -= 75
        self.email = Input(coordiantes)
        self.button = Button(
            "Log In", 150, 32, (WIDTH/2, coordiantes[1] + 150))
        coordiantes[1] -= 50

        # Labels
        self.error_label = TextLabel("", 6, (50, coordiantes[1]))
        coordiantes[1] -= 50
        self.login_label = TextLabel(
            "Witamy Samuraju", 36, (45, coordiantes[1]))

    def catch_events(self, event):
        """Catching events

        Check all actor interaction with objects.

        Arguments:
            event, Event, Pygame event.`
        """
        self.email.catch_events(event)
        self.password.catch_events(event)
        if self.button.is_button_pressed(event):
            self.connection_successful = self.network.is_connected_to_server(
                self.email.user_text,
                self.password.user_text
            )
            self.button.change_button_color()
            self.error_label.change_text(str(self.network.errors))

    def update(self):
        """Update

        Updating positions and draw objects.
        """
        self.email.update()
        self.password.update()
        self.button.update()
        self.login_label.update()
        self.error_label.update()
