from vk-language.base import Node

# base.py
class Node:
    def eval(self):
        pass

class Number(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return float(self.value)

class Boolean(Node):
    def __init__(self, value):
        self.value = value.lower() == "true"

    def eval(self):
        return bool(self.value)

class String(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class Word(Node):
    def __init__(self, value):
        self.value = value

    @property
    def name(self):
        return self.value

    def eval(self):
        return self.value

class Print(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())

class Statement(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value.eval()

class VarDeclare(Node):
    def __init__(self, var, value):
        self.var = var
        self.value = value

    def eval(self):
        var_name = self.var.eval()
        value = self.value.eval()
        return var_name, value

class VarAssign(Node):
    def __init__(self, var, value):
        self.var = var
        self.value = value

    def eval(self):
        var_name = self.var.eval()
        value = self.value.eval()
        return var_name, value

class Expression(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value.eval()


# control.py
from .base import Node

class IfCondition(Node):
    def __init__(self, condition, value):
        self.condition = condition
        self.value = value

    def eval(self):
        if self.condition.eval():
            return self.value.eval()
        return

class ForLoop(Node):
    def __init__(self, range_start, range_end, stmts):
        self.range_start = range_start
        self.range_end = range_end
        self.stmts = stmts

    def eval(self):
        st = int(self.range_start.eval())
        end = int(self.range_end.eval())
        for _ in range(st, end):
            self.stmts.eval()

# ops.py
from .base import Node

class UnaryOpBase(Node):
    def __init__(self, value):
        self.value = value

class UnarySum(UnaryOpBase):
    def eval(self):
        return float(self.value.eval())

class UnarySub(UnaryOpBase):
    def eval(self):
        return float(-self.value.eval())

class BinaryOpBase(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Sum(BinaryOpBase):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOpBase):
    def eval(self):
        return self.left.eval() - self.right.eval()

# blocks.py
from .base import Node

class StatementsBlock(Node):
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        return [stmt.eval() for stmt in self.statements]

class MainBlock(Node):
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        return self.statements.eval()

