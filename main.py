class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[0;36m'

def install(package):
    import importlib
    try:
        print(colors.WARNING + "Checking packages ..." + colors.ENDC)
        importlib.import_module(package)
    except ImportError:
        print(colors.FAIL + "Package not found '" + package + "'" + colors.ENDC)
        confirm = input(colors.WARNING + "Do you want to install the package? (the program won't work without it) [Y/N] " + colors.ENDC)
        if confirm in ['Y','y','yes']:
            import pip
            pip.main(['install', package])
        if confirm in ['N','n','no']:
            print(colors.FAIL + 'Leaving program' + colors.ENDC)
            exit()
    finally:
        globals()[package] = importlib.import_module(package)
        print(colors.OKGREEN + "'" + package + "'" + " is installed" + colors.ENDC)
        
def mult(p1, p2):
    return p1 * p2
def suma(p1, p2):
    return p1 + p2
def res(p1, p2):
    return p1 - p2
def div(p1, p2):
    return p1 / p2

def initial():
    print(colors.CYAN + "                  _                               _     _      " + colors.ENDC)
    time.sleep(0.1)
    print(colors.CYAN + "                 | |                             | |   | |     " + colors.ENDC) 
    time.sleep(0.1)
    print(colors.CYAN + "  _ __     ___   | |  _   _   _ __ ___     __ _  | |_  | |__   " + colors.ENDC) 
    time.sleep(0.1)
    print(colors.CYAN + " | '_ \   / _ \  | | | | | | | '_ ` _ \   / _` | | __| | '_ \  " + colors.ENDC) 
    time.sleep(0.1)
    print(colors.CYAN + " | |_) | | (_) | | | | |_| | | | | | | | | (_| | | |_  | | | | " + colors.ENDC) 
    time.sleep(0.1)
    print(colors.CYAN + " | .__/   \___/  |_|  \__, | |_| |_| |_|  \__,_|  \__| |_| |_| " + colors.ENDC) 
    time.sleep(0.1)
    print(colors.CYAN + " | |                   __/ |                                   " + colors.ENDC)
    time.sleep(0.1)
    print(colors.CYAN + " |_|                  |___/                                    " + colors.ENDC)
    print("\n")
    time.sleep(1)

def start():
    home_input = input(colors.WARNING + 'Press "S" to start calculator, "E" to exit the program, "I" to show info or "C" to show credits.\nThen press enter. ' + colors.ENDC)
    if home_input in ['S','s','start']:
        variables()
    if home_input in ['E','e','exit']:
        print(colors.FAIL + 'Leaving program' + colors.ENDC)
        exit()
    if home_input in ['I','i','info']:
        print(colors.OKGREEN + 'Polymath is a simple two polynomial terminal script calculator written in Python! \nIn mathematics, a polynomial is an expression consisting of variables and coefficients. A polynomial is composed of several monomials.\nAn example of a polynomial is x**2 − 4*x + 7.' + colors.ENDC)
        print(colors.CYAN + 'SINTAX: \n- To write powers use "**", ex: x**7 (x to the 7). \n- To write multiplications use "*", ex: x*5. \n- To write divisions use "/", ex: 5*x/x. \n- To write additions and subtractions use "+" and "-", ex: 5+x-4.' + colors.ENDC)
        print(" ")
        time.sleep(3)
        start()
    if home_input in ['C','c','credits']:
        print(colors.CYAN + 'Script by PyJavaPulver 2020. For more info, visit my GitHub: PyJavaPulver. \nThis script is under MIT lisence.' + colors.ENDC)
        print(" ")
        time.sleep(2)
        start()
    else:
        print(colors.FAIL + 'Error, type a valid input' + colors.ENDC)
        start()

def variables():
    variables.P1 = input(colors.CYAN + "First polynomial: " + colors.ENDC)
    variables.P2 = input(colors.CYAN + "Second polynomial: " + colors.ENDC)
    math()

def pol1():
    variables.P1 = input(colors.CYAN + "New First polynomial: " + colors.ENDC)
    print(colors.OKGREEN + "P1 successfully changed to " + variables.P1 + colors.ENDC)
    math()

def pol2():
    variables.P2 = input(colors.CYAN + "New Second polynomial: " + colors.ENDC)
    print(colors.OKGREEN + "P2 successfully changed to " + variables.P2 + colors.ENDC)
    math()

def math():
    sympy.init_printing()
    x,y = sympy.symbols('x,y')

    math.Poly1 = sympy.Poly(variables.P1)
    math.Poly2 = sympy.Poly(variables.P2)
    tipo()

def tipo():
    selec = input(colors.CYAN + "Type: \n" + colors.ENDC + "[" + colors.OKGREEN + "1" + colors.ENDC + "] multiplication; [" + colors.OKGREEN + "2" + colors.ENDC + "] division; [" + colors.OKGREEN + "3" + colors.ENDC + "] addition; [" + colors.OKGREEN + "4" + colors.ENDC + "] subtraction. " + colors.ENDC + "\n[" + colors.OKGREEN + "P1" + colors.ENDC + "] change first polynomial; " + "[" + colors.OKGREEN + "P2" + colors.ENDC + "] change second polynomial. " + colors.CYAN + '\nOr press "R" to restart the calculator or "E" to exit ' + colors.ENDC)
    if selec in ['1','one']:
      print(colors.OKGREEN + "Result: ", mult(math.Poly1, math.Poly2), colors.ENDC)
      time.sleep(2)
      print(" ")
      tipo()
    if selec in ['2','two']:
      print(colors.OKGREEN + "Result: ", div(math.Poly1, math.Poly2), colors.ENDC)
      time.sleep(2)
      print(" ")
      tipo()
    if selec in ['3','three']:
      print(colors.OKGREEN + "Result: ", suma(math.Poly1, math.Poly2), colors.ENDC)
      time.sleep(2)
      print(" ")
      tipo()
    if selec in ['4','four']:
      print(colors.OKGREEN + "Result: ", res(math.Poly1, math.Poly2), colors.ENDC)
      time.sleep(2)
      print(" ")
      tipo()
    if selec in ['p1','P1']:
      pol1()
    if selec in ['p2','P2']:
      pol2()
    if selec in ['R','r','restart']:
      print(" ")
      confirm = input(colors.FAIL + "Are you sure? [Y/N] " + colors.ENDC)
      if confirm in ['Y','y','yes']:
          variables()
      if confirm in ['N','n','no']:
          tipo()
      else:
          print(colors.FAIL + 'Error, type a valid input' + colors.ENDC)
          print(" ")
          tipo()
    if selec in ['E','e','exit']:
      print(" ")
      confirm = input(colors.FAIL + "Are you sure? [Y/N] " + colors.ENDC)
      if confirm in ['Y','y','yes']:
          start()
      if confirm in ['N','n','no']:
          tipo()
      else:
          print(colors.FAIL + 'Error, type a valid input' + colors.ENDC)
          print(" ")
          tipo()
    else:
      print(colors.FAIL + 'Error, type a valid input' + colors.ENDC)
      print(" ")
      tipo()

install('sympy')
install('time')
initial()
start()
