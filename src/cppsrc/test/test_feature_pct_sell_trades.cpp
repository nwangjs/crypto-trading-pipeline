#include "../percent_sell_feature.hpp"
#include "gtest/gtest.h"

using namespace intproj;

TEST(FeatureTests, PctSellTest)
{
    PercentSellFeature psf;
    EXPECT_NEAR(psf.compute_feature({ { 1, 1, false } }), 1, 1e-2);
    EXPECT_NEAR(psf.compute_feature({ { 1, 1, false }, { 1, 1, true } }), 0.5, 1e-2);
    EXPECT_NEAR(psf.compute_feature({ { 1, 1, false }, { 1, 1, true }, { 1, 2, false } }), 0.67, 1e-2);
}
