#include <iostream>
#include <string>
#include <vector>

std::vector<char> uniqueInOrder(const std::string& iterable);

int main(int argc, char* argv[]) {
  	const std::string& iterable = argv[1];
  
  for (char i: uniqueInOrder(iterable)) {
    std::cout << i << ' ';
  }
  std::cout << std::endl;

  return 0;
}
