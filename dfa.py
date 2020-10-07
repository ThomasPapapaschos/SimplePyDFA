# PAPAPASCHOS THOMAS
from typing import Dict
from getch import getche
import pprint


def fileToDFA():
    """Read a text file.Create a DFA as a dictionary and return it and its initial state
	"""
    dictionary: Dict[str, Dict[str, bool]] = {}
    with open('dfa.txt', 'r') as dict:
        states = int(next(dict))  # number of states (1st line)
        for s in range(states):
            # save the states
            # for now T is False just for initialization
            dictionary[str(s)] = {'T': False}

        next(dict)  # Alphabet characters  (2nd line) , will use exception handling for simplicity so i just skip this line
        initial_state = next(dict)  # The initial state	(3rd line)
        terminal_states = next(dict).split()  # Terminal(Accept) states (4th line)
        for s in terminal_states:
            # Now that we know which of the states are terminal we set the value to True
            dictionary[s]['T'] = True
        # State transitions 5th line - end of file.
        for line in dict:
            current, symbol, nxt = line.split()
            dictionary[current][symbol] = nxt

        return dictionary, initial_state


choice = 'y'
dfa, initial_state = fileToDFA()  # function provides us with the dfa behaviour
pprint.pprint(dfa)  # pretty print dictionary dfa
print("Start by typing characters one by one and then press enter to test string")
while choice != 'n':  # if user wishes to give another string
    notInAlphabet: bool = False
    current_state = initial_state
    while True:
        pressedKey = getche()  # get char from user and echo
        if pressedKey == '\n':
            break
        else:
            # current state is of type str so we need to strip the /n at the end to be able to use it as a key
            current_state = current_state.rstrip()
            try:
                next_state = dfa[current_state][pressedKey]  # state transitions accordingly
            except KeyError:
                # key error exception handling
                # this means an invalid symbol was used , so we reject the string
                print("\nInput string is Rejected because it has characters that do not belong to the given alphabet.")
                notInAlphabet = True
                break
            current_state = next_state  # go to the next state
    if not notInAlphabet:
        if dfa[current_state]['T']:
            print("Input string is Accepted by the DFA.")
        else:
            print("Input string is Rejected by the DFA.")
    choice = input('Test another string?[y/n]: ')
