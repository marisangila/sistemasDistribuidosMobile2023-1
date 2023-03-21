import os

# Cria um novo pipe
r, w = os.pipe()

# Cria um novo processo filho
pid = os.fork()

if pid: # Processo pai
    os.close(w) # Fecha a extremidade de escrita do pipe
    r = os.fdopen(r) # Converte a extremidade de leitura do pipe em um objeto de arquivo

    # Lê dados do pipe e imprime na tela
    data = r.readline().strip()
    print("Mensagem recebida do processo filho:", data)
    r.close() # Fecha a extremidade de leitura do pipe

else: # Processo filho
    os.close(r) # Fecha a extremidade de leitura do pipe
    w = os.fdopen(w, 'w') # Converte a extremidade de escrita do pipe em um objeto de arquivo

    # Escreve uma mensagem no pipe
    w.write("Olá, mundo!")
    w.close() # Fecha a extremidade de escrita do pipe