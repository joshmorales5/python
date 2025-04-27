class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        """
        Constructor to initialize the television object
        """
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn on/off the television
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to mute/unmute the television
        """
        if self.__status:
            self.__muted = not self.__muted



    def channel_up(self) -> None:
        """
        Method to increase the channel of the television
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the channel of the television
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the volume of the television
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1


    def volume_down(self) -> None:
        """
        Method to decrease the volume of the television
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tc status, channel, and volume
        :return: tv status, channel, and volume
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
