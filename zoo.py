# Importo il modulo re per lavorare con le espressioni regolari
import re

# Funzione ausiliaria per la validazione della regex
def valida_regex(pattern, stringa):
    return re.search(pattern, stringa) # Il metodo search() trova la prima corrispondenza del pattern nella stringa, viene restituito un oggetto Match se viene trovata una corrispondenza, altrimenti viene restituito None.

# Funzione ausiliaria per il controllo dell'esistenza dell'animale nel dizionario zoo
def controllo_esistenza_animale(zoo, nome):
    keys = zoo.keys()
    if nome not in keys:
        return False
    return True

# Funzione ausiliaria di (conta_sangue, conta_classe, conta_specie)
def conta(zoo, parametro, indice):
    conta = 0
    # Itero su ogni animale presente nel dizionario zoo
    for animal in zoo:
        # Accedo alla tupla associata all'animale corrente
        tupla_animal = zoo[animal]
        if tupla_animal[indice] == parametro:
            conta += 1
    return conta

#(nome, classe, specie, numero_zampe, sangue_caldo, ambiente, zona, verso)
def inserisci(zoo, nome, classe, specie, numero_zampe, sangue_caldo, ambiente, zona, verso):

    # valori ammessi per il parametro ambiente
    lista_ambiente = ["Acqua", "Terra", "Aria"]

    if type(nome) != str:
         return False
    if type(classe) != str:
        return False
    if type(specie) != str or specie == "Uomo":
        return False
    if type(numero_zampe) != int:
        return False
    if type(sangue_caldo) != bool:
        return False
    # Controllo che il parametro ambiente sia presente in lista_ambiente. Se l'elemento non viene trovato viene restituito False
    for el in ambiente:
        if el not in lista_ambiente:
            return False
    # Controllo che il parametro zona sia composta da una lettera maiuscola seguita da un numero intero
    x = valida_regex(r"[A-Z]\d", zona)
    if not x:
        return False
    if type(verso) != str:
         return False
    
    # Nuovo animale da aggiungere al dizionario esistente
    nuovo_animale = {
        nome: (nome, classe, specie, numero_zampe, sangue_caldo, ambiente, zona, verso)
    }
    #  Controllo se l'animale non è presente nel dizionario, se non è presente aggiungo nuovo_animale al dizionario già esistente
    if nome in zoo:
        return False
    else:
        zoo.update(nuovo_animale)

    return True

def serializza(zoo):
    stringa_output = ""
    # Itero su ogni chiave del dizionario zoo
    for animal in zoo:
        # A ogni iterazione, converto i valori del dizionario zoo in una lista
        animal_list = list(zoo.values())
        # Uso join() per creare una stringa concatenando i valori di animal_list, separandoli con uno spazio e aggiungendo un a capo (\n).
        # Siccome il metodo join() in python funziona solo con valori di tipo stringa, faccio in modo che ogni elemento della lista sia di tipo stringa utilizzando il metodo map()
        stringa_output = " ".join(map(str, animal_list)) + "\n" # Il metodo map() consente di applicare una funzione specifica a ogni elemento di un iterabile (come una lista). La funzione che viene applicata è str(), per convertire ogni elemento della lista in una stringa.
    return stringa_output

def animale(zoo, nome):
    # Restituisco la tupla dell'animale, oppure None se non esiste
    return zoo.get(nome)

def elimina(zoo, nome):
    # Controllo l'esistenza dell'animale
    controllo = controllo_esistenza_animale(zoo, nome)
    if not controllo:
        return False
    
    # Elimino l'animale con nome "nome" dal dizionario zoo
    del zoo[nome]

    return True

def cambia_zona(zoo, nome, zona):
    if type(zona) != str:
        return False
    
    # Controllo l'esistenza dell'animale
    controllo_esistenza_animale(zoo, nome)

    # Controllo che il parametro zona sia composta da una lettera maiuscola seguita da un numero intero
    x = valida_regex(r"[A-Z]\d", zona)
    if not x:
        return False
    
    # Converto la tupla in una lista per modificare il valore della zona
    animal_list = list(zoo[nome])
    animal_list[6] = zona
    # Aggiorno il dizionario riconvertendo la lista in tupla
    zoo[nome] = tuple(animal_list)

    return True

