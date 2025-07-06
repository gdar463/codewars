#include <string>
#include <vector>

template <typename T>
std::vector<T> uniqueInOrder(const std::vector<T> &iterable) {
  std::vector<T> output = {' '};
  for (T single : iterable) {
    if (output.back() != single) {
      output.push_back(single);
    }
  }
  output.erase(output.begin());
  return output;
}

std::vector<char> uniqueInOrder(const std::string &iterable) {
  std::vector<char> output = {' '};
  for (char single : iterable) {
    if (output.back() != single) {
      output.push_back(single);
    }
  }
  output.erase(output.begin());
  return output;
}
