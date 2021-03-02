#include <stdio.h>
#include <windows.h>

int main()
{
    int h, m, s;

    int d = 1000; //Nós adicionamos um delay de 1000 millisegundos pra usar na função sleep.
    printf("Set time: \n");
    scanf("%d%d%d", &h, &m, &s);

    if (h > 12 || m > 60 || s > 60)
    {
        printf("Error! \n");
        exit(0);
    }
    while (1) //  Esse é um loop infinito e nada dentro dele vai desativá-lo.
    {
        s++;
        if (s > 59)
        {
            m++;
            s = 0;
        }
        if (m > 59)
        {
            h++;
            m = 0;
        }
        if (h > 12)
        {
            h = 1;
        }
        printf("\n Clock: ");
        printf("\n %02d:%02d:%02d:", h, m, s); // Isso vai deixar o formato 00:00:00.
        Sleep(d);                                   // A função sleep diminue a velocidade do while loop de deixa-0 mias parecido a um relógio real.
        system("cls");                              // Limpa a tela
    }
}
