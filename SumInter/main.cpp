#include <cstring>
#include <iostream>
#include <utility>
#include <vector>

int sum_intervals(std::vector<std::pair<int, int>> intervals);

int main(int argc, char *argv[]) {
  std::vector<std::pair<int, int>> intervals;
  for (int i = 1; i < argc; i++) {
    char *arg = strtok(argv[i], ",");
    int first = atoi(arg);
    arg = strtok(nullptr, ",");
    intervals.push_back(std::make_pair(first, atoi(arg)));
  }

  std::cout << sum_intervals(intervals) << std::endl;

  return 0;
}
