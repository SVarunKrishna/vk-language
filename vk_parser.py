class VK_Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = 0

    def parse(self):
        self.current_token = self.tokens[self.index]
        self.index += 1
        return self.statement_list()

    def statement_list(self):
        results = []
        while self.current_token is not None:
            results.append(self.statement())
        return results

    def statement(self):
        token = self.current_token
        if token == 'int_mukiyam':
            return self.variable_declaration()
        elif token == 'haa':
            return self.if_statement()
        elif token == 'aku':
            return self.for_loop()
        elif token == 'ohhh':
            return self.while_loop()
        elif token == 'kick':
            return self.do_while_loop()
        elif token == 'Paaru':
            return self.print_statement()
        elif token == 'sollu':
            return self.scan_statement()
        elif token.isalpha():
            return self.assignment_statement()
        else:
            raise SyntaxError("Invalid statement")

    def variable_declaration(self):
        self.eat('int_mukiyam')
        variable = self.current_token
        self.eat(variable)
        self.eat('=')
        value = self.expr()
        self.eat(';')
        return ('variable', variable, value)

    def if_statement(self):
        # Implement if statement parsing
        pass

    def for_loop(self):
        # Implement for loop parsing
        pass

    def while_loop(self):
        # Implement while loop parsing
        pass

    def do_while_loop(self):
        # Implement do-while loop parsing
        pass

    def print_statement(self):
        # Implement print statement parsing
        pass

    def scan_statement(self):
        # Implement scan statement parsing
        pass

    def assignment_statement(self):
        variable = self.current_token
        self.eat(variable)
        self.eat('=')
        value = self.expr()
        self.eat(';')
        return ('assignment', variable, value)

    def expr(self):
        # Implement expression parsing
        pass

    def eat(self, token_type):
        if self.current_token == token_type:
            if self.index < len(self.tokens):
                self.current_token = self.tokens[self.index]
                self.index += 1
            else:
                self.current_token = None
        else:
            raise SyntaxError(f"Expected {token_type}, found {self.current_token}")
              
