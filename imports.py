from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QDialog, QLabel, QWidget, QFileDialog
from PySide6.QtCore import Qt, QSize, QCoreApplication
from PySide6.QtGui import QPixmap, QCursor, QIcon, QImage
from ipokedex import Ui_pokedex
import sys, os, socket, io, database.db as db
from pokemon.pokemon import Pokemon as p
from type.type import Type as t
