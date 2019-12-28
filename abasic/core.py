from .lexer.scanner import Scanner


def main(program):
    scanner = Scanner(program)
    result = scanner.getNextLexem()
    print(result)