def zone(zoo):
    # Inizializzo una lista vuota per raccogliere le zone
    lista_zone = []
    # Itero su ogni animale presente nel dizionario zoo
    for animal in zoo:
        # Accedo alla tupla associata all'animale corrente
        tupla_animal = zoo[animal]
        # Aggiungo alla lista la zona, l'elemento ache corrisponde all'indice 6 della tupla
        if tupla_animal[6] not in lista_zone:
            lista_zone.append(tupla_animal[6])
    # Restituisco la lista completa delle zone
    return lista_zone

def animali_zona(zoo, zona):
    # Inizializzo una lista vuota per raccogliere gli animali presenti nella zona "zona"
    lista_animali = []
    # Itero su ogni animale presente nel dizionario zoo
    for animal in zoo:
        # Accedo alla tupla associata all'animale corrente
        tupla_animal = zoo[animal]
        if tupla_animal[6] == zona:
            lista_animali.append(tupla_animal[0])
    # Restituisco la lista completa degli animali
    return lista_animali

def zone_animali(zoo):
    zone_animali_dict = {}
    # Ciclo sia le chiavi che i valori, utilizzando il metodo items()
    for animale, zona in zoo.items():
        if zona[6] not in zone_animali_dict:
            zone_animali_dict[zona[6]] = []
        zone_animali_dict[zona[6]].append(animale)
    # Restituisco un dizionario che ha come chiavi le zone e come valori la lista degli animali presenti in quella zona
    return zone_animali_dict

def animali_classe(zoo, classe):
    # Inizializzo una lista vuota per raccogliere gli animali presenti nella classe "classe"
    lista_animali = []
    # Itero su ogni animale presente nel dizionario zoo
    for animal in zoo:
        # Accedo alla tupla associata all'animale corrente
        tupla_animal = zoo[animal]
        if tupla_animal[1] == classe:
            lista_animali.append(tupla_animal[0])
    # Restituisco la lista completa degli animali
    return lista_animali

def animali_specie(zoo, specie):
    # Inizializzo una lista vuota per raccogliere gli animali della specie "specie"
    lista_animali = []
    # Itero su ogni animale presente nel dizionario zoo
    for animal in zoo:
        # Accedo alla tupla associata all'animale corrente
        tupla_animal = zoo[animal]
        if tupla_animal[2] == specie:
            lista_animali.append(tupla_animal[0])
    # Restituisco la lista completa degli animali
    return lista_animali

def animali_ambiente(zoo, ambiente):
    # Inizializzo una lista vuota per raccogliere gli animali che vivono nell'ambiente "ambiente"
    lista_animali = []
    # Itero su ogni animale presente nel dizionario zoo
    for animal in zoo:
        # Accedo alla tupla associata all'animale corrente
        tupla_animal = zoo[animal]
        lista_ambiente = tupla_animal[5]
        # Controllo se l'animale vive nell'ambiente "ambiente"
        if ambiente in lista_ambiente:
            lista_animali.append(tupla_animal[0])
    # Restituisco la lista completa degli animali
    return lista_animali

def animali_con_zampe_almeno(zoo, numero_zampe=2):
    # Inizializzo una lista vuota per raccogliere gli animali che hanno almeno "numero_zampe" zampe
    lista_animali = []
    # Itero su ogni animale presente nel dizionario zoo
    for animal in zoo:
        # Accedo alla tupla associata all'animale corrente
        tupla_animal = zoo[animal]
        if tupla_animal[3] >= numero_zampe:
            lista_animali.append(tupla_animal[0])
    # Restituisco la lista completa degli animali
    return lista_animali

def conta_sangue(zoo, sangue_caldo):
    conta_animali_sangue = conta(zoo, sangue_caldo, 4)
    # Restituisco il numero di animali con sangue caldo o freddo
    return conta_animali_sangue

def conta_classe(zoo, classe):
    conta_animali_classe = conta(zoo, classe, 1)
    # Restituisco il numero di animali della classe "classe"
    return conta_animali_classe

def conta_specie(zoo, specie):
    conta_animali_specie = conta(zoo, specie, 2)
    # Restituisco il numero di animali della specie "specie"
    return conta_animali_specie