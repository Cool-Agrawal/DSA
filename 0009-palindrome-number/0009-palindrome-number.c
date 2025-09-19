bool isPalindrome(int x) {
    int no=x;
        if (x < 0 || (x % 10 == 0 && x != 0)) {
        return 0; 
        }
        long long int r=0;
    while(x>0){
        int s = x%10;
        r = r*10 + s;
        x = x/10;
    }
    if(no == r){
        return true;
    }
    else
   return false;
}