#include <iostream>
#include <string>

std::size_t duplicateCount(const std::string &in);

int main(int argc, char *argv[]) {
  const std::string &in = argv[1];

  std::cout << duplicateCount(in) << std::endl;

  return 0;
}
