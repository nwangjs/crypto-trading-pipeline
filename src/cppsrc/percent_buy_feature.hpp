#include "base_feature.hpp"
#include <algorithm>

namespace intproj {

class PercentBuyFeature : public BaseFeature
{
  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        return static_cast<float>(std::count_if(data.begin(), data.end(), [](const std::tuple<float, float, bool> &t) {
            return std::get<2>(t);
        })) / data.size();
    }
};


}// namespace intproj