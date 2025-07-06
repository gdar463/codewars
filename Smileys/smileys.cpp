#include <string>
#include <vector>

int countSmileys(std::vector<std::string> arr) {
  int count = 0;
  for (std::string face : arr) {
    if (face.front() == ':' || face.front() == ';') {
      char second = *(face.begin() + 1);
      if (second == '-' || second == '~') {
        if (face.back() == ')' || face.back() == 'D') {
          count++;
        }
      } else if (second == ')' || second == 'D') {
        count++;
      }
    }
  }
  return count;
}
