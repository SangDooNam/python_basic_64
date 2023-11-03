class TV:
    def __init__(self):
        """The constructor. Called when you instantiate a TV."""
        self.channel = 1
        self.volume_level = 1
        self.turned_on = False

    def turn_on(self):
        """Turns the TV on."""
        self.turned_on = True
        return self.turned_on

    def turn_off(self):
        """Turns the TV off."""
        self.turned_on = False
        return self.turned_on

    def channel_up(self):
        """Scrolls the channel up."""
        if self.turned_on:
            self.channel += 1
            if self.channel >= 100:
                self.channel = 100
                return self.channel
        return self.channel
    

    def channel_down(self):
        """Scrolls the channel down."""
        if self.turned_on:
            self.channel -= 1
            if self.channel <= 1:
                self.channel = 1
                return self.channel
        return self.channel

    def set_channel(self, new_channel: int):
        """
        Sets the channel to the desired channel.

        :param int new_channel: The new channel
        """
        if self.turned_on:
            self.channel = new_channel
            if new_channel >= 100:
                new_channel = 100
                self.channel = new_channel
                return self.channel
            elif new_channel <= 1:
                new_channel = 1
                self.channel = new_channel
                return self.channel
        return self.channel
            
    def volume_up(self):
        """Increases the volume."""
        if self.turned_on:
            self.volume_level += 1
            if self.volume_level >= 10:
                self.volume_level = 10
                return self.volume_level
        return self.volume_level

    def volume_down(self):
        """Decreases the volume."""
        if self.turned_on:
            self.volume_level -= 1
            if self.volume_level <= 1:
                self.volume_level = 1
                return self.volume_level
        return self.volume_level

    def is_on(self):
        """Returns 'on' when the TV is on and otherwise 'off'."""
        if self.turned_on:
            return "on"
        return "off"
