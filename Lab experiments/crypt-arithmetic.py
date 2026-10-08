def solve():
    letters = "SENDMORY"
    digits = {}
    used = set()

    def backtrack(index):
        if index == len(letters):
            S, E, N, D = digits['S'], digits['E'], digits['N'], digits['D']
            M, O, R, Y = digits['M'], digits['O'], digits['R'], digits['Y']

            SEND = 1000*S + 100*E + 10*N + D
            MORE = 1000*M + 100*O + 10*R + E
            MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

            return SEND + MORE == MONEY

        letter = letters[index]

        for digit in range(10):

            
            if digit in used:
                continue

            if (letter == 'S' or letter == 'M') and digit == 0:
                continue

            digits[letter] = digit
            used.add(digit)

            if backtrack(index + 1):
                return True

            used.remove(digit)
            del digits[letter]

        return False

    if backtrack(0):
        print("Solution:")
        print(digits)

        S, E, N, D = digits['S'], digits['E'], digits['N'], digits['D']
        M, O, R, Y = digits['M'], digits['O'], digits['R'], digits['Y']

        SEND = 1000*S + 100*E + 10*N + D
        MORE = 1000*M + 100*O + 10*R + E
        MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

        print(SEND, "+", MORE, "=", MONEY)


solve()
