import os

# os.system('cls')



#################################################################
# Finde die Größe des Terminals, um die passende Länge für 
# Trennlinien zu berechnen
#################################################################
size = os.get_terminal_size()
scree_width=size.columns
scree_height=size.lines



#################################################################
# globale Konstanten
#################################################################

trennlinie="="
maximale_inventory_items = 5


################################################################
# Liste des Inventars
################################################################
inventar = []




prolog = """Sie sind Teil einer mutigen Crew, die auf einer Mission im tiefen Raum unterwegs ist, 
um gestrandete Wissenschaftler in einer fernen Galaxie zu retten. Sie haben keine Ahnung, 
was Sie erwartet, wenn Sie den Gamma-Quadranten erreichen, aber Sie wissen, 
dass Sie sich auf unbekanntem Terrain bewegen werden. 
Ihr Raumschiff ist mit modernster Technologie ausgestattet und 
Ihr Team wurde aufgrund seiner Fähigkeiten und Erfahrung sorgfältig ausgewählt.
Ihre Mission ist von großer Bedeutung, denn die Wissenschaftler, 
die Sie retten sollen, arbeiten an einem wichtigen Projekt, das das Schicksal der Galaxie beeinflussen könnte. Die Mission ist gefährlich und voller Herausforderungen, aber Sie sind bereit, sich allen Widrigkeiten zu stellen und die Wissenschaftler zu retten, um ihre wichtige Arbeit fortzusetzen.
Als Sie sich auf den Weg machen, in die Tiefen des Weltraums, 
können Sie nur hoffen, dass Sie und Ihr Team stark genug sind, 
um die Herausforderungen zu bewältigen und diese Mission erfolgreich abzuschließen."""




umgebung = [
                [],
                [],
                ['Asteroid abbauen', 'Schiffswrack'],
                ['Phaser', 'Phaser', 'Sonde', 'Reperatur Kit'],
                [],
                [],
                [],
                ['Gold', 'Diamant'],
                [],
                [],
                [],
                [],
                []


            ]

