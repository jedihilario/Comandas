from os import system
import menus

def main ():
    menus.mainMenu()

if (__name__ == "__main__"):
    empty_db = False

    try:
        with open('db.json') as db:
            if (len(db.read()) == 0): empty_db = True
    except:
        with open('db.json', 'w') as db:
            db.write('[]')

    if (empty_db):
        with open('db.json', 'w') as db:
            db.write('[]')

    main()