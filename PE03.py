class Rectangle(object):
    def __init__(self, length=int(), width=int()):
        self.length = self.validate('length', length)
        self.width = self.validate('width', width)
        self.area = self.area(self.length, self.width)
        self.perimeter = self.perimeter(self.length, self.width)

    def validate(self, dimension, number):
        '''
        Validates if user input or predefined input is a integer and corrects as needed.
        :param dimension: length or width
        :param number: predefined number, if needed.  Input overrides if no predefined number exist.
        :return:
        '''
        while True:
            if not number:
                try:
                    number = int(input("What is the {} of the Rectangle? ".format(dimension)))
                except ValueError:
                    print("Input was not a valid number. Please enter a valid number.")
                    number = int()
            elif isinstance(number, int):
                return number


    def area(self, length, width):
        '''
        Calculates the area of a rectangle.
        :param length:int object length
        :param width:int object width
        :return: area:int
        '''
        area = length * width
        return area


    def perimeter(self, length, width):
        '''
        Calculates the perimeter of a rectangle.
        :param length:int object length
        :param width:int object width
        :return: perimeter:int
        '''
        perimeter = length * 2 + width * 2
        return perimeter


    def print(self):
        '''
        Prints object results.
        :return:
        '''
        print("Length & Width: {} X {}".format(self.length, self.width))
        print("Area: {}".format(self.area))
        print("Perimeter: {}".format(self.perimeter))


def print_rectangles(rectangles):
    '''
    For loop to print all objects from Rectangle().
    :param rectangles
    :return:
    '''
    counter = 0
    for rectangle in rectangles:
        counter = counter + 1
        print("*" * 30)
        print("Rectangle", counter)
        rectangle.print()
    print("*" * 30)


def main():
    rectangle1 = Rectangle()
    rectangles = [rectangle1]
    print_rectangles(rectangles)

if __name__ == "__main__":
    main()