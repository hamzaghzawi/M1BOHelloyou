from secrets import choice
import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]



def stukje1():
    print("Hassan was een keertje aan het lopen en toen zeg hij een zwarte tas op de grond")
    print("wat kies je")
    time.sleep(2)
    print("A: de tas pakken ")
    print("B: de tas niet pakken")
    vraag = input()
    if vraag in answer_A: 
            stukje2()

    elif vraag in answer_B:
            stukje16()

    else:
        print("typ een geldig antwoord !")


def stukje2():
    print("Hij  pakte de tas en ging snel naar huis om de tas te openen ")
    print("wat kies je ")
    time.sleep(2)
    print("A: de tas openen")
    print("B: de tas niet openen")
    vraag = input()
    if vraag in answer_A: 
                stukje3()

    elif vraag in answer_B:
                stukje17()

    else:
        print("typ een geldig antwoord !")

def stukje3():
    print("Hij doet de tas open er stond een briefje en een schatkaart er stond drieduizend euro in de briefje")
    print("wat kies je nu")
    time.sleep(2)
    vraag = input()
    if vraag in answer_A: 
                stukje4()

    elif vraag in answer_B:
                stukje18()

    else:
        print("typ een geldig antwoord !")

def stukje4():
    print("Er stond in de schatkaart dat de schat in Egypte was")
    print("wat kies je nu ?")
    time.sleep(2)
    print("A: naar egypte gaan")
    time.sleep(1)
    print("niet naar egypte gaan")
    vraag = input()
    if vraag in answer_A: 
                stukje5()

    elif vraag in answer_B:
                stukje19()

    else:
        print("typ een geldig antwoord !")


def stukje5():
    print("Er was maar een manier om naar Egypte te gaan en dat is door de zee")
    print("wat kies je nu ?")
    time.sleep(2)
    print("A:Door de zee gaan ")
    print("B: met een andere manier gaan")
    vraag = input()
    if vraag in answer_A: 
                stukje6()

    elif vraag in answer_B:
                stukje20()

    else:
        print("typ een geldig antwoord !")

def stukje6():
    print("Hassan begon zijn reis")
    print("maar hij had vergeten om eten mee te nemen")
    print(" denk je dat hij dood gaat?")
    time.sleep(2)
    print("A: hij gaat dood.")
    print("B: hij blijft nog leven")
    vraag = input()
    if vraag in answer_A: 
                stukje21()

    elif vraag in answer_B:
                stukje7()

    else:
        print("typ een geldig antwoord !")

def stukje7():
    print("Hassan zag een kleine eiland in de verte hij twijfelde om naar die Eiland te gaan maar hij had eten nodig")
    print("wat kies je ?")
    time.sleep(2)
    print("A: naar de eiland gaan.")
    print("B: niet gaan en door varen")
    vraag = input()
    if vraag in answer_A: 
                stukje8()

    elif vraag in answer_B:
                print(" fout gekozen, begin op nieuw")

    else:
        print("typ een geldig antwoord !")

def stukje8():
    print("""Hassan besloot om naar die eiland te gaan Hassan was op het eiland aangekomen Hassan was heel bang omdat het donker was")
    print("en hij hoorde enge geluiden in de eiland. 
    Hassan ging binnen de bos in hij zag een kleine huisje hij wist niet voor 
    wie die huisje was hij wou een beetje in die huisje zitten tot het zon schijnt zodat hij eten kan halen en goed kan zien""")
    time.sleep(2)
    print("A: door gaan met de verhaal")
    vraag = input()
    if vraag in answer_A: 
                stukje9()

    else:
        print("typ een geldig antwoord !")


def stukje9():
    print(""" Toen hij aan het wandelen was liep er een meisje op een paard met heel veel mannen
     Hassan wist niet wie dat meisje was.""")
    print("wat kies je ?")
    time.sleep(2)
    print("""A: iemand vragen wie dat meisje is
    B: niks doen """)
    vraag = input()
    if vraag in answer_A: 
                stukje10()

    elif vraag in answer_B:
                print(" fout gekozen, begin op nieuw")

    else:
        print("typ een geldig antwoord !")

