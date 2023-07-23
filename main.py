import sys
import os

# Определите путь к папке "lib" внутри вашего проекта
lib_dir = os.path.join(os.path.dirname(__file__), 'lib')

# Добавьте путь к модулям в папке "lib"
sys.path.append(lib_dir)

# Определите пути к другим зависимым модулям
other_module_dir = os.path.join(os.path.dirname(__file__), 'path_to_other_module')
sys.path.append(other_module_dir)

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from main_window import MainWindow


def main():
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
