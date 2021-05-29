int value;
int count;
int n;
main{
    n = read();
    repeat{
        value = read();
        if(value % 2 != 0){
            print(value);
            print("\n");
            count = count + 1;
        }
        n = n-1;
    }until(n==0)
    print(count);
    print("\n");
}