#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: test_DiagramFactory.py
# Author: imguagua
# mail: harry.fan@foxmail.com
# Created Time: 2016-07-20

from app.diagram import DiagramFactory
import unittest

class DiagramFactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.diagramfactory = DiagramFactory()

    def tearDown(self):
        self.diagramfactory = None

    def test_make_diagram(self):
        diagram = self.diagramfactory.make_diagram(30, 7)
        self.assertTrue(isinstance(diagram, DiagramFactory.Diagram))
        self.assertEqual(len(diagram.diagram), 7)
        for y, row in enumerate(diagram.diagram):
            self.assertEqual(len(diagram.diagram[y]), 30)

    def test_make_rectangle(self):
        rectangle = self.diagramfactory.make_rectangle(4, 1, 22, 5, "yellow")
        self.assertTrue(isinstance(rectangle, DiagramFactory.Rectangle))
        self.assertEqual(len(rectangle.rows), 5)
        for y, row in enumerate(rectangle.rows):
            self.assertEqual(len(rectangle.rows[y]), 22)

    def test_make_text(self):
        
        text = self.diagramfactory.make_text(7, 3, "Abstract Factory")
        self.assertTrue(isinstance(text, DiagramFactory.Text))
        self.assertEqual(len(text.rows), 1)
        self.assertEqual(len(text.rows[0]), 16)

