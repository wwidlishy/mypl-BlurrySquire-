# PROGRAMMING LANGUAGE FRONT END #
from lexer import Lexer
import sys

def CleanTokens(token_list = []):
    new_tokens = []

    for token in token_list:
        new_tokens.append(f'{token.type}: {token.value}')
    
    return new_tokens


lexer = Lexer()

shell_run = True

title = "____ Python Programming Language ____"
print(title)
print("___ V0.1.0 ___".center(len(title), "_"), end='\n\n')

while shell_run:
    text = input("Programming Language> ")

    if text.lower().strip() == 'exit': break

    tokens = lexer.create_tokens(text)
    print(CleanTokens(tokens))

sys.exit()