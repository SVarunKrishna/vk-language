import re

class VK_Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
        self.keywords = {
            'thodarai': 'CLASS',
            'athu': 'DEF',
            'idam': 'INIT',
            'mudhala': 'END',
            'niyal': 'FOR',
            'siru': 'IF',
            'koodal': 'ELSE',
            'ippathaal': 'ELIF',
            'annippadu': 'RETURN',
            'kootu': 'APPEND',
            'moolyam': 'INTEGER',
            'varisai': 'FLOAT',
            'vaathiyar': 'CHAR',
            'pali': 'BOOLEAN',
            'solluvai': 'STRING',
            'Paaru': 'PRINTF',
            'sollu': 'SCANF',
            'int mukiyam': 'INT_MAIN',
            'seru': 'ADD',
            'kora': 'SUBTRACT',
            'Ona': 'MULTIPLY',
            'piri': 'DIVIDE',
            'chutti': 'SWITCH',
            'pirandh': 'TRY',
            'pirindhu': 'CATCH',
            'paeru': 'FINALLY',
            'vaathiyar_padithaal': 'INPUT',
            'vaathiyar_kodu': 'OUTPUT',
            'moolyam_vivarithi': 'MATH_LIBRARY',
            'moolyam_mithalai': 'SQRT',
            'moolyam_sin': 'SIN',
            'vaakku_vivarithi': 'STRING_LIBRARY',
            'vaakku_seer': 'CONCAT',
            'vaakku_udaiya': 'TO_UPPER',
            'kaar_vivarithi': 'DATETIME_LIBRARY',
            'udaiya_kaar': 'CURRENT_DATE',
            'kaar_vithaika': 'FORMAT_DATE',
            'arai_kuthirai': 'RANDOM_LIBRARY',
            'arai_kuthirai_mithalai': 'RANDOM_INT',
            'arai_kuthirai_vithai': 'RANDOM_CHOICE',
            'veezh_vivarithi': 'OS_LIBRARY',
            'veezh_vaakiyam': 'LIST_FILES',
            'veezh_udaiya_kattam': 'CREATE_DIRECTORY',
            'mann_kadhai': 'VK_LIBRARY',
            'mann_pirachanai': 'VK_VERSION',
            'mann_ootru': 'PLATFORM_ID'
        }
        self.operators = {
            '+': 'ADD',
            '-': 'SUBTRACT',
            '*': 'MULTIPLY',
            '/': 'DIVIDE',
            '(': 'LPAREN',
            ')': 'RPAREN',
            ':': 'COLON',
            '=': 'EQUALS',
            ',': 'COMMA'
        }
        self.regex_patterns = [
            (r'\b(?:nool|vaanavil)\b', 'KEYWORD'),  # switch case keywords
            (r'\b(?:pirindhu)\b', 'KEYWORD'),  # try-catch block keywords
            (r'"[^"]*"', 'STRING'),  # String literals
            (r'\d+\.\d+', 'FLOAT'),  # Float literals
            (r'\d+', 'INTEGER'),  # Integer literals
            (r'thodarai|athu|mudhala|niyal|siru|koodal|ippathaal|annippadu|kootu|int mukiyam|varisai|vaathiyar|pali|solluvai|Paaru|sollu|vaathiyar_padithaal|vaathiyar_kodu|moolyam_vivarithi|moolyam_mithalai|moolyam_sin|vaakku_vivarithi|vaakku_seer|vaakku_udaiya|kaar_vivarithi|udaiya_kaar|kaar_vithaika|arai_kuthirai|arai_kuthirai_mithalai|arai_kuthirai_vithai|veezh_vivarithi|veezh_vaakiyam|veezh_udaiya_kattam|mann_kadhai|mann_pirachanai|mann_ootru', 'KEYWORD'),  # Keywords
            (r'\+|-|\*|/|\(|\)|:|=|,', 'OPERATOR'),  # Operators
            (r'[a-zA-Z_][a-zA-Z0-9_]*', 'VARIABLE'),  # Variables
            (r'\n', 'NEWLINE')  # Newline
        ]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def peek(self):
        peek_pos = self.pos + 1
        return self.text[peek_pos] if peek_pos < len(self.text) else None

    def get_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
                continue
            if self.current_char in self.operators:
                token_type = self.operators[self.current_char]
                self.advance()
                return {'type': token_type, 'value': token_type}
            if self.current_char == '"':
                self.advance()
                start_pos = self.pos
                while self.current_char != '"':
                    self.advance()
                token_value = self.text[start_pos:self.pos]
                self.advance()  # Consume closing "
                return {'type': 'STRING', 'value': token_value}
            if self.current_char.isdigit():
                token_value = ''
                while self.current_char is not None and self.current_char.isdigit():
                    token_value += self.current_char
                    self.advance()
                if self.current_char == '.':
                    token_value += self.current_char
                    self.advance()
                    while self.current_char is not None and self.current_char.isdigit():
                        token_value += self.current_char
                        self.advance()
                    return {'type': 'FLOAT', 'value': token_value}
                else:
                    return {'type': 'INTEGER', 'value': token_value}
            if self.current_char.isalpha() or self.current_char == '_':
                token_value = ''
                while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
                    token_value += self.current_char
                    self.advance()
                token_type = self.keywords.get(token_value, 'VARIABLE')
                return {'type': token_type, 'value': token_value}
            if self.current_char == '\n':
                self.advance()
                return {'type': 'NEWLINE', 'value': '\n'}
            self.error()
        return {'type': 'EOF', 'value': None}
                
