/////////////////////////////////////
// File name : c.cpp
// Create date : 2018-07-23 08:53
// Modified date : 2018-07-23 11:24
// Author : DARREN
// Describe : not set
// Email : lzygzh@126.com
////////////////////////////////////


class Solution {
public:
    //run:141ms memory:4944k
    int InversePairs(vector<int> data) {
        if(data.size() == 0){
            return 0;
        }
        vector<int> copy;
        for(int i = 0; i < data.size(); ++i){
            copy.push_back(data[i]);
        }
        return InversePairsCore(data, copy, 0, data.size() - 1) % 1000000007;
    }
    
    long InversePairsCore(vector<int> &data, vector<int> &copy, int begin, int end){
        if(begin == end){
            copy[begin] = data[end];
            return 0;
        }
        int mid = (end + begin) >> 1;
        long leftCount = InversePairsCore(copy, data, begin, mid);
        long rightCount = InversePairsCore(copy, data, mid + 1, end);
        int i = mid;
        int j = end;
        int indexcopy = end;
        long count = 0;
        while(i >= begin && j >= mid + 1){
            if(data[i] > data[j]){
                copy[indexcopy--] = data[i--];
                count += j - mid;
            }
            else{
                copy[indexcopy--] = data[j--];
            }
        }
        for(;i >= begin; --i){
            copy[indexcopy--] = data[i];
        }
        for(;j >= mid + 1; --j){
            copy[indexcopy--] = data[j];
        }
        return leftCount + rightCount + count;
    }
};