#include <iostream>
{{imports}}
#define println(string) (std::cout << string << std::endl);
#define print(string) (std::cout << string);

{{signature}} {
  println("Hello from {{project}}!")
  return 0;
}
