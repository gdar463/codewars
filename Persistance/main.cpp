#include <iostream>

int persistence(long long n);

int main(int argc, char* argv[]) {
  long long n = std::atoll(argv[1]);
  
  std::cout << persistence(n) << std::endl;

  return 0;
}
