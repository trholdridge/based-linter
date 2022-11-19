# -*- coding: utf-8 -*-

import ast

def parse(lineList):
    fullCode = "\n".join(lineList)
    fullAst = ast.parse(fullCode)
    p = PlaintextVisitor()
    v = VariableVisitor()
    p.visit(fullAst)
    v.visit(fullAst)
    parsed = {}
    parsed["plaintext"] = p.matchingNodes
    parsed["variable"] = v.matchingNodes
    return parsed
    

class TypeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.matchingNodes = set()
    
    def generic_visit(self, node):
        if self.match(node):
            self.matchingNodes.add((self.transform(node), node.lineno))
        ast.NodeVisitor.generic_visit(self, node)
        
    def match(self, node):
        return True
    
    def transform(self, node):
        return type(node).__name__

                
class PlaintextVisitor(TypeVisitor):
    def __init__(self):
        super().__init__()
    
    def match(self, node):
        return type(node) is ast.Constant and type(node.value) is str
    
    def transform(self, node):
        return node.value
    

class VariableVisitor(TypeVisitor):
    def __init__(self):
        super().__init__()

    def match(self, node):
        return type(node) is ast.Name
    
    def transform(self, node):
        return node.id
    