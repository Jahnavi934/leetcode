class Solution {
public:
    bool isSubsequence(string s, string t) {
        int length = s.size();
        int c = 0;

        // edge case 1
        if (length == 0){
            return true;
        }

        for (int i = 0; i < t.size(); i++){
            if (s[c] == t[i]){
                c++;
            }
        }

        if (c == length)    return true;
        return false;
    }
};
