import json
from id import unique_id
id = unique_id()

# print("Enter your ID\n>")
# manager = ["silviu"]
# operator = []
# gestionar = []

class Operator:

    def __init__(self, functie, id_unic, nume, prenume, calificare, creat_produse):
        self.functie = functie
        self.id_unic = id_unic
        self.nume = nume
        self.prenume = prenume
        self.calificare = calificare
        self.creat_produse = creat_produse



class Manager(Operator):
    def __init__(self, functie, id_unic, nume, prenume, calificare, creat_produse, adaugare_operatori, eliminare_operatori):
        super().__init__(functie, id_unic, nume, prenume, calificare, creat_produse)
        self.adaugare_operatori = adaugare_operatori
        self.eliminare_operatori = eliminare_operatori



class Gestionar(Manager):
    def __init__(self, functie, id_unic, nume, prenume,calificare, creat_produse, adaugare_operatori, eliminare_operatori, adauga_materie_prima_in_magazie, stoc_materie_prima, adauga_produs_finit, stoc_produs_finit):
        super().__init__(functie, id_unic, nume, prenume, calificare,creat_produse,adaugare_operatori, eliminare_operatori)
        self.adauga_materie_prima_in_magazie = adauga_materie_prima_in_magazie
        self.stoc_materie_prima = stoc_materie_prima
        self.adauga_produs_finit = adauga_produs_finit
        self.stoc_produs_finit = stoc_produs_finit

class Logare(Gestionar):

    def __init__(self, functie, id_unic, nume, prenume,calificare, creat_produse,adaugare_operatori, eliminare_operatori, adauga_materie_prima_in_magazie, stoc_materie_prima, adauga_produs_finit, stoc_produs_finit):
        super().__init__(functie, id_unic, nume, prenume,calificare,creat_produse, adaugare_operatori, eliminare_operatori, adauga_materie_prima_in_magazie, stoc_materie_prima, adauga_produs_finit, stoc_produs_finit)

    def add_client(self):
        while True:
            # man = input()
            # if man in manager:
            read_angajati_json = open("angajati.json", "r")
            # angajat = json.load(read_angajati_json)
            log = input("Logheaza-te\n>")
            for i in read_angajati_json:
                if log in i:
                    print("Esti manager!")
                    for c in menu1:
                        print(c)
                    optiune = int(input("Selecteaza o optiune:\n>"))
                    if optiune == 1:
                        self.nume = input("Numele angajatului: \n>")
                        self.prenume = input("Prenumele angajatului: \n>")
                        self.functie = input("Functia:\n>")
                        self.calificare =  input("Calificarea:\n>")
                        self.creat_produse = input("produce:\n>")



                        angajat = {f"{id}": {"id_unic:" :f"{self.id_unic}",
                                            "nume":f"{self.nume}",
                                            "prenume": f"{self.prenume}",
                                            "functie":f"{self.functie}",
                                            "calificare": f"{self.calificare}",
                                             "produce": f"{self.creat_produse}"}}

                        read_angajati_json = open("angajati.json", "r")
                        converted_json = json.load(read_angajati_json)
                        read_angajati_json.close()
                        converted_json = angajat
                        read_angajati_json = open("angajati.json", "r")
                        new_json = json.dumps(converted_json, indent=5)
                        write_angajati_json = open("angajati.json", "a")
                        write_angajati_json.write(new_json)
                        write_angajati_json.close()
                        return print("adaugat")

                        # angajat_nou_json = json.dumps(dictionar_nou, indent = 5)
                        # dictionar_nou = json.load(angajat_nou_json)
                        # write_angajati_json = open("angajati.json", "a")
                        # write_angajati_json.write(angajat_nou_json)
                        # write_angajati_json.close()
                        break

            else:
                print("user invalid")
                continue

            #     if self.functie == "operator":
            #         f2 = open("operatori.txt ","a")
            #         f2.write(f"{self.id_unic}")
            #     elif self.functie == "manager":
            #         f3 = open("manageri.txt", "a")
            #         f3.write(f"{self.id_unic}")
            #     elif self.functie == "gestionar":
            #         f4 = open("gestionar.txt" , "a")
            #         f4.write(f"{self.id_unic}")
            #         return False
            #
            #     # if optiune == 2:
            #
            # elif self.id_unic in open("operatori.txt","r"):
            #     print("Esti operator")
            #
            #
            # elif self.id_unic in open("gestionar.txt","r"):
            #     print("Esti gestionar!")
            #
            # else:
            #     print("Id invalid!\n> Introdu un id valid!")
            #     continue





# calificari = {
#     "electrician": {"tablou_electric": ["sigurante", "carcasa_tablou","sonerie" ]},
#     "instalatori": {"tevi": ["racorduri", "robineti", "inbinari"]},
#     "electronisti" : {"placi_de_baza": ["diode", "condensatori", "rezistente"]}
# }


menu1 = ["1.Adaugare angajati", "2.Eliminare angajati", "3.Modificare date/calificari ale angajatilo", "4.Iesire"]
menu2 = ["1.Calificarea angajatului", "2.Produse ce le poate crea", "3.Iesire"]
menu3 = ["1.Verifica stoc materie prima","2.Adauga materie prima in stoc" "3.Verifica stoc produse finite:", "Adauga produse finite in stoc"]
a = Logare( "functie","id_unic", "nume", "prenume","calificare", "creat_produse","adaugare_operatori", "eliminare_operatori", "adauga_materie_prima_in_magazie", "stoc_materie_prima", "adauga_produs_finit", "stoc_produs_finit")

a.add_client()




