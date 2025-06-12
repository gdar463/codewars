#include <iostream>
#include <string>

bool solution(std::string const &str, std::string const &ending);

int main(int argc, char *argv[]) {
  const std::string str = argv[0];
  const std::string ending = argv[1];

  std::cout << solution(str, ending);

  return 0;
}
