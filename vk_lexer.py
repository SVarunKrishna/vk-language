import re

class VK_Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        keyword_patterns = {
            'haa': r'\bhaa\b',
            'uhh': r'\buhh\b',
            'aku': r'\baku\b',
            'ohhh': r'\bohhh\b',
            'kick': r'\bkick\b',
            'Paaru': r'\bPaaru\b',
            'sollu': r'\bsollu\b',
            'int_mukiyam': r'\bint\s+mukiyam\b'
        }
        
        all_keywords_pattern = '|'.join(pattern for pattern in keyword_patterns.values())

        self.tokens = re.findall(r'\b(?:' + all_keywords_pattern + r'|\d+|\+|\-|\*|\/|\(|\)|[a-zA-Z_][a-zA-Z0-9_]*)\b', self.code)
        return self.tokens
      