def stukje10():
    print("hij vroeg iemand wie dat meisje was toen zei de man dat dat meisje de dochter van de koning van Egypte was")
    print(""" Hassan vond haar leuk en wou met haar trouwen. hij vroeg een oude man waar de kasteel ligt van haar vader
    en wou naar de kasteel gaan""")
    time.sleep(2)
    print("wat kies je ?")
    print("""A: naar de kasteel gaan
    B: niet naar de kasteel gaan """)
    vraag = input()
    if vraag in answer_A: 
                stukje11()

    elif vraag in answer_B:
                print(" fout gekozen, begin op nieuw")

    else:
        print("typ een geldig antwoord !")

def stukje11():
    print("""Hassan was naar de kasteel gegaan
    toen hij onderweg was werd hij aangevallen door twee soldaten maar hij had ze dood gemaakt. Hij zag dat er een briefje in de zak van een van die soldaten lag""")
    print("wat kies je ")
    time.sleep(2)
    print("""A: de briefje lezen
            B: de briefje niet lezen""")
    vraag = input()
    if vraag in answer_A: 
                stukje12()

    elif vraag in answer_B:
                print(" je bent dood")

    else:
        print("typ een geldig antwoord !")

def stukje12():
    print("""er stond in de briefje dat de schat in de kasteel zat, maar 
    om daar binnen te komen moet je de koningin vrij maken 
    hassan ging meteen naar de kasteel hij zag veel soldaten staan. hij had een manier bedacht
    om naar binnen te komen""")
    time.sleep(2)
    print("wat is de manier denk je ?")
    time.sleep(1)
    print("""A: de kleding aan doen van de soldaat die dood was en naar binnen gaan
             B: de soldaten aanvallen en naar binnen komen""")
    vraag = input()
    if vraag in answer_A: 
                stukje13()

    elif vraag in answer_B:
                print(" je bent dood")

    else:
        print("typ een geldig antwoord !")

def stukje13():
    print(""" Hij had de kleding aan gedaan van de soldaten die dood waren en ging naar binnen. 
    Hij zag twee grote deuren een van die deuren was de ingang tot de kamer van de dochter van de koning maar Hassan weet niet welke deur dat was""")
    time.sleep(2)
    print("welke deur was het denk je ?")
    print("""A: Deur 1
        B: Deur 2""")
    vraag = input()
    if vraag in answer_A: 
                print("fout")

    elif vraag in answer_B:
         stukje14

    else:
        print("typ een geldig antwoord !")

def stukje14():
    print("""oke hassan heeft nu deur 2 geopend en zag dat meisje hij zei tegen haar dat hij met haar wilt trouwen
    ze zei ja maar ze zei dat ze van hier snel weg moeten gaan anders gaat haar vader hun dood maken""")
    time.sleep(2)
    print("hassan had geen tijd en moest kiezen of de schat pakken of de koningin redden")
    time.sleep(1)
    print("wat heeft hij gekozen denk je ?")
    time.sleep(2)
    print("A: de koningin")
    print("B: de schat")
    vraag = input()
    if vraag in answer_A: 
                stukje15

    elif vraag in answer_B:
         print("hassan had de schat gekozen maar werd hij gepakt en is hij dood gegaan")

    else:
        print("typ een geldig antwoord !")

def stukje15():
    print(""" Hassan had de dochter van de koning gekozen en gingen samen weg rennen. 
    Daarna gingen ze trouwen en hebben twee kinderen gekregen en waren ze heel blij""")
    time.sleep(2)
    print("goed gedaan")
    time.sleep(1)
    print("einde 1 normaal einde!")

def stukje16():
        print("Hassan had de tas niet gepakt en ging door lopen ")
        time.sleep(2)
        print("einde 2 doodlopende einde")

def stukje17():
    print("Hassan had de tas gepakt en nam hem mee naar huis maar hij had hem niet geopend")
    print("A: door gaan ")
    vraag = input()
    if vraag in answer_A: 
                stukje18

    else:
        print("typ een geldig antwoord !")


def stukje18():
    print("""Hassan had de briefje geopend en er stond 3000 euro in de briefje. 
    Hassan had de 3000 gepakt en ging een paar spullen kopen.""")
time.sleep(1)
print("einde 3 doodlopende einde")

def stukje19():
    print("""Hassan ging niet naar Egypte en bleef arm 
 Einde 3 Dood lopende einde
""")


def stukje20():
    print("""Hassan ging dood de woestijn. Dat was verkeerde keuze en ging hij dood 
Einde 4 Dood lopende einde
""")

def stukje21():
    print("""Hassan ging na twee uur dood omdat hij geen eten meer had.
Einde 5 dood lopende einde
""")




















stukje1()
