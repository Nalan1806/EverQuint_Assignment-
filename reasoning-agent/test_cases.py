from agent import solve

test_questions = [
    # EASY
    "What is 2 + 3?",
    "What is 10 * 5?",
    "Alice has 3 apples and twice as many green apples. How many apples?",
    "Train leaves at 14:30 and arrives at 18:05. Duration?",
    "What is 100 / 4?",

    # TRICKY
    "Alice has 5 apples, gives away 2, then doubles remaining. Total?",
    "Meeting is 60 min, slots 09:00–09:30, 09:45–10:30, 11:00–12:00. Which works?",
    "What is (2 + 3) * 4?",
    "Train leaves at 23:30 and arrives at 01:00. Duration?",
]

for q in test_questions:
    print("\nQuestion:", q)
    result = solve(q)
    print(result)