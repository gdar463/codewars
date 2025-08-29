#include <iostream>
#include <vector>

std::vector<int> move_zeroes(const std::vector<int> &input);

int main(int argc, char *argv[]) {
  std::vector<int> input;
  for (int i = 0; i < argc; i++) {
    input.push_back(atoi(argv[i]));
  }

  for (int i : move_zeroes(input)) {
    std::cout << i << ' ';
  }
  std::cout << std::endl;

  return 0;
}
