import sys


class Player:
    def __init__(
        self,
        user,
        money=0,
        squirrel=0,
        dwarf=0,
        plant=0,
        robot=0,
        printer=0,
        goose=0,
        midas=1,
    ):
        self.user = user.strip()
        if user == "debug":
            self.money = 500000000000
        else:
            self.money = money
        self.squirrel = squirrel
        self.dwarf = dwarf
        self.plant = plant
        self.robot = robot
        self.printer = printer
        self.goose = goose
        self.midas = midas

    def __str__(self):
        return str(self.dictionary())

    def dictionary(self):
        return {
            "user": self.user,
            "money": self.money,
            "squirrel": self.squirrel,
            "dwarf": self.dwarf,
            "plant": self.plant,
            "robot": self.robot,
            "printer": self.printer,
            "goose": self.goose,
            "midas": self.midas,
        }

    @classmethod
    def make(self, dict):
        user = dict["user"]
        try:
            money = int(dict["money"])
            squirrel = int(dict["squirrel"])
            dwarf = int(dict["dwarf"])
            plant = int(dict["plant"])
            robot = int(dict["robot"])
            printer = int(dict["printer"])
            goose = int(dict["goose"])
            midas = int(dict["midas"])
        except:
            raise ValueError("File formatted incorrectly")

        return Player(user, money, squirrel, dwarf, plant, robot, printer, goose, midas)

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, username):
        self._user = username

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money = money

    @property
    def squirrel(self):
        return self._squirrel

    @squirrel.setter
    def squirrel(self, squirrel):
        self._squirrel = squirrel

    @property
    def dwarf(self):
        return self._dwarf

    @dwarf.setter
    def dwarf(self, dwarf):
        self._dwarf = dwarf

    @property
    def robot(self):
        return self._robot

    @robot.setter
    def robot(self, robot):
        self._robot = robot

    @property
    def printer(self):
        return self._printer

    @printer.setter
    def printer(self, printer):
        self._printer = printer

    @property
    def plant(self):
        return self._plant

    @plant.setter
    def plant(self, plant):
        self._plant = plant

    @property
    def goose(self):
        return self._goose

    @goose.setter
    def goose(self, goose):
        self._goose = goose

    @property
    def midas(self):
        return self._midas

    @midas.setter
    def midas(self, midas):
        self._midas = midas
