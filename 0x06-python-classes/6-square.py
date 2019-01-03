#!/usr/bin/python3
class Square:
    __size = 0
    __position = (0,0)   
    
    def __init__(self, size=0, position=(0,0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
    
    def area(self):
        return self.__size * self.__size
    
    def my_print(self):
        if self.__position[1] > 0:
            for d in range(self.__position[1]):
                print()
        if self.__size is not 0:
            for r in range(self.__size):
                for rt in range(self.__position[0]):
                    print(end=" ")
                for c in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return __position

    @position.setter
    def position(self, value):
        if type(value) is not "tuple":
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
