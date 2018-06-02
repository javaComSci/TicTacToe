
def main():
	print("Welcome to Tic-Tae-Toe")
	while True:
		ans = str(input("Do you want to play Tic-Tae-Toe? Yes or No? "))
		if ans == 'No':
			return
		elif ans != 'Yes':
			print('Enter Yes or No')
			continue

		board = [' ' for i in range(1,10)]
		displayBoard(board)
		sign = str(input("Do you want to use X or O? "))
		if sign == 'X':
			sign1 = 'X'
			sign2 = 'O'
		else:
			sign1 = 'O'
			sign2 = 'X'
		print(f'Player 1 sign: {sign1}\nPlayer 2 sign: {sign2}\n')
		currPlayer = 0
		prevNums = []
		while True:
			print(f'Player {currPlayer + 1} turn')
			num = int(input("Enter number from 1-9 for input "))
			if num < 1 and num > 9:
				print("Enter valid number")
				continue
			if num in prevNums:
				print("Spot already filled, pick another spot")
				continue
			prevNums.append(num)
			if currPlayer == 0:
				board[num - 1] = sign1
				mustBreak = winner(sign1, board, currPlayer)
			else:
				board[num - 1] = sign2
				mustBreak = winner(sign2, board, currPlayer)
			
			if mustBreak:
				break

			displayBoard(board)
			currPlayer = 1 - currPlayer

def displayBoard(board):
	print(f"   |   |")
	print(f" {board[0]} | {board[1]} | {board[2]} ")
	print(f"   |   |")
	print("-----------")
	print(f"   |   |")
	print(f" {board[3]} | {board[4]} | {board[5]} ")
	print(f"   |   |")
	print("-----------")
	print(f"   |   |")
	print(f" {board[6]} | {board[7]} | {board[8]} ")
	print(f"   |   |")

def winner(sign, board, curr):
	if (' ' not in board):
		print("There is a tie. DRAW!")
		return True

	b = False
	if board[0] == board[1] == board[2] == sign:
		b =  True
	if board[3] == board[4] == board[5] == sign:
		b =  True
	if board[6] == board[7] == board[8] == sign:
		b =  True
	if board[2] == board[5] == board[8] == sign:
		b =  True
	if board[1] == board[4] == board[7] == sign:
		b =  True
	if board[0] == board[3] == board[6] == sign:
		b =  True
	if board[2] == board[4] == board[6] == sign:
		b =  True
	if board[0] == board[4] == board[8] == sign:
		b =  True
	if b == True:
		print(f'Player {curr + 1} has won! CONGRATS! \n')
		return True
	return False


if __name__ == '__main__':
	main()