        class VK_Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        parsed_code = []
        while self.current_token_index < len(self.tokens):
            token_type, token_value = self.tokens[self.current_token_index]

            if token_type == 'KEYWORD':
                if token_value == 'INT_MAIN':
                    parsed_code.append(self.parse_int_main())
                elif token_value == 'SCANF':
                    parsed_code.append(self.parse_scanf())
                elif token_value == 'PRINTF':
                    parsed_code.append(self.parse_printf())
                elif token_value == 'IF':
                    parsed_code.append(self.parse_if_statement())
                elif token_value == 'FOR':
                    parsed_code.append(self.parse_for_loop())
                elif token_value == 'WHILE':
                    parsed_code.append(self.parse_while_loop())
                elif token_value == 'DO_WHILE':
                    parsed_code.append(self.parse_do_while_loop())
            self.current_token_index += 1
        return parsed_code

    def parse_int_main(self):
        # Parse the main function block
        self.consume('PUNCTUATION', '{')
        main_block = self.parse_block()
        self.consume('PUNCTUATION', '}')
        return ('INT_MAIN', main_block)

    def parse_scanf(self):
        # Parse the variable to scan into
        variable = self.consume('IDENTIFIER')
        return ('SCANF', variable)

    def parse_printf(self):
        # Parse the print format string and values
        format_string = self.consume('STRING')
        values = []
        while self.peek()[0] != 'PUNCTUATION' or self.peek()[1] != ';':
            values.append(self.consume('IDENTIFIER'))
        return ('PRINTF', format_string, values)

    def parse_if_statement(self):
        # Parse the if statement
        self.consume('PUNCTUATION', '(')
        condition = self.parse_condition()
        self.consume('PUNCTUATION', ')')
        true_block = self.parse_block()
        false_block = None
        if self.peek() == ('KEYWORD', 'ELSE'):
            self.consume('KEYWORD', 'ELSE')
            false_block = self.parse_block()
        return ('IF', condition, true_block, false_block)

    def parse_for_loop(self):
        # Parse the for loop
        self.consume('PUNCTUATION', '(')
        initialization = self.parse_assignment()
        self.consume('PUNCTUATION', ';')
        condition = self.parse_condition()
        self.consume('PUNCTUATION', ';')
        update = self.parse_assignment()
        self.consume('PUNCTUATION', ')')
        loop_block = self.parse_block()
        return ('FOR', initialization, condition, update, loop_block)

    def parse_while_loop(self):
        # Parse the while loop
        self.consume('PUNCTUATION', '(')
        condition = self.parse_condition()
        self.consume('PUNCTUATION', ')')
        loop_block = self.parse_block()
        return ('WHILE', condition, loop_block)

    def parse_do_while_loop(self):
        # Parse the do-while loop
        loop_block = self.parse_block()
        self.consume('KEYWORD', 'WHILE')
        self.consume('PUNCTUATION', '(')
        condition = self.parse_condition()
        self.consume('PUNCTUATION', ')')
        self.consume('PUNCTUATION', ';')
        return ('DO_WHILE', condition, loop_block)

    def parse_condition(self):
        # Parse the condition for if, while, and do-while statements
        return self.parse_expression()

    def parse_block(self):
        # Parse a block of statements
        block = []
        while self.peek() != ('PUNCTUATION', '}'):
            block.append(self.parse_statement())
        return block

    def parse_statement(self):
        # Parse a single statement
        token_type, token_value = self.peek()
        if token_type == 'KEYWORD':
            if token_value == 'IF':
                return self.parse_if_statement()
            elif token_value == 'FOR':
                return self.parse_for_loop()
            elif token_value == 'WHILE':
                return self.parse_while_loop()
            elif token_value == 'DO_WHILE':
                return self.parse_do_while_loop()
        elif token_type == 'IDENTIFIER':
            return self.parse_assignment()
        # Add support for other statement types here

    def parse_assignment(self):
        # Parse an assignment statement
        variable = self.consume('IDENTIFIER')
        self.consume('OPERATOR', '=')
        value = self.parse_expression()
        self.consume('PUNCTUATION', ';')
        return ('ASSIGNMENT', variable, value)

    def parse_expression(self):
        # Parse an expression
        # Placeholder implementation
        return ('EXPRESSION', 'Placeholder')

    def peek(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None

    def consume(self, expected_type, expected_value=None):
        token_type, token_value = self.tokens[self.current_token_index]
        if token_type == expected_type and (expected_value is None or token_value == expected_value):
            self.current_token_index += 1
            return token_value
        else:
            raise SyntaxError(f"Expected {expected_type}, got {token_type} with value '{token_value}'")
        
