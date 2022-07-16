from traceback import print_tb


class VoterEligiblity(Exception):
    def __init__(self) -> None:
        super()
        
try:
    age = 12
    if age < 18:
        raise VoterEligiblity
except VoterEligiblity:
    print("Age is less than 18 !")
else:
    print("Age is greater or equal to 18 !")
finally:
    print("End the progaram !!!")