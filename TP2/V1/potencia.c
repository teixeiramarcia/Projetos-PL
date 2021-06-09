int res;
int expoente;
int base;
int aux = 1;

potencia{
    print("Escreva a base\n");
    base = read();
    print("Escreva o expoente\n");
    expoente = read();
    repeat{
        aux = aux * base;
        expoente = expoente-1;
    } until(expoente == 0)
    return aux;
}

main{
    res = potencia();
    print(res);
}