#include <algorithm>
#include <climits>
#include <string>
#include <unordered_map>
#include <utility>

using Ingredients = std::unordered_map<std::string, int>;
using IngredientPair = std::pair<const std::string, const int>;

int cakes(const Ingredients &recipe, const Ingredients &available) {
  for (IngredientPair n : recipe) {
    if (available.find(n.first) == available.end()) {
      return 0;
    }
  }
  int min = INT_MAX;
  for (IngredientPair n : available) {
    if (auto found = recipe.find(n.first); found != recipe.end()) {
      min = std::min(min, n.second / found->second);
    }
  }
  return min;
}
