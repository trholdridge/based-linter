# -*- coding: utf-8 -*-

import ast

def parse(lineList):
    fullCode = "".join(lineList)
    fullAst = ast.parse(fullCode)
    print(ast.dump(fullAst))
    contentTypes = ["plaintext", "variable", "import"]
    visitors = [PlaintextVisitor(), VariableVisitor(), ImportVisitor()]
    parsed = {}
    for i, visitor in enumerate(visitors):
        visitor.visit(fullAst)
        parsed[contentTypes[i]] = visitor.matchingNodes
        
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
    
    
class ImportVisitor(TypeVisitor):
    def __init__(self):
        super().__init__()
    
    def match(self, node):
        return type(node) is ast.ImportFrom or type(node) is ast.Import
    
    def transform(self, node):
        if type(node) is ast.ImportFrom:
            return node.module
        elif type(node) is ast.Import:
            return node.names[0].name