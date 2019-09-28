"""
HEAVY METAL DETECTION BOTS
Author: Stefan Schneider
Github: StefSchneider

Lange galt das Periodensystem der Elemente als vollständig. Doch dann begannen Forscher, nach neuen Elementen zu suchen.
Und so schufen sie neue Elemente wie ...
Was sie nicht wussten: Unter der Erdoberfläche schlummerte noch ein weiteres außergewöhnliches Elemente: Lemmium.
Mit seiner Dichte von ... und ... gilt es als das schwerste jemals entdeckte Metall. Doch Lemmium ist rar und nur
schwer zu finden. Und so entwickelten die Forscher Bots, um das kostbare Metall zu finden - die Heavy Metal Dectection Bots,
kurz HMDB. Die HMDB agieren autark als Schwarm. Dabei folgende sie einfachen Regeln:
1. Bewege dich mit einem Schritt in eine der vier Richtungen vorne, hinten, links, rechts.
2. Halte stets Kontakt zu mindestens einem Nebenmann.
3. Werde umso langsamer, je mehr du dich dem Lemmium näherst.

"""

## project: Heavy Metal Detection Bots
## 10.8.2019 # 16:00 # A
## 10.8.2019 # 17:00 # E
## 12.8.2019 # 8:10 # A # create story
## 12.8.2019 # 8:20 # E
## 12.8.2019 # 19:10 # A
## 12.8.2019 # 21:00 # E
## 17.8.2019 # 17:15 # A
## 17.8.2019 # 17:55 # E
## 17.8.2019 # 22:20 # A # Classes Field and Area
## 17.8.2019 # 22:54 # E
## 18.8.2019 # 7:55 # A
## 18.8.2019 # 8:31 # E
## 18.8.2019 # 10:16 # A
## 18.8.2019 # 10:53 # E
## 18.8.2019 # 13:36 # A
## 18.8.2019 # 13:47 # E
## 18.8.2019 # 21:34 # A
## 18.8.2019 # 22:34 # E
## 19.8.2019 # 9:02 # A
## 19.8.2019 # 9:44 # E
## 19.8.2019 # 18:01 # A
## 19.8.2019 # 18:40 # E
## 20.8.2019 # 21:37 # A
## 20.8.2019 # 22:27 # E
## 21.8.2019 # 7:38 # A
## 21.8.2019 # 8:02 # E
## 21.8.2019 # 15:41 # A
## 21.8.2019 # 16:36 # E
## 21.8.2019 # 18:28 # A # Documentation
## 21.8.2019 # 19:12 # E
## 21.8.2019 # 21:32 # A
## 21.8.2019 # 21:51 # E
## 22.8.2019 # 9:15 # A
## 22.8.2019 # 9:35 # E
## 22.8.2019 # 15:21 # A
## 22.8.2019 # 16:13 # E
## 22.8.2019 # 18:16 # A
## 22.8.2019 # 19:01 # E
## 30.8.2019 # 8:47 # A
## 30.8.2019 # 10:58 # E
## 4.9.2019 # 7:37 # A
## 4.9.2019 # 8:25 # E
## 6.9.2019 # 7:27 # A
## 6.9.2019 # 8:18 # E
## 9.9.2019 # 7:49 # A # Refactoring
## 9.9.2019 # 8:19 # E
## 10.9.2019 # 8:04 # A # Refactoring
## 10.9.2019 # 8:25 # E
## 10.9.2019 # 15:22 # A
## 10.9.2019 # 16:00 # E
## 17.9.2019 # 7:40 # A
## 17.9.2019 # 8:41 # E
## 17.9.2019 # 14:27 # A
## 17.9.2019 # 14:51 # E
## 17.9.2019 # 17:00 # A
## 17.9.2019 # 17:25 # E
## 17.9.2019 # 18:55 # A # set rocks
## 17.9.2019 # 20:34 # E
## 18.9.2019 # 8:09 # A
## 18.9.2019 # 9:19 # E
## 20.9.2019 # 20:00 # A
## 20.9.2019 # 20:47 # E
## 21.9.2019 # 14:22 # A # Refactoring / Documentation
## 21.9.2019 # 15:14 # E
## 21.9.2019 # 16:58 # A # Refactoring / Documentation
## 22.9.2019 # 17:46 # E
## 22.9.2019 # 19:52 # A # Refactoring data structure ITEM_FORMS
## 22.9.2019 # 21:41 # E
## 24.9.2019 # 7:50 # A # Bot __init___
## 24.9.2019 # 8:23 # E
## 25.9.2019 # 19:45 # A
## 25.9.2019 # 21:18 # E
## 26.9.2019 # 20:13 # A
## 26.9.2019 # 20:32 # E
## 28.9.2019 # 16:57 # A # create Git repository




