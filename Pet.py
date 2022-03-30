import threading as th

mk_hungryth = None
mk_funth = None


def stop_threads():
    mk_hungryth.cancel()
    mk_funth.cancel()


class Pet:
    _name = ""
    type = ""
    __health = 0
    __hunger = 0
    __fun = 0
    time = 0

    __lost_fun = 0
    __gain_hunger = 0

    def __init__(self, name, health, hunger, fun, time):
        self._name = name
        self.__health = health
        self.__hunger = hunger
        self.__fun = fun
        self.time = time

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        elif value > 100:
            self.__health = 100
        else:
            self.__health = value

    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, value):
        if value < 0:
            self.__hunger = 0
        elif value > 100:
            self.__hunger = 100
        else:
            self.__hunger = value

    @property
    def fun(self):
        return self.__fun

    @fun.setter
    def fun(self, value):
        if value < 0:
            self.__fun = 0
        elif value > 100:
            self.__fun = 100
        else:
            self.__fun = value

    @property
    def lost_fun(self):
        return self.__lost_fun

    @lost_fun.setter
    def lost_fun(self, value):
        if value < 0:
            self.__lost_fun = 0
        elif value > 100:
            self.__lost_fun = 100
        else:
            self.__lost_fun = value

    @property
    def gain_hunger(self):
        return self.__gain_hunger

    @gain_hunger.setter
    def gain_hunger(self, value):
        if value < 0:
            self.__gain_hunger = 0
        elif value > 100:
            self.__gain_hunger = 100
        else:
            self.__gain_hunger = value

    def vet(self):
        self.health += (self.health * 1 / 2)
        self.fun -= (self.fun * 1 / 3)

    def feed(self):
        self.hunger -= 5

    def play(self):
        self.fun += 5


class Horse(Pet):
    def __init__(self, name, health, hunger, fun, time):
        super().__init__(name, health, hunger, fun, time)
        self.type = "Horse"

    def mk_hungry(self):
        mk_hungryth = th.Timer(1, self.mk_hungry)
        self.hunger += 1
        self.health -= (self.health - 1 / 8 * self.hunger)
        mk_hungryth.start()

    def mk_fun(self):
        mk_funth = th.Timer(1, self.mk_fun)
        self.fun -= 1
        self.health -= (1 / 8 * (100 - self.fun))
        mk_funth.start()


class Eagle(Pet):
    def __init__(self, name, health, hunger, fun, time):
        super().__init__(name, health, hunger, fun, time)
        self.type = "Eagle"

    def mk_hungry(self):
        mk_hungryth = th.Timer(1, self.mk_hungry)
        self.hunger += 3
        self.health -= (self.health - 1 / 6 * self.hunger)
        mk_hungryth.start()

    def mk_fun(self):
        mk_funth = th.Timer(1, self.mk_fun)
        self.fun -= 3
        self.health -= (1 / 6 * (100 - self.fun))
        mk_funth.start()


class Panther(Pet):
    def __init__(self, name, health, hunger, fun, time):
        super().__init__(name, health, hunger, fun, time)
        self.type = "Panther"

    def mk_hungry(self):
        mk_hungryth = th.Timer(1, self.mk_hungry)
        self.hunger += 5
        self.health -= (self.health - 1 / 4 * self.hunger)
        mk_hungryth.start()

    def mk_fun(self):
        mk_funth = th.Timer(1, self.mk_fun)
        self.fun -= 5
        self.health -= (1 / 4 * (100 - self.fun))
        mk_funth.start()
