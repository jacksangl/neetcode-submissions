class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> timemap;
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        this->timemap[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
    if (!timemap.contains(key)) return "";

    auto& vec = timemap[key];
    int l = 0, r = vec.size() - 1;
    string res = "";

    while (l <= r) {
        int m = l + (r - l) / 2;

        if (vec[m].first <= timestamp) {
            res = vec[m].second; 
            l = m + 1;           
        } else {
            r = m - 1;
        }
    }

    return res;
}
};
