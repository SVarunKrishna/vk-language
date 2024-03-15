import re

class VkLexer:
    def __init__(self, code):
        self.code = code
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
            'moolyam': 'VARIABLE',
            'Paaru': 'PRINTF',
            'sollu': 'SCANF',
            'int mukiyam': 'INT_MAIN',
            'seru': 'ADD',
            'kora': 'SUBTRACT',
            'Ona': 'MULTIPLY',
            'piri': 'DIVIDE',
            'vaathiyar_padithaal': 'SCAN',
            'vaathiyar_kodu': 'PRINT',
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
            '+': 'PLUS',
            '-': 'MINUS',
            '*': 'MULTIPLY',
            '/': 'DIVIDE',
            '%': 'MODULO',
            '==': 'EQUALS',
            '!=': 'NOT_EQUALS',
            '<': 'LESS_THAN',
            '>': 'GREATER_THAN',
            '<=': 'LESS_THAN_OR_EQUAL',
            '>=': 'GREATER_THAN_OR_EQUAL'
        }
        self.tokens = []

    def tokenize(self):
        code_without_comments = re.sub(r'//[^\n]*', '', self.code)  # Remove single-line comments
        code_without_comments = re.sub(r'/\*.*?\*/', '', code_without_comments, flags=re.DOTALL)  # Remove multi-line comments

        tokens = []
        current_word = ''
        in_string = False

        for char in code_without_comments:
            if char == '"':
                if in_string:
                    tokens.append(('STRING', current_word))
                    current_word = ''
                in_string = not in_string
            elif in_string:
                current_word += char
            elif char.isalnum() or char == '_':
                current_word += char
            else:
                if current_word:
                    if current_word in self.keywords:
                        tokens.append((self.keywords[current_word], current_word))
                    elif current_word.isdigit():
                        tokens.append(('NUMBER', int(current_word)))
                    else:
                        tokens.append(('IDENTIFIER', current_word))
                    current_word = ''
                if char.strip():
                    if char in self.operators:
                        tokens.append((self.operators[char], char))
                    else:
                        tokens.append(('SYMBOL', char))

        return tokens

# Example usage:
code = """
int mukiyam() {
    Paaru "Hello, Vk!";
    int x = 5 + 3;
    sollu x;
}

int main() {
    int y = 10;
    Paaru y;
    niyal(int i = 0; i < 5; i++) {
        Paaru i;
    }
    annippadu 0;
}
"""
lexer = VkLexer(code)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
                        
