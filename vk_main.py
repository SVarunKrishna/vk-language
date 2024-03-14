from vk_lexer import VK_Lexer
from vk_parser import VK_Parser
from vk_interpreter import VK_Interpreter

def main():
    code = """
    int mukiyam() {
        int a = 5;
        int b = 3;
        Paaru a;
        sollu b;
        int c = a + b;
        Paaru c;
    }
    """

    lexer = VK_Lexer(code)
    tokens = lexer.tokenize()

    parser = VK_Parser(tokens)
    parsed_code = parser.parse()

    interpreter = VK_Interpreter()
    result = interpreter.interpret(parsed_code)
    print("Output:", result)

if __name__ == "__main__":
    main()
  
