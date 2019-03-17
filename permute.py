#! python3
# Algorithm to list all permutations of a given string with unique letters.

# We begin by implementing the factorial functions in a non-recursive and then
# recursive way. These will come in handy to test our permutation functions.

# Factorial without recursion
def fac(n):
    if isinstance(n, int):
        if n > 0:
            result = n
            for i in range(n - 1, 0, -1):
                result = result * i
        elif n == 0:
            result = 1
        elif n < 0:
            raise Exception('Factorial of a negative number is undefined.')
        return result
    else:
        raise Exception('Input of factorial has to be an integer.')

# Factorial with recursion
def rec_fac(n):
    if isinstance(n, int):
        if n > 0:
            result = n * rec_fac(n - 1)
        elif n == 0:
            result = 1
        elif n < 0:
            raise Exception('Factorial of a negative number is undefined.')
        return result
    else:
        raise Exception('Input of factorial has to be an integer.')

# Function inserts a given letter into all possible slots of each string in a given
# list of strings and returns the result as a list
def letter_insert(string_list, letter):
    result = []
    for string in string_list:
        result.extend([string[:i] + letter + string[i:] \
            for i in range(0, len(string) + 1)])
    return result

# We next implement the permutation function in a non-recursive and then recursive way.

# Permutation function starts from base case of swapping the first two letters of
# a given string; we assume all of the string's letters occur only once, else the
# resulting list will have repititions
def permute(string):
    result = [string[0]]
    for i in range(1, len(string)):
        result = letter_insert(result, string[i])
    if len(result) != fac(len(string)):
        raise Exception('Output does not have the expected number of permutations.')
    return result

def rec_permute(string):
    if len(string) > 1:
        temp = rec_permute(string[:-1])
        result = letter_insert(temp, string[-1])
        if len(result) != rec_fac(len(string)):
            raise Exception('Output does not have the expected number of permutations.')
        return result
    else:
        return(string)
