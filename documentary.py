class Documentaire:
    nbobj = 0

    def __init__(self, code, titre, date):
        self.code = code
        self.titre = titre
        self.date = date
        Documentaire.nbobj += 1

    def getcode(self):
        return self.code

    def gettitre(self):
        return self.titre

    def getdate(self):
        return self.date

    def getnbobj(self):
        return Documentaire.nbobj

    def setcode(self, value):
        self.code = value

    def settitre(self, value):
        self.titre = value

    def setdate(self, value):
        self.date = value

    def Tostring(self):
        return f"Titre: {self.titre}, Date de sortie: {self.date}"

    def Equals(self, doc2):
        return self.code == doc2.code


class Exemplaire(Documentaire):
    def __init__(self, code, titre, date, numero, dateachat):
        super().__init__(code, titre, date)
        self.numero = numero
        self.dateachat = dateachat

    def getnumero(self):
        return self.numero

    def getdateachat(self):
        return self.dateachat

    def setnumero(self, value):
        self.numero = value

    def setdateachat(self, value):
        self.dateachat = value

    def Tostring(self):
        return f"Titre: {self.titre}, Date de sortie: {self.date}, Numero: {self.numero}, Date d'achat: {self.dateachat}"

    def Equals(self, doc2):
        return self.code == doc2.code


doc1 = Documentaire(code="2222", titre="knkn", date="16/12/2005")
doc2 = Documentaire(code="4353", titre="uggj", date="7/6/2000")
doc3 = Documentaire(code="5673", titre="jkhhk", date="1/8/2001")
exp1 = Exemplaire(code="7700", titre="abbb", date="1/9/2001", numero=2, dateachat="8/9/2018")
exp2 = Exemplaire(code="6809", titre="jkljl", date="1/11/2001", numero=3, dateachat="9/3/2018")

print(Documentaire.nbobj)
print(f"Documentaire 1 - ToString: {doc1.Tostring()}")
print(f"Documentaire 2 - Equals Documentaire 1: {doc2.Equals(doc1)}")
print(f"Exemplaire 1 - ToString: {exp1.Tostring()}")
print(f"Exemplaire 2 - Equals Exemplaire 1: {exp2.Equals(exp1)}")

