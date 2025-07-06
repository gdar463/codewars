#include <iostream>
#include <string>
#include <vector>

int countSmileys(std::vector<std::string> arr);

int main(int argc, char* argv[]) {
	std::vector<std::string> arr(argv + 1, argv + argc);
  
  std::cout << countSmileys(arr) << std::endl;

  return 0;
}
