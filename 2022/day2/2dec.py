# 1: rock, 2: paper, 3: scissors
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.

#Getting input data

with open('2dec.in') as file:
    rounds = [i for i in file.read().strip().split("\n")]

   #print(rounds)

# ALL POSSIBLE OUTCOMES
# ---------------------
# Left vs right | Right+Outcome | Outcome
# A vs X = 1+3 = 4 = DRAW
# A vs Y = 2+6 = 8 = WIN
# A vs Z = 3+0 = 3 = LOSS
# B vs X = 1+0 = 1 = LOSS
# B vs Y = 2+3 = 5 = DRAW
# B vs Z = 3+6 = 9 = WIN
# C vs X = 1+6 = 7 = WIN
# C vs Y = 2+0 = 2 = LOSS
# C vs Z = 3+3 = 6 = DRAW

#Part 1 
outcomes = {
"A X":3, "A Y":8, "A Z":3, 
"B X":1, "B Y":5, "B Z":9, 
"C X":7, "C Y":2, "C Z":6
}

totalscore_p1 = 0
for round in rounds:
    totalscore_p1 += outcomes[round]


print("Puzzle answer Part1:",totalscore_p1)

#Part2
outcomes_p2 = {
"A X":3, "A Y":4, "A Z":8, 
"B X":1, "B Y":5, "B Z":9, 
"C X":2, "C Y":6, "C Z":7
}

totalscore_p2 = 0
for round in rounds:
    totalscore_p2 += outcomes_p2[round]


print("Puzzle answer Part2:",totalscore_p2)