################################################################
# Die story Liste beinhaltet als Elemente die Kapitel der Geschichte
################################################################
story = [ 
            "Du bist auf einer langen Mission, mit dem Ziel gestrandete Wissenschaftler aus dem gamma-Quadranten zu retten.\nDu bist der Captain auf einem Sternenschiff tausende Lichtjahre von der Erde entfernt. Es passiert seit mehreren Tagen nichts Spannendes mehr, du gehst schon in dein Zimmer und willst den Tag beenden, doch auf einmal ertönt durch die Sprechanlage des Schiffs ein Alarm. Du läufst auf die Brücke. Dein Offizier teilt dir mit, dass 2 feindliche Schiffe auf dem Radar aufgetaucht sind.",
            "Du entscheidest dich, zu bleiben und zu kämpfen. Du gibst den Befehl, das Schiff in Angriffsposition zu bringen und sich auf den Feind vorzubereiten. Die Feindschiffe kommen näher und du kannst ihre Waffen auf dem Radar sehen. Der Kampf beginnt und es ist ein harter Kampf. Beide Seiten erleiden Verluste und das Schiff wird schwer beschädigt. Die verbliebene Energie reicht nicht mehr aus, um Schilde und Waffen gleichzeitig zu benützen. Du musst als Captain wieder eine wichtige Entscheidung treffen.",
            "Du entscheidest dich schließlich dafür, zu fliehen. Du gibst den Befehl, das Schiff in den Hyperraum zu bringen und die Flucht zu ergreifen. Dein Offizier arbeitet schnell und das Schiff springt in den Hyperraum. Ihr seid in Sicherheit, zumindest vorerst. Während des Fluges denkst du über die Situation nach. Du fragst dich, wer die feindlichen Schiffe waren und warum sie euch verfolgt haben. Du überlegst auch, wie ihr sicherstellen könnt, dass ihr in Zukunft besser vorbereitet seid, falls ihr erneut auf Feinde stoßt.",
            "Nach einem langen Schussaustausch taucht ein Schlachtschiff der Vulkanier aus dem Hyperraum auf. Sie erkennen sofort die Situation und schreiten zur Hilfe. Gemeinsam könnt ihr die feindlichen Schiffe in die Flucht schlagen. Das feindliche Schiff gibt auf und schaltet seine Schilde und Waffen aus.",
            "Ein Team von Vulkanischen Technikern und Ingenieuren hilft dir, dein Schiff wieder in Takt zu setzen. Du merkst, dass dein Hyperantrieb beschädigt ist und nur Minuten vor dem Explodieren ist. Du läufst zum evakuierten Maschinenraum, wo sich der Antrieb befindet und siehst 2 Knöpfe. Du weißt, dass einer der beiden Knöpfe den Hyperantrieb ausschaltet, doch du weißt nicht welcher.",
            "Da du des roten Knopfes des Hyperantriebs ausgeschalten hast, wird er sofort runtergefahren. Die Gefahr einer unkontrollierten Explosion ist vorerst vorüber. Du und deine Crew versucht für die nächsten Tage das Schiff zu reparieren.",
            "Die Reparatur Arbeiten sind fertig. Du setzt deine Reise zur Rettung der Wissenschaftler fort.Nach ein paar Tagen kommst du an den Planeten namens Boradis III an. Du versuchst aus dem Orbit den Aufenthaltsort der Wissenschaftler zu finden. Durch atmosphärische Störungen ist es schwierig.",
            "Die Teams beginnen mit der Suche der gestrandeten Wissenschaftler. Zwei Teams melden Angriffe durch unbekannte Lebewesen und werden sofort zurückgebeamt. Das letzte Team findet den Eingang einer Höhle, die tief in das Innere des Planeten zu führen scheint. Sie entscheiden sich für einen Abstieg, um weiter nach den verlorenen Wissenschaftler Ausschau zu halten. Das Team kommt zu einer Weggabelung.",
            "Sobald die Sonden die Oberfläche erreichen, werden sie von unbekannten Wesen angegriffen und zerstört.",
            "Das Team hat sich für den rechten Weg entschieden. Je tiefer sie hinabsteigen, desto heißer wird es. Sie sind erschöpft und am Ende ihrer Kräfte. Plötzlich werden sie von unbekannten Wesen angegriffen.",
            "Nach dem längeren Schussaustausch, bemerkt einer der Soldaten, dass die Höhle einzustürzen droht.",
            "Nach langer Suche findet das Außenteam schließlich die verlorenen Wissenschaftler. Sie wissen nicht, dass sie auf der Erde als verschollen gelten und weigern sich ihre Arbeit zu beenden. Das Team muss sie zur Aufgabe ihrer Arbeit überreden. Nach einigen Diskussionen erklären sie sich bereit, ihre Instrumente einzupacken und begeben sich mit Hilfe des Außenteams zurück zur Oberfläche. Dort angekommen kontaktieren sie das Schiff und lassen sich hochbeamen. Die Mission ist ein voller Erfolg.  Zuhause auf der Erde wird die Besatzung des Schiffes für ihre Heldentaten gefeiert und erhalten die „Christopher Pike Heldenmedaille“. Du als Captain freust dich aber auf die nächsten Abenteuer mit deinem Schiff und deiner Crew.  Well done, Commander!",
            "Game Over"
            
        ]

