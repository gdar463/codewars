#include <iostream>
#include <string>

unsigned int countBits(unsigned long long n);

int main(int argc, char *argv[]) {
  unsigned long long n = std::stoull(argv[1]);

  std::cout << int(n) << std::endl;

  return 0;
}
