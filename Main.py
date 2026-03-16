class Personagens:
  def __init__(self, nome, vida, ataque, defesa):
    self.nome = nome
    self.vida = vida
    self.ataque = ataque
    self.defesa = defesa
  def mostrar_infor(self):
    print(f"o nome do personagem é {self.nome}")
    print(f"a vida dele está em {self.vida}")
    print(f"seu ataque é {self.ataque} pts")
    print(f"sua defesa é {self.defesa} pts")
  def atacar(self, inimigo):
    if self.ataque > inimigo.defesa:
      inimigo.vida -= self.ataque
      print(f"tirou {self.ataque} pts")
      if inimigo.vida <= 0:
        print(f"{inimigo.nome} morreu kkkkkkk")
    else:
      print("Não infringiu dano")
  def treinar(self):
    self.ataque += 1
    print(f"{self.nome} treinou")
sapo = Personagens("sapo", 10, 3, 3) 
pato = Personagens("pato", 10, 3, 3)
while sapo.vida > 0 and pato.vida > 0:
   turno = input("1 - atacar, 2 - mostrar info, 3 - treinar, 4 - mostrar info do inimigo")
   if turno == "1":
     sapo.atacar(pato)
   elif turno == "2":
    sapo.mostrar_infor()
   elif turno == "3":
     sapo.treinar()
   elif turno == "4":
     pato.mostrar_infor()
   else: 
     print("Número Invalido")
   print('-' * 80)