import os
import posix_ipc

# cria a fila de mensagens
mq = posix_ipc.MessageQueue("/fila", flags=posix_ipc.O_CREAT)

while True:
    # recebe os números do processo A
    n1, n2 = map(int, mq.receive()[0].decode().split())

    # calcula a soma
    soma = n1 + n2

    # espera um segundo
    os.sleep(1)

    # envia a soma para o processo A
    mq.send(str(soma).encode())
