#include "base_feature.hpp"

namespace intproj {

class NTradesFeature : public BaseFeature
{
  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        return data.size();
    }
};


}// namespace intproj
