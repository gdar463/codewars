#include <algorithm>
#include <cctype>
#include <string>
#include <vector>

std::vector<std::size_t> find_all(std::string text, std::string pattern) {
  std::vector<std::size_t> positions;
  size_t pos = text.find(pattern);
  while (pos != std::string::npos) {
    positions.push_back(pos);
    pos = text.find(pattern, pos + 1);
  }
  return positions;
}

std::string to_camel_case(std::string text) {
  std::vector<std::size_t> pos = find_all(text, "-");
  std::vector<std::size_t> posLower = find_all(text, "_");
  pos.insert(pos.end(), posLower.begin(), posLower.end());
  std::sort(pos.begin(), pos.end());
  for (int i = 0; i < pos.size(); i++) {
    text[pos[i] + 1 - i] = std::toupper(text[pos[i] + 1 - i]);
    text.erase(pos[i] - i, 1);
  }
  return text;
}