import numpy as np
import random
import sys
import pprint


# KONSTANTEN
"""
Konstanten werden verwendet, um schnelle Anpassungen für die Spielumgebung vornehmen zu können, beispielsweise die
Größe der Umgebung, die Größe der Feldformationen oder die Anzahl der Bots.
"""

INTRO_TEXT: str = ""
AREA_SIZE: list = [30, 30] # bestimmt, aus wie vielen Feldern die Spielumgebung besteht, x-, y-Wert
FIELD_SIZE: list = [10, 10] # bestimmt, aus wie vielen Zellen ein Feld besteht
CELL_SIZE: list = [1, 1] # bestimmt, aus wie vielen Parts eine Zelle besteht, dabei ist eine Zelle die kleinste Einheit
ROCK_NUMBER: int = 6 # Anzahl der Felsformationen, die in der Spielumgebung platziert werden
ITEM_FORMS: dict = {"Plain": {"string": "plain", # Kurzversion des Namens
                              "short": " ", # Eintrag, der auf dem Spielfeld angezeigt wird
                              "accessible": True, # Bot darf auf dem Item platziert werden (ja = True, nein = False)
                              "size": [1, 1], # Anzahl der Felder [x, y], die das Item umfasst
                              "min_size": [1, 1] # Minimale Größe [x, y], die das Item haben muss
                              },
                    "Rock": {"string": "rock",
                             "short": "R",
                             "accessible": False,
                             "size": [3, 3],
                             "min_size": [1, 1]
                             },
                    "Lemmium Light": {"string": "light",
                                      "short": "LL",
                                      "accessible": True,
                                      "size": [5, 5],
                                      "min_size": [5, 5]
                                      },
                    "Lemmium Medium": {"string": "medium",
                                       "short": "LM",
                                       "acccessible": True,
                                       "size": [3, 3],
                                       "min_size": [3, 3]
                                       },
                    "Lemmium Heavy": {"string": "heavy",
                                      "short": "LH",
                                      "accessible": True,
                                      "size": [1, 1],
                                      "min_size": [1, 1]
                                      }
                    }
BOT_NUMBER: int = 10 # Anzahl der Bots, die in der Spielumgebung platziert werden
BOT_SIZE: list = [2, 2] # Anzahl der Zellen, die ein Bot einnimmt.
BOT_VELOCITY: dict = {"normal": 10,
                      "medium": 5,
                      "slow": 3,
                      "stop": 0
                      } # Geschwindigkeit (Anzahl der Zellen), mit der sich ein Bot in den Feldern bewegt
BOT_SCAN_RADIUS: list = [10, 10]    # Anzahl der Zellen, die einen Bot umgibt. Mindestens eine Zelle soll sich mit den
                                    # Zellen des Nachbarn überschneiden
BOT_DIRECTIONS = {"up": [-1, 0], # [y, x]-Reihenfolge wg. numpy.ndarray
                  "down": [1, 0],
                  "left": [0, -1],
                  "right": [0, 1],
                  "none": [0, 0]
                  }

# VARIABLEN

