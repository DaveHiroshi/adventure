# Weltraum rettung, ein Text-Adventure

## Einleitung

Weltraum rettung is ein Text-Adventure Spiel, das vollständig in Python programmiert wurde.
Wie üblich für Text basierten Adventure Spiele besteht dieses Spiel aus einzelnen Szenen, die dem
Spieler schrittweise vorgestellt werden. Nach jeder Szene erhält der Spieler eine gewisse Anzahl von 
Auswahlmöglichkeiten, aus denen er jeweils eine wählen kann. Seine Entscheidung bestimmt die Wahl der 
nächsten Szene.

Um genau dieses Prinzip möglichst einfach umzusetzen, wurden alle Szenen in einer Liste gespeichert.
Die jeweiligen Fragen wurden ebenfalls in einer Liste gespeichert. 
Die Liste der Fragen ist eine 3-fach verschchtelte Liste. 

1. Die erste Ebene ist der Index der zugehörigen Szene.
2. Die zweite Ebene beinhaltet die Liste der Antworten
3. Die dritte Ebene beinhaltet zwei Elemente: die Frage und den Index der zugehörigen **Zielszene**.


In einem abstrakten Modell stellen die Geschichte und die Fragen (Wahlmöglichkeiten) einen gerichteten 
Graphen dar. Dieser besteht aus den Szenen als Knoten und die Antworten als Kanten. 
Diese Vorgehensweise eliminiert die Notwendigkeit von komplexen, verschachtelten IF Anweisungen und
vereinfacht zugleich die interne Darstellung des **Handlugsgraphen**. 
Desweiteren lässt sich die Geschichte umgestalten oder gar vollständig umschreiben, 
ohne den Code verändern zu müssen.


## Code Dokumentation
Im folgenden werden alle Datenstrukturen und Funktionen beschrieben. Eine kurze Erkläung der Funktionsweise soll dabei das Lesen des Source Code vereinfachen.

### Datenstrukturen
In diesem Kapitel beschreiben wir die verwendeten Datenstrukturen. In diesem Programm werden nur Listen verwendet. Diese sind aber wen notwendig auch verschachtelt, also eine Liste von Listen.

_________________________________
#### story:
Die Story ist eine Liste, die die Szenen des Spiels beinhaltet. Sie hat insgesamt 13 Elemente. Die ersten 12 sind die Szenen des Spiels und das 13. Element ist die Endszene.


```python
story = [ 
            "Du bist auf einer lang ...",
            "Du entscheidest dich, zu bleiben ...",
			 ... ,
			 ... ,
			 ...            
        ]
```

_________________________________
#### Fragen:
Die Liste der Fragen ist eine verschachtelten Struktur mit dem Namen **fragen**. 

Die Ebenen haben jeweils die folgende Bedeutung:

1. Die erste Ebene ist der Index der zugehörigen Szene.
2. Die zweite Ebene beinhaltet die Liste der Antworten
3. Die dritte Ebene beinhaltet zwei Elemente: die Frage und den Index der zugehörigen Zielszene bei der Wahl dieser Antwort.


```
fragen = [ 
            [
                ["Du bleibst stehen und wartest bis die ...","1"],
                ["Du versuchst zu fliehen.","2"]
            ],
            ...,
            ...
]
```

_________________________________
#### Inventar:
Eine am Anfang des Spieles leere Liste namens **inventar** , die zur Speicherung der Objekte dient, die der Spieler während des Spiels sammeln in verschiedenen Szenen kann.

```python
inventar = []
```

_________________________________
#### Umgebung:
Die Variable **umgebung** hält die Objekte der jeweiligen Szene fest. 
Sie ist ebenfalls verschechtelt und beihaltet pro Szene eine Liste der in dieser Szene vorhandenen Objekte.

```
mgebung = [
	[],
	['Asteroid abbauen', 'Schiffswrack'],
	['Phaser', 'Phaser', 'Sonde', 'Reperatur Kit'],
	...,
	...
]
```


### Funktionen
Im folgenden Abschnitt werden alle Funktionen, ihre Parameter und deren Ausgaben beschrieben.

_________________________________

#### print_story:
Die Funktion **print_story(k):** stellt den Inhalt des k-ten Kapitels in der Konsole dar.
Sie nimmt die Ganzzahl **k** als Eingangsparameter und gibt mittels der Python Funktion **print()** den Inhalt der Liste **story** mit dem Index **k** in der Konsole aus.


_________________________________
#### print_fragen
Die Funktion **print_fragen** nimmt ebenfalls den Index eines Kapitels in Form einer Ganzzahl **k** als Parameter entgegen und gibt die zu diesem Kapitel gehörigen Fragen aus der Liste der **fragen** in der Konsole aus. Außerdem printet sie die Standardaktionen, wie **[i]** Inventory, **[u]** Scann Umgebung und **[q]** Spiel beenden .

Danach wird der Spieler um seine Wahl gebeten. Diese Wahl muss entweder einer der Standardaktionen entsprechen oder aus der Liste der möglichen Antworten des aktuellen Kapitels sein. 

Ist das nicht der Fall, wird dem Spieler eine **Fehlermeldung** (*Die korrekte Wahl kann nur ... oder [q] sein. Versuche es nochmals*)  gezeigt und nach der nochmaligen Ausgabe der aktuellen Auswahlmöglichkeiten nochtmals um eine gültige Antwort gebeten.











