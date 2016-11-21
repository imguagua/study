#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: manager.py
# Author: imguagua
# mail: harry.fan@foxmail.com
# Created Time: 2016-07-20
import os
import sys
import tempfile
from app.diagram import DiagramFactory
from app.diagram import SvgDiagramFactory


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-p":
        create_diagram(DiagramFactory).save(sys.stdout)
        create_diagram(SvgDiagramFactory).save(sys.stdout)
        #  return

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()

    textFilename = os.path.join(tempfile.gettempdir(), "diagram.txt")
    svgFilename = os.path.join(tempfile.gettempdir(), "diagram.svg")

    txtDiagram = create_diagram(DiagramFactory)
    txtDiagram.save(textFilename)
    print("wrote", textFilename)

    svgDiagram = create_diagram(SvgDiagramFactory)
    svgDiagram.save(svgFilename)
    print("wrote", svgFilename)

def test():
    import unittest
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test)


def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "have good time")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram

if __name__ == "__main__":
    main()
