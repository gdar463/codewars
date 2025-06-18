#include <string>

int calc(long long n, int i) {
  std::string str = std::to_string(n);
  if (str.length() == 1) {
    return i;
  }
  int out = 1;
  for (int j = 0; j < str.length(); j++) {
    out *= str[j] - '0';
  }
  return calc(out, i + 1);
}

int persistence(long long n) { return calc(n, 0); }
