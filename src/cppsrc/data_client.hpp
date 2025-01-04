#include <cpr/cpr.h>
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>
#include <unordered_map>
#include <vector>

namespace intproj {

const std::string BASE_URL = "https://api.gemini.com/v1/trades/";

struct trade
{
    long long timestamp;
    long long timestampms;
    float price;
    float amount;
    std::string exchange;
    std::string type;

    trade(long long timestamp, long long timestampms, float price, float amount, std::string exchange, std::string type)
      : timestamp(timestamp), timestampms(timestampms), price(price), amount(amount), exchange(exchange), type(type)
    {}
};

class DataClient
{
  private:
    std::unordered_map<std::string, std::vector<trade>> data;
    long long last_timestampms = 0;

    void _query_api(const std::string symbol)
    {
        try {
            std::string url = BASE_URL + symbol;
            cpr::Response response;

            if (last_timestampms) {
                response =
                  cpr::Get(cpr::Url{ url }, cpr::Parameters{ { "timestamp", std::to_string(last_timestampms) } });
            } else {
                response = cpr::Get(cpr::Url{ url });
            }

            if (response.status_code == 200) {
                auto trade_history = nlohmann::json::parse(response.text);

                if (!trade_history.empty()) {
                    last_timestampms = trade_history[0]["timestampms"];
                } else {
                    std::cerr << "No trades retrieved from API Query" << std::endl;
                }

                _parse_message(symbol, trade_history);
            } else {
                std::cerr << "API Query response code is not 200 OK" << std::endl;
            }

        } catch (const std::exception &e) {
            std::cerr << "API Query Failed: " << e.what() << std::endl;
        }
    }

    void _parse_message(const std::string symbol, const nlohmann::json &trade_history)
    {
        std::vector<trade> trades;

        for (const auto &entry : trade_history) {
            trade t(entry["timestamp"],
              entry["timestampms"],
              entry["price"],
              entry["amount"],
              entry["exchange"],
              entry["type"]);
            trades.push_back(t);
        }

        data[symbol] = trades;
    }

  public:
    DataClient() {}

    std::vector<trade> get_data(const std::string symbol)
    {
        _query_api(symbol);
        return data[symbol];
    }
};

}// namespace intproj