################################################################
# Die Fragen werden in einer 3-fach verschachtelten Liste gespeichert
# die erste Ebene der Liste ist der Index des Kapitels selbst
# die zweite Ebene ist die Liste der Antworten der Geschichte des Kapitels
# die dritte Ebene ist eine Antwort gemeinsam mit dem Index des nächsten Kapitels
################################################################
fragen = [ 
            [
                ["Du bleibst stehen und wartest bis die gegnerischen Schiffe in Feuerreichweite sind.","1"],
                ["Du versuchst zu fliehen.","2"]
            ],
            [
                ["Du leitest die ganze Energie zu den Waffen", "3"], 
                ["Du leitest die ganze Energie zu den Schilden", "12"]
            ],
            [
                ["Du schickst einen Notruf ab.", "3"], 
                ["Du entscheidest dich, den Hyperraumantrieb auszuschalten", "12"]
            ], 
            [
                ["Du zerstörst das Schiff und bittest die Vulkanier um Hilfe.", "4"], 
                ["Du beamst mit einem Team auf das andere Schiff und versuchst Informationen zu sammeln.", "12"]
            ],
            [
                ["Du drückst den roten Knopf", "5"], 
                ["Du drückst den grünen Knopf", "12"]
            ],
            [
                ["Du entscheidest dich, eines deiner Reparierkits aufzubrauchen", "6"], 
                ["Du behältst die Reparierkits für einen möglichen späteren Notfall auf", "12"]
            ],
            [
                ["Du stellst mehrere Teams zusammen und beamst die Teams auf den Planeten.", "7"], 
                ["Du sendest drei Sonden runter auf die Oberfläche des Planeten ", "8"]
            ],
            [
                ["Du wählst den rechten Weg.", "9"], 
                ["Du wählst den linken Weg.", "12"]
            ],
            [
                ["Schick eine weitere Sonde ", "8"], 
                ["Stelle 3 bewaffnete Rettungsteams zusammen und beam sie auf die Oberfläche. ", "7"]
            ],
            [
                [" Sie versuchen zu entkommen ", "11"], 
                ["Sie schießen zurück", "10"]
            ],
            [
                ["Sie Projizieren Hologramme von sich selbst und lenken dadurch die Gegner ab. Sie können jetzt ihren Weg fortsetzen. ", "11"], 
                ["Sie bleiben und feuern weiter auf ihre Gegner. ", "12"]
            ],
            [
                ["Deine Reise findet ein plötzliches Ende. Du bekommst einen Ehrenplatz in den Reihen der gefallenen Helden der Sternenflotte.","12"],
                ["dummy","12"]
            ]                        
        ]
################################################################
# Hilfsfunktion zur Darstellung von Story Kapitel
# Die Funktion nimmt die Nummer des Kapitels als Parameter
# und printet den Inhalt des Kapitels.
################################################################
def print_story(k):
    print(trennlinie*scree_width)
    print(f"\033[1mSzene {k+1}:\033[0m")
    # print(f"\033[5mKapitel {k+1}:\033[0m")
    print(story[k])
    print(trennlinie*scree_width)

################################################################
# Hilfsfunktion zu scannen der Umgebung
# Die Funktion nimmt die Nummer des Kapitels als Parameter
# und printet die Items aus der Liste "umgebung".
################################################################
def scan_umgebung(k):
    print(trennlinie*scree_width)
    if (len(umgebung[k])!= 0):

        eingabe=choose_element_from_list(umgebung[k])

        print(f"Du hast das Item {eingabe} gewählt.")
        
        ergebnis = add_to_inventory(k, int(eingabe)-1)

        # ergebnis ist -1, wenn Inventar voll war
        if(ergebnis==-1):
            print("Dein Inventar ist voll, du kannst ein Objekt wegwerfen, um Platz für Neues zu schaffen.")
            objekt_index=choose_element_from_list(inventar)
            result=remove_from_inventory(objekt_index)
            if(result != 0):
                print("Fehler beim Löschen des {objekt_index}-ten Elements aus dem Inventar")


    else:
        print("Deine Umgebung ist leider völlig leer ... so ist es meistens in Vakuum des Weltalls.")
    

################################################################
# Hilfsfunktion zur Verwaltung der Inventar
# Die Funktion hat den Index eines Items aus der aktuellen Umgebung als
# Parameter und fügt dieses der Inventarliste hinzu, sofern
# die Länge der Liste maximale_inventory_items nicht überschreitet.
# maximale_inventory_items is eine globale Grenze für die Anzahl der
# Items in Inventar
################################################################

