int a;
int b;
int c;
int d;
main{
    print("Escreva o primeiro lado do quadrado\n");
    a = read();
    print("Escreva o segundo lado do quadrado\n");
    b = read();
    print("Escreva o terceiro lado do quadrado\n");
    c = read();
    print("Escreva o quarto lado do quadrado\n");
    d = read();

    if((not a) || (not b) || (not c) || (not d)){
        print("Pelo menos um valor é nulo\n");
    }
    elif(a == b && b == c && c == d){
        print("Estes valores fazem um quadrado\n");
    }
    else{
        print("Estes valores fazem um retangulo");
    }
}