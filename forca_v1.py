# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.posicao = 0
		self.word = word
		self.word_hidden = self.hide_word(word)
		self.letras_certas = []
		self.letras_erradas = []
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word:
			self.letras_certas.append(letter)
			self.unhide_word(letter)
		else:
			self.letras_erradas.append(letter)
			self.posicao += 1
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if self.posicao == len(board):
			return True
		else:
			return False
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if self.word_hidden.count('_') == 0:
			return True
		else:
			return False

	# Método para não mostrar a letra no board
	def hide_word(self, word):
		hidden = '_'
		return str([hidden for x in word])

	# Método para mostrar a letra no board quando o jogador acertar a letra
	def unhide_word(self, letter):
		letter_positions = [x for x in range(0, len(self.word)) if letter == self.word[x]]
		for x in letter_positions:
			self.word_hidden[x] = self.word[x]
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

