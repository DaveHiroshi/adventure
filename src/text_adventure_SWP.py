import os

os.system('cls')
print('Willkommen,')


trennlinie="------------------------------"
################################################################
# Liste des Inventars
################################################################
inventar = []

umgebung = [
                [],
                [],
                ['[1] Asteroid abbauen', '[2] Schiffswrack'],
                ['[1] Phaser', '[2] Phaser', '[3] Sonde', '[4] Reperatur Kit'],
                [],
                [],
                [],
                ['[1] Gold', '[2] Diamant'],
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
    print("=============================================")
    print(story[k])
    print("=============================================")

################################################################
# Hilfsfunktion zur Darstellung von Fragen
# Die Funktion nimmt die Nummer des Kapitels als Parameter
# und printet die Liste der Fragen des Kapitels und 
# parst die Antwort des Benutzers
################################################################
def print_fragen(k):
    if(k==len(fragen)):
        return
        
    print("Wähle die gewünschte Antwort aus!")

    for j in range(len(fragen[k])):
        print("[" + str(j+1) + "] "+ fragen[k][j][0])
    
    print('[i] Inventar')
    print('[u] Umgebung Scannen')

    eingabe = ""
    while(eingabe not in ["1","2","i"]):
        eingabe = input()

        if eingabe == ('i'):
            print('inventar:')
            print(inventar)
            print(trennlinie)
            print_fragen(k)
        elif eingabe == ('u'):
            print('Umgebung:')
            print_umgebung(k)
            print(trennlinie)
            print_fragen(k)
        elif eingabe in ["1","2"]:
            break
        else:
            print("Falsche Auswahl: "+ eingabe)
            print("Die korrekte Wahl kann nur [1], [2] oder [i] sein. Versuche es nochmals.")
            print("-----------------------------------------------------------------------.")

    # die richtige Antwort wurde gelesen
    if (eingabe in ["1","2"]):
        j=int(eingabe)-1

        # hier wählen das nächste Kapitel aus
        next_step=int(fragen[k][j][1])
        kapitel(next_step)

def print_umgebung(k):
    print(umgebung[k])

################################################################
# Printe Kapitel 0
#
################################################################
def kapitel(k):
    # print(f">>>>>>> kapitel called with k={k}")
    print_story(k)
    print_fragen(k)

################################################################
# Start des Programms
################################################################

kapitel(k=0)



