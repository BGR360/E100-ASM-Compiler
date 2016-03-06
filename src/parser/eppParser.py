# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .eppListener import eppListener
else:
    from eppListener import eppListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\23B\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\4")
        buf.write(u"\3\4\3\4\3\4\5\4\35\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\5\5*\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\3\6\3\6\3")
        buf.write(u"\6\5\6@\n\6\3\6\2\4\4\b\7\2\4\6\b\n\2\2F\2\f\3\2\2\2")
        buf.write(u"\4\16\3\2\2\2\6\34\3\2\2\2\b)\3\2\2\2\n?\3\2\2\2\f\r")
        buf.write(u"\5\4\3\2\r\3\3\2\2\2\16\17\b\3\1\2\17\20\5\6\4\2\20\25")
        buf.write(u"\3\2\2\2\21\22\f\4\2\2\22\24\5\6\4\2\23\21\3\2\2\2\24")
        buf.write(u"\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\5\3\2\2\2")
        buf.write(u"\27\25\3\2\2\2\30\31\5\b\5\2\31\32\7\3\2\2\32\35\3\2")
        buf.write(u"\2\2\33\35\7\3\2\2\34\30\3\2\2\2\34\33\3\2\2\2\35\7\3")
        buf.write(u"\2\2\2\36\37\b\5\1\2\37 \5\n\6\2 !\7\4\2\2!\"\5\b\5\n")
        buf.write(u"\"*\3\2\2\2#$\7\t\2\2$%\5\b\5\2%&\7\n\2\2&*\3\2\2\2\'")
        buf.write(u"*\5\n\6\2(*\7\13\2\2)\36\3\2\2\2)#\3\2\2\2)\'\3\2\2\2")
        buf.write(u")(\3\2\2\2*9\3\2\2\2+,\f\t\2\2,-\7\5\2\2-8\5\b\5\n./")
        buf.write(u"\f\b\2\2/\60\7\6\2\2\608\5\b\5\t\61\62\f\7\2\2\62\63")
        buf.write(u"\7\7\2\2\638\5\b\5\b\64\65\f\6\2\2\65\66\7\b\2\2\668")
        buf.write(u"\5\b\5\7\67+\3\2\2\2\67.\3\2\2\2\67\61\3\2\2\2\67\64")
        buf.write(u"\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:\t\3\2\2\2;")
        buf.write(u"9\3\2\2\2<=\7\f\2\2=@\7\17\2\2>@\7\17\2\2?<\3\2\2\2?")
        buf.write(u">\3\2\2\2@\13\3\2\2\2\b\25\34)\679?")
        return buf.getvalue()


class eppParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"';'", u"'='", u"'+'", u"'-'", u"'*'", 
                     u"'/'", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"Constant", u"Type", u"Boolean", u"Whitespace", 
                      u"Identifier", u"AlphaNumeric", u"Integer", u"Alpha", 
                      u"Digit" ]

    RULE_program = 0
    RULE_statementList = 1
    RULE_statement = 2
    RULE_expression = 3
    RULE_leftValue = 4

    ruleNames =  [ u"program", u"statementList", u"statement", u"expression", 
                   u"leftValue" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    Constant=9
    Type=10
    Boolean=11
    Whitespace=12
    Identifier=13
    AlphaNumeric=14
    Integer=15
    Alpha=16
    Digit=17

    def __init__(self, input):
        super(eppParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(eppParser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(eppParser.StatementListContext,0)


        def getRuleIndex(self):
            return eppParser.RULE_program

        def enterRule(self, listener):
            if isinstance( listener, eppListener ):
                listener.enterProgram(self)

        def exitRule(self, listener):
            if isinstance( listener, eppListener ):
                listener.exitProgram(self)




    def program(self):

        localctx = eppParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.statementList(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(eppParser.StatementListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(eppParser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(eppParser.StatementListContext,0)


        def getRuleIndex(self):
            return eppParser.RULE_statementList

        def enterRule(self, listener):
            if isinstance( listener, eppListener ):
                listener.enterStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, eppListener ):
                listener.exitStatementList(self)



    def statementList(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = eppParser.StatementListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_statementList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = eppParser.StatementListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statementList)
                    self.state = 15
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 16
                    self.statement() 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(eppParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(eppParser.ExpressionContext,0)


        def getRuleIndex(self):
            return eppParser.RULE_statement

        def enterRule(self, listener):
            if isinstance( listener, eppListener ):
                listener.enterStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, eppListener ):
                listener.exitStatement(self)




    def statement(self):

        localctx = eppParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 26
            token = self._input.LA(1)
            if token in [eppParser.T__6, eppParser.Constant, eppParser.Type, eppParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.expression(0)
                self.state = 23
                self.match(eppParser.T__0)

            elif token in [eppParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(eppParser.T__0)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(eppParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def leftValue(self):
            return self.getTypedRuleContext(eppParser.LeftValueContext,0)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(eppParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(eppParser.ExpressionContext,i)


        def Constant(self):
            return self.getToken(eppParser.Constant, 0)

        def getRuleIndex(self):
            return eppParser.RULE_expression

        def enterRule(self, listener):
            if isinstance( listener, eppListener ):
                listener.enterExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, eppListener ):
                listener.exitExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = eppParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 29
                self.leftValue()
                self.state = 30
                self.match(eppParser.T__1)
                self.state = 31
                self.expression(8)
                pass

            elif la_ == 2:
                self.state = 33
                self.match(eppParser.T__6)
                self.state = 34
                self.expression(0)
                self.state = 35
                self.match(eppParser.T__7)
                pass

            elif la_ == 3:
                self.state = 37
                self.leftValue()
                pass

            elif la_ == 4:
                self.state = 38
                self.match(eppParser.Constant)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 53
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = eppParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 41
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 42
                        self.match(eppParser.T__2)
                        self.state = 43
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = eppParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 44
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 45
                        self.match(eppParser.T__3)
                        self.state = 46
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = eppParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 47
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 48
                        self.match(eppParser.T__4)
                        self.state = 49
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = eppParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 50
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 51
                        self.match(eppParser.T__5)
                        self.state = 52
                        self.expression(5)
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class LeftValueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(eppParser.LeftValueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Type(self):
            return self.getToken(eppParser.Type, 0)

        def Identifier(self):
            return self.getToken(eppParser.Identifier, 0)

        def getRuleIndex(self):
            return eppParser.RULE_leftValue

        def enterRule(self, listener):
            if isinstance( listener, eppListener ):
                listener.enterLeftValue(self)

        def exitRule(self, listener):
            if isinstance( listener, eppListener ):
                listener.exitLeftValue(self)




    def leftValue(self):

        localctx = eppParser.LeftValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_leftValue)
        try:
            self.state = 61
            token = self._input.LA(1)
            if token in [eppParser.Type]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(eppParser.Type)
                self.state = 59
                self.match(eppParser.Identifier)

            elif token in [eppParser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(eppParser.Identifier)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.statementList_sempred
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def statementList_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         



