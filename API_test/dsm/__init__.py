import multiprocessing


def worker(num, shared_array):
    """Função que é executada em um processo separado"""
    shared_array[num] = num  # atualiza um valor no array compartilhado
    print(f"Valor atualizado em shared_array[{num}]: {shared_array[num]}")


if __name__ == '__main__':
    # cria um array compartilhado de 10 elementos, inicializados com zeros
    shared_array = multiprocessing.Array('i', 10)

    # cria 3 processos, cada um chamando a função worker com um índice diferente
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i, shared_array))
        processes.append(p)
        p.start()

    # espera pelos processos terminarem
    for p in processes:
        p.join()

    # imprime o array compartilhado atualizado pelos processos
    print(f"shared_array: {list(shared_array)}")