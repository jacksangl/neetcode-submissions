class MinStack {
public:
    vector<int> regstack;
    vector<int> minstack;
    
    void push(int val) {
        this->regstack.push_back(val);
        if (this->minstack.size() == 0 || val <= this->minstack.back()) this->minstack.push_back(val);
    }
    
    void pop() {
        int val = this->regstack.back();
        this->regstack.pop_back();
        if (val == this->minstack.back()) this->minstack.pop_back();
    }
    
    int top() {
        return this->regstack.back();
    }
    
    int getMin() {
        return this->minstack.back();
    }
};
