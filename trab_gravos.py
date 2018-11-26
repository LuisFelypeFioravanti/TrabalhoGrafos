//gravos
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