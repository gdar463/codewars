#include <cctype>
#include <string>
#include <unordered_map>

std::size_t duplicateCount(const std::string &in) {
  std::size_t count = 0;
  std::unordered_map<char, int> found;
  for (int i = 0; i < in.length(); i++) {
    char curr = std::tolower(in[i]);
    found.insert_or_assign(
        curr, found.find(curr) != found.end() ? found.at(curr) + 1 : 1);
  }
  for (auto const &x : found) {
    if (x.second > 1) {
      count++;
    }
  }
  return count;
}
