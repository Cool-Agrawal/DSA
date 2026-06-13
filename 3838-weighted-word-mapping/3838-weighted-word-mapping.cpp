class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        string res;
        for(string& word : words){
            int total = 0;
            for(char i : word){
                total += weights[i-'a'];
            }
            int mod = total%26;
            char mapped = 'z'-mod;
            res.push_back(mapped);
        }
        return res;
    }
};