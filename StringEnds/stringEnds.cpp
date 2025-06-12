#include <algorithm>
#include <string>

bool solution(std::string const &str, std::string const &ending) {
  std::string::const_iterator str_end = str.end() - 1;
  std::string::const_iterator ending_end = ending.end() - 1;
  for (int i = 0; i < std::min(ending.length(), str.length()); i++) {
    if (*str_end != *ending_end) {
      return false;
    }
    str_end--;
    ending_end--;
  }
  return true;
}
