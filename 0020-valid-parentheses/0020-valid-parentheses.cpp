class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            }
            else {
                if (st.empty()) {
                    return false;
                }
                char open = st.top();
                st.pop();
                if (!isMatching(open, c)) {
                    return false;
                }
            }
        }
        return st.empty();
    }

    bool isMatching(char open, char close) {
        return (open == '(' && close == ')')
                || (open == '[' && close == ']')
                || (open == '{' && close == '}');
    }
};