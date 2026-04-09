from pathlib import Path

folderName = Path(__file__).parent.resolve()
inputFilename = Path(folderName, "Input4.txt")
with open(inputFilename, "r") as f:
    lines = f.read().splitlines()

# Part 1
numbers = lines[0].split(",")
boards = []
marks = []
newBoard = []
newMarks = []
for line in lines[2:]:
    if line == "":
        boards.append(newBoard)
        marks.append(newMarks)
        newBoard = []
        newMarks = []
    else:
        boardRow = []
        marksRow = []
        for number in line.split():
            boardRow.append(int(number))
            marksRow.append(0)
        newBoard.append(boardRow)
        newMarks.append(marksRow)


def calculateScore(board, marks, number):
    boardSum = 0
    for row in range(len(board)):
        for column in range(len(board[0])):
            if marks[row][column] != 1:
                boardSum += board[row][column]
    return int(number) * boardSum


winscores = []
winners = []
for number in numbers:
    # Mark the Boards
    for boardnum in range(len(boards)):
        for rownum in range(len(boards[0])):
            for columnnum in range(len(boards[0][0])):
                if boards[boardnum][rownum][columnnum] == int(number):
                    marks[boardnum][rownum][columnnum] = 1
    # Check for a winner
    for boardnum in range(len(boards)):
        if boardnum in winners:
            continue
        for rownum in range(len(boards[0])):
            if sum(marks[boardnum][rownum]) == 5:
                print(f"A Row Bingo on row {rownum} of board {boardnum}!")
                winners.append(boardnum)
                winscores.append(
                    calculateScore(boards[boardnum], marks[boardnum], number)
                )
        for columnnum in range(len(boards[0][0])):
            columnmarks = 0
            for rownum in range(len(boards[0][0])):
                columnmarks += marks[boardnum][rownum][columnnum]
            if columnmarks == 5:
                print(f"A Column Bingo on column {columnnum} of board {boardnum}!")
                winners.append(boardnum)
                winscores.append(
                    calculateScore(boards[boardnum], marks[boardnum], number)
                )
print("Part 1")
print("======")
print(f"Final Score: {winscores[0]}")
# Part 2

print("Part 2")
print("======")
print(f"Final Score: {winscores[-1]}")