bots: list = [] # Liste mit allen Bots
bots_on_lemmium: set = {}   # Sobald ein Bot ein Heavy-Lemmium-Feld erreicht hat, wird seine Nummer in die Menge
                            # aufgenommen. Falls die Länge dieser Menge der Anzahl der Bots entspricht, haben alle
                            # Bots Hevy Lemmium erreicht und die Suche ist beendet.


# KLASSEN

class Area:
    """
    Die Klasse Area steuert die gesamte Spielumgebung. Sie wird über die Methode __init__ erzeugt, anschließend
    werden über die Methode build alle Elemente wie Rocks oder Lemmium platzert.
    """

    def __init__(self, x_size: int, y_size: int):
        """
        :param x_size: Anzahl der Zellen in der Breite des Arrays
        :param y_size: Anzahl der Zellen in der Höhe des Arrays
        """
        self.x_size = x_size
        self.y_size = y_size
        self.area = np.ndarray(shape=(self.y_size, self.x_size), dtype=Cell) # Anlage des Arrays für Area

    def __str__(self):
        """
        :return: Symbol, das im Spielfeld für Objekte der Klasse Area eingetragen wird.
        """

        return "A"

    def __repr__(self):
        """
        :return: Wenn eine Instanz der Klasse aufgerufen wird, wird das Objekt zurückgegeben
        """

        return self.area

    def create(self, item_form: str)-> list:
        """
        Die Methode steuert, welches Element neu geschaffen werden soll. Dazu wird die jeweilige Methode aufgerufen
        :param item_form: Element, das neu geschaffen werden soll
        :return: Liste der Felder, die das neu geschaffene Element umfasst ([x, y], Kurzanzeige)
        """
        self.item_form = item_form
        fields: list = []
        if self.item_form == "Plain":
            fields = self.create_plain()
        elif self.item_form == "Rock":
            fields = self.create_rock()
        elif self.item_form == "Lemmium":
            fields = self.create_lemmium()

        return fields

    def create_plain(self)-> list:
        """
        Bei Plain handelt es sich um ein leeres Feld, d.h. es kann anschließend mit beliebigen Items oder Bots
        überschrieben werden. Da mit der Methode build durch Plain die initiale Befüllung der gesamten Spielumgebung
        vorgenommen wird, kann der Startpunkt für Plain immer auf [0, 0] gesetzt werden.
        :return: Liste der Felder, die mit einer Instanz der Klasse Plain gefüllt werden sollen
        """
        plain_fields: list = [([0, 0], "Plain")]

        return plain_fields

    def create_rock(self)-> list:
        """
        Die Methode baut ein Element der Gruppe Rock (Klasse Item) auf. Um eine unterschiedliche Größe und Struktur
        des einzelnen Rock-Elements werden aus der Liste mit allen Feldern per Zufallsgenerator wieder Felder gelöscht.
        :return: Liste aller Felder, die das einzelne Rock-Element umfassen soll ([x, y], Kurzanzeige).
        """
        rock_fields: list = []
        for x in range(ITEM_FORMS["Rock"]["size"][0]):
            for y in range(ITEM_FORMS["Rock"]["size"][1]):
                rock_fields.append(([x, y], "Rock"))
        number_delete_fields: int = random.randint(0, ITEM_FORMS["Rock"]["size"][0]*ITEM_FORMS["Rock"]["size"][1]-
                                                   ITEM_FORMS["Rock"]["min_size"][0]*ITEM_FORMS["Rock"]["min_size"][1])
        for i in range(number_delete_fields): # löscht einzelne Felder aus der Rock-Liste anhand von Zufallszahlen
            number_rock_fields = len(rock_fields)
            rock_fields.pop(random.randint(0, number_rock_fields-1))

        return rock_fields

    def create_lemmium(self)-> list:
        """
        Ein Lemmium-Feld besteht aus drei Komponenten: Lemmium-Light-Felder, Lemmium-Medium-Felder und mindestens
        einem Lemmium_Heavy-Feld. Die Größe jeder Komponente ist in den Konstanten (ITEM_FORMS) festgehalten. Die
        Komponenten haben Auswirkungen auf das verhalten der Bots. Das Lemmium-Feld wird von außen nach innen aufgebaut:
        Zunächst wird das Lemmium-Feld komplett mit Lemmium-Light-Feldern bestückt. Danach wird der Startpunkt für
        die Lemmium-Medium-Felder innerhalb des Lemmium-Feldes ermittelt. Die Lemmium-Light-Felder, die in Lemmium-
        Medium-Felder umgewandelt werden, werden aus der Gesamtliste entfernt, die Lemmium-Medium-Felder an die Liste
        angehangen. Das gleiche geschieht mit den Lemmium-Heavy-Feldern.
        Beispieldarstellung: Lemmium Light [5, 5], Lemmium Medium [3, 3], Lemmium Heavy [1, 1]
        ------------------------------------
        |light |light |light |light |light |
        ------------------------------------
        |light |medium|medium|medium|light |
        ------------------------------------
        |light |medium|heavy |medium|light |
        ------------------------------------
        |light |medium|medium|medium|light |
        ------------------------------------
        |light |light |light |light |light |
        ------------------------------------
        :return: Liste alle Felder, die das Lemmium-Feld umfasst ([x, y], Kurzanzeige)
        """
        lemmium_fields: list = [] # Liste aller Felder, die das gesamte Lemmium-Feld umfasst
        # initiales Befüllen mit Lemmium-Light-Feldern
        for x in range(ITEM_FORMS["Lemmium Light"]["size"][0]):
            for y in range(ITEM_FORMS["Lemmium Light"]["size"][1]):
                lemmium_fields.append(([x, y], ITEM_FORMS["Lemmium Light"]["short"]))
        # Aufnahme der Lemmium-Medium-Felder in die Liste durch Austausch entsprechender Lemmium-Light-Felder
        start_lemmium_medium: list = [int(ITEM_FORMS["Lemmium Light"]["size"][0]/
                                          ITEM_FORMS["Lemmium Medium"]["size"][0]),
                                      int(ITEM_FORMS["Lemmium Light"]["size"][1]/
                                          ITEM_FORMS["Lemmium Medium"]["size"][1])]
        for x in range(start_lemmium_medium[0], start_lemmium_medium[0]+ITEM_FORMS["Lemmium Medium"]["size"][0]):
            for y in range(start_lemmium_medium[1], start_lemmium_medium[1]+ITEM_FORMS["Lemmium Medium"]["size"][1]):
                lemmium_fields.remove(([x, y], "LL"))
                lemmium_fields.append(([x, y], ITEM_FORMS["Lemmium Medium"]["short"]))
        # Aufnahme der Lemmium-Heavy-Felder in die Liste durch Austausch entsprechender Lemmium-Medium-Felder
        start_lemmium_heavy: list = [int((ITEM_FORMS["Lemmium Light"]["size"][0]/
                                          ITEM_FORMS["Lemmium Heavy"]["size"][0]/2)),
                                     int((ITEM_FORMS["Lemmium Light"]["size"][1]/
                                          ITEM_FORMS["Lemmium Heavy"]["size"][1]/2))]
        for x in range(start_lemmium_heavy[0], start_lemmium_heavy[0]+ITEM_FORMS["Lemmium Heavy"]["size"][0]):
            for y in range(start_lemmium_heavy[1], start_lemmium_heavy[1]+ITEM_FORMS["Lemmium Heavy"]["size"][1]):
                lemmium_fields.remove(([x, y], "LM"))
                lemmium_fields.append(([x, y], ITEM_FORMS["Lemmium Heavy"]["short"]))

        return lemmium_fields

    def fill_fields(self, fields_in: list, item_form: str):
        """
        Füllt alle Zellen der als Parameter übertragenen Felder mit dem angegebenen Element.
        :param list_of_fields: Liste aller Felder [x, y], die mit der entsprechenden Element gefüllt werden sollen
        :param form: Element, das auf den Feldern platziert werden soll
        """
        self.fields_in = fields_in
        self.item_form = item_form
        for fields in self.fields_in:
            x_start = fields[0]*FIELD_SIZE[0]
            y_start = fields[1]*FIELD_SIZE[1]
            for x in range(x_start, x_start+FIELD_SIZE[0]):
                for y in range(y_start, y_start+FIELD_SIZE[1]):
                    self.area[y, x] = Item(self.item_form)

    def field_complete_empty(self, field: list)-> bool:
        """
        Überprüft, ob alle Zellen eines Feldes mit Plain belegt sind und dadurch für andere Elemente genutzt werden
        können. Dazu wird das entsprechende Feld aus dem Array kopiert und Zelle für Zelle überprüft.
        :param field: [x, y]-Position des Feldes
        :return: Wahrheitswert, ob alle Zellen des Feldes leer sind.
        """
        self.field = field
        field_empty: bool = False
        x_start: int = self.field[0]*FIELD_SIZE[0]
        y_start: int = self.field[1]*FIELD_SIZE[1]
        for x in range(x_start, x_start+FIELD_SIZE[0]):
            for y in range(y_start, y_start+FIELD_SIZE[1]):
                if str(self.area[y, x]) == ITEM_FORMS["Plain"]["short"]:
                    field_empty = True
                else:
                    field_empty = False
                    break

        return field_empty

    def determine_start_point(self, fields_in: list, item_form: str)-> list:
        """
        Ermittelt einen geeigneten Startpunkt [x, y] für ein Element, indem solange per Zufallsgenerator ein Startpunkt
        ermittelt und überprüft werden, ob damit in die Spielumgebung passt, bis der Startpunkt gefunden ist.
        :param input_list: Liste der Felder, die das Element umfasst
        :return: [x, y]-Werte des geeigneten Startpunkts
        """
        self.fields_in = fields_in
        self.item_form = item_form
        item_fits: bool = False
        start_field: list = []
        while item_fits == False:
            start_field = [random.randint(0, AREA_SIZE[0]-ITEM_FORMS[self.item_form]["size"][0]),
                           random.randint(0, AREA_SIZE[1]-ITEM_FORMS[self.item_form]["size"][1])]
            for field in self.fields_in:
                if self.field_complete_empty([field[0]+start_field[0], field[1]+start_field[1]]) == True:
                    item_fits = True
                else:
                    item_fits = False
                    break

        return start_field

    def build(self):
        """
        Nachdem über die Methode __init__ das Spielfeld als Array angelegt wurde, wird die Spielumgebung in mehreren
        Schritten aufgebaut:
        1. Füllen aller Zellen mit Plain
        2. Platzierung der Felder für Lemmium
        3. Platzierung der Felder für Rocks
        4. Platzierung der Bots
        """
        # 1. Füllen aller Zellen mit Plain
        all_cells: list = []
        start_field: list = self.create("Plain")[0][0] # zieht nur die Liste mit dem x-/y-Element aus der Liste
        for x in range(AREA_SIZE[0]): # Füllt alle Zellen initial mit Objekt der Klasse Item(Plain)
            for y in range(AREA_SIZE[1]):
                all_cells.append([x+start_field[0], y+start_field[1]])
        self.fill_fields(all_cells, "Plain")
        # 2. Platzierung der Felder für Lemmium
        lemmium_fields_all_data = self.create("Lemmium")
        lemmium_light_fields: list = []
        lemmium_medium_fields: list = []
        lemmium_heavy_fields: list = []
        for fields in lemmium_fields_all_data:
            if fields[1] == "LL":
                lemmium_light_fields.append(fields[0])
            elif fields[1] == "LM":
                lemmium_medium_fields.append(fields[0])
            elif fields[1] == "LH":
                lemmium_heavy_fields.append(fields[0])
        start_field = self.determine_start_point(lemmium_light_fields, "Lemmium Light")
        for i, field in enumerate(lemmium_light_fields):
            lemmium_light_fields[i] = [field[0]+start_field[0], field[1]+start_field[1]]
        self.fill_fields(lemmium_light_fields, "Lemmium Light")
        for i, field in enumerate(lemmium_medium_fields):
            lemmium_medium_fields[i] = [field[0]+start_field[0], field[1]+start_field[1]]
        self.fill_fields(lemmium_medium_fields, "Lemmium Medium")
        for i, field in enumerate(lemmium_heavy_fields):
            lemmium_heavy_fields[i] = [field[0]+start_field[0], field[1]+start_field[1]]
        self.fill_fields(lemmium_heavy_fields, "Lemmium Heavy")
        # 3. Platzierung der Felder für Rocks
        for rock_numbers in range(ROCK_NUMBER):
            rock_fields_split: list = []
            rock_fields_all_data = self.create("Rock")
            for fields in rock_fields_all_data: # zieht nur die x-/y-Elemente aus der Liste
                rock_fields_split.append(fields[0])
            start_field = self.determine_start_point(rock_fields_split, "Rock")
            rock_fields: list = []
            for field in rock_fields_split:
                    rock_fields.append([field[0]+start_field[0], field[1]+start_field[1]])
            self.fill_fields(rock_fields, "Rock")
        # 4. Platzierung der Bots

    def line_content(self, line: list)-> str:
        """
        Die Methode baut eine einzelne Zeile aus dem Spielumgebungsarray eine Zeile mit vertikalen Trennstrichen auf.
        Die Platzierung dieser Trennstriche hängt von der Breite von Field (FIELD_SIZE[0] ab. Die Einträge pro Zelle
        werden auf 2 Stellen begrenzt und linksbündig angezeigt. Gleichzeitig wird weitere Leerzeile zur besseren
        Abgrenzung eingefügt.
        :param line: Zeile aus dem Array, die umgewandelt werden soll.
        :return: out_line: komplette Zeile mit Inhalt und Trennern
        """
        divider: str = "|"
        out_line: str = ""
        self.line = line
        for i,v in enumerate(self.line):
            if i%FIELD_SIZE[0] == 0:
                out_line += divider + " "
            out_line += str(self.line[i])[:2].ljust(3, " ")
        out_line += divider

        return out_line

    def line_divider(self)-> str:
        """
        Die Methode baut eine Trennlinie zusammen, die genauso lang ist wie die Zeile für den Inhalte. Wann ein Kreuz
        gesetzt wird, hängt von der Breite der Klasse Field ab (FIELD_SIZE[0])
        :return: komplette erzeugte Trennlinie
        """
        divider: str = "--"
        cross: str = "+"
        out_divider: str = ""
        for i in range(self.area.shape[1]): # Länge der Linie
            if i%FIELD_SIZE[0] == 0: # setzt ein Kreuz in Abhängigkeit der Feldbreite
                out_divider += cross + " "
            out_divider += divider + " "
        out_divider += cross

        return out_divider

    def fullprint(self):
        """
        Das gesamte Array soll in der richtigen Form auf dem Bildschirm ohne Zeilenumbrüche angezeigt werden. Dazu
        werden die Methoden line_content (liefert die Inhalte einer einzelnen Zeile) und line_divider (baut eine
        Trennlinie) aufgerufen.
        """
        for i in range(self.area.shape[0]):
            if i%FIELD_SIZE[1] == 0:
                print(self.line_divider())
            print(self.line_content(self.area[i]))
        print(self.line_divider())


