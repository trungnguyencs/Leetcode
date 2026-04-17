class Solution {
public:
    int mySqrt(int x) {
        int l = 0, r = x;
        while (l <= r) {
            int m = l + (r - l) / 2;
            long long sq = 1LL * m * m;
            if (sq == x) return m;
            if (sq < x) l = m + 1;
            else r = m - 1;
        }
        return r;
    }
};