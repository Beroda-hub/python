class Television:
    """
    Class-Variables:
        MIN_VOLUME (integer): Minimum volume level, set to 0.
        MAX_VOLUME (integer): Maximum volume level, set to 2.
        MIN_CHANNEL (integer): Minimum channel number, set to 0.
        MAX_CHANNEL (integer): Maximum channel number, set to 3.

    Instance-Variables:
        status (boolean): Indicates whether the TV is on (True) or off (False).
        muted (boolean): Indicates whether the TV is muted (True) or not (False).
        volume (integer): Current volume level of the TV.
        channel (integer): Current channel number of the TV.
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Default settings:
        - TV is off (status = False).
        - TV is not muted (muted = False).
        - Volume is set to the minimum level (volume = MIN_VOLUME).
        - Channel is set to the minimum channel (channel = MIN_CHANNEL).
        """
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        """
        Toggles the power status of the TV.
        - If the TV is off, it turns on.
        - If the TV is on, it turns off.
        """
        self.status = not self.status

    def mute(self):
        """
        Toggles the mute status of the TV
        - If the TV is muted, it becomes unmuted.
        - If the TV is unmuted, it becomes muted.
        """
        if self.status:
            self.muted = not self.muted

    def channel_up(self):
        """
        Increases the TV's channel by 1 wrapping around to MIN_CHANNEL
        if the current channel is MAX_CHANNEL.
        """
        if self.status:
            if self.channel < Television.MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Decreases the TV's channel by 1 wrapping around to MAX_CHANNEL
        if the current is MIN_CHANNEL.
        """
        if self.status:
            if self.channel > Television.MIN_CHANNEL:
                self.channel -= 1
            else:
                self.channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Increases the TV's volume by 1 to MAX_VOLUME. Automatically unmutes
        the TV if muted.
        """
        if self.status:
            if self.muted:
                self.muted = False
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        """
        Decreases the TV's volume by 1 to MIN_VOLUME. Automatically unmutes
        the TV if muted.
        """
        if self.status:
            if self.muted:
                self.muted = False
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        """
        Returns a string representation of the TV's current state
        "Power = [status], Channel = [channel], Volume = [volume]"
        If the TV is muted, the volume will always display as 0.
        """
        if self.muted and self.status:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = 0'
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
