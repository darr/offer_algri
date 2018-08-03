/////////////////////////////////////
// File name : c.cpp
// Create date : 2018-07-23 08:53
// Modified date : 2018-07-23 11:24
// Author : DARREN
// Describe : not set
// Email : lzygzh@126.com
////////////////////////////////////


class Solution{
private:
    stack<int> stack1;
    stack<int> stack2;
public:
    //run:4ms memory:460k
    void push(int node) {
        stack1.push(node);
    }
    
    int pop() {
        if (stack2.empty())
            while(!stack1.empty()){
                stack2.push(stack1.top());
                stack1.pop();
            }

        int ret = stack2.top();
        stack2.pop();
        return ret;
    }
};



