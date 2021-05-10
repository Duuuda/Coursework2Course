from typing import List, Union, Iterable, Tuple
from copy import deepcopy
from math import floor, ceil
from Utils import cached_property


class HanoiLogic:
    def __init__(self, initial_number: str):
        if not initial_number.isdecimal():
            raise ValueError("The 'initial_number' parameter must be a decimal string")
        if len(initial_number) < 3:
            raise ValueError("The 'initial_number' parameter too short")

        self.__initial_number = initial_number
        self.__scheme = self.__generate_scheme(self.__initial_number)

    @staticmethod
    def __generate_scheme(initial_number: str) -> List[List[int]]:
        new_scheme = [[] for _ in initial_number]
        for (shaft_index, shaft_num), disks_count in zip(enumerate(range(len(initial_number), 0, -1)),
                                                         map(int, initial_number)):
            for disk_num in range(disks_count, 0, -1):
                new_scheme[shaft_index].append(shaft_num * 10 + disk_num)
        return new_scheme

    @cached_property
    def __iterations_count(self) -> int:
        _step_map = list(map(int, list(self.__initial_number)))
        iterations_count = int()

        for a, b, c in zip(range(0, len(_step_map) - 2, 2),
                           range(1, len(_step_map) - 1, 2),
                           range(2, len(_step_map), 2)):
            iterations_count += 2 ** _step_map[c] - 1
            _step_map[c], _step_map[b] = 0, _step_map[c] + _step_map[b]

            iterations_count += 2 ** _step_map[b] - 1
            _step_map[b], _step_map[a] = 0, _step_map[b] + _step_map[a]

            iterations_count += 2 ** _step_map[a] - 1
            _step_map[a], _step_map[c] = 0, _step_map[a] + _step_map[c]

        if not len(_step_map) % 2:
            iterations_count += 2 ** _step_map[-1] - 1
            _step_map[-1], _step_map[-2] = 0, _step_map[-1] + _step_map[-2]

            iterations_count += 2 ** _step_map[-2] - 1
            _step_map[-2], _step_map[-1] = 0, _step_map[-2] + _step_map[-1]

        return iterations_count

    @property
    def __iterations_numbers(self) -> List[Union[int, Tuple[int, int, float]]]:
        iterations_numbers = list()
        for percent in range(101):
            iteration_number = self.__iterations_count / 100 * percent
            if iteration_number.is_integer():
                iterations_numbers.append(int(iteration_number))
            else:
                iterations_numbers.append((floor(iteration_number), ceil(iteration_number), iteration_number))
        return iterations_numbers

    @staticmethod
    def __move(shaft_scheme_1: List[int], shaft_scheme_2: List[int]) -> int:
        if not len(shaft_scheme_1) and not len(shaft_scheme_2):
            return 0
        elif not len(shaft_scheme_1):
            shaft_scheme_1.append(shaft_scheme_2.pop())
            return 1
        elif not len(shaft_scheme_2):
            shaft_scheme_2.append(shaft_scheme_1.pop())
            return 1
        elif shaft_scheme_1[-1] > shaft_scheme_2[-1]:
            shaft_scheme_1.append(shaft_scheme_2.pop())
            return 1
        else:
            shaft_scheme_2.append(shaft_scheme_1.pop())
            return 1

    @staticmethod
    def __get_iterations_args(_from: List[int],
                              _to: List[int],
                              _buffer: List[int]) -> Iterable[Tuple[List[int], List[int]]]:
        __sum_of_disks = len(_from) + len(_to)
        __is_odd = bool(len(_from) % 2)
        while len(_to) != __sum_of_disks:
            if __is_odd:
                yield _from, _to
                if len(_to) == __sum_of_disks:
                    break
                yield _from, _buffer
            else:
                yield _from, _buffer
                if len(_to) == __sum_of_disks:
                    break
                yield _from, _to
            if len(_to) == __sum_of_disks:
                break
            yield _buffer, _to

    @staticmethod
    def __combine_iterations(iteration_1: List[List[int]],
                             iteration_2: List[List[int]]) -> Tuple[List[List[int]], int, int, int]:
        _disk_diameter = int()
        _from_index = int()
        _to_index = int()
        for (shaft_1_index, shaft_1), (shaft_2_index, shaft_2) in zip(enumerate(iteration_1), enumerate(iteration_2)):
            if len(shaft_1) > len(shaft_2):
                _disk_diameter = shaft_1.pop()
                _from_index = shaft_1_index
            elif len(shaft_1) < len(shaft_2):
                _disk_diameter = shaft_2.pop()
                _to_index = shaft_2_index
        return iteration_1, _disk_diameter, _from_index, _to_index

    @property
    def get_iterations(self) -> Iterable[Tuple[Union[int, float],
                                               List[List[int]],
                                               Union[int, None],
                                               Union[int, None],
                                               Union[int, None]]]:
        __scheme = deepcopy(self.__scheme)
        __iterations_numbers = self.__iterations_numbers
        prev_iteration = None
        current_iteration = int()

        if __iterations_numbers[0] == current_iteration:
            yield __iterations_numbers.pop(0), deepcopy(__scheme), None, None, None

        for _a, _b, _c in zip(__scheme[:-2:2], __scheme[1:-1:2], __scheme[2::2]):
            for _shaft_1, _shaft_2 in self.__get_iterations_args(_c, _b, _a):
                if len(__iterations_numbers):
                    current_iteration += self.__move(_shaft_1, _shaft_2)
                    if isinstance(__iterations_numbers[0], tuple):
                        if current_iteration == __iterations_numbers[0][0]:
                            prev_iteration = deepcopy(__scheme)
                        elif current_iteration == __iterations_numbers[0][1]:
                            yield __iterations_numbers.pop(0)[2],\
                                  *self.__combine_iterations(prev_iteration, deepcopy(__scheme))
                    else:
                        if current_iteration == __iterations_numbers[0]:
                            yield __iterations_numbers.pop(0), deepcopy(__scheme), None, None, None
                else:
                    break

            for _shaft_1, _shaft_2 in self.__get_iterations_args(_b, _a, _c):
                if len(__iterations_numbers):
                    current_iteration += self.__move(_shaft_1, _shaft_2)
                    if isinstance(__iterations_numbers[0], tuple):
                        if current_iteration == __iterations_numbers[0][0]:
                            prev_iteration = deepcopy(__scheme)
                        elif current_iteration == __iterations_numbers[0][1]:
                            yield __iterations_numbers.pop(0)[2],\
                                  *self.__combine_iterations(prev_iteration, deepcopy(__scheme))
                    else:
                        if current_iteration == __iterations_numbers[0]:
                            yield __iterations_numbers.pop(0), deepcopy(__scheme), None, None, None
                else:
                    break

            for _shaft_1, _shaft_2 in self.__get_iterations_args(_a, _c, _b):
                if len(__iterations_numbers):
                    current_iteration += self.__move(_shaft_1, _shaft_2)
                    if isinstance(__iterations_numbers[0], tuple):
                        if current_iteration == __iterations_numbers[0][0]:
                            prev_iteration = deepcopy(__scheme)
                        elif current_iteration == __iterations_numbers[0][1]:
                            yield __iterations_numbers.pop(0)[2],\
                                  *self.__combine_iterations(prev_iteration, deepcopy(__scheme))
                    else:
                        if current_iteration == __iterations_numbers[0]:
                            yield __iterations_numbers.pop(0), deepcopy(__scheme), None, None, None
                else:
                    break

        if not len(__scheme) % 2:
            for _shaft_1, _shaft_2 in self.__get_iterations_args(__scheme[-1], __scheme[-2], __scheme[-3]):
                if len(__iterations_numbers):
                    current_iteration += self.__move(_shaft_1, _shaft_2)
                    if isinstance(__iterations_numbers[0], tuple):
                        if current_iteration == __iterations_numbers[0][0]:
                            prev_iteration = deepcopy(__scheme)
                        elif current_iteration == __iterations_numbers[0][1]:
                            yield __iterations_numbers.pop(0)[2],\
                                  *self.__combine_iterations(prev_iteration, deepcopy(__scheme))
                    else:
                        if current_iteration == __iterations_numbers[0]:
                            yield __iterations_numbers.pop(0), deepcopy(__scheme), None, None, None
                else:
                    break

            for _shaft_1, _shaft_2 in self.__get_iterations_args(__scheme[-2], __scheme[-1], __scheme[-3]):
                if len(__iterations_numbers):
                    current_iteration += self.__move(_shaft_1, _shaft_2)
                    if isinstance(__iterations_numbers[0], tuple):
                        if current_iteration == __iterations_numbers[0][0]:
                            prev_iteration = deepcopy(__scheme)
                        elif current_iteration == __iterations_numbers[0][1]:
                            yield __iterations_numbers.pop(0)[2],\
                                  *self.__combine_iterations(prev_iteration, deepcopy(__scheme))
                    else:
                        if current_iteration == __iterations_numbers[0]:
                            yield __iterations_numbers.pop(0), deepcopy(__scheme), None, None, None
                else:
                    break
