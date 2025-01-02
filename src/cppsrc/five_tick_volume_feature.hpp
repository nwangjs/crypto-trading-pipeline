#include "base_feature.hpp"
#include <numeric>
#include <queue>

namespace intproj {

class FiveTickVolumeFeature : public BaseFeature
{
  private:
    std::queue<int> q;
    int last_five_volume = 0;

  public:
    float compute_feature(std::vector<std::tuple<float, float, bool>> data)
    {
        int curr_tick_volume =
          std::accumulate(data.begin(), data.end(), 0, [](int sum, const std::tuple<float, float, bool> &t) {
              return sum + std::get<1>(t);
          });

        q.push(curr_tick_volume);
        last_five_volume += curr_tick_volume;

        if (q.size() > 5) {
            last_five_volume -= q.front();
            q.pop();
        }

        return last_five_volume;
    }

    virtual ~FiveTickVolumeFeature() {}
};


}// namespace intproj
