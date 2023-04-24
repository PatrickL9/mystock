import baostock as bs
import pandas as pd
import sys
import datetime

pd.set_option('display.width', None)  # 设置字符显示无限制
pd.set_option('display.max_rows', None)  # 设置行数显示无限制


def get_stock_codes(date=None):
    """
    获取指定日期的A股代码列表
    若参数date为空，则返回最近1个交易日的A股代码列表
    若参数date不为空，且为交易日，则返回date当日的A股代码列表
    若参数date不为空，但不为交易日，则打印提示非交易日信息，程序退出
    :param date: 日期
    :return: A股代码的列表
    """

    # 登录baostock
    bs.login()

    # 从BaoStock查询股票数据
    stock_df = bs.query_all_stock(date).get_data()

    # 如果获取数据长度为0，表示日期date非交易日
    if 0 == len(stock_df):

        # 如果设置了参数date，则打印信息提示date为非交易日
        if date is not None:
            print('当前选择日期为非交易日或尚无交易数据，请设置date为历史某交易日日期')
            sys.exit(0)

        # 未设置参数date，则向历史查找最近的交易日，当获取股票数据长度非0时，即找到最近交易日
        delta = 1
        while 0 == len(stock_df):
            stock_df = bs.query_all_stock(datetime.date.today() - datetime.timedelta(days=delta)).get_data()
            delta += 1

    # 注销登录
    bs.logout()

    # 筛选股票数据，上证和深证股票代码在sh.600000与sz.39900之间
    stock_df = stock_df[(stock_df['code'] >= 'sh.600000') & (stock_df['code'] < 'sz.399000')]

    # 返回股票列表
    return stock_df['code'].tolist()


def get_stock_data(stock_codes):
    # 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取沪深A股历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    for stock_code in stock_codes:
        rs = bs.query_history_k_data_plus(stock_code,
                                          "date, code, open, high, low, close, preclose, volume, amount, adjustflag, turn, \
                                            tradestatus, pctChg, isST",
                                          start_date='2023-01-01',
                                          end_date='2023-04-24',
                                          frequency="d",
                                          adjustflag="3"
                                          )
        print('query_history_k_data_plus respond error_code:' + rs.error_code)
        print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

        # 打印结果集 ####
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        # 结果集输出到csv文件 ####
        # result.to_csv("D:\\history_A_stock_k_data.csv", index=False)
        print(result)

    # 登出系统 ####
    bs.logout()


if __name__ == '__main__':
    get_stock_data(get_stock_codes())
