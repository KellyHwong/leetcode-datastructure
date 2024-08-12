#include <iostream>
#include <map>
#include <string>
#include <vector>
using std::map;
using std::vector;

class Solution {
 public:
  void setZeroes(vector<vector<int>> &matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    bool first_row = false;
    bool first_col = false;

    if (matrix[0][0] == 0) {
      first_row = true;
      first_col = true;
    }

    for (int i = 0; i < m; i++) {
      if (matrix[i][0] == 0) {
        first_col = true;
        break;
      }
    }
    for (int j = 0; j < n; j++) {
      if (matrix[0][j] == 0) {
        first_row = true;
        break;
      }
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] == 0) {
          matrix[i][0] = 0;  // 第i行的最上方作为标记
          matrix[0][j] = 0;  // 第j列的最左方作为标记
        }
      }
    }

    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        if (matrix[i][0] == 0 || matrix[0][j] == 0) {
          matrix[i][j] = 0;
        }
      }
    }

    if (first_row) {
      for (int j = 1; j < n; j++) {
        matrix[0][j] = 0;
      }
    }
    if (first_col) {
      for (int i = 1; i < m; i++) {
        matrix[i][0] = 0;
      }
    }
  };
};

void print_matrix(vector<vector<int>> &matrix) {
  int m = matrix.size();
  int n = matrix[0].size();

  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      std::cout << matrix[i][j] << ' ';
    }
    std::cout << '\n';
  }
}

int main(int argc, char **argv) {
  vector<vector<int>> matrix = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
  //   Solution sol = Solution();
  //   ans = sol.twoSum(nums, target);
  print_matrix(matrix);
  Solution sol = Solution();
  sol.setZeroes(matrix);
  print_matrix(matrix);
  return 0;
}