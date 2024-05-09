def vynasob(a: float, b: float) -> float:
  return a * b

def vydel(a: float, b: float) -> float:
  return a/b

def odecti (a: float, b: float) -> float:
  return a - b

def secti (a: float, b: float) -> float:
  return a + b

def main():
  print(secti(a=5, b=3))

# git add . # prepise vsechny soubory v pocitaci
# git add app.py #prepise app.py v pocitaci  
# git commit -am "pridal jsem funcki na odecitani" # vytvori a prepise commit a koment v pocitaci(prikaz na vsechno)
# git push  # pushne to do githubu z lokalni databaze
