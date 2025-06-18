#include <string>

std::string alphabet_position(const std::string &text) {
  std::string out = "";
  for (int i = 0; i < text.length(); i++) {
    if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122))
      out +=
          std::to_string(((text[i] & 0b11011111) ^ 0b100000) - 'a' + 1) + ' ';
  }
  return out.substr(0, out.size() - 1);
}
