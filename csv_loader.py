import threading
import time
import csv
import gi
from gi.repository import GLib

gi.require_version("Gtk", "3.0")


class CsvLoader(threading.Thread):
    def __init__(self, filename, callback):
        threading.Thread.__init__(self)
        self.filename = filename
        self.callback = callback

    def run(self):
        rows = []
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)

        GLib.idle_add(self.callback, rows)
