from typing import List


class Stats:
    def __init__(self, array: List[int]) -> None:
        """
        Initializes the stats.
        """
        self._data: List[int] = array

    def less(self, number: int) -> int:
        """
        Stats method that performs less than logic
        """
        return len([*filter(lambda x: x < number, self._data)])

    def greater(self, number: int) -> int:
        """
        Stats method that performs greater than logic
        """
        return len([*filter(lambda x: x > number, self._data)])

    def between(self, smaller_num: int, greater_num: int) -> int:
        """
        Stats method that performs between logic                
        """
        return len([*filter(lambda x:greater_num >= x >= smaller_num, self._data)])


class DataCapture():
    def __init__(self) -> None:
        """
        Init data capture.
        """
        self.data: List[int] = []

    def add(self, number: int) -> None:
        """
        Adds the given number to the array.
        """
        self.data.append(number)

    def build_stats(self) -> Stats:
        """
        Builds the stats from DataCapture data
        """
        stats: Stats = Stats(self.data)

        return stats
