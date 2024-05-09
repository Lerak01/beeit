from math import inf

def vynasob(a: float, b: float) -> float:
  return a * b

def vydel(a: float, b: float) -> float:
  if b == 0:      #opraveni issue 2-deleni-neni-bezpecne
    return inf
  else:
    return a/b

def odecti (a: float, b: float) -> float:
  return a - b

def secti (a: float, b:float) -> float:
  return a + b

def main():
  print(secti(a=5, b=3))

# git add . # prepise vsechny soubory v pocitaci
# git add app.py #prepise app.py v pocitaci  
# git commit -am "pridal jsem funcki na odecitani" # vytvori a prepise commit a koment v pocitaci(prikaz na vsechno)
# git push  # pushne to do githubu z lokalni databaze
# git fetch origin # command pro reseni issues (stahnuti vetvi z githubu)
# git checkout 2-deleni-neni-bezpecne (checkout je stary univerzalni command na vice veci, lepsi je git branch) # prepnuti do urciteho issue (vetve)
# git branch #ukaze mi aktualni vetev
# git switch main # prepinani vetvi napr do main
# git stash  #vymaze necomitly ulozeny kod protoze se jinak nemuzu switchnout
# vetve - alternativni verze kodu , muzu mezi nimi prepinat 

# nejlepší je v práci v teamu na začátku práce vždy pullnout predchozi praci druheho z githubu aby se predeslo konfliktum


