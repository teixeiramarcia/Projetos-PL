int i;
int min;
int aux;
int value;
main{
    i = read();
    aux = i;
    repeat{
        value = read();
        if(i==aux){
            min = value;
        }
        elif(value<min){
            min = value;
        }
        print(min);
        print("\n");
        i = i - 1;
    }until (i==0)
}