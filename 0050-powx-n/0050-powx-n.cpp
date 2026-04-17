class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        if (n == INT_MIN) return 1.0/(x * myPow(x, -(n + 1))); //-INT_MIN would cause an overflow error
        if (n < 0) return 1/myPow(x, -n);
        double tmp = myPow(x, n/2);
        if (n % 2 == 0) return tmp * tmp;
        return tmp * tmp * x;
    }
};