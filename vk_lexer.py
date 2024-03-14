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
            'piri': 'DIVIDE'
        }
        
        operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=']
        
        tokens = []
        code_lines = self.code.split('\n')
        
        for line in code_lines:
            line = line.strip()
            if not line:
                continue
            
            tokens.extend(self.tokenize_line(line, keywords, operators))
            
        self.tokens = tokens
        return tokens

    def tokenize_line(self, line, keywords, operators):
        tokens = []
        current_token = ''
        
        i = 0
        while i < len(line):
            char = line[i]
            
            if char.isalpha() or char == '_':
                current_token += char
                i += 1
                while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                    current_token += line[i]
                    i += 1
                
                if current_token in keywords:
                    tokens.append((current_token, keywords[current_token]))
                else:
                    tokens.append((current_token, 'IDENTIFIER'))
                
                current_token = ''
            
            elif char.isdigit():
                current_token += char
                i += 1
                while i < len(line) and line[i].isdigit():
                    current_token += line[i]
                    i += 1
                
                tokens.append((current_token, 'NUMBER'))
                current_token = ''
            
            elif char in operators:
                if i + 1 < len(line) and line[i:i+2] in operators:
                    tokens.append((line[i:i+2], 'OPERATOR'))
                    i += 2
                else:
                    tokens.append((char, 'OPERATOR'))
                    i += 1
            
            elif char.isspace():
                i += 1
            
            else:
                i += 1
        
        return tokens

# Example usage:
code = """
thodarai VK_Lexer:
    athu __init__(self, code):
        idam(self):
            'code': code
            'tokens': []
        mudhala(self)

    thodarai tokenize(self):
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
            'piri': 'DIVIDE'
        }
        
        operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=']
        
        tokens = []
        code_lines = self.code.split('\\n')
        
        for line in code_lines:
            line = line.strip()
            if not line:
                continue
            
            tokens.extend(self.tokenize_line(line, keywords, operators))
            
        self.tokens = tokens
        return tokens

    thodarai tokenize_line(self, line, keywords, operators):
        tokens = []
        current_token = ''
        
        i = 0
        while i < len(line):
            char = line[i]
            
            if char.isalpha() or char == '_':
                current_token += char
                i += 1
                while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                    current_token += line[i]
                    i += 1
                
                if current_token in keywords:
                    tokens.append((current_token, keywords[current_token]))
                else:
                    tokens.append((current_token, 'IDENTIFIER'))
                
                current_token = ''
            
            elif char.isdigit():
                current_token += char
                i += 1
                while i < len(line) and line[i].isdigit():
                    current_token += line[i]
                    i += 1
                
                tokens.append((current_token, 'NUMBER'))
                current_token = ''
            
            elif char in operators:
                if i + 1 < len(line) and line[i:i+2] in operators:
                    tokens.append((line[i:i+2], 'OPERATOR'))
                    i += 2
                else:
                    tokens.append((char, 'OPERATOR'))
                    i += 1
            
            elif char.isspace():
                i += 1
            
            else:
                i += 1
        
        return tokens

# Testing the Lexer
lexer = VK_Lexer(code)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
    
