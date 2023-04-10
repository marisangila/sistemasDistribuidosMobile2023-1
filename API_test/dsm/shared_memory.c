// Arquivo shm.c: cria e usa uma área de memória compartilhada POSIX.
// Em Linux, compile usando: cc -Wall shm.c -o shm -lrt

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>

int main(int argc, char *argv[])
{
    int fd, value, *ptr;

    // Passos 1 a 3: abre/cria uma area de memoria compartilhada
    fd = shm_open("/sharedmem", O_RDWR | O_CREAT, S_IRUSR | S_IWUSR);
    if (fd == -1)
    {
        perror("shm_open");
        exit(1);
    }

    // ajusta o tamanho da area compartilhada para sizeof (value)
    if (ftruncate(fd, sizeof(value)) == -1)
    {
        perror("ftruncate");
        exit(1);
    }

    // Passos 4 a 6: mapeia a area no espaco de enderecamento deste processo
    ptr = mmap(NULL, sizeof(value), PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (ptr == MAP_FAILED)
    {
        perror("mmap");
        exit(1);
    }

    for (;;)
    {
        // Passo 8: escreve um valor aleatorio na area compartilhada
        value = random() % 1000;
        (*ptr) = value; // escreve na area
        printf("Wrote value %i\n", value);
        sleep(1);

        // Passo 8: le e imprime o conteudo da area compartilhada
        value = (*ptr); // le da area
        printf("Read value %i\n", value);
        sleep(1);
    }
}