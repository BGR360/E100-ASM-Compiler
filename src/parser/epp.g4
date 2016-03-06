grammar epp;

program : statementList
        ;

statementList : statementList statement
              | statement
              ;

statement : expression ';'
          | ';'
          ;

expression : leftValue '=' expression
           | expression '+' expression
           | expression '-' expression
           | expression '*' expression
           | expression '/' expression
           | '(' expression ')'
           | leftValue
           | Constant
           ;

leftValue : Type Identifier
          | Identifier
          ;

Constant : Integer
         | Boolean
         ;

Type : ('int' | 'bool');
Boolean : ('true' | 'false');

Whitespace : [ \t\r\n]+ -> skip;

Identifier
    :   Alpha AlphaNumeric*;

AlphaNumeric : (Alpha | Digit);
Integer : Digit+;
Alpha : [a-zA-Z_];
Digit : [0-9];