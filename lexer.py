from token_types import TokenTypes as token_types

# token types init
TokenTypes = token_types()

class Token():
    def __init__(self, t_type, t_value=None):
        self.type = t_type
        self.value = t_value

class Lexer():
    def __init__(self):
        self.tokens = []
        self.pos = 0
        self.input_text = ''
        self.error = None
        self.keyword = ''
    
    def advance(self):
        self.pos += 1
    
    def current_char(self):
        if self.pos >= len(self.input_text): return None
        else: return self.input_text[self.pos]
    
    def create_tokens(self, input_text):
        self.input_text = input_text

        while self.pos < len(self.input_text):
            if self.current_char() == None: break

            elif self.current_char() == '\n': self.tokens.append(Token(TokenTypes.NEWLINE))

            elif self.current_char() == '(': self.tokens.append(Token(TokenTypes.L_BRACK))
            elif self.current_char() == ')': self.tokens.append(Token(TokenTypes.R_BRACK))

            else:
                self.get_keyword()
            
                self.advance()

        return self.tokens

    def get_keyword(self):
        self.keyword = ''

        while True:

            self.keyword += str(self.current_char())

            if self.keyword == 'println':
                self.tokens.append(Token(TokenTypes.PRINT))
                break
                
            self.advance()