import backtrader as bt
from datetime import datetime
import yfinance as yf

class MovingAverageStrategy(bt.Strategy):

    params = (('period_fast', 30), ('period_slow', 200))

    def __init__(self):
        self.close_data = self.data.close

        self.fast_sma = bt.indicators.MovingAverageSimple(self.close_data, period=self.params.period_fast)
        self.slow_sma = bt.indicators.MovingAverageSimple(self.close_data, period=self.params.period_slow)
        

    def next(self):
        if not self.position:
            if self.fast_sma[0] > self.slow_sma[0] and self.fast_sma[-1] < self.slow_sma[-1]:
                self.buy()
        else:
            if self.fast_sma[0] < self.slow_sma[0] and self.fast_sma[-1] > self.slow_sma[-1]:
                self.close()



if __name__ == '__main__':
    cerebro = bt.Cerebro()

    df = yf.download('AAPL', start='2015-01-01', end='2020-01-01')
    data = bt.feeds.PandasData(dataname=df)

    cerebro.adddata(data)
    cerebro.addstrategy(MovingAverageStrategy)

    cerebro.addobserver(bt.observers.Value)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate=0)
    cerebro.addanalyzer(bt.analyzers.Returns)
    cerebro.addanalyzer(bt.analyzers.DrawDown)

    cerebro.broker.set_cash(3000)
    print('Initial capital: $%.2f' % cerebro.broker.getvalue()) 

    cerebro.broker.setcommission(0.01)

    results = cerebro.run()

    print('Sharpe ratio: %.2f' % results[0].analyzers.sharperatio.get_analysis()['sharperatio'])
    print('Return: %.2f%%' % results[0].analyzers.returns.get_analysis()['rnorm100'])
    print('Max drawdown: %.2f%%' % results[0].analyzers.drawdown.get_analysis()['max']['drawdown'])
    print('Capital: $%.2f' % cerebro.broker.getvalue())
