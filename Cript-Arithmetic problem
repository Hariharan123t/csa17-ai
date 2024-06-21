import itertools

def solve_cryptarithmetic():
    # Define the unique letters in the problem
    letters = 'SENDMORY'
    
    # Generate all permutations of the digits 0-9 of length equal to the number of unique letters
    for perm in itertools.permutations('0123456789', len(letters)):
        # Create a mapping from letters to digits
        mapping = dict(zip(letters, perm))
        
        # Ensure that none of the leading digits are zero
        if mapping['S'] == '0' or mapping['M'] == '0':
            continue
        
        # Convert the words to numbers based on the current mapping
        send = int("".join(mapping[letter] for letter in 'SEND'))
        more = int("".join(mapping[letter] for letter in 'MORE'))
        money = int("".join(mapping[letter] for letter in 'MONEY'))
        
        # Check if the equation holds
        if send + more == money:
            return mapping, send, more, money
    
    return None

result = solve_cryptarithmetic()
if result:
    mapping, send, more, money = result
    print("Solution found:")
    print(f"SEND = {send}")
    print(f"MORE = {more}")
    print(f"MONEY = {money}")
    print("Mapping of letters to digits:", mapping)
else:
    print("No solution found.")
