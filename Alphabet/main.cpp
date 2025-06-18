#include <iostream>
#include <string>

std::string alphabet_position(const std::string &text);

int main(int argc, char *argv[]) {
  const std::string text = argv[1];

  std::cout << alphabet_position(text) << std::endl;

  return 0;
}
