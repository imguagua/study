#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: diagram.py
# Author: imguagua
# mail: harry.fan@foxmail.com
# Created Time: 2016-07-20


class DiagramFactory:

    @classmethod
    def make_diagram(Class, width, height):
        return Class.Diagram(width, height)

    @classmethod
    def make_rectangle(Class, x, y, width, height,fill="white",
            stroke="black"):
        return Class.Rectangle(x, y, width, height, fill, stroke)

    @classmethod
    def make_text(Class, x, y, text, fontsize=12):
        return Class.Text(x, y, text, fontsize)

    BLANK = " "
    CORNER = "+"
    HORIZONTAL = "-"
    VERTICAL = "|"

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
            file = (None if isinstance(filenameOrFile, str) else
                    filenameOrFile)

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
            self.rows = DiagramFactory._create_rectangle(width, height,
                    DiagramFactory.BLANK if fill == "white" else "%")

    class Text:

        def __init__(self, x, y, text, fontsize):
            self.x = x
            self.y = y
            self.rows = [list(text)]

    @classmethod
    def _create_rectangle(Class, width, height, fill):
        rows = [[fill for _ in range(width)] for _ in range(height)]
        for x in range(1, width - 1):
            rows[0][x] = DiagramFactory.HORIZONTAL
            rows[height - 1][x] = DiagramFactory.HORIZONTAL
        for y in range(1, height - 1):
            rows[y][0] = DiagramFactory.VERTICAL
            rows[y][width - 1] = DiagramFactory.VERTICAL
        for y, x in ((0, 0), (0, width - 1), (height - 1, 0),
                (height -1, width -1)):
            rows[y][x] = DiagramFactory.CORNER
        return rows
            
class SvgDiagramFactory(DiagramFactory):

    # The make_* class methods are inherited

    SVG_START = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
    "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"
    width="{pxwidth}px" height="{pxheight}px">"""

    SVG_END = "</svg>\n"

    SVG_RECTANGLE = """<rect x="{x}" y="{y}" width="{width}" \
height="{height}" fill="{fill}" stroke="{stroke}"/>"""

    SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
font-family="sans-serif" stroke="red" font-size="{fontsize}">{text}</text>"""

    SVG_SCALE = 20

    class Diagram:

        def __init__(self, width, height):
            pxwidth = width * SvgDiagramFactory.SVG_SCALE
            pxheight = height * SvgDiagramFactory.SVG_SCALE
            self.diagram = [SvgDiagramFactory.SVG_START.format(**locals())]
            outline = SvgDiagramFactory.Rectangle(0, 0, width, height,
                    "lightgreen", "black")
            self.diagram.append(outline.svg)

        def add(self, component):
            self.diagram.append(component.svg)

        def save(self, filenameOrFile):
            file = (None if isinstance(filenameOrFile, str) else
                    filenameOrFile)
            try:
                if file is None:
                    file = open(filenameOrFile, "w+")
                
                print >> file, "\n".join(self.diagram) 
                print >> file, "\n" + SvgDiagramFactory.SVG_END

            finally:
                if isinstance(filenameOrFile, str) and file is not None:
                    file.close()
    class Rectangle:
        def __init__(self, x, y, width, height, fill, stroke):
            x *= SvgDiagramFactory.SVG_SCALE
            y *= SvgDiagramFactory.SVG_SCALE
            width *= SvgDiagramFactory.SVG_SCALE
            height *= SvgDiagramFactory.SVG_SCALE
            self.svg = SvgDiagramFactory.SVG_RECTANGLE.format(**locals())


    class Text:
        
        def __init__(self, x, y, text, fontsize):
            x *= SvgDiagramFactory.SVG_SCALE
            y *= SvgDiagramFactory.SVG_SCALE
            fontsize *= SvgDiagramFactory.SVG_SCALE // 10
            self.svg = SvgDiagramFactory.SVG_TEXT.format(**locals())