#include <iostream>
#include <map>
#include <string>
#include <vector>
using std::map;
using std::vector;

class Solution {
 public:
  vector<int> twoSum(vector<int> &nums, int target) {
    map<int, int> d;
    map<int, int>::iterator iter;
    int count = nums.size();

    for (int i = 0; i < count; i++) {
      int num = nums[i];
      int to_find = target - num;
      iter = d.find(to_find);  // 查找表
      if (!(iter == d.end())) {
        vector<int> ret = {};
        ret = {d[to_find], i};
        return ret;
      } else {
        d[num] = i;
      }
    }

    return {-1};
  }
};

int main(int argc, char **argv) {
  vector<int> nums = {2, 7, 11, 15};
  int target = 9;
  vector<int> ans;
  Solution sol = Solution();
  ans = sol.twoSum(nums, target);

  for (int i = 0; i < ans.size(); i++) {
    std::cout << ans[i] << " ";
  }
  std::cout << std::endl;

  return 0;
}
