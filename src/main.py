import sys

from antlr4 import *
from parser.eppLexer import eppLexer
from parser.eppParser import eppParser

def main(argv):
	input = FileStream(argv[1])
	lexer = eppLexer(input)
	stream = CommonTokenStream(lexer)
	parser = eppParser(stream)
	tree = parser.program()

if __name__ == '__main__':
	main(sys.argv)