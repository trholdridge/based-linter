# -*- coding: utf-8 -*-

import ast

def parse(lineList):
    fullCode = "\n".join(lineList)
    fullAst = ast.parse(fullCode)
    tv = TypeVisitor(None)
    tv.visit(fullAst)

class TypeVisitor(ast.NodeVisitor):
    def __init__(self, matchLambda, transformLambda=lambda x: x):
        self.matchingNodes = set()
        self.matchLambda = matchLambda
        self.transformLambda = transformLambda
    
    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)

#    def getMatchingNodes(self, parentNode):
#        for node in ast.walk(parentNode):
#           if self.matchLambda(node):
#                self.matchingNodes.add(self.transformLambda(node))

class PrintTypeVisitor(TypeVisitor):
    def __init__(self):
        self.matchLambda = lambda node: True
        self.transformLambda = lambda node: print(type(node))
                
#class PlaintextVisitor(TypeVisitor):
#    def __init__(self):
#        matchString = lambda node: (type(node) is ast.Constant && type(node.value) is str)
#        super(matchString)