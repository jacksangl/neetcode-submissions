#include <cctype>
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector <string> stah;

        for (string token : tokens) {
            
            if (token.length() > 1 || isdigit((unsigned char)token[0])) {
                stah.push_back(token);
                continue;
            }
            int num2 = stoi(stah.back());
            stah.pop_back();
            int num1 = stoi(stah.back());
            stah.pop_back();
            if (token == "+") stah.push_back(to_string(num1 + num2));
            else if (token == "-") stah.push_back(to_string(num1 - num2));
            else if (token == "*") stah.push_back(to_string(num1 * num2));
            else stah.push_back(to_string(static_cast<int>(num1 / num2)));
        }
        return stoi(stah[0]);
    }
};
