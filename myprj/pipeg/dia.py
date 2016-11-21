#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: dia.py
# Author: imguagua
# mail: harry.fan@foxmail.com
# Created Time: 2016-07-26

class DiagramFactory():


    @classmethod
    def make_diagram(Class, width, height):
        return Class.Diagram(width, height)
        
    @classmethod
    def make_rectangle(Class, x, y, width, height, fill="white"):
        return Class.Rectangle(x, y, width, height, fill,
                stroke="black")

    @classmethod
    def make_text(Class, x, y, text, fontsize=12):
        return Class.Text(x, y, text, fontsize)

    BLANK = " "
    CORNER = "+"
    HORIZONTAL = "-"
    VERTICAL = "|"

    @classmethod
    def _create_rectangle(Class, width, height, fill):
        rows = [[fill for _ in range(width)] for _ in range(height)]
        for x in range(1, width - 1):
            rows[0][x] = DiagramFactory.HORIZONTAL
            rows[height -1][x] = DiagramFactory.HORIZONTAL
        for y in range(1, height - 1):
            rows[y][0] = DiagramFactory.VERTICAL
            rows[y][width -1] = DiagramFactory.VERTICAL
        for y,x in ((0, 0), (0, width - 1), (height - 1, 0),
                (height - 1, width - 1)):
            rows[y][x] = DiagramFactory.CORNER
        return rows


    class Diagram:

        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.diagram = DiagramFactory._create_rectangle(self.width,
                    self.height, DiagramFactory.BLANK)

        def add(self, component):
            for y, row in enumerate(component.rows):
                for x, char in enumerate(row):
                    self.diagram[y + component.y][x + component.x] = char

        def save(self, filenameOrFile):
            file = (None if isinstance(filenameOrFile, str)
                    else filenameOrFile)
            try:
                if file is None:
                    file = open(filenameOrFile, "w+")
                for row in self.diagram:
                    print >> file, "".join(row)
            finally:
                if isinstance(filenameOrFile, str) and file is not None:
                    file.close()

    class Rectangle:

        def __init__(self, x, y, width, height, fill, stroke):
            self.x = x
            self.y = y
            print fill
            self.rows = DiagramFactory._create_rectangle(width, height, 
                    DiagramFactory.BLANK if fill == "white" else "%")

    class Text:
        def __init__(self, x, y, text, fontsize):
            self.x = x
            self.y = y
            self.rows = [list("{:*^16}".format(text))]


import sys
def main():
    create_diagram(DiagramFactory).save(sys.stdout)

def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, fill="yellow")
    text = factory.make_text(7, 3, "good boy")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram

if __name__ == "__main__":
    main()
    

