class Combine:
    number_of_combines = 0
    volume = 0
    __fuel_consumption = 0
    __engine_power = 0
    __size_of_harvester = 0
    __speed_of_one_hectare = 0
    __comfort_for_driver = False

    def __init__(self, volume=0, fuel_consumption=0, engine_power=0, size_of_harvester=0, speed_of_one_hectare=0,
                 comfort_for_driver=False):
        self.volume = volume
        self.__fuel_consumption = fuel_consumption
        self.__engine_power = engine_power
        self.__size_of_harvester = size_of_harvester
        self.__speed_of_one_hectare = speed_of_one_hectare
        self.__comfort_for_driver = comfort_for_driver
        Combine.number_of_combines += 1

    def __del__(self):
        del self

    def __str__(self):
        return f"volume: {self.volume}\n \
               fuel consumption: {self.__fuel_consumption}\n \
               engine power: {self.__engine_power}\n \
               size of harvester: {self.__size_of_harvester}\n \
               speed of one hectare: {self.__speed_of_one_hectare}\n \
               comfort for driver: {self.__comfort_for_driver}"

    @staticmethod
    def get_number():
        return Combine.number_of_combines


def main():
    combine_1 = Combine(300, 10, 500, 2, 3, False)
    combine_2 = Combine(400, 12, 550, 3, 4, True)
    combine_3 = Combine(500, 14, 600, 4, 5, True)
    print("Combine 1:\n", combine_1)
    print("Combine 2:\n", combine_2)
    print("Combine 3:\n", combine_3)
    print("Number of combines: ", Combine.get_number())


if __name__ == '__main__':
    main()