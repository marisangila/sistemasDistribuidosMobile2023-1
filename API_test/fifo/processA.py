import os
import random
import posix_ipc

# cria a fila de mensagens
mq = posix_ipc.MessageQueue("/fila", flags=posix_ipc.O_CREAT)

while True:
    # sorteia os números aleatórios
    n1 = random.randint(0, 99)
    n2 = random.randint(0, 99)

    # envia os números para o processo B
    mq.send(f"{n1} {n2}".encode())

    # recebe a soma do processo B
    soma = int(mq.receive()[0].decode())

    # escreve a operação e o resultado
    print(f"{n1} + {n2} = {soma}")
