int n = 5;
int res = 1;
main{
    repeat{
        res = res * read();
        n = n - 1;
    }until(n==0)
    print(res);
    print("\n");
}