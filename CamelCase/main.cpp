#include <iostream>
#include <string>

std::string to_camel_case(std::string text);

int main(int argc, char *argv[]) {
  std::string text = argv[1];

  std::cout << to_camel_case(text) << std::endl;

  return 0;
}
