#include <algorithm>
#include <utility>
#include <vector>

int sum_intervals(std::vector<std::pair<int, int>> intervals) {
  std::sort(intervals.begin(), intervals.end());
  int out = 0;
  int start = intervals[0].first;
  int end = intervals[0].second;
  for (int i = 1; i < intervals.size(); i++) {
    int currStart = intervals[i].first;
    int currEnd = intervals[i].second;
    if (currStart <= end) {
      end = std::max(currEnd, end);
    } else {
      out += (end - start);
      start = currStart;
      end = currEnd;
    }
  }
  out += end - start;
  return out;
}