class Field:
    """

    """

    def __init__(self):
        """

        """
        pass

    def __str__(self):
        """

        :return:
        """
        pass

    def __repr__(self):
        """

        :return:
        """
        pass


class Cell:
    """

    """

    def __init__(self):
        """

        """
        pass


class Item:
    """
    Erzeugt neue Elemente für das Spielfeld wie Rocks oder Lemmium.
    """

    def __init__(self, item_form: str):
        """
        :param item_form: Name des Elements, das erzeugt werden soll
         """
        self.item_form = item_form


    def __str__(self):
        """
        :return: Symbol, das im Spielfeld für das Objekte der Klasse Item eingetragen wird.
        """

        return ITEM_FORMS[self.item_form]["short"]

    def __repr__(self):
        """
        :return: Wenn eine Instanz der Klasse aufgerufen wird, wird das Objekt zurückgegeben
        """

        return self.object


class Bot:
    """

    """
    id: int = 0
    bot_cells: list = []    # Liste der Zellen, die der einzelne Bot belegt. Muss außerhalb der __init__-Methode stehen,
                            # da sie regelmäßig angepasst werden muss.
    bot_directions: list = list(BOT_DIRECTIONS.keys()) # ermittelt aus der Konstanten die möglichen Richtungen
    overlap_cells: int = 0 # Anzahl der Zellen, die sich der Bot mit anderen Bots überschneidet

    def __init__(self):
        """

        """
        # initiales Befüllen mit Bot-Zellen
        for x in range(BOT_SCAN_RADIUS[0]):
            for y in range(BOT_SCAN_RADIUS[1]):
                bot_cells(([x, y], "1"))
        # Aufnahme der Lemmium-Medium-Felder in die Liste durch Austausch entsprechender Lemmium-Light-Felder
        start_bot_core: list = [int((BOT_SCAN_RADIUS[0]-BOT_SIZE[0])/2), int((BOT_SCAN_RADIUS[1]-BOT_SIZE[1])/2)]
        for x in range(start_bot_core[0], start_bot_core[0]+BOT_SIZE[0]):
            for y in range(start_bot_core[1], start_bot_core[1]+BOT_SIZE[1]):
                bot_cells.remove(([x, y], "1"))
                bot_cells.append(([x, y], "B"))

    def __str__(self):
        """

        :return:
        """

    def __repr__(self):
        """

        :return:
        """

    def drop(self):
        """
        Sucht eine passende Stelle für den Bot auf dem Spielfeld und platziert ihn dort.
        Überprüfen: Kann sich der Bot anschließend in eine Richtung bewegen oder stößt er rundherum auf Hindernisse?
        Dann muss eine neue Stelle für den Bot gesucht werden
        :return:
        """
        pass

    def find_direction(self) -> complex:
        """
        Mit der Methode wird eine Richtung ermittelt, in die sich der jeweile Bot bewegen kann. Das geschieht unter
        Berücksichtgung der jeweiligen Regeln:
        a) muss in der Nähe mindestens eines Nachbarn bleiben
        b) muss Hindernisse berücksichtigen
        return: Richtung, in die sich der jeweilige Bot bewegen soll (komplexe Zahl)
        """
        direction: complex = 0+0j

        return direction

    def move_to(self)-> bool:
        """
        Die Methode greift das Ergebnis der Methode find_direction auf und bewegt den Bot in die vorgegebene Richtung
        in der Spielumgebung.
        return: Sobald der Bot ein Feld mit Heavy Lemmium gefunden hat, wird der Wert für reached_heavy_lemmium auf
        True gesetzt. Mit dem Kennzeichen kann gesteuert werden, ob der Bot dann für weitere Bewegungen ausscheidet.
        Zudem kann die Bot-Nummer in eine Mengen-Variable aufgenommen werden. Ist len(Menge= gleich der Anzahl der
        Bots, müssen sie alle auf einem Heavy-Lemmium-Feld stehen
        """

        reached_heavy_lemmium: bool = False

        return reached_heavy_lemmium


class Gui:
    """

    """

    def __int__(self):
        """

        :return:
        """
        pass


# HAUPTPROGRAMM

area = Area(AREA_SIZE[0]*FIELD_SIZE[0]*CELL_SIZE[0], AREA_SIZE[1]*FIELD_SIZE[1]*CELL_SIZE[1])
area.build()
area.fullprint()
