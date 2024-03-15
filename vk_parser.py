class VK_Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        parsed_code = []
        while self.current_token_index < len(self.tokens):
            token_type, token_value = self.tokens[self.current_token_index]

            if token_type == 'KEYWORD':
                if token_value == 'int_mukiyam':
                    parsed_code.append(self.parse_int_main())
                elif token_value == 'sollu':
                    parsed_code.append(self.parse_scan())
                elif token_value == 'Paaru':
                    parsed_code.append(self.parse_print())
                elif token_value == 'haa':
                    parsed_code.append(self.parse_if_statement())
                elif token_value == 'haan':
                    parsed_code.append(self.parse_for_loop())
                elif token_value == 'Mm':
                    parsed_code.append(self.parse_while_loop())
                elif token_value == 'ye_mm':
                    parsed_code.append(self.parse_do_while_loop())
                elif token_value == 'annippadu':
                    parsed_code.append(self.parse_return())
            elif token_type == 'IDENTIFIER':
                # This could be a variable assignment or function call
                if self.peek()[0] == 'OPERATOR' and self.peek()[1] == '=':
                    parsed_code.append(self.parse_assignment())
                else:
                    parsed_code.append(self.parse_function_call())
            self.current_token_index += 1
        return parsed_code

    def parse_int_main(self):
        # Parse the main function block
        self.consume('PUNCTUATION', '{')
        main_block = self.parse_block()
        self.consume('PUNCTUATION', '}')
        return ('int_mukiyam', main_block)

    def parse_scan(self):
        # Parse the variable to scan into
        variable = self.consume('IDENTIFIER')
        self.consume('PUNCTUATION', ';')
        return ('sollu', variable)

    def parse_print(self):
        # Parse the print format string and values
        format_string = self.consume('STRING')
        values = []
        while self.peek()[0] != 'PUNCTUATION' or self.peek()[1] != ';':
            values.append(self.parse_expression())
        self.consume('PUNCTUATION', ';')
        return ('Paaru', format_string, values)

    def parse_return(self):
        # Parse the return statement
        value = self.parse_expression()
        self.consume('PUNCTUATION', ';')
        return ('annippadu', value)

    def parse_if_statement(self):
        # Parse the if statement
        condition = self.parse_expression()
        true_block = self.parse_block()
        false_block = self.parse_block() if self.peek()[1] == 'haa uhh' else None
        return ('haa', condition, true_block, false_block)

    def parse_for_loop(self):
        # Parse the for loop
        variable = self.consume('IDENTIFIER')
        self.consume('KEYWORD', 'seru')
        start = self.parse_expression()
        self.consume('KEYWORD', 'till')
        end = self.parse_expression()
        step = self.parse_expression() if self.peek()[1] == 'seru' else 1
        block = self.parse_block()
        return ('haan', variable, start, end, step, block)

    def parse_while_loop(self):
        # Parse the while loop
        condition = self.parse_expression()
        block = self.parse_block()
        return ('Mm', condition, block)

    def parse_do_while_loop(self):
        # Parse the do-while loop
        block = self.parse_block()
        self.consume('KEYWORD', 'so_long')
        condition = self.parse_expression()
        self.consume('PUNCTUATION', ';')
        return ('ye_mm', block, condition)

    def parse_assignment(self):
        # Parse variable assignment
        variable = self.consume('IDENTIFIER')
        self.consume('OPERATOR', '=')
        value = self.parse_expression()
        self.consume('PUNCTUATION', ';')
        return ('assignment', variable, value)

    def parse_function_call(self):
        # Parse function call
        function_name = self.consume('IDENTIFIER')
        arguments = []
        while self.peek()[0] != 'PUNCTUATION' or self.peek()[1] != ';':
            arguments.append(self.parse_expression())
        self.consume('PUNCTUATION', ';')
        return ('function_call', function_name, arguments)

    def parse_block(self):
        # Parse a block of statements
        block = []
        while self.peek()[0] != 'PUNCTUATION' or self.peek()[1] != '}':
            block.append(self.parse_statement())
        return block

    def parse_statement(self):
        # Parse a single statement
        token_type, token_value = self.peek()
        if token_type == 'KEYWORD':
            if token_value in ['haa', 'haan', 'Mm', 'ye_mm']:
                return self.parse_control_statement()
            elif token_value == 'int_mukiyam':
                return self.parse_int_main()
            elif token_value == 'sollu':
                return self.parse_scan()
            elif token_value == 'Paaru':
                return self.parse_print()
            elif token_value == 'annippadu':
                return self.parse_return()
        elif token_type == 'IDENTIFIER':
            return self.parse_assignment()
        elif token_type == 'OPERATOR':
            # Handle arithmetic operations
            return self.parse_expression()
        # Other cases...
    
    # Add other parsing methods...

    def consume(self, expected_type, expected_value=None):
        # Consume the current token if it matches the expected type and value
        token_type, token_value = self.tokens[self.current_token_index]
        if token_type == expected_type and (expected_value is None or token_value == expected_value):
            self.current_token_index += 1
            return token_value
        else:
            raise SyntaxError(f"Expected {expected_type} but found {token_type} '{token_value}'")

    def peek(self):
        # Peek at the current token
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        else:
            return None
            
