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
    long long tid;
    float price;
    float amount;
    std::string exchange;
    std::string type;

    trade(long long timestamp,
      long long timestampms,
      long long tid,
      float price,
      float amount,
      std::string exchange,
      std::string type)
      : timestamp(timestamp), timestampms(timestampms), tid(tid), price(price), amount(amount), exchange(exchange),
        type(type)
    {}
};

class DataClient
{
  private:
    std::unordered_map<std::string, std::vector<trade>> data;
    long long last_tid = 0;

    int _query_api(const std::string symbol)
    {
        try {
            std::string url = BASE_URL + symbol;
            cpr::Response response;

            response = cpr::Get(
              cpr::Url{ url }, cpr::Parameters{ { "since_tid", std::to_string(last_tid) } }, cpr::VerifySsl{ false });

            if (response.status_code == 200) {
                auto trade_history = nlohmann::json::parse(response.text);
                _parse_message(symbol, trade_history);

                if (!trade_history.empty()) {
                    last_tid = static_cast<long long>(trade_history[0]["tid"]);
                } else {
                    std::cerr << "No trades retrieved from API Query" << std::endl;
                    return 1;
                }

            } else {
                std::cerr << "API Query failed with status code: " << response.status_code << std::endl;
                std::cerr << "Response text: " << response.text << std::endl;
                std::cerr << "Error details: " << response.error.message << std::endl;
                return 1;
            }

        } catch (const std::exception &e) {
            std::cerr << "API Query Failed: " << e.what() << std::endl;
            return 1;
        }

        return 0;
    }

    void _parse_message(const std::string symbol, const nlohmann::json &trade_history)
    {
        std::vector<trade> trades;

        for (const auto &entry : trade_history) {
            trade t(entry["timestamp"],
              entry["timestampms"],
              entry["tid"],
              std::stof(entry["price"].get<std::string>()),
              std::stof(entry["amount"].get<std::string>()),
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
        if (_query_api(symbol)) { return {}; }

        return data[symbol];
    }
};

}// namespace intproj
