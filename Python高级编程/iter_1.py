import tokenize

reader = open('./amina.py').next()
tokens = tokenize.generate_tokens(reader)
print(tokens.next())
