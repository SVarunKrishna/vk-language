import re

class VK_Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        keywords = {
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
            'moolyam': 'VARIABLE',
            'Paaru': 'PRINTF',
            'sollu': 'SCANF',
            'int mukiyam': 'INT_MAIN',
            'seru': 'ADD',
            'kora': 'SUBTRACT',
            'Ona': 'MULTIPLY',
            'piri': 'DIVIDE',
            'nirvarthai': 'IDENTIFIER'
        }

        tokens_regex = '|'.join([re.escape(keyword) for keyword in keywords.keys()])
        pattern = re.compile(tokens_regex)

        matches = pattern.finditer(self.code)
        for match in matches:
            token = match.group()
            if token in keywords:
                self.tokens.append((keywords[token], token))
            else:
                self.tokens.append(('NUMBER', token))  # Assuming all other tokens are numbers
        return self.tokens
        
