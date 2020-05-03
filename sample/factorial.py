# Sample Repository
# Copyright (C) 2020  Jan Rodolf Espinas
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>
'''Compute the factorial of a number'''
import os
import math

import numpy as np

from sample.module import bisection_method

__author__ = "Jan Rodolf Espinas"
__version__ = "1.0.0"

np.random.seed(7)

class Sample:
    def __init__(self):
        pass 

    def speak(self,name):
        print(name)


def factorial(number):
    return 1 if number == 1 or number == 0 else number * factorial(number - 1)


def main():
    pass

if __name__ == "__main__":
    main()