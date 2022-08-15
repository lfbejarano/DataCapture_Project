from typing import List
from dataclasses import dataclass
from config import MAX_VALUE


class Stats:
    def __init__(self, final_data: dict, count: int) -> None:
        """
        Initializes the stats.
        """
        self._data: dict = final_data
        self._count: int = count

    def less(self, number: int) -> int:
        """
        Stats method that retrieves the amount of numbers lesser than the
        input value in the array
        """
        return self._data[number].less

    def greater(self, number: int) -> int:
        """
        Stats method that retrieves the amount of numbers greater than the
        input value in the array
        """
        return self._data[number].greater

    def between(self, smaller_num: int, greater_num: int) -> int:
        """
        Returns the number of numbers between the two given numbers, including
        both numbers counts.
        """
        if smaller_num < greater_num:
            pass
        else:
            greater_num, smaller_num = smaller_num, greater_num

        return self._count - self._data[smaller_num].less - \
            self._data[greater_num].greater


class DataCapture():
    def __init__(self) -> None:
        """
        Init data capture with a dictionary of data_objects where the
        key is the added number and the value is a dataclass object that
        contains the stats for that added number
        """
        self.data: dict = {}
        self.total_count: int = 0

    def add(self, number: int) -> None:
        """
        Adds the given number to the array.
        """
        if number not in self.data.keys():
            self.data[number] = data_object(0, 0, 0)
        self.data[number].count += 1
        self.total_count += 1

    def build_stats(self) -> Stats:
        """
        Builds the stats from DataCapture data. A dictionary is completed with
        all the possible input values from 1 to MAX_VALUE where the key is the
        number and the value is a data_object class with count , less and greater
        attributes
        """
        less: int = 0
        greater: int = self.total_count
        initial_collection = self.data.keys()

        for number in range(1, MAX_VALUE+1):
            if number not in initial_collection:
                self.data[number] = data_object(0, 0, 0)
            self.data[number].less = less
            self.data[number].greater = greater - \
                self.data[number].count
            less += self.data[number].count
            greater -= self.data[number].count

        stats: Stats = Stats(self.data, self.total_count)
        return stats


@dataclass
class data_object:
    """
    This class is defined for the main dictionary in order to call its
    attributes based on user number
    """
    count: int
    less: int
    greater: int
