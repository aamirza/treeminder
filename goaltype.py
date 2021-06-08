from enum import Enum, EnumMeta


class EnumContainer(EnumMeta):
    def __contains__(self, item):
        return item.lower() in [member.lower() for member in self.__members__]


class GoalType(Enum, metaclass=EnumContainer):
    BADGES = 1
    POINTS = 2
