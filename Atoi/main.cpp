#include <iostream>
#include <string>

int string_to_number(const std::string& s);

int main(int argc, char* argv[]) {
  const std::string& s = argv[1];
  
  std::cout << string_to_number(s) << std::endl;

  return 0;
}
