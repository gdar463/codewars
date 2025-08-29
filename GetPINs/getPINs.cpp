#include <string>
#include <unordered_map>
#include <vector>

std::unordered_map<char, std::vector<char>> variants = {
    {'0', {'8', '0'}},
    {'1', {'1', '2', '4'}},
    {'2', {'1', '2', '3', '5'}},
    {'3', {'2', '3', '6'}},
    {'4', {'1', '4', '5', '7'}},
    {'5', {'2', '4', '5', '6', '8'}},
    {'6', {'3', '5', '6', '9'}},
    {'7', {'4', '7', '8'}},
    {'8', {'5', '7', '8', '9', '0'}},
    {'9', {'6', '8', '9'}}};

std::vector<std::string> get_pins(std::string observed) {
  std::vector<std::string> out{""};

  for (char n : observed) {
    std::vector<std::string> temp;
    for (const std::string &pre : out) {
      for (char var : variants[n]) {
        temp.push_back(pre + var);
      }
    }
    out.swap(temp);
  }

  return out;
}
