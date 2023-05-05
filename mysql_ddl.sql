--K线图原始数据
create table stock_k_data_daily (
dt  varchar(20) comment '交易所行情日期',
code  varchar(20) comment '证券代码',
open_price  decimal(30,20) default null comment '开盘价',
high_price  decimal(30,20) default null comment '最高价',
low_price  decimal(30,20) default null comment '最低价',
close_price  decimal(30,20) default null comment '收盘价',
preclose_price  decimal(30,20) default null comment '前收盘价',
volume bigint default null comment '成交量（累计 单位：股）',
amount  decimal(50,20) default null comment '成交额（单位：人民币元）',
adjustflag  int default null comment '复权状态(1：后复权， 2：前复权，3：不复权）',
turn  decimal(30,20) default null comment '换手率：[指定交易日的成交量(股)/指定交易日的股票的流通股总股数(股)]*100%',
tradestatus  int default null comment '交易状态(1：正常交易 0：停牌)',
pctChg	 decimal(30,20) default null comment '涨跌幅（百分比）：日涨跌幅=[(指定交易日的收盘价-指定交易日前收盘价)/指定交易日前收盘价]*100%',
peTTM  decimal(30,20) default null comment '滚动市盈率:(指定交易日的股票收盘价/指定交易日的每股盈余TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/归属母公司股东净利润TTM',
pbMRQ  decimal(30,20) default null comment '市净率:(指定交易日的股票收盘价/指定交易日的每股净资产)=总市值/(最近披露的归属母公司股东的权益-其他权益工具)',
psTTM  decimal(30,20) default null comment '滚动市销率:(指定交易日的股票收盘价/指定交易日的每股销售额)=(指定交易日的股票收盘价*截至当日公司总股本)/营业总收入TTM',
pcfNcfTTM  decimal(30,20) default null comment '滚动市现率:(指定交易日的股票收盘价/指定交易日的每股现金流TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/现金以及现金等价物净增加额TTM',
isST  int default null comment '是否ST股，1是，0否'
) comment '股票K线数据';
