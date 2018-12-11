
import random

class Vertices:
    def __init__(self, volumePedido, valorPedido, qtdPacotes):
        self.volumePedido = volumePedido
        self.valorPedido = valorPedido
        self.qtdPacotes = qtdPacotes
        self.x = random.uniform(0,100)
        self.y = random.uniform(0,100)

    def __str__(self):
        return str(self.v) + " " + str(self.p) + " " + str(self.n) + "\n"

class Veiculo:
    def __init__(self, volumeMáximo, valorMáximo, qtdVeiculos, vf, vd, tc, td, ph, pkm, pf):
        self.volumeMáximo = volumeMáximo
        self.valorMáximo = valorMáximo
        self.qtdVeiculos = qtdVeiculos
        self.vf = random.randint(vf - 5, vf + 5)
        self.vd = random.randint(vd - 5, vd + 5)
        self.tc = random.uniform(tc, 3*tc)
        self.td = td
        self.ph = ph
        self.pkm = pkm
        self.pf = pf

