#include <iostream>
#include <string>

bool solution(std::string const &str, std::string const &ending);

int main(int argc, char *argv[]) {
  const std::string str = argv[1];
  const std::string ending = argv[2];

  std::cout << solution(str, ending) << std::endl;

  return 0;
}
