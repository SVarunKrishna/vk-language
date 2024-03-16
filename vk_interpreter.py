# Define your VK_Lexer and VK_Parser classes here

class VKInterpreter:
    def __init__(self, parser):
        self.parser = parser
        self.variables = {}
        self.functions = {}

    def interpret(self):
        parsed_code = self.parser.parse()
        for statement in parsed_code:
            if statement[0] == 'int mukiyam':
                self.functions[statement[1]] = (statement[2], statement[3])
            elif statement[0] == 'haa':
                self.handle_if_statement(statement)
            elif statement[0] == 'haan':
                self.handle_for_loop(statement)
            elif statement[0] == 'Mm':
                self.handle_while_loop(statement)
            elif statement[0] == 'ye':
                self.handle_do_while_loop(statement)
            elif statement[0] == 'sollu':
                self.handle_scan_statement(statement)
            elif statement[0] == 'Paaru':
                self.handle_print_statement(statement)

    def handle_if_statement(self, statement):
        condition = self.evaluate_expression(statement[1])
        if condition:
            self.execute_block(statement[2])
        elif len(statement) > 3:  # If there's an else block
            self.execute_block(statement[3])

    def handle_for_loop(self, statement):
        init_statement = statement[1]
        condition = self.evaluate_expression(statement[2])
        update_statement = statement[3]
        loop_block = statement[4]

        self.execute_statement(init_statement)
        while condition:
            self.execute_block(loop_block)
            self.execute_statement(update_statement)
            condition = self.evaluate_expression(statement[2])

    def handle_while_loop(self, statement):
        condition = self.evaluate_expression(statement[1])
        loop_block = statement[2]
        
        while condition:
            self.execute_block(loop_block)
            condition = self.evaluate_expression(statement[1])

    def handle_do_while_loop(self, statement):
        loop_block = statement[1]
        condition = self.evaluate_expression(statement[2])

        self.execute_block(loop_block)
        while condition:
            self.execute_block(loop_block)
            condition = self.evaluate_expression(statement[2])

    def handle_scan_statement(self, statement):
        variable_name = statement[1]
        value = input("Enter a value for {}: ".format(variable_name))
        self.variables[variable_name] = int(value) if value.isdigit() else value

    def handle_print_statement(self, statement):
        for item in statement[1]:
            if isinstance(item, tuple):
                print(self.evaluate_expression(item), end=" ")
            else:
                print(item, end=" ")
        print()

    def execute_block(self, block):
        for statement in block:
            if isinstance(statement, tuple):
                if statement[0] == 'int mukiyam':
                    self.handle_function_definition(statement)
                elif statement[0] == 'haa':
                    self.handle_if_statement(statement)
                elif statement[0] == 'haan':
                    self.handle_for_loop(statement)
                elif statement[0] == 'Mm':
                    self.handle_while_loop(statement)
                elif statement[0] == 'ye':
                    self.handle_do_while_loop(statement)
                elif statement[0] == 'sollu':
                    self.handle_scan_statement(statement)
                elif statement[0] == 'Paaru':
                    self.handle_print_statement(statement)
            else:
                self.execute_statement(statement)

    def execute_statement(self, statement):
        if statement[0] in self.functions:
            func_params, func_body = self.functions[statement[0]]
            for i, param in enumerate(func_params):
                self.variables[param[1]] = self.evaluate_expression(statement[i + 1])
            self.execute_block(func_body)

    def evaluate_expression(self, expression):
        if isinstance(expression, tuple):
            operator = expression[0]
            if operator == 'ADD':
                return self.evaluate_expression(expression[1]) + self.evaluate_expression(expression[2])
            elif operator == 'SUBTRACT':
                return self.evaluate_expression(expression[1]) - self.evaluate_expression(expression[2])
            elif operator == 'MULTIPLY':
                return self.evaluate_expression(expression[1]) * self.evaluate_expression(expression[2])
            elif operator == 'DIVIDE':
                return self.evaluate_expression(expression[1]) / self.evaluate_expression(expression[2])
        elif isinstance(expression, int) or expression.isdigit():
            return int(expression)
        elif expression in self.variables:
            return self.variables[expression]
        else:
            return expression


# Usage example:
from vk_lexer import VK_Lexer
from vk_parser import VK_Parser

text = """
athu int mukiyam add(int moolyam a, int moolyam b) idam
    mudhala a seru b
mudhala

athu
    moolyam num1 vaathiyar_padithaal() idam
    moolyam num2 vaathiyar_padithaal() idam
    moolyam sum add(num1, num2) idam
    Paaru "Sum is: ", sum idam
mudhala
"""

lexer = VK_Lexer(text)
parser = VK_Parser(lexer.tokenize())
interpreter = VKInterpreter(parser)
interpreter.interpret()
                
