class Solution {
public:
    void reverseString(vector<char>& s) {
        helper(s, 0, s.size() - 1);
    }

    void helper(vector<char>& s, int l, int r) {
        if (l >= r) return;
        char tmp = s[l];
        s[l] = s[r];
        s[r] = tmp;
        helper(s, l + 1, r - 1);
    }
};