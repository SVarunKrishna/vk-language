from typing import List
from rply import ParserGenerator
from ..ast.base import Expression, Print
from ..ast.blocks import (
    MainBlock,
    ProgramBlock,
    FunctionsBlock,
    StatementsBlock
)
from ..ast.control import (
    IfCondition,
    IfElseCondition,
    ForLoop,
    WhileLoop,
    Break,
    FuncCall,
    FuncCallAssign,
    FuncReturn,
    Function
)
from ..ast.ops import (
    Sum,
    Sub,
    Mul,
    Div,
    Mod,
    LogicalGT,
    LogicalGTE,
    LogicalLT,
    LogicalLTE,
    LogicalEQ,
    LogicalNEQ,
    UnarySum,
    UnarySub
)
from ..ast.base import (
    Number,
    Boolean,
    String,
    Word
)


class ParserBase:
    def __init__(self, tokens: List[str]) -> None:
        self.pg = ParserGenerator(
            tokens=tokens,
            precedence=[
                ("left", ["NOOP"]),
                ("left", ["LOGICOP"]),
                ("left", ["MATHOP"]),
                ("left", ["SUM", "SUB"]),
                ("left", ["MUL", "DIV", "MOD"]),
            ],
        )

        self.parsers = []

    def parse(self):
        pass

    def init_parsers(self):
        for parser in self.parsers:
            parser.parse(self.pg)

        @self.pg.error
        def error(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()


class AtomParser:
    def parse(self, pg):
        @pg.production("forvar : NUMBER")
        @pg.production("expression : NUMBER")
        def number_expr(p):
            return Number(p[0].value)

        @pg.production("expression : BOOL_TRUE")
        @pg.production("expression : BOOL_FALSE")
        def bool_expr(p):
            return Boolean(p[0])

        @pg.production("expression : STRING")
        def string_expr(p):
            return String(p[0].value)

        @pg.production("forvar : WORD")
        @pg.production("expression : WORD")
        @pg.production("variable : WORD")
        def word_expr(p):
            return Word(p[0])

        @pg.production("func_name : WORD")
        def func_word(p):
            return FuncWord(p[0])


class ExpressionParser:
    def parse(self, pg):
        @pg.production("expression : expression mathop expression", precedence="MATHOP")
        def binary_arith_expr(p):
            left = p[0]
            right = p[2]
            OpNode = p[1]
            return OpNode(left, right)

        @pg.production("expression : expression logicalop expression", precedence="LOGICOP")
        @pg.production("logical_expression : expression logicalop expression", precedence="LOGICOP")
        def binary_logical_op(p):
            left = p[0]
            right = p[2]
            OpNode = p[1]
            return OpNode(left, right)

        @pg.production("expression : SUB expression")
        @pg.production("expression : SUM expression")
        def unary_expr(p):
            if p[0].gettokentype() == "SUM":
                return UnarySum(p[1])
            if p[0].gettokentype() == "SUB":
                return UnarySub(p[1])


class ConditionalParser:
    def parse(self, pg):
        @pg.production("statement : IF_COND logical_expression L_BRACE statements R_BRACE END_BLOCK SEMI_COLON")
        def if_stmt(p):
            return IfCondition(p[1], p[3])

        @pg.production("statement : IF_COND logical_expression L_BRACE statements R_BRACE ELSE_COND L_BRACE statements R_BRACE END_BLOCK SEMI_COLON")
        def if_else_stmt(p):
            return IfElseCondition(p[1], p[3], p[7])


class LoopParser:
    def parse(self, pg):
        @pg.production("statement : BREAK_LOOP SEMI_COLON")
        def break_stmt(p):
            return Break()

        @pg.production("statement : FOR_START forvar FOR_RANGE_START forvar FOR_RANGE_END L_BRACE statements R_BRACE END_BLOCK SEMI_COLON")
        def for_loop(p):
            return ForLoop(p[1], p[3], p[6])

        @pg.production("statement : WHILE_LOOP expression L_BRACE statements R_BRACE END_BLOCK SEMI_COLON")
        def while_loop(p):
            return WhileLoop(p[1], p[3])


class FunctionParser:
    def parse(self, pg):
        @pg.production("functions : functions function")
        def functions(p):
            return FunctionsBlock(p[0], p[1])

        @pg.production("functions : ")
        def empty_function(p):
            return FunctionsBlock()

        @pg.production("function : FUNC_DECLARE func_name statements END_FUNC")
        def parse_function_no_args(p):
            return Function(p[1], p[2])

        @pg.production("statement : FUNC_RETURN expression SEMI_COLON")
        def return_stmt(p):
            return FuncReturn(p[1])

        @pg.production("statement : FUNC_CALL func_name SEMI_COLON")
        def func_call(p):
            return FuncCall(p[1])

        @pg.production("statement : variable FUNC_CALL func_name SEMI_COLON")
        def func_call_assign(p):
            return FuncCallAssign(p[0], p[2])


class BinaryMathOpsParser:
    def parse(self, pg):
        @pg.production("mathop : SUM")
        def binary_sum(p):
            return Sum

        @pg.production("mathop : SUB")
        def binary_sub(p):
            return Sub

        @pg.production("mathop : MUL")
        def binary_mul(p):
            return Mul

        @pg.production("mathop : DIV")
        def binary_div(p):
            return Div

        @pg.production("mathop : MOD")
        def binary_mod(p):
            return Mod


class BinaryLogicalOpsParser:
    def parse(self, pg):
        @pg.production("logicalop : GT")
        def binary_gt(p):
            return LogicalGT

        @pg.production("logicalop : GTE")
        def binary_gte(p):
            return LogicalGTE

        @pg.production("logicalop : LT")
        def binary_lt(p):
            return LogicalLT

        @pg.production("logicalop : LTE")
        def binary_lte(p):
            return LogicalLTE

        @pg.production("logicalop : EQ")
        def binary_eq(p):
            return LogicalEQ

        @pg.production("logicalop : NEQ")
        def binary_neq(p):
            return LogicalNEQ


class PrintParser:
    def parse(self, pg):
        @pg.production("printexprs : printexprs expression", precedence="NOOP")
        def print_exprs(p):
            return PrintBlock(p[0], p[1])

        @pg.production("printexprs : ")
        def printexprs_empty(p):
            return PrintBlock()


class StatementParser:
    def parse(self, pg):
        @pg.production("statements : statements statement")
        def statements(p):
            return StatementsBlock(p[0], p[1])

        @pg.production("statements : ")
        def statements_empty(p):
            return StatementsBlock()

        @pg.production("statement : PRINT printexprs SEMI_COLON")
        def statement_print(p):
            return Print(p[1])


class VariableParser:
    def parse(self, pg):
        @pg.production("statement : START_DECLARE variable DECLARE expression SEMI_COLON")
        @pg.production("statement : START_DECLARE variable DECLARE_ALT expression SEMI_COLON")
        def declare_var_expr(p):
            return VarDeclare(p[1], p[3])

        @pg.production("statement : variable ASSIGN expression SEMI_COLON")
        def assign_var_expr(p):
            return VarAssign(p[0], p[2])


class ProgramParser(ParserBase):
    def __init__(self, tokens: List[str]) -> None:
        super().__init__(tokens)
        self.parsers += [
            ConditionalParser(),
            LoopParser(),
            FunctionParser(),
        ]

    def parse(self):
        @self.pg.production("program : functions main")
        def program(p):
            return ProgramBlock(p[0], p[1])

        @self.pg.production("main : PGM_START statements PGM_END")
        def main(p):
            return MainBlock(p[1])

        self.init_parsers()


class LineParser(ParserBase):
    def __init__(self, tokens: List[str]) -> None:
        super().__init__(tokens)

    def parse(self):
        @self.pg.production("statement : PRINT printexprs SEMI_COLON")
        def print_stmt(p):
            return Print(p[1])

        @self.pg.production("statement : expression SEMI_COLON")
        def expr_stms(p):
            return Expression(p[0])

        self.init_parsers()
            
