// Arquivo mqsend.c: envia mensagens para uma fila de mensagens POSIX.
// Em Linux, compile usando: cc -Wall mqsend.c -o mqsend -lrt
#include <stdio.h>
#include <stdlib.h>
#include <mqueue.h>
#include <unistd.h>

#define QUEUE "/to_b"

typedef struct{
    int n1;
    int n2;
}Numbers;


int main(int argc, char *argv[])
{
    mqd_t queue; // descritor da fila  
    Numbers numbers;

    int sum;
    // abre a fila de mensagens, se existir
    if ((queue = mq_open(QUEUE, O_RDWR)) < 0)
    {
        perror("mq_open");
        exit(1);
    }
    for (;;)
    {
        numbers.n1 = random() % 100;
        numbers.n2 = random() % 100;
        
        if (mq_send(queue, (char *) &numbers, sizeof(Numbers), 0) == -1) {
            perror("mq_send");
            exit(1);
        }

        if (mq_receive(queue, (char *) &sum, sizeof(int), NULL) == -1) {
            perror("mq_receive");
            exit(1);
        }

        printf("Sent message with value %d and %d. \n", numbers.n1,numbers.n2);
        printf("Received message with sum value: %d. \n",sum);
        sleep(1);
    }
}
