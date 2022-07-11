# Simple Compiler
# Jesus Monterrubio, a01114287

from tokens import Tokens;

# ---------------------------------- Scanner code

global content_index;
global content;
content_index = 0;

def peek():
    global content_index;
    global content;
    return content[content_index];

def advance():
    global content_index;
    val = peek();
    content_index += 1; 
    return val;

def eof(): #End of file
    global content_index;
    global content;
    return content_index >= len(content);

def scan_digits():
    ans = {
        'val': ' '    
    }
    while peek() in '0123456789':
        ans['val'] = ans['val'] + advance();
    if peek() != '.':
        ans['type'] = 'inum';
    else:
        ans['type'] = 'fnum';
        ans['val'] = ans['val'] + advance();
        while peek() in '0123456789':
            ans['val'] = ans['val'] + advance();
    return ans;

def scanner():
    global content_index;
    global content;
    ans = {};
    while not eof() and (peek() == ' ' or peek() == '\n'):
        advance();
    if eof():
        ans['type'] = '$';
    else:
        if peek() in '0123456789':
            ans = scan_digits();
        else:
            ch = advance();
            if ch in 'abcdeghjklmnoqrstuvwxyz':
                ans['type'] = 'id';
                ans['val'] = ch;
            elif ch == 'f':
                ans['type'] = 'floatdcl';
            elif ch == 'i':
                ans['type'] = 'intdcl';
            elif ch == 'p':
                ans['type'] = 'print';
            elif ch == '=':
                ans['type'] = 'assign';
            elif ch == '+':
                ans['type'] = 'plus';
            elif ch == '-':
                ans['type'] = 'minus';
            else:
                print('Error lexico');
                exit();
    return ans;

class Node:
    val = None;
    type = None;
    childs = None;

    def __init__(self, type = None, val = None):
        self.val = val;
        self.type = type;
        self.childs = [];

    def setVal(self, val):
        self.val = val;

    def setType(self, type):
        self.type = type;

    def addChilds(self, nodes):
        for node in nodes:
            self.childs.append(node);
            
    #def advance():

    def error(self):
        print('Error.');
        exit();

    def __str__(self, level = 0):
        ret = '\t' * level + repr(self.type)+'\n';
        for child in self.childs:
            ret += child.__str__(level+1);
        return ret;

# ---------------------------------- Parser code

def match():
    if tokens.peek()['type'] == 'id' or tokens.peek()['type'] == 'assign':
        print(tokens.advance()['type']); #Funcion advance() no implementada.
    else:
        error();

def error():
    print('Error.');
    exit();

def stmt(tokens):
    if tokens.peek()['type'] == 'id':
        match(); #Posiblemente incompleto.
        #val(); #No implementado aun.
        #expr(); #No implementado aun.
    else:
        if tokens.peek() == 'print':
            match(); #Posiblemente incompleto.
        else:
            error();

def stmts(tokens):
    if tokens.peek()['type'] == 'id' or tokens.peek()['type'] == 'print':
        stmt(tokens);
        stmts(tokens);
    else:
        if tokens.peek() == '$':
            return [];
        else:
            error();

def dcl(tokens):
    if tokens.peek()['type'] == 'intdcl' or tokens.peek()['type'] == 'floatdcl':
        node = Node(tokens.advance()['type']); #Funcion advance() no implementada.
        if tokens.peek()['type'] == 'id':
            node.setVal(tokens.advance()['val']); #Funcion advance() no implementada.
            return [node];
        else:
            error();
    return [];

def dcls(tokens):
    if tokens.peek()['type'] == 'intdcl' or tokens.peek()['type'] == 'floatdcl':
        nodes = dcl(tokens);
        return nodes + dcls(tokens);
    return [];

def prog(tokens):
    root = Node('prog');
    root.addChilds(dcls(tokens));
    root.addChilds(stmts(tokens));
    return root;

# ---------------------------------- File code

with open('input.txt') as f:
    content = f.read();
tokens = Tokens();
while not eof():
    tokens.append(scanner());
tokens.append(scanner());

print(prog(tokens));

#Programa no terminado por completo debido a diversos factores justificables y aunque no funcione por completo, favor de tomar en cuenta la lógica y código en si, más que la salida.