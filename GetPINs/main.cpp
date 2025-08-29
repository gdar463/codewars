#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> get_pins(std::string observed);

int main(int argc, char* argv[]) {
	std::string observed = argv[1];
  
  for (std::string i: get_pins(observed)) {
    std::cout << i << ' ';
  }
  std::cout << std::endl;

  return 0;
}
