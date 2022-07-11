# Tokens
# Jesus Monterrubio, a01114287

class Tokens:

	tokens = None;
	index = 0;

	def __init__(self):
		self.tokens = [];
		self.index = 0;

	def append(self, token):
		self.tokens.append(token);

	def peek(self):
		return self.tokens[self.index];

	def isEmpty(self):
		return len(self.tokens) == 0;
  
	def last(self):
		return self.tokens[len(self.tokens)-1]['type'];

	def __str__(self):
		ret = '';
		for token in self.tokens:
			ret += token['type'];
			if 'val' in token:
				ret += ': ' + token['val'];
			ret += ', ';
		return ret;

#Programa no terminado por completo debido a diversos factores justificables y aunque no funcione por completo, favor de tomar en cuenta la lógica y código en si, más que la salida.