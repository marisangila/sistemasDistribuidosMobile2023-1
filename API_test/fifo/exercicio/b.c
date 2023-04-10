// Arquivo mqrecv.c: recebe mensagens de uma fila de mensagens POSIX.
// Em Linux, compile usando: cc -Wall mqrecv.c -o mqrecv -lrt

#include <stdio.h>
#include <stdlib.h>
#include <mqueue.h>
#include <sys/stat.h>

#define QUEUE "/process_A"

struct Numbers{
    int n1;
    int n2;
};

int main(int argc, char *argv[])
{
    mqd_t queue;         	// descritor da fila de mensagens
    struct mq_attr attr; 	// atributos da fila de mensagens

    int sum;             	
    struct Numbers numbers;
    // define os atributos da fila de mensagens
    attr.mq_maxmsg = 10;           // capacidade para 10 mensagens
    attr.mq_msgsize = sizeof(msg); // tamanho de cada mensagem
    attr.mq_flags = 0;

    // abre ou cria a fila com permissoes 0666
    if ((queue = mq_open(QUEUE, O_RDWR | O_CREAT, 0666, &attr)) < 0)
    {
        perror("mq_open");
        exit(1);
    }

    // recebe cada mensagem e imprime seu conteudo
    while (true)
    {
        if (mq_receive(mq, (char *) &numbers, sizeof(Numbers), NULL) == -1) {
            perror("mq_receive");
            exit(1);
        }

        sum = numbers.n1 + numbers.n2;

        if (mq_send(mq, (char *) &sum, sizeof(int), 0) == -1) {
            perror("mq_send");
            exit(1);
        }

        sleep(1);

        printf("Received message with value %d and %d. \n", numbers.n1,numbers.n2);
        print("Sent message with sum value: %d. \n",sum)
    }
}