def add_to_inventory(k, index):
    # wenn kein Platz im Inventar vorhanden ist, dann schreibe eine Fehlermeldung
    if(len(inventar) >= maximale_inventory_items):
        print(f"Inventar ist voll. Es sind nur {maximale_inventory_items} Objekte in Inventar erlaubt.")
        return -1
    else:
        inventar.append(umgebung[k].pop(index))
        return 0
################################################################
# Hilfsfunktion zur Enfernung von Objekten aus dem Inventar
################################################################

def remove_from_inventory(index):
    # wenn Inventar leer ist, dann schreibe eine Fehlermeldung
    index=int(index)

    if(len(inventar) == 0 ):
        print(f"Dein Inventar ist leer, deshalb kannst du nichts daraus entfernen.")
        return -1
    elif (index > len(inventar)):
        print(f"Der gegebene Index {index} ist größer als die Länge des Inventars.")
        return -2        
    else:
        inventar.pop(index)
        return 0


################################################################
# Hilfsfunktion zur Auswahl eines Elementes aus einer Liste
# Sie listet die Elemente der Liste auf und lässt den User ein Element auswählen
# und gibt den Index des Objektes zurück
# diese Funktion hat die Liste als Parameter
################################################################
def choose_element_from_list(liste):
    for i in range(len(liste)):
        print(f"[{i+1}] {liste[i]}")

    print("Wähle ein Objekt aus!")
    eingabe = ""
    while(not eingabe.isdigit()):
        
        eingabe = input()

        if(eingabe.isdigit()):
            if(int(eingabe)>len(liste)):
                print("Falsche Eingabe! Wähle eine Zahl zwischen [1] und [" + str(len(liste)) + "]:")
                # lösche falsche Benutzereingabe
                eingabe=""
        # wenn die Eingabe keine Zahl war, dann ist es ein Fehler
        else:
            print("Falsche Eingabe! Wähle eine Zahl, die zwischen [1] und [" + str(len(liste)) +"]: liegt.")
            # lösche falsche Benutzereingabe
            eingabe=""

    return eingabe


################################################################
# Hilfsfunktion zur Darstellung von Fragen
# Die Funktion nimmt die Nummer des Kapitels als Parameter
# und printet die Liste der Fragen des Kapitels und 
# parst die Antwort des Benutzers
################################################################
def print_fragen(k):

    ###########################################################
    # das ist nur eine Fehlerbehandlung für das letzte Kapitel 
    # wenn es keine Fragen mehr zu printen gibt.
    ###########################################################
    if(k==len(fragen)):
        return

        
    print("Wähle die gewünschte Antwort aus!")

    for j in range(len(fragen[k])):
        print("[" + str(j+1) + "] "+ fragen[k][j][0])
    
    print('[i] Inventar')
    print('[u] Umgebung Scannen')
    print('[q] Spiel beenden')
    print(trennlinie*scree_width)

    eingabe = ""
    while(eingabe not in ["1","2","i"]):
        eingabe = input()

        if eingabe == ('i'):
            print('inventar:')
            print(inventar)
            print(trennlinie*scree_width)
            print_fragen(k)
        elif eingabe == ('u'):
            print('Umgebung:')
            scan_umgebung(k)
            print(trennlinie*scree_width)
            print_fragen(k)
        elif eingabe in ["1","2"]:
            break
        elif eingabe == ('q'):
            quit()
        else:
            print("Falsche Auswahl: "+ eingabe)
            print("Die korrekte Wahl kann nur [1], [2], [i], [u] oder [q] sein. Versuche es nochmals.")
            print(trennlinie*scree_width)

    # die richtige Antwort wurde gelesen
    if (eingabe in ["1","2"]):
        # Achtung, Listen beginnen mit 0 als Index, deshalb "eingabe-1"
        j=int(eingabe)-1

        # hier wählen wir das nächste Kapitel aus
        next_step=int(fragen[k][j][1])
        kapitel(next_step)

################################################################
# Printe Kapitel 0
#
################################################################
def kapitel(k):
    print_story(k)
    print_fragen(k)

################################################################
# Start des Programms
################################################################
print(trennlinie*scree_width)
print(prolog)


kapitel(k=0)




