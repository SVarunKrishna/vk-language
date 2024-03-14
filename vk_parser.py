class VK_Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        parsed_code = []

        while self.current_token_index < len(self.tokens):
            statement = self.parse_statement()
            parsed_code.append(statement)

        return parsed_code

    def parse_statement(self):
        current_token = self.tokens[self.current_token_index]

        if current_token[1] == 'IF':
            return self.parse_if_statement()
        elif current_token[1] == 'FOR':
            return self.parse_for_loop()
        elif current_token[1] == 'WHILE':
            return self.parse_while_loop()
        elif current_token[1] == 'DO':
            return self.parse_do_while_loop()
        elif current_token[1] == 'PRINTF':
            return self.parse_print_statement()
        elif current_token[1] == 'SCANF':
            return self.parse_scan_statement()
        elif current_token[1] == 'INT_MAIN':
            return self.parse_main_function()
        elif current_token[1] == 'IDENTIFIER':
            return self.parse_assignment_statement()
        else:
            raise SyntaxError("Invalid statement")

    def parse_if_statement(self):
        if_statement = ['IF']
        self.current_token_index += 1  # Skip 'siru' keyword
        condition = self.parse_expression()
        if_statement.append(condition)

        # Parse the true block
        true_block = []
        self.current_token_index += 1  # Skip 'niyal' keyword
        while self.tokens[self.current_token_index][0] != 'koodal':
            true_block.append(self.parse_statement())
        if_statement.append(true_block)

        # Check for 'koodal' keyword (start of else block)
        current_token = self.tokens[self.current_token_index]
        if current_token[0] == 'koodal':
            self.current_token_index += 1  # Skip 'koodal' keyword
            else_block = []
            while self.tokens[self.current_token_index][0] != 'mudhala':
                else_block.append(self.parse_statement())
            if_statement.append(else_block)

        return if_statement

    def parse_for_loop(self):
        for_loop = ['FOR']
        self.current_token_index += 1  # Skip 'niyal' keyword
        variable = self.tokens[self.current_token_index][0]
        for_loop.append(variable)
        
        # Skip variable, start, 'seru', end, 'seru', step, 'mudhala'
        self.current_token_index += 7
        block = []
        while self.tokens[self.current_token_index][0] != 'mudhala':
            block.append(self.parse_statement())
        for_loop.append(block)

        return for_loop

    def parse_while_loop(self):
        while_loop = ['WHILE']
        self.current_token_index += 1  # Skip 'niyal' keyword
        condition = self.parse_expression()
        while_loop.append(condition)
        
        # Skip 'mudhala'
        self.current_token_index += 1
        block = []
        while self.tokens[self.current_token_index][0] != 'mudhala':
            block.append(self.parse_statement())
        while_loop.append(block)

        return while_loop

    def parse_do_while_loop(self):
        do_while_loop = ['DO']
        self.current_token_index += 1  # Skip 'niyal' keyword
        
        # Skip 'mudhala'
        self.current_token_index += 1
        block = []
        while self.tokens[self.current_token_index][0] != 'mudhala':
            block.append(self.parse_statement())
        do_while_loop.append(block)
        
        # Skip 'ye', 'mm', condition
        self.current_token_index += 3
        condition = self.parse_expression()
        do_while_loop.append(condition)

        return do_while_loop

    def parse_print_statement(self):
        print_statement = ['PRINTF']
        self.current_token_index += 1  # Skip 'Paaru' keyword
        
        values = []
        while self.tokens[self.current_token_index][0] != 'mudhala':
            values.append(self.parse_expression())
        print_statement.append(values)

        return print_statement

    def parse_scan_statement(self):
        scan_statement = ['SCANF']
        self.current_token_index += 1  # Skip 'sollu' keyword
        
        variable = self.tokens[self.current_token_index][0]
        scan_statement.append(variable)
        
        return scan_statement

    def parse_main_function(self):
        main_function = ['INT_MAIN']
        self.current_token_index += 1  # Skip 'int mukiyam' keyword
        
        # Skip '{'
        self.current_token_index += 1
        block = []
        while self.tokens[self.current_token_index][0] != 'mudhala':
            block.append(self.parse_statement())
        main_function.append(block)

        return main_function

    def parse_assignment_statement(self):
        assignment_statement = ['ASSIGNMENT']
        variable = self.tokens[self.current_token_index][0]
        assignment_statement.append(variable)
        
        # Skip variable, '=', value, 'mudhala'
        self.current_token_index += 4
        value = self.parse_expression()
        assignment_statement.append(value)

        return assignment_statement

    def parse_expression(self):
        token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        return token[0]
        
