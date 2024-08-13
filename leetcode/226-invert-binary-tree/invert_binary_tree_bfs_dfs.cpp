/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */

#include <queue>
#include <stack>
using std::queue;
using std::stack;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
 public:
  TreeNode *invertTreeBFS(TreeNode *root) {
    // invertTreeBFS
    // 层序遍历方式翻转
    // 用队列实现
    if (root == nullptr) return root;
    queue<TreeNode *> q;
    q.push(root);
    TreeNode *node;
    while (!q.empty()) {
      node = q.front();
      q.pop();
      TreeNode *tmp = node->left;
      node->left = node->right;
      node->right = tmp;
      if (node->left != nullptr) q.push(node->left);
      if (node->right != nullptr) q.push(node->right);
    }
    return root;
  }

  TreeNode *invertTreeDFS(TreeNode *root) {
    // invertTreeDFS
    // 深度优先遍历的方式翻转
    // 用栈实现
    if (root == nullptr) return root;
    stack<TreeNode *> s;
    s.push(root);
    TreeNode *node;
    while (!s.empty()) {
      node = s.top();
      s.pop();
      TreeNode *tmp = node->left;
      node->left = node->right;
      node->right = tmp;
      if (node->right != nullptr) s.push(node->right);
      if (node->left != nullptr) s.push(node->left);
    }
    return root;
  }
};