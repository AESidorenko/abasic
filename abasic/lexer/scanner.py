from .lexem import Lexem, Token
from . import exception


class Scanner:
    program = ""
    pos = 0

    def __init__(self, program=""):
        self.program = program
        self.pos = 0

    def getNextChar(self):
        if self.pos >= len(self.program):
            raise exception.EOFReached()

        char = self.program[self.pos]
        self.pos += 1

        return char

    def getNextLexem(self):
        try:
            c = ""
            while c == Token.WHITESPACE:
                c = self.getNextChar()
        except exception.EOFReached:
            return Lexem.EOF

        if c.isalpha():
            return self.getAlphanumericToken()

    def getAlphanumericToken(self):
        nc = self.getNextChar()
        while nc.isalnum() or nc == Token.UNDERSCORE:
            c += nc
            nc = self.getNextChar()

        return c
