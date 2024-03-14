class VK_Interpreter:
    def __init__(self):
        self.symbol_table = {}

    def interpret(self, parsed_code):
        output = []
        for statement in parsed_code:
            result = self.execute_statement(statement)
            if result is not None:
                output.append(result)
        return output

    def execute_statement(self, statement):
        keyword = statement[0]
        if keyword == 'haa':
            # Handle 'if' statement
            condition = statement[1]
            true_block = statement[2]
            false_block = statement[3] if len(statement) > 3 else None
            if self.eval_expr(condition):
                self.interpret(true_block)
            elif false_block:
                self.interpret(false_block)
        elif keyword == 'haan':
            # Handle 'for' loop
            variable, start, end, step, block = statement[1:]
            self.symbol_table[variable] = start
            while self.symbol_table[variable] <= end:
                self.interpret(block)
                self.symbol_table[variable] += step
        elif keyword == 'Mm':
            # Handle 'while' loop
            condition, block = statement[1:]
            while self.eval_expr(condition):
                self.interpret(block)
        elif keyword == 'ye mm':
            # Handle 'do-while' loop
            condition, block = statement[1:]
            self.interpret(block)
            while self.eval_expr(condition):
                self.interpret(block)
        elif keyword == 'Paaru':
            # Handle 'print' statement
            values = statement[1:]
            output = ' '.join(str(self.eval_expr(expr)) for expr in values)
            print(output)
        elif keyword == 'sollu':
            # Handle 'scan' statement
            variable = statement[1]
            value = input("Enter value for {}: ".format(variable))
            self.symbol_table[variable] = int(value)  # Assuming input is always an integer
        elif keyword == 'int mukiyam':
            # Function definition, do nothing for now
            pass
        elif keyword == 'seru' or keyword == 'kora' or keyword == 'Ona' or keyword == 'piri':
            # Handle arithmetic operations
            operator = keyword
            operand2 = self.eval_expr(statement[2])
            operand1 = self.eval_expr(statement[1])
            if operator == 'seru':
                return operand1 + operand2
            elif operator == 'kora':
                return operand1 - operand2
            elif operator == 'Ona':
                return operand1 * operand2
            elif operator == 'piri':
                if operand2 == 0:
                    raise ValueError("Division by zero")
                return operand1 / operand2
        else:
            raise RuntimeError("Invalid statement")

    def eval_expr(self, expr):
        if isinstance(expr, int):
            return expr
        elif expr in self.symbol_table:
            return self.symbol_table[expr]
        else:
            return expr
                
