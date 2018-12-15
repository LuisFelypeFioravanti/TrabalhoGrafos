
import random

class Vertices:
    def __init__(self,x,y, volumePedido, valorPedido, qtdPacotes):
        self.volumePedido = volumePedido
        self.valorPedido = valorPedido
        self.qtdPacotes = qtdPacotes
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.v) + " " + str(self.p) + " " + str(self.n) + "\n"

class Veiculo:
    def __init__(self, volumeMáximo, valorMáximo, qtdVeiculos, vf, vd, tc, td, ph, pkm, pf):
        self.volumeMáximo = volumeMáximo
        self.valorMáximo = valorMáximo
        self.qtdVeiculos = qtdVeiculos
        self.vf = vf
        self.vd = vd
        self.tc = tc
        self.td = td
        self.ph = ph
        self.pkm = pkm
        self.pf = pf

