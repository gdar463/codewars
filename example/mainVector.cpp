#include <iostream>
{{imports}}
{{signature}}

int main(int argc, char* argv[]) {
{{inputs}}
  
  for ({{type}} i: {{call}}) {
    std::cout << i << ' ';
  }
  std::cout << std::endl;

  return 0;
}
