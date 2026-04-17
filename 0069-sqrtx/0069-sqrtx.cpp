class Solution {
public:
    int mySqrt(int x) {
        int l = 0;
        int r = x/2;
        while (l <= r) {
            int m = l + (r - l)/2;
            if (m * m <= x && (m + 1) * (m + 1) > x) return m;
            if (m * m < x) l = m + 1;
            else r = m - 1;
        }
        return 0;
    }
};