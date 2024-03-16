import re

class VK_Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.token_index = -1
        self.advance()

    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None

    def parse(self):
        parsed_code = []
        while self.current_token:
            if self.current_token['type'] == 'KEYWORD':
                if self.current_token['value'] == 'int':
                    parsed_code.append(self.parse_variable_declaration())
                elif self.current_token['value'] == 'haa':
                    parsed_code.append(self.parse_if_statement())
                elif self.current_token['value'] == 'haan':
                    parsed_code.append(self.parse_for_loop())
                elif self.current_token['value'] == 'Mm':
                    parsed_code.append(self.parse_while_loop())
                elif self.current_token['value'] == 'ye':
                    parsed_code.append(self.parse_do_while_loop())
                elif self.current_token['value'] == 'sollu':
                    parsed_code.append(self.parse_scan_statement())
                elif self.current_token['value'] == 'Paaru':
                    parsed_code.append(self.parse_print_statement())
                elif self.current_token['value'] == 'int mukiyam':
                    parsed_code.append(self.parse_function_definition())
                elif self.current_token['value'] == 'chutti':
                    parsed_code.append(self.parse_switch_statement())
                elif self.current_token['value'] == 'pirandh':
                    parsed_code.append(self.parse_try_catch_blocks())
            self.advance()
        return parsed_code

    def parse_variable_declaration(self):
        var_type = self.current_token['value']
        self.advance()  # Consume variable type
        var_name = self.current_token['value']
        self.advance()  # Consume variable name
        self.advance()  # Consume '='
        var_value = self.parse_expression()
        return (var_type, var_name, var_value)

    def parse_if_statement(self):
        self.advance()  # Consume 'haa'
        condition = self.parse_expression()
        true_block = self.parse_block()
        false_block = None
        if self.current_token and self.current_token['value'] == 'koodal':
            self.advance()  # Consume 'koodal'
            false_block = self.parse_block()
        return ('haa', condition, true_block, false_block)

    def parse_for_loop(self):
        self.advance()  # Consume 'haan'
        init_statement = self.parse_variable_declaration()
        self.advance()  # Consume ';'
        condition = self.parse_expression()
        self.advance()  # Consume ';'
        update_statement = self.parse_variable_declaration()
        loop_block = self.parse_block()
        return ('haan', init_statement, condition, update_statement, loop_block)

    def parse_while_loop(self):
        self.advance()  # Consume 'Mm'
        condition = self.parse_expression()
        loop_block = self.parse_block()
        return ('Mm', condition, loop_block)

    def parse_do_while_loop(self):
        self.advance()  # Consume 'ye'
        loop_block = self.parse_block()
        self.advance()  # Consume 'kuraivu'
        condition = self.parse_expression()
        return ('ye', loop_block, condition)

    def parse_scan_statement(self):
        self.advance()  # Consume 'sollu'
        var_name = self.current_token['value']
        self.advance()  # Consume variable name
        return ('sollu', var_name)

    def parse_print_statement(self):
        self.advance()  # Consume 'Paaru'
        values = []
        while self.current_token and self.current_token['type'] != 'NEWLINE':
            if self.current_token['type'] == 'STRING':
                values.append(self.current_token['value'])
            else:
                values.append(self.parse_expression())
        return ('Paaru', values)

    def parse_function_definition(self):
        self.advance()  # Consume 'int mukiyam'
        function_name = self.current_token['value']
        self.advance()  # Consume function name
        self.advance()  # Consume '('
        parameters = []
        while self.current_token['type'] != 'RPAREN':
            param_type = self.current_token['value']
            self.advance()  # Consume parameter type
            param_name = self.current_token['value']
            self.advance()  # Consume parameter name
            parameters.append((param_type, param_name))
            if self.current_token['type'] == 'COMMA':
                self.advance()  # Consume ','
        self.advance()  # Consume ')'
        function_body = self.parse_block()
        return ('int mukiyam', function_name, parameters, function_body)

    def parse_switch_statement(self):
        self.advance()  # Consume 'chutti'
        expression = self.parse_expression()
        cases = []
        while self.current_token and self.current_token['value'] != 'mudhala':
            if self.current_token['value'] == 'nool':
                self.advance()  # Consume 'nool'
                value = self.parse_expression()
                self.advance()  # Consume ':'
                statements = self.parse_block()
                cases.append(('nool', value, statements))
            # Optionally handle 'vaanavil' (default) case here
        self.advance()  # Consume 'mudhala'
        return ('chutti', expression, cases)

    def parse_try_catch_blocks(self):
        try_block = self.parse_block()
        catch_blocks = []
        finally_block = None
        while self.current_token and self.current_token['value'] == 'pirindhu':
            self.advance()  # Consume 'pirindhu'
            exception_type = self.current_token['value']
            self.advance()  # Consume exception type
            exception_var = self.current_token['value']
            self.advance()  # Consume exception variable
            catch_block = self.parse_block()
            catch_blocks.append(('pirindhu', exception_type, exception_var, catch_block))
        if self.current_token and self.current_token['value'] == 'paeru':
            self.advance()  # Consume 'paeru'
            finally_block = self.parse_block()
        return ('try', try_block, catch_blocks, finally_block)

    def parse_expression(self):
        term = self.parse_term()
        while self.current_token and self.current_token['type'] in ('ADD', 'SUBTRACT'):
            if self.current_token['type'] == 'ADD':
                self.advance()
                term = ('ADD', term, self.parse_term())
            elif self.current_token['type'] == 'SUBTRACT':
                self.advance()
                term = ('SUBTRACT', term, self.parse_term())
        return term

    def parse_term(self):
        factor = self.parse_factor()
        while self.current_token and self.current_token['type'] in ('MULTIPLY', 'DIVIDE'):
            if self.current_token['type'] == 'MULTIPLY':
                self.advance()
                factor = ('MULTIPLY', factor, self.parse_factor())
            elif self.current_token['type'] == 'DIVIDE':
                self.advance()
                factor = ('DIVIDE', factor, self.parse_factor())
        return factor

    def parse_factor(self):
        token = self.current_token
        if token['type'] == 'LPAREN':
            self.advance()  # Consume '('
            expression = self.parse_expression()
            self.advance()  # Consume ')'
            return expression
        elif token['type'] == 'INTEGER':
            self.advance()
            return ('INTEGER', int(token['value']))
        elif token['type'] == 'FLOAT':
            self.advance()
            return ('FLOAT', float(token['value']))
        elif token['type'] == 'VARIABLE':
            self.advance()
            return ('VARIABLE', token['value'])
        elif token['type'] == 'BOOLEAN':
            self.advance()
            return ('BOOLEAN', True if token['value'] == 'true' else False)
        elif token['type'] == 'STRING':
            self.advance()
            return ('STRING', token['value'])

    def parse_block(self):
        self.advance()  # Consume '{'
        statements = []
        while self.current_token and self.current_token['value'] != 'mudhala':
            statements.append(self.parse())
        self.advance()  # Consume 'mudhala'
        return statements
        
