int reverse(int x){
 long long r=0;
 while(x>0 || x<0){
    int k = x%10;
     if (r > 214748364) {
            return 0;  // Positive overflow
        }
        if (r < -214748364) {
            return 0;  
        }
    r = r*10 + k;
    x = x/10;
 }
 return r;
}