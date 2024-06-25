import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.navigationController import NavigationController
from view.navigationView import NavigationView  #vista principal



def main():
    view = NavigationView()  #instanciación de la vista principal de la navegación
    navigationController = NavigationController(view)
    navigationController.displayMenu()

if __name__ == "__main__":
    main()