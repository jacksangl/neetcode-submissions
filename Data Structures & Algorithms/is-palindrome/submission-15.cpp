class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.length() - 1;
        while (l <= r) {
            while (!isalnum(s[l])) l += 1;
            while (!isalnum(s[r])) r -= 1;
            if (l > r) break;

            if (tolower(s[l]) != tolower(s[r])) return false;
            l += 1;
            r -= 1;
            
        }
        return true;
    }
};
