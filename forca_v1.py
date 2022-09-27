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
		self.letras_certas = []
		self.letras_erradas = []
		self.word_hidden = self.hide_word(word)
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word:
			self.letras_certas.append(letter)
			self.word_hidden = self.hide_word(self.word)
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
		lista_escondida = [letra for letra in word]
		word_hidden = ''
		for i in range(0, len(word)):
			if lista_escondida[i] not in self.letras_certas:
				word_hidden += hidden
			else:
				word_hidden += lista_escondida[i]
		return word_hidden

	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		game_over = False
		while not game_over:
			print(board[self.posicao])
			print("Palavra " + self.word_hidden)
			print("Letras erradas: " + str(self.letras_erradas))
			print("Letras corretas: " + str(self.letras_certas))
			print("")
			letter = input("Digite uma letra: ")
			if letter not in self.letras_certas and letter not in self.letras_erradas:
				self.guess(letter)
			if self.hangman_won() or self.hangman_over():
				game_over = True
		

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0, len(bank) - 1)].strip()


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

