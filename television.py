class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Initialize an object of the Television Class
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self):
        """
        Function to turn the "tv" on and off
        :return: Changing status True or False
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        """
        Function to "Mute" the tv
        :return: Changing the mute status to True or False
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
            else:
                self.__muted = False

    def channel_down(self):
        """
        Function to lower the "Channel" by 1
        :return: Changing the current channel variable by -1
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def channel_up(self):
        """
        Function to raise the "Channel" by 1
        :return: Changing the current channel variable by +1
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def volume_down(self):
        """
        Function to decrease the volume variable by 1
        :return: Changing the volume by -1
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def volume_up(self):
        """
        Function to increase the volume variable by 1
        :return: Changing the volume by +1
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def __str__(self) -> str:
        """
        If print(class) is called this string with be printed
        :return: A string of what the current values of Power Channel and Volume are
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

