using ull = unsigned long long;

unsigned int countBits(ull n) {
  unsigned int count = 0;
  while (n != 0) {
    ull shifted = n & 1;
    if (shifted == 1)
      count++;
    n >>= 1;
  }
  return count;
}
