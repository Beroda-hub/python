class Television:
    """
    Class-Variables:
        MIN_VOLUME (integer): Minimum volume level, set to 0.
        MAX_VOLUME (integer): Maximum volume level, set to 2.
        MIN_CHANNEL (integer): Minimum channel number, set to 0.
        MAX_CHANNEL (integer): Maximum channel number, set to 3.

    Instance-Variables (private):
        __status (boolean): Indicates whether the TV is on (True) or off (False).
        __muted (boolean): Indicates whether the TV is muted (True) or not (False).
        __volume (integer): Current volume level of the TV.
        __channel (integer): Current channel number of the TV.
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Default settings:
        - TV is off (__status = False).
        - TV is not muted (__muted = False).
        - Volume is set to the minimum level (__volume = MIN_VOLUME).
        - Channel is set to the minimum channel (__channel = MIN_CHANNEL).
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Toggles the power status of the TV.
        - If the TV is off, it turns on.
        - If the TV is on, it turns off.
        """
        self.__status = not self.__status

    def mute(self):
        """
        Toggles the mute status of the TV
        - If the TV is muted, it becomes unmuted.
        - If the TV is unmuted, it becomes muted.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Increases the TV's channel by 1 wrapping around to MIN_CHANNEL
        if the current channel is MAX_CHANNEL.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Decreases the TV's channel by 1 wrapping around to MAX_CHANNEL
        if the current is MIN_CHANNEL.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Increases the TV's volume by 1 to MAX_VOLUME. Automatically unmutes
        the TV if muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Decreases the TV's volume by 1 to MIN_VOLUME. Automatically unmutes
        the TV if muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Returns a string representation of the TV's current state
        "Power = [status], Channel = [channel], Volume = [volume]"
        If the TV is muted, the volume will always display as 0.
        """
        if self.__muted and self.__status:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

    def get_status(self):
        return self.__status

    def get_muted(self):
        return self.__muted

    def get_volume(self):
        return self.__volume

    def get_channel(self):
        return self.__channel

    def set_status(self, status):
        self.__status = status

    def set_muted(self, muted):
        self.__muted = muted

    def set_volume(self, volume):
        if volume >= Television.MIN_VOLUME and volume <= Television.MAX_VOLUME:
            self.__volume = volume

    def set_channel(self, channel):
        if channel >= Television.MIN_CHANNEL and channel <= Television.MAX_CHANNEL:
            self.__channel = channel
