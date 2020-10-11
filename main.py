import json
import re
import sys
import os
from CalculatorBase import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

############################ Consts ############################
HTMLOPENER = '<html><head/><body><p align="center"><span style=" font-size:9pt;">showing results for Molecule/Element : </span>'
HTMLCLOSE = '</p></body></html>'
MOLES = 1
GRAMS = 2
MASS = 3

############################ Miscs ############################
def resource_path(relative_path):
    """ Get absolute path to resource, used for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

############################ Engine ############################
# Basic element class represents one atom from the periodic table
class Element:
    def __init__(self, atomic_number, molaric_mass, symbol, repeat = 1):
        """
        Constructor
        :param atomic_number: The atomic number as presents in the period tabel
        :param molaric_mass: The molar mass as presents in the period tabel
        :param symbol: The symbol as presents in the period tabel
        :param repeat: Use if we want to contruct a mulecute containing only <symbol>X<repeat> times
        """
        self.atomic_number = atomic_number
        self.molaric_mass = molaric_mass
        self.repeat = repeat
        self.symbol = symbol

    def mol_calc(self, grams):
        """
        Calculate how much moles you have with the given grams of the element
        :param grams: The amount of grams wanted for the calculation
        :return: Number of moles
        """
        if self.molaric_mass == 0:
            return 0
        return grams/self.molaric_mass

    def set_repeatance(self, repeat):
        """
        Sets repeatance from outside the constructor
        :param repeat: The new 'repeat' value
        """
        self.repeat = repeat

# Molecule class represents a number of elements combined
class Molecule:
    def __init__(self, elements):
        """
        Constructor
        :param elements: An array of elements
        """
        self.elements = elements

    def molaric_mass(self):
        """
        Calculates the molar mass of the molecule
        :return: The molar mass in gr/mole
        """
        overall_mass = 0
        for element in self.elements:
            overall_mass += (element.molaric_mass * float(element.repeat))
        return overall_mass

    def mol_calc(self, grams):
        """
        Calculate how much moles you have with the given grams of the molecule
        :param grams: The amount of grams wanted for the calculation
        :return: Number of moles
        """
        mass = self.molaric_mass()
        if mass == 0:
            return 0
        return grams / mass

    def gram_calc(self, mol):
        """
        Calculate the mass of <mol> amount of the molecule
        :param grams: The amount of grams wanted for the calculation
        :return: The mass in grams
        """
        mass = self.molaric_mass()
        if mass == 0:
            return 0
        return mol * mass

# The main class of the calculations engine. used mainly for creating molecule from plain text
class PeriodicTable():
    def __init__(self, path):
        """
        Constructor
        :param path: A path to the periodic table data json file
        """
        with open(path) as json_file:
            self.data = json.load(json_file)

    def find_element(self, symbol):
        """
        Used to create new instance of Element class from the data. The search is using the symbol input
        :param symbol: The symbol of the desired element
        :return: New Element instance with the wanted data. None if could not find it
        """
        i = 0
        ret_val = None
        for element in self.data['elements']:
            if element['symbol'] == symbol:
                ret_val = Element(element['number'], element['atomic_mass'], symbol)
        if not ret_val:
            print('Cant find element with the symbol ' + '"' + symbol + '"')
        return ret_val

    def text_to_molecule(self, text):
        """
        The main function of the class. using other functions of the class to create a molecule from plain text.
        For example, if the user give an input of "H2OCl3", then the function
        returns a molecule with the elements H,O,Cl with the needed repeatency
        :param text: The molecule in the format <SYMBOL<repeatece>SYMBOL<repeatece>SYMBOL<repeatece>...>
        :return: Instance of the molecule class with the corresponding elements and repeatence
        """
        elements = []
        # Regexp to catch all the Capital letter starting words. (negative effect
        # is campturing spaces aswell, and we will deal with it later)
        # For example, if the input is SeanIsVeryStrong, the regex will find
        # Sean,Is,Very,Strong
        for item in re.findall('[A-Z][^A-Z]*', text):
            # Trim all white spaces from the item. For example, if the item is
            # "H    2   O    4   Cl 1" the result is "H2O4Cl1"
            no_spaces_item = re.sub(r'\s+','',item)
            ele = self.create_element_with_repetance(no_spaces_item)
            if(ele):
                elements.append(ele)
            else:
                return None
        if not elements:
            return None
        return Molecule(elements)

    def create_element_with_repetance(self, text):
        """
        Creating element from plain text. for example if the input is "H6",
        then the fucntion returns Element instance with symbol of H and repeatence of 6
        :param text: An element in the format SYMBOL<repeatece>
        :return: The element matches the input
        """
        # Regexp to capture pairs of letter and number
        reg = re.search(r'(\D+)(\d+)', text)
        element = None
        if reg:
            element = self.find_element(reg.group(1))
            if element:
                element.set_repeatance(reg.group(2))
        else:
            element = self.find_element(text)
        return element

############################ Qt ############################
def error_alert(msg):
    """
    Constructs a quick error pop-up window to alert the user beacuse some error occurd
    :param msg: The massage on the error pop-up window
    """
    alert = QMessageBox()
    alert.setWindowTitle("ERROR")
    alert.setText(msg)
    alert.exec_()


def html_normal_text_gen(text):
    """
    Used for the html format type of the top "showing results to" label.
    :param text: The symbol of the element for example, for the element H4, the input is H
    :return: Hard-coded html string with the input text
    """
    return '<span style="font-size:9pt;">' + text + '</span>'

def html_sub_text_gen(text):
    """
    Used for the html format type of the top "showing results to" label.
    :param text: The symbol of the element for example, for the element H4, the input is 4
    :return: Hard-coded html string with the input text with sub notation
    """
    return '<span style="font-size:9pt;vertical-align:sub;">' + text + '</span>'


# The main window of the app. Inherits from QDialog
class Calculator(QDialog):
    def __init__(self, parent=None):
        """
        Constructor. Sets up the ui and all the initializing steps
        :param parent: Parent widget of this widget
        """
        super(Calculator, self).__init__()
        # Setup the ui
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Initialize members that are not ui-related
        self.periodic_table = PeriodicTable(resource_path('Cdata/PeriodicTableJSON.json'))
        self.calc_mode = MOLES
        # Initializations of the window and the ui elements
        self.ui.screen.display(0)
        self.ui.comboBox.currentTextChanged.connect(self.selected_calc_changed)
        self.ui.showing_results_label.setText('')
        self.ui.calculate_btn.clicked.connect(self.calculate)
        self.ui.clear_btn.clicked.connect(self.clear_calculator)
        self.ui.exit_btn.clicked.connect(self.exit_calculator)
        self.ui.comboBox.addItem('Molar mass (gr/mole)')
        self.setWindowTitle("Chemistry Calculator")
        icon = QIcon(resource_path('icons/mainIcon.png'))
        self.setWindowIcon(icon)
        self.setWindowFlags(
            Qt.WindowTitleHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowMinimizeButtonHint |
            Qt.MSWindowsFixedSizeDialogHint
        )

    def calculate(self):
        """
        Slot for calculate button. When called, calaculates what is needed from the fields in the ui
        """
        user_molecule_text = self.ui.molecule_line_edit.text()
        if not user_molecule_text:
            error_alert('Please enter a Molecule/Element')
            return
        user_molecule = self.periodic_table.text_to_molecule(user_molecule_text)
        if not user_molecule:
            error_alert('Cant find Molecule/Element ' + '"' + user_molecule_text + '"')
            return
        if not self.calc_mode == MASS:
            try:
                user_calc_param = float(self.ui.calc_param_line_edit.text())
            except ValueError:
                error_alert('Please enter a number in the input parameter')
                return
        if self.calc_mode == MOLES:
            self.ui.screen.display(user_molecule.mol_calc(user_calc_param))
        if self.calc_mode == GRAMS:
            self.ui.screen.display(user_molecule.gram_calc(user_calc_param))
        if self.calc_mode == MASS:
            self.ui.screen.display(user_molecule.molaric_mass())
        text = HTMLOPENER
        for element in user_molecule.elements:
            repeatance = int(element.repeat)
            text += html_normal_text_gen(element.symbol)
            if repeatance > 1:
                text += html_sub_text_gen(str(repeatance))
        text += HTMLCLOSE
        self.ui.showing_results_label.setText(text)

    def selected_calc_changed(self, text):
        """
        Slot invoked when user change value in the comboBox.
        Adjasting the ui according to the new value.
        :param text: The new value of the comboBox
        """
        if 'Moles' in text:
            self.calc_mode = MOLES
            self.ui.input_asker.setDisabled(False)
            self.ui.calc_param_line_edit.setDisabled(False)
            self.ui.input_asker.setText(
                '<html><head/><body><span style=" font-size:14pt;">How many grams do you have?</span></p></body></html>')
        if 'Mass (gr)' in text:
            self.calc_mode = GRAMS
            self.ui.input_asker.setDisabled(False)
            self.ui.calc_param_line_edit.setDisabled(False)
            self.ui.input_asker.setText(
                '<html><head/><body><p><span style=" font-size:14pt;">How many moles do you have?</span></p></body></html>')
        if 'gr/mole' in text:
            self.calc_mode = MASS
            self.ui.input_asker.setDisabled(True)
            self.ui.calc_param_line_edit.setDisabled(True)

    def clear_calculator(self):
        """
        This slot invoked when clicking in the "clear" button. just clears and brings back
        the calculator to the initial state
        """
        self.ui.screen.display(0)
        self.ui.molecule_line_edit.setText('')
        self.ui.calc_param_line_edit.setText('')
        self.ui.showing_results_label.setText('')

    def exit_calculator(self):
        """
        Closes the calculator
        """
        self.close()


############################ Main ############################
if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
