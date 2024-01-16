class Hardware:
    def __init__(self, typ_zariadenia, seriove_cislo, nazov_zariadenia):
        self.type = typ_zariadenia
        self.sn = seriove_cislo
        self.name = nazov_zariadenia

    def laptop(self):
        print(f"Vlastnis toto zariadenie\nTyp: {self.type}\nSN: {self.sn}\nNazov: {self.name}")


notebook=Hardware("Notebook", 7885641, "Dell Latitude")

# notebook._hardware__laptop() ako obist privat funkciu aby bola dostupna

class Person(Hardware):
    def __init__(self, typ_zariadenia, seriove_cislo, nazov_zariadenia, persone_name, conpany, job_title):
        super().__init__(typ_zariadenia, seriove_cislo, nazov_zariadenia)
        self.name_person = persone_name
        self.conpany = conpany
        self.job = job_title

    def user(self):
        print(f"{self.name_person} toto je tvoj kompletny vypis\n {self.name}\n{self.sn}\n{self.conpany}\n{self.job}")




notebook=Hardware("Notebook", 7885641, "Dell Latitude")
notebook_full = Person("Notebook", "7885641", "Dell Latitude", "Danko maniak", "NRSR", "Povalac stlpov")

# notebook._hardware__laptop() ako obist privat funkciu aby bola dostupna
#notebook.laptop()
notebook_full.user()





