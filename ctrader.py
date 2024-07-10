import clr
clr.AddReference('QuantConnect.Indicators')
clr.AddReference('QuantConnect.Common')

from QuantConnect.Orders import OrderStatus
from QuantConnect.Securities import OrderDirection
from QuantConnect.Orders import MarketOrder, OrderSubmission
from QuantConnect.Algorithm.Framework.Alphas import IAlphaModel
from QuantConnect.Orders import UpdateOrderRequest
from QuantConnect.Securities.Forex import Forex
from QuantConnect.Orders.Fees import ConstantFeeModel

class MyAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2023, 1, 1)
        self.SetCash(100000)

        self.symbol = self.AddForex('EURUSD', Resolution.Minute)
        self.Schedule.On(self.DateRules.EveryDay(), self.TimeRules.AfterMarketOpen('EURUSD', 10), self.Rebalance)

    def OnData(self, slice):
        pass

    def Rebalance(self):
        # Your signal logic here
        last_close, sma, direction = self.Signal('EURUSD', Resolution.Minute, 10)

        # Close existing positions
        for position in self.Portfolio.Values:
            if direction == 'buy' and position.IsShort:
                self.Liquidate(position.Symbol)
            elif direction == 'sell' and position.IsLong:
                self.Liquidate(position.Symbol)

        # Market order
        if direction == 'buy':
            self.MarketOrder('EURUSD', 1000)
        elif direction == 'sell':
            self.MarketOrder('EURUSD', -1000)

    def Signal(self, symbol, resolution, sma_period):
        history = self.History([symbol], 20, resolution)
        bars = [x.Close for x in history.itertuples()]
        last_close = bars[-1]
        sma = sum(bars) / len(bars)

        direction = 'flat'
        if last_close > sma:
            direction = 'buy'
        elif last_close < sma:
            direction = 'sell'

        return last_close, sma, direction
