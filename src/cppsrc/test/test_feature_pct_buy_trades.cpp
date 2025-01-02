#include "../percent_buy_feature.hpp"
#include "gtest/gtest.h"

using namespace intproj;

TEST(FeatureTests, PctBuyTest)
{
    PercentBuyFeature ptf;
    EXPECT_NEAR(ptf.compute_feature({ { 1, 1, false } }), 0, 1e-2);
    EXPECT_NEAR(ptf.compute_feature({ { 1, 1, false }, { 1, 1, true } }), 0.5, 1e-2);
    EXPECT_NEAR(ptf.compute_feature({ { 1, 1, true } }), 1, 1e-2);
}
