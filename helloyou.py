from optparse import Option
import time



print("je was aan het lopen daarna zag je een zwarte tas")
time.sleep(1)
print("wat ga je doen?")
time.sleep(1)
print("""
A. de tas pakken
B.De tas niet pakken""")

antwoord = input("")

if antwoord == "a":
  option_pick()
elif antwoord == "b":
    print("je bent dood")
    


def option_pick():
    print ("hij pakte de tas en ging snel naar huis."
  "de tas openen ?")
    time.sleep(1)
print ("""  
    A. de tas openen
    B. niet openen""")

if antwoord == "a":
  option_open()
elif antwoord == "b":
  print("dat kan ook")

def option_open():
  print("Hij doet de tas open er stond een briefje en een schatkaart er stond drieduizend euro in de briefje")
print("""wat kiesje ?
A.de briefje en de schatkaart lezen
B.alleen de briefje openen
""")
if antwoord == "a":
  ()
elif antwoord == "b":
    print("je bent dood")