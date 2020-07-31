import os
import subprocess
import sys
import time


def notify(title, text):
    os.system(
        """osascript -e 'display notification "{}" with title "{}"'""".format(text, title))
    os.system('afplay /System/Library/Sounds/Submarine.aiff')


try:
    timeparts = int(input("Duur van leerperiode in minuten: "))
    pause = int(input("Duur van pauze in minuten: "))
    times = int(input("Aantal herhalingen voor het stopt: "))

    def studytime(timeparts, pause, times):
        notify("Begonnen", "Je leertijd gaat nu in")
        for i in range(times):
            time.sleep(timeparts)
            notify("Pauze",  "Er zijn {} min verstreken, tijd voor pauze".format(
                (timeparts/60)))
            time.sleep(pause)
            notify("Einde pauze", "Je pauze is voorbij, tijd om weer te leren")
            i+1
        notify("Goed bezig geweest",
               "Het leer programma dat je hebt ingesteld is afgelopen")

    studytime((timeparts * 60), (pause * 60), times)
except:
    notify("Error",
           "Er is een fout opgetreden, waarschijnlijk in je input, controleer alles en probeer het opnieuw")
