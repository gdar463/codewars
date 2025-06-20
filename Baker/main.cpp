#include <iostream>
#include <regex>
#include <string>
#include <unordered_map>

using Ingredients = std::unordered_map<std::string, int>;

int cakes(const Ingredients &recipe, const Ingredients &available);

Ingredients get_from_string(std::string input) {
  Ingredients out;
  std::regex pairRegex("\\{\\s*\"([^\"]+)\"\\s*,\\s*(\\d+)\\s*\\}");
  auto begin = std::sregex_iterator(input.begin(), input.end(), pairRegex);
  auto end = std::sregex_iterator();

  for (auto it = begin; it != end; ++it) {
    std::smatch match = *it;
    std::string key = match[1];
    int value = std::stoi(match[2]);
    out[key] = value;
  }
  return out;
}

int main(int argc, char *argv[]) {
  Ingredients recipe;
  Ingredients available;

  std::string first = argv[1];
  std::string second = argv[2];

  std::cout << cakes(get_from_string(first), get_from_string(second))
            << std::endl;

  return 0;
}
