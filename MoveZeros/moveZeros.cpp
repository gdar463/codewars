#include <vector>

std::vector<int> move_zeroes(const std::vector<int> &input) {
  std::vector<int> out;
  int zeros = 0;
  for (int n : input) {
    if (n == 0) {
      zeros++;
      out.push_back(0);
    } else {
      out.emplace(out.end() - zeros, n);
    }
  }
  return out;
}
