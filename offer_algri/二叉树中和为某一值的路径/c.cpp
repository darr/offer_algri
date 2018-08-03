/////////////////////////////////////
// File name : c.cpp
// Create date : 2018-07-23 08:53
// Modified date : 2018-07-23 11:24
// Author : DARREN
// Describe : not set
// Email : lzygzh@126.com
////////////////////////////////////


/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {

public:
    //run:3ms memory:484k
    vector<vector<int>> FindPath(TreeNode* root, int expectNumber){
        vector<vector<int>> ret;
        vector<int> lt;
        if (NULL == root) return ret;
        return FindAPath(root,expectNumber,ret,lt);
    }
    
    vector<vector<int>> FindAPath(TreeNode* root, int expectNumber, 
                                  vector<vector<int>> &path_list,vector<int> lt){
        if (NULL == root) return path_list;
        expectNumber -= root->val;
        lt.push_back(root->val);
        if (expectNumber != 0){
            vector<int> left_lt(lt);
            FindAPath(root->left,expectNumber,path_list,lt);
            vector<int> right_lt(lt);
            FindAPath(root->right,expectNumber,path_list,lt);
        }else if(NULL == root->left && NULL == root->right)
            path_list.push_back(lt);
        return path_list;
    }
    
    //run:3ms memory:480k
    vector<vector<int> > FindPath2(TreeNode* root,int expectNumber){
        if(root) dfsFind(root, expectNumber);
        return allRes;
    }
     
    void dfsFind(TreeNode * node , int target){
        tmp.push_back(node->val);
        if(!node->left && !node->right){
            if(target - node->val == 0) allRes.push_back(tmp);
        }else{
            if(node->left) dfsFind(node->left, target - node->val);
            if(node->right) dfsFind(node->right, target - node->val);
        }
         
        if(!tmp.empty())
            tmp.pop_back();
    }
    private:
        vector<vector<int> >allRes;
        vector<int> tmp;
};