class Veiculos:
   #cosntrutor
    def __init__(self, marca, maxima, cor="branca" ):
        self.marca = marca
        self.maxima = maxima
        self.velo_atual = 0
        self.ligado = True
        self.cor = cor
        
        
    def Ligar_desligar(self):        
        if(self.velo_atual == 0):
            self.ligado = not self.ligado
            
    def Acelerar(self, valor):
        if(self.ligado) and ((self.velo_atual + valor) <= self.maxima):
            self.velo_atual += valor
            
    def Parar(self, valor):
        if self.ligado and (self.velo_atual + valor) >= 0:
            self.velo_atual -= valor
            
            
opala=Veiculos("gm", 200)
opala.Acelerar(120)
print(opala.velo_atual)
opala.Ligar_desligar()
opala.Acelerar(100)
print(opala.velo_atual)
opala.Parar(20)
print(opala.velo_atual)

