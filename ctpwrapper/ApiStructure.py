# encoding=utf-8
import ctypes
from ctpwrapper.base import Base


class DisseminationField(Base):
    """信息分发"""
    _fields_ = [
        ('SequenceSeries', ctypes.c_short),  # 序列系列号
        ('SequenceNo', ctypes.c_int),  # 序列号
    ]

    def __init__(self, SequenceSeries: int = 0, SequenceNo: int = 0):
        super(DisseminationField, self).__init__()
        self.SequenceSeries = int(SequenceSeries)
        self.SequenceNo = int(SequenceNo)


class ReqUserLoginField(Base):
    """用户登录请求"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Password', ctypes.c_char * 41),  # 密码
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', ctypes.c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', ctypes.c_char * 11),  # 协议信息
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('OneTimePassword', ctypes.c_char * 41),  # 动态密码
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('LoginRemark', ctypes.c_char * 36),  # 登录备注
        ('ClientIPPort', ctypes.c_int),  # 终端IP端口
        ('ClientIPAddress', ctypes.c_char * 33),  # 终端IP地址
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', UserID: str = '', Password: str = '', UserProductInfo: str = '', InterfaceProductInfo: str = '', ProtocolInfo: str = '',
                 MacAddress: str = '', OneTimePassword: str = '', reserve1: str = '', LoginRemark: str = '', ClientIPPort: int = 0, ClientIPAddress: str = ''):
        super(ReqUserLoginField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.Password = self._to_bytes(Password)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.InterfaceProductInfo = self._to_bytes(InterfaceProductInfo)
        self.ProtocolInfo = self._to_bytes(ProtocolInfo)
        self.MacAddress = self._to_bytes(MacAddress)
        self.OneTimePassword = self._to_bytes(OneTimePassword)
        self.reserve1 = self._to_bytes(reserve1)
        self.LoginRemark = self._to_bytes(LoginRemark)
        self.ClientIPPort = int(ClientIPPort)
        self.ClientIPAddress = self._to_bytes(ClientIPAddress)


class RspUserLoginField(Base):
    """用户登录应答"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('LoginTime', ctypes.c_char * 9),  # 登录成功时间
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('SystemName', ctypes.c_char * 41),  # 交易系统名称
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('MaxOrderRef', ctypes.c_char * 13),  # 最大报单引用
        ('SHFETime', ctypes.c_char * 9),  # 上期所时间
        ('DCETime', ctypes.c_char * 9),  # 大商所时间
        ('CZCETime', ctypes.c_char * 9),  # 郑商所时间
        ('FFEXTime', ctypes.c_char * 9),  # 中金所时间
        ('INETime', ctypes.c_char * 9),  # 能源中心时间
        ('SysVersion', ctypes.c_char * 41),  # 后台版本信息
        ('GFEXTime', ctypes.c_char * 9),  # 广期所时间
    ]

    def __init__(self, TradingDay: str = '', LoginTime: str = '', BrokerID: str = '', UserID: str = '', SystemName: str = '', FrontID: int = 0, SessionID: int = 0, MaxOrderRef: str = '',
                 SHFETime: str = '', DCETime: str = '', CZCETime: str = '', FFEXTime: str = '', INETime: str = '', SysVersion: str = '', GFEXTime: str = ''):
        super(RspUserLoginField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.LoginTime = self._to_bytes(LoginTime)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.SystemName = self._to_bytes(SystemName)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.MaxOrderRef = self._to_bytes(MaxOrderRef)
        self.SHFETime = self._to_bytes(SHFETime)
        self.DCETime = self._to_bytes(DCETime)
        self.CZCETime = self._to_bytes(CZCETime)
        self.FFEXTime = self._to_bytes(FFEXTime)
        self.INETime = self._to_bytes(INETime)
        self.SysVersion = self._to_bytes(SysVersion)
        self.GFEXTime = self._to_bytes(GFEXTime)


class UserLogoutField(Base):
    """用户登出请求"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = ''):
        super(UserLogoutField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class ForceUserLogoutField(Base):
    """强制交易员退出"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = ''):
        super(ForceUserLogoutField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class ReqAuthenticateField(Base):
    """客户端认证请求"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('AuthCode', ctypes.c_char * 17),  # 认证码
        ('AppID', ctypes.c_char * 33),  # App代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', UserProductInfo: str = '', AuthCode: str = '', AppID: str = ''):
        super(ReqAuthenticateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.AuthCode = self._to_bytes(AuthCode)
        self.AppID = self._to_bytes(AppID)


class RspAuthenticateField(Base):
    """客户端认证响应"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('AppID', ctypes.c_char * 33),  # App代码
        ('AppType', ctypes.c_char),  # App类型
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', UserProductInfo: str = '', AppID: str = '', AppType: str = ''):
        super(RspAuthenticateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.AppID = self._to_bytes(AppID)
        self.AppType = self._to_bytes(AppType)


class AuthenticationInfoField(Base):
    """客户端认证信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('AuthInfo', ctypes.c_char * 129),  # 认证信息
        ('IsResult', ctypes.c_int),  # 是否为认证结果
        ('AppID', ctypes.c_char * 33),  # App代码
        ('AppType', ctypes.c_char),  # App类型
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('ClientIPAddress', ctypes.c_char * 33),  # 终端IP地址
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', UserProductInfo: str = '', AuthInfo: str = '', IsResult: int = 0, AppID: str = '', AppType: str = '', reserve1: str = '',
                 ClientIPAddress: str = ''):
        super(AuthenticationInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.AuthInfo = self._to_bytes(AuthInfo)
        self.IsResult = int(IsResult)
        self.AppID = self._to_bytes(AppID)
        self.AppType = self._to_bytes(AppType)
        self.reserve1 = self._to_bytes(reserve1)
        self.ClientIPAddress = self._to_bytes(ClientIPAddress)


class RspUserLogin2Field(Base):
    """用户登录应答2"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('LoginTime', ctypes.c_char * 9),  # 登录成功时间
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('SystemName', ctypes.c_char * 41),  # 交易系统名称
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('MaxOrderRef', ctypes.c_char * 13),  # 最大报单引用
        ('SHFETime', ctypes.c_char * 9),  # 上期所时间
        ('DCETime', ctypes.c_char * 9),  # 大商所时间
        ('CZCETime', ctypes.c_char * 9),  # 郑商所时间
        ('FFEXTime', ctypes.c_char * 9),  # 中金所时间
        ('INETime', ctypes.c_char * 9),  # 能源中心时间
        ('RandomString', ctypes.c_char * 17),  # 随机串
    ]

    def __init__(self, TradingDay: str = '', LoginTime: str = '', BrokerID: str = '', UserID: str = '', SystemName: str = '', FrontID: int = 0, SessionID: int = 0, MaxOrderRef: str = '',
                 SHFETime: str = '', DCETime: str = '', CZCETime: str = '', FFEXTime: str = '', INETime: str = '', RandomString: str = ''):
        super(RspUserLogin2Field, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.LoginTime = self._to_bytes(LoginTime)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.SystemName = self._to_bytes(SystemName)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.MaxOrderRef = self._to_bytes(MaxOrderRef)
        self.SHFETime = self._to_bytes(SHFETime)
        self.DCETime = self._to_bytes(DCETime)
        self.CZCETime = self._to_bytes(CZCETime)
        self.FFEXTime = self._to_bytes(FFEXTime)
        self.INETime = self._to_bytes(INETime)
        self.RandomString = self._to_bytes(RandomString)


class TransferHeaderField(Base):
    """银期转帐报文头"""
    _fields_ = [
        ('Version', ctypes.c_char * 4),  # 版本号，常量，1.0
        ('TradeCode', ctypes.c_char * 7),  # 交易代码，必填
        ('TradeDate', ctypes.c_char * 9),  # 交易日期，必填，格式：yyyymmdd
        ('TradeTime', ctypes.c_char * 9),  # 交易时间，必填，格式：hhmmss
        ('TradeSerial', ctypes.c_char * 9),  # 发起方流水号，N/A
        ('FutureID', ctypes.c_char * 11),  # 期货公司代码，必填
        ('BankID', ctypes.c_char * 4),  # 银行代码，根据查询银行得到，必填
        ('BankBrchID', ctypes.c_char * 5),  # 银行分中心代码，根据查询银行得到，必填
        ('OperNo', ctypes.c_char * 17),  # 操作员，N/A
        ('DeviceID', ctypes.c_char * 3),  # 交易设备类型，N/A
        ('RecordNum', ctypes.c_char * 7),  # 记录数，N/A
        ('SessionID', ctypes.c_int),  # 会话编号，N/A
        ('RequestID', ctypes.c_int),  # 请求编号，N/A
    ]

    def __init__(self, Version: str = '', TradeCode: str = '', TradeDate: str = '', TradeTime: str = '', TradeSerial: str = '', FutureID: str = '', BankID: str = '', BankBrchID: str = '',
                 OperNo: str = '', DeviceID: str = '', RecordNum: str = '', SessionID: int = 0, RequestID: int = 0):
        super(TransferHeaderField, self).__init__()
        self.Version = self._to_bytes(Version)
        self.TradeCode = self._to_bytes(TradeCode)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.TradeSerial = self._to_bytes(TradeSerial)
        self.FutureID = self._to_bytes(FutureID)
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)
        self.OperNo = self._to_bytes(OperNo)
        self.DeviceID = self._to_bytes(DeviceID)
        self.RecordNum = self._to_bytes(RecordNum)
        self.SessionID = int(SessionID)
        self.RequestID = int(RequestID)


class TransferBankToFutureReqField(Base):
    """银行资金转期货请求，TradeCode=202001"""
    _fields_ = [
        ('FutureAccount', ctypes.c_char * 13),  # 期货资金账户
        ('FuturePwdFlag', ctypes.c_char),  # 密码标志
        ('FutureAccPwd', ctypes.c_char * 17),  # 密码
        ('TradeAmt', ctypes.c_double),  # 转账金额
        ('CustFee', ctypes.c_double),  # 客户手续费
        ('CurrencyCode', ctypes.c_char * 4),  # 币种：RMB-人民币 USD-美圆 HKD-港元
    ]

    def __init__(self, FutureAccount: str = '', FuturePwdFlag: str = '', FutureAccPwd: str = '', TradeAmt: float = 0.0, CustFee: float = 0.0, CurrencyCode: str = ''):
        super(TransferBankToFutureReqField, self).__init__()
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.FuturePwdFlag = self._to_bytes(FuturePwdFlag)
        self.FutureAccPwd = self._to_bytes(FutureAccPwd)
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferBankToFutureRspField(Base):
    """银行资金转期货请求响应"""
    _fields_ = [
        ('RetCode', ctypes.c_char * 5),  # 响应代码
        ('RetInfo', ctypes.c_char * 129),  # 响应信息
        ('FutureAccount', ctypes.c_char * 13),  # 资金账户
        ('TradeAmt', ctypes.c_double),  # 转帐金额
        ('CustFee', ctypes.c_double),  # 应收客户手续费
        ('CurrencyCode', ctypes.c_char * 4),  # 币种
    ]

    def __init__(self, RetCode: str = '', RetInfo: str = '', FutureAccount: str = '', TradeAmt: float = 0.0, CustFee: float = 0.0, CurrencyCode: str = ''):
        super(TransferBankToFutureRspField, self).__init__()
        self.RetCode = self._to_bytes(RetCode)
        self.RetInfo = self._to_bytes(RetInfo)
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferFutureToBankReqField(Base):
    """期货资金转银行请求，TradeCode=202002"""
    _fields_ = [
        ('FutureAccount', ctypes.c_char * 13),  # 期货资金账户
        ('FuturePwdFlag', ctypes.c_char),  # 密码标志
        ('FutureAccPwd', ctypes.c_char * 17),  # 密码
        ('TradeAmt', ctypes.c_double),  # 转账金额
        ('CustFee', ctypes.c_double),  # 客户手续费
        ('CurrencyCode', ctypes.c_char * 4),  # 币种：RMB-人民币 USD-美圆 HKD-港元
    ]

    def __init__(self, FutureAccount: str = '', FuturePwdFlag: str = '', FutureAccPwd: str = '', TradeAmt: float = 0.0, CustFee: float = 0.0, CurrencyCode: str = ''):
        super(TransferFutureToBankReqField, self).__init__()
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.FuturePwdFlag = self._to_bytes(FuturePwdFlag)
        self.FutureAccPwd = self._to_bytes(FutureAccPwd)
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferFutureToBankRspField(Base):
    """期货资金转银行请求响应"""
    _fields_ = [
        ('RetCode', ctypes.c_char * 5),  # 响应代码
        ('RetInfo', ctypes.c_char * 129),  # 响应信息
        ('FutureAccount', ctypes.c_char * 13),  # 资金账户
        ('TradeAmt', ctypes.c_double),  # 转帐金额
        ('CustFee', ctypes.c_double),  # 应收客户手续费
        ('CurrencyCode', ctypes.c_char * 4),  # 币种
    ]

    def __init__(self, RetCode: str = '', RetInfo: str = '', FutureAccount: str = '', TradeAmt: float = 0.0, CustFee: float = 0.0, CurrencyCode: str = ''):
        super(TransferFutureToBankRspField, self).__init__()
        self.RetCode = self._to_bytes(RetCode)
        self.RetInfo = self._to_bytes(RetInfo)
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferQryBankReqField(Base):
    """查询银行资金请求，TradeCode=204002"""
    _fields_ = [
        ('FutureAccount', ctypes.c_char * 13),  # 期货资金账户
        ('FuturePwdFlag', ctypes.c_char),  # 密码标志
        ('FutureAccPwd', ctypes.c_char * 17),  # 密码
        ('CurrencyCode', ctypes.c_char * 4),  # 币种：RMB-人民币 USD-美圆 HKD-港元
    ]

    def __init__(self, FutureAccount: str = '', FuturePwdFlag: str = '', FutureAccPwd: str = '', CurrencyCode: str = ''):
        super(TransferQryBankReqField, self).__init__()
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.FuturePwdFlag = self._to_bytes(FuturePwdFlag)
        self.FutureAccPwd = self._to_bytes(FutureAccPwd)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferQryBankRspField(Base):
    """查询银行资金请求响应"""
    _fields_ = [
        ('RetCode', ctypes.c_char * 5),  # 响应代码
        ('RetInfo', ctypes.c_char * 129),  # 响应信息
        ('FutureAccount', ctypes.c_char * 13),  # 资金账户
        ('TradeAmt', ctypes.c_double),  # 银行余额
        ('UseAmt', ctypes.c_double),  # 银行可用余额
        ('FetchAmt', ctypes.c_double),  # 银行可取余额
        ('CurrencyCode', ctypes.c_char * 4),  # 币种
    ]

    def __init__(self, RetCode: str = '', RetInfo: str = '', FutureAccount: str = '', TradeAmt: float = 0.0, UseAmt: float = 0.0, FetchAmt: float = 0.0, CurrencyCode: str = ''):
        super(TransferQryBankRspField, self).__init__()
        self.RetCode = self._to_bytes(RetCode)
        self.RetInfo = self._to_bytes(RetInfo)
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.TradeAmt = float(TradeAmt)
        self.UseAmt = float(UseAmt)
        self.FetchAmt = float(FetchAmt)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferQryDetailReqField(Base):
    """查询银行交易明细请求，TradeCode=204999"""
    _fields_ = [
        ('FutureAccount', ctypes.c_char * 13),  # 期货资金账户
    ]

    def __init__(self, FutureAccount: str = ''):
        super(TransferQryDetailReqField, self).__init__()
        self.FutureAccount = self._to_bytes(FutureAccount)


class TransferQryDetailRspField(Base):
    """查询银行交易明细请求响应"""
    _fields_ = [
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('TradeCode', ctypes.c_char * 7),  # 交易代码
        ('FutureSerial', ctypes.c_int),  # 期货流水号
        ('FutureID', ctypes.c_char * 11),  # 期货公司代码
        ('FutureAccount', ctypes.c_char * 22),  # 资金帐号
        ('BankSerial', ctypes.c_int),  # 银行流水号
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBrchID', ctypes.c_char * 5),  # 银行分中心代码
        ('BankAccount', ctypes.c_char * 41),  # 银行账号
        ('CertCode', ctypes.c_char * 21),  # 证件号码
        ('CurrencyCode', ctypes.c_char * 4),  # 货币代码
        ('TxAmount', ctypes.c_double),  # 发生金额
        ('Flag', ctypes.c_char),  # 有效标志
    ]

    def __init__(self, TradeDate: str = '', TradeTime: str = '', TradeCode: str = '', FutureSerial: int = 0, FutureID: str = '', FutureAccount: str = '', BankSerial: int = 0, BankID: str = '',
                 BankBrchID: str = '', BankAccount: str = '', CertCode: str = '', CurrencyCode: str = '', TxAmount: float = 0.0, Flag: str = ''):
        super(TransferQryDetailRspField, self).__init__()
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.TradeCode = self._to_bytes(TradeCode)
        self.FutureSerial = int(FutureSerial)
        self.FutureID = self._to_bytes(FutureID)
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.BankSerial = int(BankSerial)
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)
        self.BankAccount = self._to_bytes(BankAccount)
        self.CertCode = self._to_bytes(CertCode)
        self.CurrencyCode = self._to_bytes(CurrencyCode)
        self.TxAmount = float(TxAmount)
        self.Flag = self._to_bytes(Flag)


class RspInfoField(Base):
    """响应信息"""
    _fields_ = [
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
    ]

    def __init__(self, ErrorID: int = 0, ErrorMsg: str = ''):
        super(RspInfoField, self).__init__()
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class ExchangeField(Base):
    """交易所"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ExchangeName', ctypes.c_char * 61),  # 交易所名称
        ('ExchangeProperty', ctypes.c_char),  # 交易所属性
    ]

    def __init__(self, ExchangeID: str = '', ExchangeName: str = '', ExchangeProperty: str = ''):
        super(ExchangeField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExchangeName = self._to_bytes(ExchangeName)
        self.ExchangeProperty = self._to_bytes(ExchangeProperty)


class ProductField(Base):
    """产品"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ProductName', ctypes.c_char * 21),  # 产品名称
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ProductClass', ctypes.c_char),  # 产品类型
        ('VolumeMultiple', ctypes.c_int),  # 合约数量乘数
        ('PriceTick', ctypes.c_double),  # 最小变动价位
        ('MaxMarketOrderVolume', ctypes.c_int),  # 市价单最大下单量
        ('MinMarketOrderVolume', ctypes.c_int),  # 市价单最小下单量
        ('MaxLimitOrderVolume', ctypes.c_int),  # 限价单最大下单量
        ('MinLimitOrderVolume', ctypes.c_int),  # 限价单最小下单量
        ('PositionType', ctypes.c_char),  # 持仓类型
        ('PositionDateType', ctypes.c_char),  # 持仓日期类型
        ('CloseDealType', ctypes.c_char),  # 平仓处理类型
        ('TradeCurrencyID', ctypes.c_char * 4),  # 交易币种类型
        ('MortgageFundUseRange', ctypes.c_char),  # 质押资金可用范围
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('UnderlyingMultiple', ctypes.c_double),  # 合约基础商品乘数
        ('ProductID', ctypes.c_char * 81),  # 产品代码
        ('ExchangeProductID', ctypes.c_char * 81),  # 交易所产品代码
        ('OpenLimitControlLevel', ctypes.c_char),  # 开仓量限制粒度
        ('OrderFreqControlLevel', ctypes.c_char),  # 报单频率控制粒度
    ]

    def __init__(self, reserve1: str = '', ProductName: str = '', ExchangeID: str = '', ProductClass: str = '', VolumeMultiple: int = 0, PriceTick: float = 0.0, MaxMarketOrderVolume: int = 0,
                 MinMarketOrderVolume: int = 0, MaxLimitOrderVolume: int = 0, MinLimitOrderVolume: int = 0, PositionType: str = '', PositionDateType: str = '', CloseDealType: str = '',
                 TradeCurrencyID: str = '', MortgageFundUseRange: str = '', reserve2: str = '', UnderlyingMultiple: float = 0.0, ProductID: str = '', ExchangeProductID: str = '',
                 OpenLimitControlLevel: str = '', OrderFreqControlLevel: str = ''):
        super(ProductField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.ProductName = self._to_bytes(ProductName)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProductClass = self._to_bytes(ProductClass)
        self.VolumeMultiple = int(VolumeMultiple)
        self.PriceTick = float(PriceTick)
        self.MaxMarketOrderVolume = int(MaxMarketOrderVolume)
        self.MinMarketOrderVolume = int(MinMarketOrderVolume)
        self.MaxLimitOrderVolume = int(MaxLimitOrderVolume)
        self.MinLimitOrderVolume = int(MinLimitOrderVolume)
        self.PositionType = self._to_bytes(PositionType)
        self.PositionDateType = self._to_bytes(PositionDateType)
        self.CloseDealType = self._to_bytes(CloseDealType)
        self.TradeCurrencyID = self._to_bytes(TradeCurrencyID)
        self.MortgageFundUseRange = self._to_bytes(MortgageFundUseRange)
        self.reserve2 = self._to_bytes(reserve2)
        self.UnderlyingMultiple = float(UnderlyingMultiple)
        self.ProductID = self._to_bytes(ProductID)
        self.ExchangeProductID = self._to_bytes(ExchangeProductID)
        self.OpenLimitControlLevel = self._to_bytes(OpenLimitControlLevel)
        self.OrderFreqControlLevel = self._to_bytes(OrderFreqControlLevel)


class InstrumentField(Base):
    """合约"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentName', ctypes.c_char * 21),  # 合约名称
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('reserve3', ctypes.c_char * 31),  # 保留的无效字段
        ('ProductClass', ctypes.c_char),  # 产品类型
        ('DeliveryYear', ctypes.c_int),  # 交割年份
        ('DeliveryMonth', ctypes.c_int),  # 交割月
        ('MaxMarketOrderVolume', ctypes.c_int),  # 市价单最大下单量
        ('MinMarketOrderVolume', ctypes.c_int),  # 市价单最小下单量
        ('MaxLimitOrderVolume', ctypes.c_int),  # 限价单最大下单量
        ('MinLimitOrderVolume', ctypes.c_int),  # 限价单最小下单量
        ('VolumeMultiple', ctypes.c_int),  # 合约数量乘数
        ('PriceTick', ctypes.c_double),  # 最小变动价位
        ('CreateDate', ctypes.c_char * 9),  # 创建日
        ('OpenDate', ctypes.c_char * 9),  # 上市日
        ('ExpireDate', ctypes.c_char * 9),  # 到期日
        ('StartDelivDate', ctypes.c_char * 9),  # 开始交割日
        ('EndDelivDate', ctypes.c_char * 9),  # 结束交割日
        ('InstLifePhase', ctypes.c_char),  # 合约生命周期状态
        ('IsTrading', ctypes.c_int),  # 当前是否交易
        ('PositionType', ctypes.c_char),  # 持仓类型
        ('PositionDateType', ctypes.c_char),  # 持仓日期类型
        ('LongMarginRatio', ctypes.c_double),  # 多头保证金率
        ('ShortMarginRatio', ctypes.c_double),  # 空头保证金率
        ('MaxMarginSideAlgorithm', ctypes.c_char),  # 是否使用大额单边保证金算法
        ('reserve4', ctypes.c_char * 31),  # 保留的无效字段
        ('StrikePrice', ctypes.c_double),  # 执行价
        ('OptionsType', ctypes.c_char),  # 期权类型
        ('UnderlyingMultiple', ctypes.c_double),  # 合约基础商品乘数
        ('CombinationType', ctypes.c_char),  # 组合类型
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('ProductID', ctypes.c_char * 81),  # 产品代码
        ('UnderlyingInstrID', ctypes.c_char * 81),  # 基础商品代码
    ]

    def __init__(self, reserve1: str = '', ExchangeID: str = '', InstrumentName: str = '', reserve2: str = '', reserve3: str = '', ProductClass: str = '', DeliveryYear: int = 0,
                 DeliveryMonth: int = 0, MaxMarketOrderVolume: int = 0, MinMarketOrderVolume: int = 0, MaxLimitOrderVolume: int = 0, MinLimitOrderVolume: int = 0, VolumeMultiple: int = 0,
                 PriceTick: float = 0.0, CreateDate: str = '', OpenDate: str = '', ExpireDate: str = '', StartDelivDate: str = '', EndDelivDate: str = '', InstLifePhase: str = '', IsTrading: int = 0,
                 PositionType: str = '', PositionDateType: str = '', LongMarginRatio: float = 0.0, ShortMarginRatio: float = 0.0, MaxMarginSideAlgorithm: str = '', reserve4: str = '',
                 StrikePrice: float = 0.0, OptionsType: str = '', UnderlyingMultiple: float = 0.0, CombinationType: str = '', InstrumentID: str = '', ExchangeInstID: str = '', ProductID: str = '',
                 UnderlyingInstrID: str = ''):
        super(InstrumentField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentName = self._to_bytes(InstrumentName)
        self.reserve2 = self._to_bytes(reserve2)
        self.reserve3 = self._to_bytes(reserve3)
        self.ProductClass = self._to_bytes(ProductClass)
        self.DeliveryYear = int(DeliveryYear)
        self.DeliveryMonth = int(DeliveryMonth)
        self.MaxMarketOrderVolume = int(MaxMarketOrderVolume)
        self.MinMarketOrderVolume = int(MinMarketOrderVolume)
        self.MaxLimitOrderVolume = int(MaxLimitOrderVolume)
        self.MinLimitOrderVolume = int(MinLimitOrderVolume)
        self.VolumeMultiple = int(VolumeMultiple)
        self.PriceTick = float(PriceTick)
        self.CreateDate = self._to_bytes(CreateDate)
        self.OpenDate = self._to_bytes(OpenDate)
        self.ExpireDate = self._to_bytes(ExpireDate)
        self.StartDelivDate = self._to_bytes(StartDelivDate)
        self.EndDelivDate = self._to_bytes(EndDelivDate)
        self.InstLifePhase = self._to_bytes(InstLifePhase)
        self.IsTrading = int(IsTrading)
        self.PositionType = self._to_bytes(PositionType)
        self.PositionDateType = self._to_bytes(PositionDateType)
        self.LongMarginRatio = float(LongMarginRatio)
        self.ShortMarginRatio = float(ShortMarginRatio)
        self.MaxMarginSideAlgorithm = self._to_bytes(MaxMarginSideAlgorithm)
        self.reserve4 = self._to_bytes(reserve4)
        self.StrikePrice = float(StrikePrice)
        self.OptionsType = self._to_bytes(OptionsType)
        self.UnderlyingMultiple = float(UnderlyingMultiple)
        self.CombinationType = self._to_bytes(CombinationType)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.ProductID = self._to_bytes(ProductID)
        self.UnderlyingInstrID = self._to_bytes(UnderlyingInstrID)


class BrokerField(Base):
    """经纪公司"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('BrokerAbbr', ctypes.c_char * 9),  # 经纪公司简称
        ('BrokerName', ctypes.c_char * 81),  # 经纪公司名称
        ('IsActive', ctypes.c_int),  # 是否活跃
    ]

    def __init__(self, BrokerID: str = '', BrokerAbbr: str = '', BrokerName: str = '', IsActive: int = 0):
        super(BrokerField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerAbbr = self._to_bytes(BrokerAbbr)
        self.BrokerName = self._to_bytes(BrokerName)
        self.IsActive = int(IsActive)


class TraderField(Base):
    """交易所交易员"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('Password', ctypes.c_char * 41),  # 密码
        ('InstallCount', ctypes.c_int),  # 安装数量
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('OrderCancelAlg', ctypes.c_char),  # 撤单时选择席位算法
    ]

    def __init__(self, ExchangeID: str = '', TraderID: str = '', ParticipantID: str = '', Password: str = '', InstallCount: int = 0, BrokerID: str = '', OrderCancelAlg: str = ''):
        super(TraderField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.Password = self._to_bytes(Password)
        self.InstallCount = int(InstallCount)
        self.BrokerID = self._to_bytes(BrokerID)
        self.OrderCancelAlg = self._to_bytes(OrderCancelAlg)


class InvestorField(Base):
    """投资者"""
    _fields_ = [
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorGroupID', ctypes.c_char * 13),  # 投资者分组代码
        ('InvestorName', ctypes.c_char * 81),  # 投资者名称
        ('IdentifiedCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('IsActive', ctypes.c_int),  # 是否活跃
        ('Telephone', ctypes.c_char * 41),  # 联系电话
        ('Address', ctypes.c_char * 101),  # 通讯地址
        ('OpenDate', ctypes.c_char * 9),  # 开户日期
        ('Mobile', ctypes.c_char * 41),  # 手机
        ('CommModelID', ctypes.c_char * 13),  # 手续费率模板代码
        ('MarginModelID', ctypes.c_char * 13),  # 保证金率模板代码
        ('IsOrderFreq', ctypes.c_char),  # 是否频率控制
        ('IsOpenVolLimit', ctypes.c_char),  # 是否开仓限制
    ]

    def __init__(self, InvestorID: str = '', BrokerID: str = '', InvestorGroupID: str = '', InvestorName: str = '', IdentifiedCardType: str = '', IdentifiedCardNo: str = '', IsActive: int = 0,
                 Telephone: str = '', Address: str = '', OpenDate: str = '', Mobile: str = '', CommModelID: str = '', MarginModelID: str = '', IsOrderFreq: str = '', IsOpenVolLimit: str = ''):
        super(InvestorField, self).__init__()
        self.InvestorID = self._to_bytes(InvestorID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorGroupID = self._to_bytes(InvestorGroupID)
        self.InvestorName = self._to_bytes(InvestorName)
        self.IdentifiedCardType = self._to_bytes(IdentifiedCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.IsActive = int(IsActive)
        self.Telephone = self._to_bytes(Telephone)
        self.Address = self._to_bytes(Address)
        self.OpenDate = self._to_bytes(OpenDate)
        self.Mobile = self._to_bytes(Mobile)
        self.CommModelID = self._to_bytes(CommModelID)
        self.MarginModelID = self._to_bytes(MarginModelID)
        self.IsOrderFreq = self._to_bytes(IsOrderFreq)
        self.IsOpenVolLimit = self._to_bytes(IsOpenVolLimit)


class TradingCodeField(Base):
    """交易编码"""
    _fields_ = [
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('IsActive', ctypes.c_int),  # 是否活跃
        ('ClientIDType', ctypes.c_char),  # 交易编码类型
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('BizType', ctypes.c_char),  # 业务类型
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
    ]

    def __init__(self, InvestorID: str = '', BrokerID: str = '', ExchangeID: str = '', ClientID: str = '', IsActive: int = 0, ClientIDType: str = '', BranchID: str = '', BizType: str = '',
                 InvestUnitID: str = ''):
        super(TradingCodeField, self).__init__()
        self.InvestorID = self._to_bytes(InvestorID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ClientID = self._to_bytes(ClientID)
        self.IsActive = int(IsActive)
        self.ClientIDType = self._to_bytes(ClientIDType)
        self.BranchID = self._to_bytes(BranchID)
        self.BizType = self._to_bytes(BizType)
        self.InvestUnitID = self._to_bytes(InvestUnitID)


class PartBrokerField(Base):
    """会员编码和经纪公司编码对照表"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('IsActive', ctypes.c_int),  # 是否活跃
    ]

    def __init__(self, BrokerID: str = '', ExchangeID: str = '', ParticipantID: str = '', IsActive: int = 0):
        super(PartBrokerField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.IsActive = int(IsActive)


class SuperUserField(Base):
    """管理用户"""
    _fields_ = [
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('UserName', ctypes.c_char * 81),  # 用户名称
        ('Password', ctypes.c_char * 41),  # 密码
        ('IsActive', ctypes.c_int),  # 是否活跃
    ]

    def __init__(self, UserID: str = '', UserName: str = '', Password: str = '', IsActive: int = 0):
        super(SuperUserField, self).__init__()
        self.UserID = self._to_bytes(UserID)
        self.UserName = self._to_bytes(UserName)
        self.Password = self._to_bytes(Password)
        self.IsActive = int(IsActive)


class SuperUserFunctionField(Base):
    """管理用户功能权限"""
    _fields_ = [
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('FunctionCode', ctypes.c_char),  # 功能代码
    ]

    def __init__(self, UserID: str = '', FunctionCode: str = ''):
        super(SuperUserFunctionField, self).__init__()
        self.UserID = self._to_bytes(UserID)
        self.FunctionCode = self._to_bytes(FunctionCode)


class InvestorGroupField(Base):
    """投资者组"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorGroupID', ctypes.c_char * 13),  # 投资者分组代码
        ('InvestorGroupName', ctypes.c_char * 41),  # 投资者分组名称
    ]

    def __init__(self, BrokerID: str = '', InvestorGroupID: str = '', InvestorGroupName: str = ''):
        super(InvestorGroupField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorGroupID = self._to_bytes(InvestorGroupID)
        self.InvestorGroupName = self._to_bytes(InvestorGroupName)


class TradingAccountField(Base):
    """资金账户"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('PreMortgage', ctypes.c_double),  # 上次质押金额
        ('PreCredit', ctypes.c_double),  # 上次信用额度
        ('PreDeposit', ctypes.c_double),  # 上次存款额
        ('PreBalance', ctypes.c_double),  # 上次结算准备金
        ('PreMargin', ctypes.c_double),  # 上次占用的保证金
        ('InterestBase', ctypes.c_double),  # 利息基数
        ('Interest', ctypes.c_double),  # 利息收入
        ('Deposit', ctypes.c_double),  # 入金金额
        ('Withdraw', ctypes.c_double),  # 出金金额
        ('FrozenMargin', ctypes.c_double),  # 冻结的保证金
        ('FrozenCash', ctypes.c_double),  # 冻结的资金
        ('FrozenCommission', ctypes.c_double),  # 冻结的手续费
        ('CurrMargin', ctypes.c_double),  # 当前保证金总额
        ('CashIn', ctypes.c_double),  # 资金差额
        ('Commission', ctypes.c_double),  # 手续费
        ('CloseProfit', ctypes.c_double),  # 平仓盈亏
        ('PositionProfit', ctypes.c_double),  # 持仓盈亏
        ('Balance', ctypes.c_double),  # 期货结算准备金
        ('Available', ctypes.c_double),  # 可用资金
        ('WithdrawQuota', ctypes.c_double),  # 可取资金
        ('Reserve', ctypes.c_double),  # 基本准备金
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('Credit', ctypes.c_double),  # 信用额度
        ('Mortgage', ctypes.c_double),  # 质押金额
        ('ExchangeMargin', ctypes.c_double),  # 交易所保证金
        ('DeliveryMargin', ctypes.c_double),  # 投资者交割保证金
        ('ExchangeDeliveryMargin', ctypes.c_double),  # 交易所交割保证金
        ('ReserveBalance', ctypes.c_double),  # 保底期货结算准备金
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('PreFundMortgageIn', ctypes.c_double),  # 上次货币质入金额
        ('PreFundMortgageOut', ctypes.c_double),  # 上次货币质出金额
        ('FundMortgageIn', ctypes.c_double),  # 货币质入金额
        ('FundMortgageOut', ctypes.c_double),  # 货币质出金额
        ('FundMortgageAvailable', ctypes.c_double),  # 货币质押余额
        ('MortgageableFund', ctypes.c_double),  # 可质押货币金额
        ('SpecProductMargin', ctypes.c_double),  # 特殊产品占用保证金
        ('SpecProductFrozenMargin', ctypes.c_double),  # 特殊产品冻结保证金
        ('SpecProductCommission', ctypes.c_double),  # 特殊产品手续费
        ('SpecProductFrozenCommission', ctypes.c_double),  # 特殊产品冻结手续费
        ('SpecProductPositionProfit', ctypes.c_double),  # 特殊产品持仓盈亏
        ('SpecProductCloseProfit', ctypes.c_double),  # 特殊产品平仓盈亏
        ('SpecProductPositionProfitByAlg', ctypes.c_double),  # 根据持仓盈亏算法计算的特殊产品持仓盈亏
        ('SpecProductExchangeMargin', ctypes.c_double),  # 特殊产品交易所保证金
        ('BizType', ctypes.c_char),  # 业务类型
        ('FrozenSwap', ctypes.c_double),  # 延时换汇冻结金额
        ('RemainSwap', ctypes.c_double),  # 剩余换汇额度
    ]

    def __init__(self, BrokerID: str = '', AccountID: str = '', PreMortgage: float = 0.0, PreCredit: float = 0.0, PreDeposit: float = 0.0, PreBalance: float = 0.0, PreMargin: float = 0.0,
                 InterestBase: float = 0.0, Interest: float = 0.0, Deposit: float = 0.0, Withdraw: float = 0.0, FrozenMargin: float = 0.0, FrozenCash: float = 0.0, FrozenCommission: float = 0.0,
                 CurrMargin: float = 0.0, CashIn: float = 0.0, Commission: float = 0.0, CloseProfit: float = 0.0, PositionProfit: float = 0.0, Balance: float = 0.0, Available: float = 0.0,
                 WithdrawQuota: float = 0.0, Reserve: float = 0.0, TradingDay: str = '', SettlementID: int = 0, Credit: float = 0.0, Mortgage: float = 0.0, ExchangeMargin: float = 0.0,
                 DeliveryMargin: float = 0.0, ExchangeDeliveryMargin: float = 0.0, ReserveBalance: float = 0.0, CurrencyID: str = '', PreFundMortgageIn: float = 0.0, PreFundMortgageOut: float = 0.0,
                 FundMortgageIn: float = 0.0, FundMortgageOut: float = 0.0, FundMortgageAvailable: float = 0.0, MortgageableFund: float = 0.0, SpecProductMargin: float = 0.0,
                 SpecProductFrozenMargin: float = 0.0, SpecProductCommission: float = 0.0, SpecProductFrozenCommission: float = 0.0, SpecProductPositionProfit: float = 0.0,
                 SpecProductCloseProfit: float = 0.0, SpecProductPositionProfitByAlg: float = 0.0, SpecProductExchangeMargin: float = 0.0, BizType: str = '', FrozenSwap: float = 0.0,
                 RemainSwap: float = 0.0):
        super(TradingAccountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.PreMortgage = float(PreMortgage)
        self.PreCredit = float(PreCredit)
        self.PreDeposit = float(PreDeposit)
        self.PreBalance = float(PreBalance)
        self.PreMargin = float(PreMargin)
        self.InterestBase = float(InterestBase)
        self.Interest = float(Interest)
        self.Deposit = float(Deposit)
        self.Withdraw = float(Withdraw)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CurrMargin = float(CurrMargin)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.CloseProfit = float(CloseProfit)
        self.PositionProfit = float(PositionProfit)
        self.Balance = float(Balance)
        self.Available = float(Available)
        self.WithdrawQuota = float(WithdrawQuota)
        self.Reserve = float(Reserve)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.Credit = float(Credit)
        self.Mortgage = float(Mortgage)
        self.ExchangeMargin = float(ExchangeMargin)
        self.DeliveryMargin = float(DeliveryMargin)
        self.ExchangeDeliveryMargin = float(ExchangeDeliveryMargin)
        self.ReserveBalance = float(ReserveBalance)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.PreFundMortgageIn = float(PreFundMortgageIn)
        self.PreFundMortgageOut = float(PreFundMortgageOut)
        self.FundMortgageIn = float(FundMortgageIn)
        self.FundMortgageOut = float(FundMortgageOut)
        self.FundMortgageAvailable = float(FundMortgageAvailable)
        self.MortgageableFund = float(MortgageableFund)
        self.SpecProductMargin = float(SpecProductMargin)
        self.SpecProductFrozenMargin = float(SpecProductFrozenMargin)
        self.SpecProductCommission = float(SpecProductCommission)
        self.SpecProductFrozenCommission = float(SpecProductFrozenCommission)
        self.SpecProductPositionProfit = float(SpecProductPositionProfit)
        self.SpecProductCloseProfit = float(SpecProductCloseProfit)
        self.SpecProductPositionProfitByAlg = float(SpecProductPositionProfitByAlg)
        self.SpecProductExchangeMargin = float(SpecProductExchangeMargin)
        self.BizType = self._to_bytes(BizType)
        self.FrozenSwap = float(FrozenSwap)
        self.RemainSwap = float(RemainSwap)


class InvestorPositionField(Base):
    """投资者持仓"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('PosiDirection', ctypes.c_char),  # 持仓多空方向
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('PositionDate', ctypes.c_char),  # 持仓日期
        ('YdPosition', ctypes.c_int),  # 上日持仓
        ('Position', ctypes.c_int),  # 今日持仓
        ('LongFrozen', ctypes.c_int),  # 多头冻结
        ('ShortFrozen', ctypes.c_int),  # 空头冻结
        ('LongFrozenAmount', ctypes.c_double),  # 开仓冻结金额
        ('ShortFrozenAmount', ctypes.c_double),  # 开仓冻结金额
        ('OpenVolume', ctypes.c_int),  # 开仓量
        ('CloseVolume', ctypes.c_int),  # 平仓量
        ('OpenAmount', ctypes.c_double),  # 开仓金额
        ('CloseAmount', ctypes.c_double),  # 平仓金额
        ('PositionCost', ctypes.c_double),  # 持仓成本
        ('PreMargin', ctypes.c_double),  # 上次占用的保证金
        ('UseMargin', ctypes.c_double),  # 占用的保证金
        ('FrozenMargin', ctypes.c_double),  # 冻结的保证金
        ('FrozenCash', ctypes.c_double),  # 冻结的资金
        ('FrozenCommission', ctypes.c_double),  # 冻结的手续费
        ('CashIn', ctypes.c_double),  # 资金差额
        ('Commission', ctypes.c_double),  # 手续费
        ('CloseProfit', ctypes.c_double),  # 平仓盈亏
        ('PositionProfit', ctypes.c_double),  # 持仓盈亏
        ('PreSettlementPrice', ctypes.c_double),  # 上次结算价
        ('SettlementPrice', ctypes.c_double),  # 本次结算价
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('OpenCost', ctypes.c_double),  # 开仓成本
        ('ExchangeMargin', ctypes.c_double),  # 交易所保证金
        ('CombPosition', ctypes.c_int),  # 组合成交形成的持仓
        ('CombLongFrozen', ctypes.c_int),  # 组合多头冻结
        ('CombShortFrozen', ctypes.c_int),  # 组合空头冻结
        ('CloseProfitByDate', ctypes.c_double),  # 逐日盯市平仓盈亏
        ('CloseProfitByTrade', ctypes.c_double),  # 逐笔对冲平仓盈亏
        ('TodayPosition', ctypes.c_int),  # 今日持仓
        ('MarginRateByMoney', ctypes.c_double),  # 保证金率
        ('MarginRateByVolume', ctypes.c_double),  # 保证金率(按手数)
        ('StrikeFrozen', ctypes.c_int),  # 执行冻结
        ('StrikeFrozenAmount', ctypes.c_double),  # 执行冻结金额
        ('AbandonFrozen', ctypes.c_int),  # 放弃执行冻结
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('YdStrikeFrozen', ctypes.c_int),  # 执行冻结的昨仓
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('PositionCostOffset', ctypes.c_double),  # 持仓成本差值
        ('TasPosition', ctypes.c_int),  # tas持仓手数
        ('TasPositionCost', ctypes.c_double),  # tas持仓成本
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', BrokerID: str = '', InvestorID: str = '', PosiDirection: str = '', HedgeFlag: str = '', PositionDate: str = '', YdPosition: int = 0, Position: int = 0,
                 LongFrozen: int = 0, ShortFrozen: int = 0, LongFrozenAmount: float = 0.0, ShortFrozenAmount: float = 0.0, OpenVolume: int = 0, CloseVolume: int = 0, OpenAmount: float = 0.0,
                 CloseAmount: float = 0.0, PositionCost: float = 0.0, PreMargin: float = 0.0, UseMargin: float = 0.0, FrozenMargin: float = 0.0, FrozenCash: float = 0.0, FrozenCommission: float = 0.0,
                 CashIn: float = 0.0, Commission: float = 0.0, CloseProfit: float = 0.0, PositionProfit: float = 0.0, PreSettlementPrice: float = 0.0, SettlementPrice: float = 0.0,
                 TradingDay: str = '', SettlementID: int = 0, OpenCost: float = 0.0, ExchangeMargin: float = 0.0, CombPosition: int = 0, CombLongFrozen: int = 0, CombShortFrozen: int = 0,
                 CloseProfitByDate: float = 0.0, CloseProfitByTrade: float = 0.0, TodayPosition: int = 0, MarginRateByMoney: float = 0.0, MarginRateByVolume: float = 0.0, StrikeFrozen: int = 0,
                 StrikeFrozenAmount: float = 0.0, AbandonFrozen: int = 0, ExchangeID: str = '', YdStrikeFrozen: int = 0, InvestUnitID: str = '', PositionCostOffset: float = 0.0, TasPosition: int = 0,
                 TasPositionCost: float = 0.0, InstrumentID: str = ''):
        super(InvestorPositionField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.PositionDate = self._to_bytes(PositionDate)
        self.YdPosition = int(YdPosition)
        self.Position = int(Position)
        self.LongFrozen = int(LongFrozen)
        self.ShortFrozen = int(ShortFrozen)
        self.LongFrozenAmount = float(LongFrozenAmount)
        self.ShortFrozenAmount = float(ShortFrozenAmount)
        self.OpenVolume = int(OpenVolume)
        self.CloseVolume = int(CloseVolume)
        self.OpenAmount = float(OpenAmount)
        self.CloseAmount = float(CloseAmount)
        self.PositionCost = float(PositionCost)
        self.PreMargin = float(PreMargin)
        self.UseMargin = float(UseMargin)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.CloseProfit = float(CloseProfit)
        self.PositionProfit = float(PositionProfit)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OpenCost = float(OpenCost)
        self.ExchangeMargin = float(ExchangeMargin)
        self.CombPosition = int(CombPosition)
        self.CombLongFrozen = int(CombLongFrozen)
        self.CombShortFrozen = int(CombShortFrozen)
        self.CloseProfitByDate = float(CloseProfitByDate)
        self.CloseProfitByTrade = float(CloseProfitByTrade)
        self.TodayPosition = int(TodayPosition)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.StrikeFrozen = int(StrikeFrozen)
        self.StrikeFrozenAmount = float(StrikeFrozenAmount)
        self.AbandonFrozen = int(AbandonFrozen)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.YdStrikeFrozen = int(YdStrikeFrozen)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.PositionCostOffset = float(PositionCostOffset)
        self.TasPosition = int(TasPosition)
        self.TasPositionCost = float(TasPositionCost)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InstrumentMarginRateField(Base):
    """合约保证金率"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('LongMarginRatioByMoney', ctypes.c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', ctypes.c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', ctypes.c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', ctypes.c_double),  # 空头保证金费
        ('IsRelative', ctypes.c_int),  # 是否相对交易所收取
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', HedgeFlag: str = '', LongMarginRatioByMoney: float = 0.0,
                 LongMarginRatioByVolume: float = 0.0, ShortMarginRatioByMoney: float = 0.0, ShortMarginRatioByVolume: float = 0.0, IsRelative: int = 0, ExchangeID: str = '', InvestUnitID: str = '',
                 InstrumentID: str = ''):
        super(InstrumentMarginRateField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InstrumentCommissionRateField(Base):
    """合约手续费率"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', ctypes.c_double),  # 开仓手续费率
        ('OpenRatioByVolume', ctypes.c_double),  # 开仓手续费
        ('CloseRatioByMoney', ctypes.c_double),  # 平仓手续费率
        ('CloseRatioByVolume', ctypes.c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', ctypes.c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', ctypes.c_double),  # 平今手续费
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('BizType', ctypes.c_char),  # 业务类型
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', OpenRatioByMoney: float = 0.0, OpenRatioByVolume: float = 0.0,
                 CloseRatioByMoney: float = 0.0, CloseRatioByVolume: float = 0.0, CloseTodayRatioByMoney: float = 0.0, CloseTodayRatioByVolume: float = 0.0, ExchangeID: str = '', BizType: str = '',
                 InvestUnitID: str = '', InstrumentID: str = ''):
        super(InstrumentCommissionRateField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.BizType = self._to_bytes(BizType)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class DepthMarketDataField(Base):
    """深度行情"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('LastPrice', ctypes.c_double),  # 最新价
        ('PreSettlementPrice', ctypes.c_double),  # 上次结算价
        ('PreClosePrice', ctypes.c_double),  # 昨收盘
        ('PreOpenInterest', ctypes.c_double),  # 昨持仓量
        ('OpenPrice', ctypes.c_double),  # 今开盘
        ('HighestPrice', ctypes.c_double),  # 最高价
        ('LowestPrice', ctypes.c_double),  # 最低价
        ('Volume', ctypes.c_int),  # 数量
        ('Turnover', ctypes.c_double),  # 成交金额
        ('OpenInterest', ctypes.c_double),  # 持仓量
        ('ClosePrice', ctypes.c_double),  # 今收盘
        ('SettlementPrice', ctypes.c_double),  # 本次结算价
        ('UpperLimitPrice', ctypes.c_double),  # 涨停板价
        ('LowerLimitPrice', ctypes.c_double),  # 跌停板价
        ('PreDelta', ctypes.c_double),  # 昨虚实度
        ('CurrDelta', ctypes.c_double),  # 今虚实度
        ('UpdateTime', ctypes.c_char * 9),  # 最后修改时间
        ('UpdateMillisec', ctypes.c_int),  # 最后修改毫秒
        ('BidPrice1', ctypes.c_double),  # 申买价一
        ('BidVolume1', ctypes.c_int),  # 申买量一
        ('AskPrice1', ctypes.c_double),  # 申卖价一
        ('AskVolume1', ctypes.c_int),  # 申卖量一
        ('BidPrice2', ctypes.c_double),  # 申买价二
        ('BidVolume2', ctypes.c_int),  # 申买量二
        ('AskPrice2', ctypes.c_double),  # 申卖价二
        ('AskVolume2', ctypes.c_int),  # 申卖量二
        ('BidPrice3', ctypes.c_double),  # 申买价三
        ('BidVolume3', ctypes.c_int),  # 申买量三
        ('AskPrice3', ctypes.c_double),  # 申卖价三
        ('AskVolume3', ctypes.c_int),  # 申卖量三
        ('BidPrice4', ctypes.c_double),  # 申买价四
        ('BidVolume4', ctypes.c_int),  # 申买量四
        ('AskPrice4', ctypes.c_double),  # 申卖价四
        ('AskVolume4', ctypes.c_int),  # 申卖量四
        ('BidPrice5', ctypes.c_double),  # 申买价五
        ('BidVolume5', ctypes.c_int),  # 申买量五
        ('AskPrice5', ctypes.c_double),  # 申卖价五
        ('AskVolume5', ctypes.c_int),  # 申卖量五
        ('AveragePrice', ctypes.c_double),  # 当日均价
        ('ActionDay', ctypes.c_char * 9),  # 业务日期
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('BandingUpperPrice', ctypes.c_double),  # 上带价
        ('BandingLowerPrice', ctypes.c_double),  # 下带价
    ]

    def __init__(self, TradingDay: str = '', reserve1: str = '', ExchangeID: str = '', reserve2: str = '', LastPrice: float = 0.0, PreSettlementPrice: float = 0.0, PreClosePrice: float = 0.0,
                 PreOpenInterest: float = 0.0, OpenPrice: float = 0.0, HighestPrice: float = 0.0, LowestPrice: float = 0.0, Volume: int = 0, Turnover: float = 0.0, OpenInterest: float = 0.0,
                 ClosePrice: float = 0.0, SettlementPrice: float = 0.0, UpperLimitPrice: float = 0.0, LowerLimitPrice: float = 0.0, PreDelta: float = 0.0, CurrDelta: float = 0.0, UpdateTime: str = '',
                 UpdateMillisec: int = 0, BidPrice1: float = 0.0, BidVolume1: int = 0, AskPrice1: float = 0.0, AskVolume1: int = 0, BidPrice2: float = 0.0, BidVolume2: int = 0, AskPrice2: float = 0.0,
                 AskVolume2: int = 0, BidPrice3: float = 0.0, BidVolume3: int = 0, AskPrice3: float = 0.0, AskVolume3: int = 0, BidPrice4: float = 0.0, BidVolume4: int = 0, AskPrice4: float = 0.0,
                 AskVolume4: int = 0, BidPrice5: float = 0.0, BidVolume5: int = 0, AskPrice5: float = 0.0, AskVolume5: int = 0, AveragePrice: float = 0.0, ActionDay: str = '', InstrumentID: str = '',
                 ExchangeInstID: str = '', BandingUpperPrice: float = 0.0, BandingLowerPrice: float = 0.0):
        super(DepthMarketDataField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve2 = self._to_bytes(reserve2)
        self.LastPrice = float(LastPrice)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)
        self.ClosePrice = float(ClosePrice)
        self.SettlementPrice = float(SettlementPrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.PreDelta = float(PreDelta)
        self.CurrDelta = float(CurrDelta)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.UpdateMillisec = int(UpdateMillisec)
        self.BidPrice1 = float(BidPrice1)
        self.BidVolume1 = int(BidVolume1)
        self.AskPrice1 = float(AskPrice1)
        self.AskVolume1 = int(AskVolume1)
        self.BidPrice2 = float(BidPrice2)
        self.BidVolume2 = int(BidVolume2)
        self.AskPrice2 = float(AskPrice2)
        self.AskVolume2 = int(AskVolume2)
        self.BidPrice3 = float(BidPrice3)
        self.BidVolume3 = int(BidVolume3)
        self.AskPrice3 = float(AskPrice3)
        self.AskVolume3 = int(AskVolume3)
        self.BidPrice4 = float(BidPrice4)
        self.BidVolume4 = int(BidVolume4)
        self.AskPrice4 = float(AskPrice4)
        self.AskVolume4 = int(AskVolume4)
        self.BidPrice5 = float(BidPrice5)
        self.BidVolume5 = int(BidVolume5)
        self.AskPrice5 = float(AskPrice5)
        self.AskVolume5 = int(AskVolume5)
        self.AveragePrice = float(AveragePrice)
        self.ActionDay = self._to_bytes(ActionDay)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.BandingUpperPrice = float(BandingUpperPrice)
        self.BandingLowerPrice = float(BandingLowerPrice)


class InstrumentTradingRightField(Base):
    """投资者合约交易权限"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('TradingRight', ctypes.c_char),  # 交易权限
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', TradingRight: str = '', InstrumentID: str = ''):
        super(InstrumentTradingRightField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.TradingRight = self._to_bytes(TradingRight)
        self.InstrumentID = self._to_bytes(InstrumentID)


class BrokerUserField(Base):
    """经纪公司用户"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('UserName', ctypes.c_char * 81),  # 用户名称
        ('UserType', ctypes.c_char),  # 用户类型
        ('IsActive', ctypes.c_int),  # 是否活跃
        ('IsUsingOTP', ctypes.c_int),  # 是否使用令牌
        ('IsAuthForce', ctypes.c_int),  # 是否强制终端认证
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', UserName: str = '', UserType: str = '', IsActive: int = 0, IsUsingOTP: int = 0, IsAuthForce: int = 0):
        super(BrokerUserField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserName = self._to_bytes(UserName)
        self.UserType = self._to_bytes(UserType)
        self.IsActive = int(IsActive)
        self.IsUsingOTP = int(IsUsingOTP)
        self.IsAuthForce = int(IsAuthForce)


class BrokerUserPasswordField(Base):
    """经纪公司用户口令"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Password', ctypes.c_char * 41),  # 密码
        ('LastUpdateTime', ctypes.c_char * 17),  # 上次修改时间
        ('LastLoginTime', ctypes.c_char * 17),  # 上次登陆时间
        ('ExpireDate', ctypes.c_char * 9),  # 密码过期时间
        ('WeakExpireDate', ctypes.c_char * 9),  # 弱密码过期时间
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', Password: str = '', LastUpdateTime: str = '', LastLoginTime: str = '', ExpireDate: str = '', WeakExpireDate: str = ''):
        super(BrokerUserPasswordField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.Password = self._to_bytes(Password)
        self.LastUpdateTime = self._to_bytes(LastUpdateTime)
        self.LastLoginTime = self._to_bytes(LastLoginTime)
        self.ExpireDate = self._to_bytes(ExpireDate)
        self.WeakExpireDate = self._to_bytes(WeakExpireDate)


class BrokerUserFunctionField(Base):
    """经纪公司用户功能权限"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('BrokerFunctionCode', ctypes.c_char),  # 经纪公司功能代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', BrokerFunctionCode: str = ''):
        super(BrokerUserFunctionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.BrokerFunctionCode = self._to_bytes(BrokerFunctionCode)


class TraderOfferField(Base):
    """交易所交易员报盘机"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('Password', ctypes.c_char * 41),  # 密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('TraderConnectStatus', ctypes.c_char),  # 交易所交易员连接状态
        ('ConnectRequestDate', ctypes.c_char * 9),  # 发出连接请求的日期
        ('ConnectRequestTime', ctypes.c_char * 9),  # 发出连接请求的时间
        ('LastReportDate', ctypes.c_char * 9),  # 上次报告日期
        ('LastReportTime', ctypes.c_char * 9),  # 上次报告时间
        ('ConnectDate', ctypes.c_char * 9),  # 完成连接日期
        ('ConnectTime', ctypes.c_char * 9),  # 完成连接时间
        ('StartDate', ctypes.c_char * 9),  # 启动日期
        ('StartTime', ctypes.c_char * 9),  # 启动时间
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('MaxTradeID', ctypes.c_char * 21),  # 本席位最大成交编号
        ('MaxOrderMessageReference', ctypes.c_char * 7),  # 本席位最大报单备拷
        ('OrderCancelAlg', ctypes.c_char),  # 撤单时选择席位算法
    ]

    def __init__(self, ExchangeID: str = '', TraderID: str = '', ParticipantID: str = '', Password: str = '', InstallID: int = 0, OrderLocalID: str = '', TraderConnectStatus: str = '',
                 ConnectRequestDate: str = '', ConnectRequestTime: str = '', LastReportDate: str = '', LastReportTime: str = '', ConnectDate: str = '', ConnectTime: str = '', StartDate: str = '',
                 StartTime: str = '', TradingDay: str = '', BrokerID: str = '', MaxTradeID: str = '', MaxOrderMessageReference: str = '', OrderCancelAlg: str = ''):
        super(TraderOfferField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.TraderConnectStatus = self._to_bytes(TraderConnectStatus)
        self.ConnectRequestDate = self._to_bytes(ConnectRequestDate)
        self.ConnectRequestTime = self._to_bytes(ConnectRequestTime)
        self.LastReportDate = self._to_bytes(LastReportDate)
        self.LastReportTime = self._to_bytes(LastReportTime)
        self.ConnectDate = self._to_bytes(ConnectDate)
        self.ConnectTime = self._to_bytes(ConnectTime)
        self.StartDate = self._to_bytes(StartDate)
        self.StartTime = self._to_bytes(StartTime)
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.MaxTradeID = self._to_bytes(MaxTradeID)
        self.MaxOrderMessageReference = self._to_bytes(MaxOrderMessageReference)
        self.OrderCancelAlg = self._to_bytes(OrderCancelAlg)


class SettlementInfoField(Base):
    """投资者结算结果"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('SequenceNo', ctypes.c_int),  # 序号
        ('Content', ctypes.c_char * 501),  # 消息正文
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, TradingDay: str = '', SettlementID: int = 0, BrokerID: str = '', InvestorID: str = '', SequenceNo: int = 0, Content: str = '', AccountID: str = '', CurrencyID: str = ''):
        super(SettlementInfoField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.SequenceNo = int(SequenceNo)
        self.Content = self._to_bytes(Content)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class InstrumentMarginRateAdjustField(Base):
    """合约保证金率调整"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('LongMarginRatioByMoney', ctypes.c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', ctypes.c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', ctypes.c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', ctypes.c_double),  # 空头保证金费
        ('IsRelative', ctypes.c_int),  # 是否相对交易所收取
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', HedgeFlag: str = '', LongMarginRatioByMoney: float = 0.0,
                 LongMarginRatioByVolume: float = 0.0, ShortMarginRatioByMoney: float = 0.0, ShortMarginRatioByVolume: float = 0.0, IsRelative: int = 0, InstrumentID: str = ''):
        super(InstrumentMarginRateAdjustField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)
        self.InstrumentID = self._to_bytes(InstrumentID)


class ExchangeMarginRateField(Base):
    """交易所保证金率"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('LongMarginRatioByMoney', ctypes.c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', ctypes.c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', ctypes.c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', ctypes.c_double),  # 空头保证金费
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', reserve1: str = '', HedgeFlag: str = '', LongMarginRatioByMoney: float = 0.0, LongMarginRatioByVolume: float = 0.0, ShortMarginRatioByMoney: float = 0.0,
                 ShortMarginRatioByVolume: float = 0.0, ExchangeID: str = '', InstrumentID: str = ''):
        super(ExchangeMarginRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.reserve1 = self._to_bytes(reserve1)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class ExchangeMarginRateAdjustField(Base):
    """交易所保证金率调整"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('LongMarginRatioByMoney', ctypes.c_double),  # 跟随交易所投资者多头保证金率
        ('LongMarginRatioByVolume', ctypes.c_double),  # 跟随交易所投资者多头保证金费
        ('ShortMarginRatioByMoney', ctypes.c_double),  # 跟随交易所投资者空头保证金率
        ('ShortMarginRatioByVolume', ctypes.c_double),  # 跟随交易所投资者空头保证金费
        ('ExchLongMarginRatioByMoney', ctypes.c_double),  # 交易所多头保证金率
        ('ExchLongMarginRatioByVolume', ctypes.c_double),  # 交易所多头保证金费
        ('ExchShortMarginRatioByMoney', ctypes.c_double),  # 交易所空头保证金率
        ('ExchShortMarginRatioByVolume', ctypes.c_double),  # 交易所空头保证金费
        ('NoLongMarginRatioByMoney', ctypes.c_double),  # 不跟随交易所投资者多头保证金率
        ('NoLongMarginRatioByVolume', ctypes.c_double),  # 不跟随交易所投资者多头保证金费
        ('NoShortMarginRatioByMoney', ctypes.c_double),  # 不跟随交易所投资者空头保证金率
        ('NoShortMarginRatioByVolume', ctypes.c_double),  # 不跟随交易所投资者空头保证金费
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', reserve1: str = '', HedgeFlag: str = '', LongMarginRatioByMoney: float = 0.0, LongMarginRatioByVolume: float = 0.0, ShortMarginRatioByMoney: float = 0.0,
                 ShortMarginRatioByVolume: float = 0.0, ExchLongMarginRatioByMoney: float = 0.0, ExchLongMarginRatioByVolume: float = 0.0, ExchShortMarginRatioByMoney: float = 0.0,
                 ExchShortMarginRatioByVolume: float = 0.0, NoLongMarginRatioByMoney: float = 0.0, NoLongMarginRatioByVolume: float = 0.0, NoShortMarginRatioByMoney: float = 0.0,
                 NoShortMarginRatioByVolume: float = 0.0, InstrumentID: str = ''):
        super(ExchangeMarginRateAdjustField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.reserve1 = self._to_bytes(reserve1)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.ExchLongMarginRatioByMoney = float(ExchLongMarginRatioByMoney)
        self.ExchLongMarginRatioByVolume = float(ExchLongMarginRatioByVolume)
        self.ExchShortMarginRatioByMoney = float(ExchShortMarginRatioByMoney)
        self.ExchShortMarginRatioByVolume = float(ExchShortMarginRatioByVolume)
        self.NoLongMarginRatioByMoney = float(NoLongMarginRatioByMoney)
        self.NoLongMarginRatioByVolume = float(NoLongMarginRatioByVolume)
        self.NoShortMarginRatioByMoney = float(NoShortMarginRatioByMoney)
        self.NoShortMarginRatioByVolume = float(NoShortMarginRatioByVolume)
        self.InstrumentID = self._to_bytes(InstrumentID)


class ExchangeRateField(Base):
    """汇率"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('FromCurrencyID', ctypes.c_char * 4),  # 源币种
        ('FromCurrencyUnit', ctypes.c_double),  # 源币种单位数量
        ('ToCurrencyID', ctypes.c_char * 4),  # 目标币种
        ('ExchangeRate', ctypes.c_double),  # 汇率
    ]

    def __init__(self, BrokerID: str = '', FromCurrencyID: str = '', FromCurrencyUnit: float = 0.0, ToCurrencyID: str = '', ExchangeRate: float = 0.0):
        super(ExchangeRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.FromCurrencyID = self._to_bytes(FromCurrencyID)
        self.FromCurrencyUnit = float(FromCurrencyUnit)
        self.ToCurrencyID = self._to_bytes(ToCurrencyID)
        self.ExchangeRate = float(ExchangeRate)


class SettlementRefField(Base):
    """结算引用"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
    ]

    def __init__(self, TradingDay: str = '', SettlementID: int = 0):
        super(SettlementRefField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)


class CurrentTimeField(Base):
    """当前时间"""
    _fields_ = [
        ('CurrDate', ctypes.c_char * 9),  # 当前交易日
        ('CurrTime', ctypes.c_char * 9),  # 当前时间
        ('CurrMillisec', ctypes.c_int),  # 当前时间（毫秒）
        ('ActionDay', ctypes.c_char * 9),  # 自然日期
    ]

    def __init__(self, CurrDate: str = '', CurrTime: str = '', CurrMillisec: int = 0, ActionDay: str = ''):
        super(CurrentTimeField, self).__init__()
        self.CurrDate = self._to_bytes(CurrDate)
        self.CurrTime = self._to_bytes(CurrTime)
        self.CurrMillisec = int(CurrMillisec)
        self.ActionDay = self._to_bytes(ActionDay)


class CommPhaseField(Base):
    """通讯阶段"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('CommPhaseNo', ctypes.c_short),  # 通讯时段编号
        ('SystemID', ctypes.c_char * 21),  # 系统编号
    ]

    def __init__(self, TradingDay: str = '', CommPhaseNo: int = 0, SystemID: str = ''):
        super(CommPhaseField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.CommPhaseNo = int(CommPhaseNo)
        self.SystemID = self._to_bytes(SystemID)


class LoginInfoField(Base):
    """登录信息"""
    _fields_ = [
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('LoginDate', ctypes.c_char * 9),  # 登录日期
        ('LoginTime', ctypes.c_char * 9),  # 登录时间
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', ctypes.c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', ctypes.c_char * 11),  # 协议信息
        ('SystemName', ctypes.c_char * 41),  # 系统名称
        ('PasswordDeprecated', ctypes.c_char * 41),  # 密码,已弃用
        ('MaxOrderRef', ctypes.c_char * 13),  # 最大报单引用
        ('SHFETime', ctypes.c_char * 9),  # 上期所时间
        ('DCETime', ctypes.c_char * 9),  # 大商所时间
        ('CZCETime', ctypes.c_char * 9),  # 郑商所时间
        ('FFEXTime', ctypes.c_char * 9),  # 中金所时间
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('OneTimePassword', ctypes.c_char * 41),  # 动态密码
        ('INETime', ctypes.c_char * 9),  # 能源中心时间
        ('IsQryControl', ctypes.c_int),  # 查询时是否需要流控
        ('LoginRemark', ctypes.c_char * 36),  # 登录备注
        ('Password', ctypes.c_char * 41),  # 密码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, FrontID: int = 0, SessionID: int = 0, BrokerID: str = '', UserID: str = '', LoginDate: str = '', LoginTime: str = '', reserve1: str = '', UserProductInfo: str = '',
                 InterfaceProductInfo: str = '', ProtocolInfo: str = '', SystemName: str = '', PasswordDeprecated: str = '', MaxOrderRef: str = '', SHFETime: str = '', DCETime: str = '',
                 CZCETime: str = '', FFEXTime: str = '', MacAddress: str = '', OneTimePassword: str = '', INETime: str = '', IsQryControl: int = 0, LoginRemark: str = '', Password: str = '',
                 IPAddress: str = ''):
        super(LoginInfoField, self).__init__()
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.LoginDate = self._to_bytes(LoginDate)
        self.LoginTime = self._to_bytes(LoginTime)
        self.reserve1 = self._to_bytes(reserve1)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.InterfaceProductInfo = self._to_bytes(InterfaceProductInfo)
        self.ProtocolInfo = self._to_bytes(ProtocolInfo)
        self.SystemName = self._to_bytes(SystemName)
        self.PasswordDeprecated = self._to_bytes(PasswordDeprecated)
        self.MaxOrderRef = self._to_bytes(MaxOrderRef)
        self.SHFETime = self._to_bytes(SHFETime)
        self.DCETime = self._to_bytes(DCETime)
        self.CZCETime = self._to_bytes(CZCETime)
        self.FFEXTime = self._to_bytes(FFEXTime)
        self.MacAddress = self._to_bytes(MacAddress)
        self.OneTimePassword = self._to_bytes(OneTimePassword)
        self.INETime = self._to_bytes(INETime)
        self.IsQryControl = int(IsQryControl)
        self.LoginRemark = self._to_bytes(LoginRemark)
        self.Password = self._to_bytes(Password)
        self.IPAddress = self._to_bytes(IPAddress)


class LogoutAllField(Base):
    """登录信息"""
    _fields_ = [
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('SystemName', ctypes.c_char * 41),  # 系统名称
    ]

    def __init__(self, FrontID: int = 0, SessionID: int = 0, SystemName: str = ''):
        super(LogoutAllField, self).__init__()
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.SystemName = self._to_bytes(SystemName)


class FrontStatusField(Base):
    """前置状态"""
    _fields_ = [
        ('FrontID', ctypes.c_int),  # 前置编号
        ('LastReportDate', ctypes.c_char * 9),  # 上次报告日期
        ('LastReportTime', ctypes.c_char * 9),  # 上次报告时间
        ('IsActive', ctypes.c_int),  # 是否活跃
    ]

    def __init__(self, FrontID: int = 0, LastReportDate: str = '', LastReportTime: str = '', IsActive: int = 0):
        super(FrontStatusField, self).__init__()
        self.FrontID = int(FrontID)
        self.LastReportDate = self._to_bytes(LastReportDate)
        self.LastReportTime = self._to_bytes(LastReportTime)
        self.IsActive = int(IsActive)


class UserPasswordUpdateField(Base):
    """用户口令变更"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('OldPassword', ctypes.c_char * 41),  # 原来的口令
        ('NewPassword', ctypes.c_char * 41),  # 新的口令
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', OldPassword: str = '', NewPassword: str = ''):
        super(UserPasswordUpdateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.OldPassword = self._to_bytes(OldPassword)
        self.NewPassword = self._to_bytes(NewPassword)


class InputOrderField(Base):
    """输入报单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('OrderRef', ctypes.c_char * 13),  # 报单引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('OrderPriceType', ctypes.c_char),  # 报单价格条件
        ('Direction', ctypes.c_char),  # 买卖方向
        ('CombOffsetFlag', ctypes.c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', ctypes.c_char * 5),  # 组合投机套保标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeTotalOriginal', ctypes.c_int),  # 数量
        ('TimeCondition', ctypes.c_char),  # 有效期类型
        ('GTDDate', ctypes.c_char * 9),  # GTD日期
        ('VolumeCondition', ctypes.c_char),  # 成交量类型
        ('MinVolume', ctypes.c_int),  # 最小成交量
        ('ContingentCondition', ctypes.c_char),  # 触发条件
        ('StopPrice', ctypes.c_double),  # 止损价
        ('ForceCloseReason', ctypes.c_char),  # 强平原因
        ('IsAutoSuspend', ctypes.c_int),  # 自动挂起标志
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('RequestID', ctypes.c_int),  # 请求编号
        ('UserForceClose', ctypes.c_int),  # 用户强评标志
        ('IsSwapOrder', ctypes.c_int),  # 互换单标志
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('ClientID', ctypes.c_char * 11),  # 交易编码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OrderRef: str = '', UserID: str = '', OrderPriceType: str = '', Direction: str = '', CombOffsetFlag: str = '',
                 CombHedgeFlag: str = '', LimitPrice: float = 0.0, VolumeTotalOriginal: int = 0, TimeCondition: str = '', GTDDate: str = '', VolumeCondition: str = '', MinVolume: int = 0,
                 ContingentCondition: str = '', StopPrice: float = 0.0, ForceCloseReason: str = '', IsAutoSuspend: int = 0, BusinessUnit: str = '', RequestID: int = 0, UserForceClose: int = 0,
                 IsSwapOrder: int = 0, ExchangeID: str = '', InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', ClientID: str = '', reserve2: str = '', MacAddress: str = '',
                 InstrumentID: str = '', IPAddress: str = ''):
        super(InputOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)
        self.IsSwapOrder = int(IsSwapOrder)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class OrderField(Base):
    """报单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('OrderRef', ctypes.c_char * 13),  # 报单引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('OrderPriceType', ctypes.c_char),  # 报单价格条件
        ('Direction', ctypes.c_char),  # 买卖方向
        ('CombOffsetFlag', ctypes.c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', ctypes.c_char * 5),  # 组合投机套保标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeTotalOriginal', ctypes.c_int),  # 数量
        ('TimeCondition', ctypes.c_char),  # 有效期类型
        ('GTDDate', ctypes.c_char * 9),  # GTD日期
        ('VolumeCondition', ctypes.c_char),  # 成交量类型
        ('MinVolume', ctypes.c_int),  # 最小成交量
        ('ContingentCondition', ctypes.c_char),  # 触发条件
        ('StopPrice', ctypes.c_double),  # 止损价
        ('ForceCloseReason', ctypes.c_char),  # 强平原因
        ('IsAutoSuspend', ctypes.c_int),  # 自动挂起标志
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('RequestID', ctypes.c_int),  # 请求编号
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderSubmitStatus', ctypes.c_char),  # 报单提交状态
        ('NotifySequence', ctypes.c_int),  # 报单提示序号
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('OrderSource', ctypes.c_char),  # 报单来源
        ('OrderStatus', ctypes.c_char),  # 报单状态
        ('OrderType', ctypes.c_char),  # 报单类型
        ('VolumeTraded', ctypes.c_int),  # 今成交数量
        ('VolumeTotal', ctypes.c_int),  # 剩余数量
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 委托时间
        ('ActiveTime', ctypes.c_char * 9),  # 激活时间
        ('SuspendTime', ctypes.c_char * 9),  # 挂起时间
        ('UpdateTime', ctypes.c_char * 9),  # 最后修改时间
        ('CancelTime', ctypes.c_char * 9),  # 撤销时间
        ('ActiveTraderID', ctypes.c_char * 21),  # 最后修改交易所交易员代码
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('UserForceClose', ctypes.c_int),  # 用户强评标志
        ('ActiveUserID', ctypes.c_char * 16),  # 操作用户代码
        ('BrokerOrderSeq', ctypes.c_int),  # 经纪公司报单编号
        ('RelativeOrderSysID', ctypes.c_char * 21),  # 相关报单
        ('ZCETotalTradedVolume', ctypes.c_int),  # 郑商所成交数量
        ('IsSwapOrder', ctypes.c_int),  # 互换单标志
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('reserve3', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OrderRef: str = '', UserID: str = '', OrderPriceType: str = '', Direction: str = '', CombOffsetFlag: str = '',
                 CombHedgeFlag: str = '', LimitPrice: float = 0.0, VolumeTotalOriginal: int = 0, TimeCondition: str = '', GTDDate: str = '', VolumeCondition: str = '', MinVolume: int = 0,
                 ContingentCondition: str = '', StopPrice: float = 0.0, ForceCloseReason: str = '', IsAutoSuspend: int = 0, BusinessUnit: str = '', RequestID: int = 0, OrderLocalID: str = '',
                 ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '', reserve2: str = '', TraderID: str = '', InstallID: int = 0, OrderSubmitStatus: str = '', NotifySequence: int = 0,
                 TradingDay: str = '', SettlementID: int = 0, OrderSysID: str = '', OrderSource: str = '', OrderStatus: str = '', OrderType: str = '', VolumeTraded: int = 0, VolumeTotal: int = 0,
                 InsertDate: str = '', InsertTime: str = '', ActiveTime: str = '', SuspendTime: str = '', UpdateTime: str = '', CancelTime: str = '', ActiveTraderID: str = '',
                 ClearingPartID: str = '', SequenceNo: int = 0, FrontID: int = 0, SessionID: int = 0, UserProductInfo: str = '', StatusMsg: str = '', UserForceClose: int = 0, ActiveUserID: str = '',
                 BrokerOrderSeq: int = 0, RelativeOrderSysID: str = '', ZCETotalTradedVolume: int = 0, IsSwapOrder: int = 0, BranchID: str = '', InvestUnitID: str = '', AccountID: str = '',
                 CurrencyID: str = '', reserve3: str = '', MacAddress: str = '', InstrumentID: str = '', ExchangeInstID: str = '', IPAddress: str = ''):
        super(OrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.OrderSource = self._to_bytes(OrderSource)
        self.OrderStatus = self._to_bytes(OrderStatus)
        self.OrderType = self._to_bytes(OrderType)
        self.VolumeTraded = int(VolumeTraded)
        self.VolumeTotal = int(VolumeTotal)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.ActiveTime = self._to_bytes(ActiveTime)
        self.SuspendTime = self._to_bytes(SuspendTime)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ActiveTraderID = self._to_bytes(ActiveTraderID)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.UserForceClose = int(UserForceClose)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerOrderSeq = int(BrokerOrderSeq)
        self.RelativeOrderSysID = self._to_bytes(RelativeOrderSysID)
        self.ZCETotalTradedVolume = int(ZCETotalTradedVolume)
        self.IsSwapOrder = int(IsSwapOrder)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.reserve3 = self._to_bytes(reserve3)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class ExchangeOrderField(Base):
    """交易所报单"""
    _fields_ = [
        ('OrderPriceType', ctypes.c_char),  # 报单价格条件
        ('Direction', ctypes.c_char),  # 买卖方向
        ('CombOffsetFlag', ctypes.c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', ctypes.c_char * 5),  # 组合投机套保标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeTotalOriginal', ctypes.c_int),  # 数量
        ('TimeCondition', ctypes.c_char),  # 有效期类型
        ('GTDDate', ctypes.c_char * 9),  # GTD日期
        ('VolumeCondition', ctypes.c_char),  # 成交量类型
        ('MinVolume', ctypes.c_int),  # 最小成交量
        ('ContingentCondition', ctypes.c_char),  # 触发条件
        ('StopPrice', ctypes.c_double),  # 止损价
        ('ForceCloseReason', ctypes.c_char),  # 强平原因
        ('IsAutoSuspend', ctypes.c_int),  # 自动挂起标志
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('RequestID', ctypes.c_int),  # 请求编号
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderSubmitStatus', ctypes.c_char),  # 报单提交状态
        ('NotifySequence', ctypes.c_int),  # 报单提示序号
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('OrderSource', ctypes.c_char),  # 报单来源
        ('OrderStatus', ctypes.c_char),  # 报单状态
        ('OrderType', ctypes.c_char),  # 报单类型
        ('VolumeTraded', ctypes.c_int),  # 今成交数量
        ('VolumeTotal', ctypes.c_int),  # 剩余数量
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 委托时间
        ('ActiveTime', ctypes.c_char * 9),  # 激活时间
        ('SuspendTime', ctypes.c_char * 9),  # 挂起时间
        ('UpdateTime', ctypes.c_char * 9),  # 最后修改时间
        ('CancelTime', ctypes.c_char * 9),  # 撤销时间
        ('ActiveTraderID', ctypes.c_char * 21),  # 最后修改交易所交易员代码
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, OrderPriceType: str = '', Direction: str = '', CombOffsetFlag: str = '', CombHedgeFlag: str = '', LimitPrice: float = 0.0, VolumeTotalOriginal: int = 0, TimeCondition: str = '',
                 GTDDate: str = '', VolumeCondition: str = '', MinVolume: int = 0, ContingentCondition: str = '', StopPrice: float = 0.0, ForceCloseReason: str = '', IsAutoSuspend: int = 0,
                 BusinessUnit: str = '', RequestID: int = 0, OrderLocalID: str = '', ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '', reserve1: str = '', TraderID: str = '',
                 InstallID: int = 0, OrderSubmitStatus: str = '', NotifySequence: int = 0, TradingDay: str = '', SettlementID: int = 0, OrderSysID: str = '', OrderSource: str = '',
                 OrderStatus: str = '', OrderType: str = '', VolumeTraded: int = 0, VolumeTotal: int = 0, InsertDate: str = '', InsertTime: str = '', ActiveTime: str = '', SuspendTime: str = '',
                 UpdateTime: str = '', CancelTime: str = '', ActiveTraderID: str = '', ClearingPartID: str = '', SequenceNo: int = 0, BranchID: str = '', reserve2: str = '', MacAddress: str = '',
                 ExchangeInstID: str = '', IPAddress: str = ''):
        super(ExchangeOrderField, self).__init__()
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.OrderSource = self._to_bytes(OrderSource)
        self.OrderStatus = self._to_bytes(OrderStatus)
        self.OrderType = self._to_bytes(OrderType)
        self.VolumeTraded = int(VolumeTraded)
        self.VolumeTotal = int(VolumeTotal)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.ActiveTime = self._to_bytes(ActiveTime)
        self.SuspendTime = self._to_bytes(SuspendTime)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ActiveTraderID = self._to_bytes(ActiveTraderID)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.BranchID = self._to_bytes(BranchID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class ExchangeOrderInsertErrorField(Base):
    """交易所报单插入失败"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
    ]

    def __init__(self, ExchangeID: str = '', ParticipantID: str = '', TraderID: str = '', InstallID: int = 0, OrderLocalID: str = '', ErrorID: int = 0, ErrorMsg: str = ''):
        super(ExchangeOrderInsertErrorField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class InputOrderActionField(Base):
    """输入报单操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OrderActionRef', ctypes.c_int),  # 报单操作引用
        ('OrderRef', ctypes.c_char * 13),  # 报单引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeChange', ctypes.c_int),  # 数量变化
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', OrderActionRef: int = 0, OrderRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '',
                 OrderSysID: str = '', ActionFlag: str = '', LimitPrice: float = 0.0, VolumeChange: int = 0, UserID: str = '', reserve1: str = '', InvestUnitID: str = '', reserve2: str = '',
                 MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(InputOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = self._to_bytes(OrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.UserID = self._to_bytes(UserID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class OrderActionField(Base):
    """报单操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OrderActionRef', ctypes.c_int),  # 报单操作引用
        ('OrderRef', ctypes.c_char * 13),  # 报单引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeChange', ctypes.c_int),  # 数量变化
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', OrderActionRef: int = 0, OrderRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '',
                 OrderSysID: str = '', ActionFlag: str = '', LimitPrice: float = 0.0, VolumeChange: int = 0, ActionDate: str = '', ActionTime: str = '', TraderID: str = '', InstallID: int = 0,
                 OrderLocalID: str = '', ActionLocalID: str = '', ParticipantID: str = '', ClientID: str = '', BusinessUnit: str = '', OrderActionStatus: str = '', UserID: str = '',
                 StatusMsg: str = '', reserve1: str = '', BranchID: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(OrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = self._to_bytes(OrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.reserve1 = self._to_bytes(reserve1)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class ExchangeOrderActionField(Base):
    """交易所报单操作"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeChange', ctypes.c_int),  # 数量变化
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, ExchangeID: str = '', OrderSysID: str = '', ActionFlag: str = '', LimitPrice: float = 0.0, VolumeChange: int = 0, ActionDate: str = '', ActionTime: str = '', TraderID: str = '',
                 InstallID: int = 0, OrderLocalID: str = '', ActionLocalID: str = '', ParticipantID: str = '', ClientID: str = '', BusinessUnit: str = '', OrderActionStatus: str = '',
                 UserID: str = '', BranchID: str = '', reserve1: str = '', MacAddress: str = '', IPAddress: str = ''):
        super(ExchangeOrderActionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.BranchID = self._to_bytes(BranchID)
        self.reserve1 = self._to_bytes(reserve1)
        self.MacAddress = self._to_bytes(MacAddress)
        self.IPAddress = self._to_bytes(IPAddress)


class ExchangeOrderActionErrorField(Base):
    """交易所报单操作失败"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
    ]

    def __init__(self, ExchangeID: str = '', OrderSysID: str = '', TraderID: str = '', InstallID: int = 0, OrderLocalID: str = '', ActionLocalID: str = '', ErrorID: int = 0, ErrorMsg: str = ''):
        super(ExchangeOrderActionErrorField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class ExchangeTradeField(Base):
    """交易所成交"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TradeID', ctypes.c_char * 21),  # 成交编号
        ('Direction', ctypes.c_char),  # 买卖方向
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('TradingRole', ctypes.c_char),  # 交易角色
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('OffsetFlag', ctypes.c_char),  # 开平标志
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('Price', ctypes.c_double),  # 价格
        ('Volume', ctypes.c_int),  # 数量
        ('TradeDate', ctypes.c_char * 9),  # 成交时期
        ('TradeTime', ctypes.c_char * 9),  # 成交时间
        ('TradeType', ctypes.c_char),  # 成交类型
        ('PriceSource', ctypes.c_char),  # 成交价来源
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('SequenceNo', ctypes.c_int),  # 序号
        ('TradeSource', ctypes.c_char),  # 成交来源
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, ExchangeID: str = '', TradeID: str = '', Direction: str = '', OrderSysID: str = '', ParticipantID: str = '', ClientID: str = '', TradingRole: str = '', reserve1: str = '',
                 OffsetFlag: str = '', HedgeFlag: str = '', Price: float = 0.0, Volume: int = 0, TradeDate: str = '', TradeTime: str = '', TradeType: str = '', PriceSource: str = '',
                 TraderID: str = '', OrderLocalID: str = '', ClearingPartID: str = '', BusinessUnit: str = '', SequenceNo: int = 0, TradeSource: str = '', ExchangeInstID: str = ''):
        super(ExchangeTradeField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TradeID = self._to_bytes(TradeID)
        self.Direction = self._to_bytes(Direction)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.TradingRole = self._to_bytes(TradingRole)
        self.reserve1 = self._to_bytes(reserve1)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Price = float(Price)
        self.Volume = int(Volume)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.TradeType = self._to_bytes(TradeType)
        self.PriceSource = self._to_bytes(PriceSource)
        self.TraderID = self._to_bytes(TraderID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.SequenceNo = int(SequenceNo)
        self.TradeSource = self._to_bytes(TradeSource)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class TradeField(Base):
    """成交"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('OrderRef', ctypes.c_char * 13),  # 报单引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TradeID', ctypes.c_char * 21),  # 成交编号
        ('Direction', ctypes.c_char),  # 买卖方向
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('TradingRole', ctypes.c_char),  # 交易角色
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('OffsetFlag', ctypes.c_char),  # 开平标志
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('Price', ctypes.c_double),  # 价格
        ('Volume', ctypes.c_int),  # 数量
        ('TradeDate', ctypes.c_char * 9),  # 成交时期
        ('TradeTime', ctypes.c_char * 9),  # 成交时间
        ('TradeType', ctypes.c_char),  # 成交类型
        ('PriceSource', ctypes.c_char),  # 成交价来源
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('SequenceNo', ctypes.c_int),  # 序号
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('BrokerOrderSeq', ctypes.c_int),  # 经纪公司报单编号
        ('TradeSource', ctypes.c_char),  # 成交来源
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OrderRef: str = '', UserID: str = '', ExchangeID: str = '', TradeID: str = '', Direction: str = '',
                 OrderSysID: str = '', ParticipantID: str = '', ClientID: str = '', TradingRole: str = '', reserve2: str = '', OffsetFlag: str = '', HedgeFlag: str = '', Price: float = 0.0,
                 Volume: int = 0, TradeDate: str = '', TradeTime: str = '', TradeType: str = '', PriceSource: str = '', TraderID: str = '', OrderLocalID: str = '', ClearingPartID: str = '',
                 BusinessUnit: str = '', SequenceNo: int = 0, TradingDay: str = '', SettlementID: int = 0, BrokerOrderSeq: int = 0, TradeSource: str = '', InvestUnitID: str = '',
                 InstrumentID: str = '', ExchangeInstID: str = ''):
        super(TradeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TradeID = self._to_bytes(TradeID)
        self.Direction = self._to_bytes(Direction)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.TradingRole = self._to_bytes(TradingRole)
        self.reserve2 = self._to_bytes(reserve2)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Price = float(Price)
        self.Volume = int(Volume)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.TradeType = self._to_bytes(TradeType)
        self.PriceSource = self._to_bytes(PriceSource)
        self.TraderID = self._to_bytes(TraderID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.SequenceNo = int(SequenceNo)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.BrokerOrderSeq = int(BrokerOrderSeq)
        self.TradeSource = self._to_bytes(TradeSource)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class UserSessionField(Base):
    """用户会话"""
    _fields_ = [
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('LoginDate', ctypes.c_char * 9),  # 登录日期
        ('LoginTime', ctypes.c_char * 9),  # 登录时间
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', ctypes.c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', ctypes.c_char * 11),  # 协议信息
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('LoginRemark', ctypes.c_char * 36),  # 登录备注
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, FrontID: int = 0, SessionID: int = 0, BrokerID: str = '', UserID: str = '', LoginDate: str = '', LoginTime: str = '', reserve1: str = '', UserProductInfo: str = '',
                 InterfaceProductInfo: str = '', ProtocolInfo: str = '', MacAddress: str = '', LoginRemark: str = '', IPAddress: str = ''):
        super(UserSessionField, self).__init__()
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.LoginDate = self._to_bytes(LoginDate)
        self.LoginTime = self._to_bytes(LoginTime)
        self.reserve1 = self._to_bytes(reserve1)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.InterfaceProductInfo = self._to_bytes(InterfaceProductInfo)
        self.ProtocolInfo = self._to_bytes(ProtocolInfo)
        self.MacAddress = self._to_bytes(MacAddress)
        self.LoginRemark = self._to_bytes(LoginRemark)
        self.IPAddress = self._to_bytes(IPAddress)


class QryMaxOrderVolumeField(Base):
    """查询最大报单数量"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('Direction', ctypes.c_char),  # 买卖方向
        ('OffsetFlag', ctypes.c_char),  # 开平标志
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('MaxVolume', ctypes.c_int),  # 最大允许报单数量
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', Direction: str = '', OffsetFlag: str = '', HedgeFlag: str = '', MaxVolume: int = 0, ExchangeID: str = '',
                 InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryMaxOrderVolumeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.Direction = self._to_bytes(Direction)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.MaxVolume = int(MaxVolume)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class SettlementInfoConfirmField(Base):
    """投资者结算结果确认信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ConfirmDate', ctypes.c_char * 9),  # 确认日期
        ('ConfirmTime', ctypes.c_char * 9),  # 确认时间
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ConfirmDate: str = '', ConfirmTime: str = '', SettlementID: int = 0, AccountID: str = '', CurrencyID: str = ''):
        super(SettlementInfoConfirmField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ConfirmDate = self._to_bytes(ConfirmDate)
        self.ConfirmTime = self._to_bytes(ConfirmTime)
        self.SettlementID = int(SettlementID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class SyncDepositField(Base):
    """出入金同步"""
    _fields_ = [
        ('DepositSeqNo', ctypes.c_char * 15),  # 出入金流水号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('Deposit', ctypes.c_double),  # 入金金额
        ('IsForce', ctypes.c_int),  # 是否强制进行
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('IsFromSopt', ctypes.c_int),  # 是否是个股期权内转
        ('TradingPassword', ctypes.c_char * 41),  # 资金密码
    ]

    def __init__(self, DepositSeqNo: str = '', BrokerID: str = '', InvestorID: str = '', Deposit: float = 0.0, IsForce: int = 0, CurrencyID: str = '', IsFromSopt: int = 0, TradingPassword: str = ''):
        super(SyncDepositField, self).__init__()
        self.DepositSeqNo = self._to_bytes(DepositSeqNo)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Deposit = float(Deposit)
        self.IsForce = int(IsForce)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.IsFromSopt = int(IsFromSopt)
        self.TradingPassword = self._to_bytes(TradingPassword)


class SyncFundMortgageField(Base):
    """货币质押同步"""
    _fields_ = [
        ('MortgageSeqNo', ctypes.c_char * 15),  # 货币质押流水号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('FromCurrencyID', ctypes.c_char * 4),  # 源币种
        ('MortgageAmount', ctypes.c_double),  # 质押金额
        ('ToCurrencyID', ctypes.c_char * 4),  # 目标币种
    ]

    def __init__(self, MortgageSeqNo: str = '', BrokerID: str = '', InvestorID: str = '', FromCurrencyID: str = '', MortgageAmount: float = 0.0, ToCurrencyID: str = ''):
        super(SyncFundMortgageField, self).__init__()
        self.MortgageSeqNo = self._to_bytes(MortgageSeqNo)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.FromCurrencyID = self._to_bytes(FromCurrencyID)
        self.MortgageAmount = float(MortgageAmount)
        self.ToCurrencyID = self._to_bytes(ToCurrencyID)


class BrokerSyncField(Base):
    """经纪公司同步"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
    ]

    def __init__(self, BrokerID: str = ''):
        super(BrokerSyncField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class SyncingInvestorField(Base):
    """正在同步中的投资者"""
    _fields_ = [
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorGroupID', ctypes.c_char * 13),  # 投资者分组代码
        ('InvestorName', ctypes.c_char * 81),  # 投资者名称
        ('IdentifiedCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('IsActive', ctypes.c_int),  # 是否活跃
        ('Telephone', ctypes.c_char * 41),  # 联系电话
        ('Address', ctypes.c_char * 101),  # 通讯地址
        ('OpenDate', ctypes.c_char * 9),  # 开户日期
        ('Mobile', ctypes.c_char * 41),  # 手机
        ('CommModelID', ctypes.c_char * 13),  # 手续费率模板代码
        ('MarginModelID', ctypes.c_char * 13),  # 保证金率模板代码
        ('IsOrderFreq', ctypes.c_char),  # 是否频率控制
        ('IsOpenVolLimit', ctypes.c_char),  # 是否开仓限制
    ]

    def __init__(self, InvestorID: str = '', BrokerID: str = '', InvestorGroupID: str = '', InvestorName: str = '', IdentifiedCardType: str = '', IdentifiedCardNo: str = '', IsActive: int = 0,
                 Telephone: str = '', Address: str = '', OpenDate: str = '', Mobile: str = '', CommModelID: str = '', MarginModelID: str = '', IsOrderFreq: str = '', IsOpenVolLimit: str = ''):
        super(SyncingInvestorField, self).__init__()
        self.InvestorID = self._to_bytes(InvestorID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorGroupID = self._to_bytes(InvestorGroupID)
        self.InvestorName = self._to_bytes(InvestorName)
        self.IdentifiedCardType = self._to_bytes(IdentifiedCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.IsActive = int(IsActive)
        self.Telephone = self._to_bytes(Telephone)
        self.Address = self._to_bytes(Address)
        self.OpenDate = self._to_bytes(OpenDate)
        self.Mobile = self._to_bytes(Mobile)
        self.CommModelID = self._to_bytes(CommModelID)
        self.MarginModelID = self._to_bytes(MarginModelID)
        self.IsOrderFreq = self._to_bytes(IsOrderFreq)
        self.IsOpenVolLimit = self._to_bytes(IsOpenVolLimit)


class SyncingTradingCodeField(Base):
    """正在同步中的交易代码"""
    _fields_ = [
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('IsActive', ctypes.c_int),  # 是否活跃
        ('ClientIDType', ctypes.c_char),  # 交易编码类型
    ]

    def __init__(self, InvestorID: str = '', BrokerID: str = '', ExchangeID: str = '', ClientID: str = '', IsActive: int = 0, ClientIDType: str = ''):
        super(SyncingTradingCodeField, self).__init__()
        self.InvestorID = self._to_bytes(InvestorID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ClientID = self._to_bytes(ClientID)
        self.IsActive = int(IsActive)
        self.ClientIDType = self._to_bytes(ClientIDType)


class SyncingInvestorGroupField(Base):
    """正在同步中的投资者分组"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorGroupID', ctypes.c_char * 13),  # 投资者分组代码
        ('InvestorGroupName', ctypes.c_char * 41),  # 投资者分组名称
    ]

    def __init__(self, BrokerID: str = '', InvestorGroupID: str = '', InvestorGroupName: str = ''):
        super(SyncingInvestorGroupField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorGroupID = self._to_bytes(InvestorGroupID)
        self.InvestorGroupName = self._to_bytes(InvestorGroupName)


class SyncingTradingAccountField(Base):
    """正在同步中的交易账号"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('PreMortgage', ctypes.c_double),  # 上次质押金额
        ('PreCredit', ctypes.c_double),  # 上次信用额度
        ('PreDeposit', ctypes.c_double),  # 上次存款额
        ('PreBalance', ctypes.c_double),  # 上次结算准备金
        ('PreMargin', ctypes.c_double),  # 上次占用的保证金
        ('InterestBase', ctypes.c_double),  # 利息基数
        ('Interest', ctypes.c_double),  # 利息收入
        ('Deposit', ctypes.c_double),  # 入金金额
        ('Withdraw', ctypes.c_double),  # 出金金额
        ('FrozenMargin', ctypes.c_double),  # 冻结的保证金
        ('FrozenCash', ctypes.c_double),  # 冻结的资金
        ('FrozenCommission', ctypes.c_double),  # 冻结的手续费
        ('CurrMargin', ctypes.c_double),  # 当前保证金总额
        ('CashIn', ctypes.c_double),  # 资金差额
        ('Commission', ctypes.c_double),  # 手续费
        ('CloseProfit', ctypes.c_double),  # 平仓盈亏
        ('PositionProfit', ctypes.c_double),  # 持仓盈亏
        ('Balance', ctypes.c_double),  # 期货结算准备金
        ('Available', ctypes.c_double),  # 可用资金
        ('WithdrawQuota', ctypes.c_double),  # 可取资金
        ('Reserve', ctypes.c_double),  # 基本准备金
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('Credit', ctypes.c_double),  # 信用额度
        ('Mortgage', ctypes.c_double),  # 质押金额
        ('ExchangeMargin', ctypes.c_double),  # 交易所保证金
        ('DeliveryMargin', ctypes.c_double),  # 投资者交割保证金
        ('ExchangeDeliveryMargin', ctypes.c_double),  # 交易所交割保证金
        ('ReserveBalance', ctypes.c_double),  # 保底期货结算准备金
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('PreFundMortgageIn', ctypes.c_double),  # 上次货币质入金额
        ('PreFundMortgageOut', ctypes.c_double),  # 上次货币质出金额
        ('FundMortgageIn', ctypes.c_double),  # 货币质入金额
        ('FundMortgageOut', ctypes.c_double),  # 货币质出金额
        ('FundMortgageAvailable', ctypes.c_double),  # 货币质押余额
        ('MortgageableFund', ctypes.c_double),  # 可质押货币金额
        ('SpecProductMargin', ctypes.c_double),  # 特殊产品占用保证金
        ('SpecProductFrozenMargin', ctypes.c_double),  # 特殊产品冻结保证金
        ('SpecProductCommission', ctypes.c_double),  # 特殊产品手续费
        ('SpecProductFrozenCommission', ctypes.c_double),  # 特殊产品冻结手续费
        ('SpecProductPositionProfit', ctypes.c_double),  # 特殊产品持仓盈亏
        ('SpecProductCloseProfit', ctypes.c_double),  # 特殊产品平仓盈亏
        ('SpecProductPositionProfitByAlg', ctypes.c_double),  # 根据持仓盈亏算法计算的特殊产品持仓盈亏
        ('SpecProductExchangeMargin', ctypes.c_double),  # 特殊产品交易所保证金
        ('FrozenSwap', ctypes.c_double),  # 延时换汇冻结金额
        ('RemainSwap', ctypes.c_double),  # 剩余换汇额度
    ]

    def __init__(self, BrokerID: str = '', AccountID: str = '', PreMortgage: float = 0.0, PreCredit: float = 0.0, PreDeposit: float = 0.0, PreBalance: float = 0.0, PreMargin: float = 0.0,
                 InterestBase: float = 0.0, Interest: float = 0.0, Deposit: float = 0.0, Withdraw: float = 0.0, FrozenMargin: float = 0.0, FrozenCash: float = 0.0, FrozenCommission: float = 0.0,
                 CurrMargin: float = 0.0, CashIn: float = 0.0, Commission: float = 0.0, CloseProfit: float = 0.0, PositionProfit: float = 0.0, Balance: float = 0.0, Available: float = 0.0,
                 WithdrawQuota: float = 0.0, Reserve: float = 0.0, TradingDay: str = '', SettlementID: int = 0, Credit: float = 0.0, Mortgage: float = 0.0, ExchangeMargin: float = 0.0,
                 DeliveryMargin: float = 0.0, ExchangeDeliveryMargin: float = 0.0, ReserveBalance: float = 0.0, CurrencyID: str = '', PreFundMortgageIn: float = 0.0, PreFundMortgageOut: float = 0.0,
                 FundMortgageIn: float = 0.0, FundMortgageOut: float = 0.0, FundMortgageAvailable: float = 0.0, MortgageableFund: float = 0.0, SpecProductMargin: float = 0.0,
                 SpecProductFrozenMargin: float = 0.0, SpecProductCommission: float = 0.0, SpecProductFrozenCommission: float = 0.0, SpecProductPositionProfit: float = 0.0,
                 SpecProductCloseProfit: float = 0.0, SpecProductPositionProfitByAlg: float = 0.0, SpecProductExchangeMargin: float = 0.0, FrozenSwap: float = 0.0, RemainSwap: float = 0.0):
        super(SyncingTradingAccountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.PreMortgage = float(PreMortgage)
        self.PreCredit = float(PreCredit)
        self.PreDeposit = float(PreDeposit)
        self.PreBalance = float(PreBalance)
        self.PreMargin = float(PreMargin)
        self.InterestBase = float(InterestBase)
        self.Interest = float(Interest)
        self.Deposit = float(Deposit)
        self.Withdraw = float(Withdraw)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CurrMargin = float(CurrMargin)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.CloseProfit = float(CloseProfit)
        self.PositionProfit = float(PositionProfit)
        self.Balance = float(Balance)
        self.Available = float(Available)
        self.WithdrawQuota = float(WithdrawQuota)
        self.Reserve = float(Reserve)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.Credit = float(Credit)
        self.Mortgage = float(Mortgage)
        self.ExchangeMargin = float(ExchangeMargin)
        self.DeliveryMargin = float(DeliveryMargin)
        self.ExchangeDeliveryMargin = float(ExchangeDeliveryMargin)
        self.ReserveBalance = float(ReserveBalance)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.PreFundMortgageIn = float(PreFundMortgageIn)
        self.PreFundMortgageOut = float(PreFundMortgageOut)
        self.FundMortgageIn = float(FundMortgageIn)
        self.FundMortgageOut = float(FundMortgageOut)
        self.FundMortgageAvailable = float(FundMortgageAvailable)
        self.MortgageableFund = float(MortgageableFund)
        self.SpecProductMargin = float(SpecProductMargin)
        self.SpecProductFrozenMargin = float(SpecProductFrozenMargin)
        self.SpecProductCommission = float(SpecProductCommission)
        self.SpecProductFrozenCommission = float(SpecProductFrozenCommission)
        self.SpecProductPositionProfit = float(SpecProductPositionProfit)
        self.SpecProductCloseProfit = float(SpecProductCloseProfit)
        self.SpecProductPositionProfitByAlg = float(SpecProductPositionProfitByAlg)
        self.SpecProductExchangeMargin = float(SpecProductExchangeMargin)
        self.FrozenSwap = float(FrozenSwap)
        self.RemainSwap = float(RemainSwap)


class SyncingInvestorPositionField(Base):
    """正在同步中的投资者持仓"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('PosiDirection', ctypes.c_char),  # 持仓多空方向
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('PositionDate', ctypes.c_char),  # 持仓日期
        ('YdPosition', ctypes.c_int),  # 上日持仓
        ('Position', ctypes.c_int),  # 今日持仓
        ('LongFrozen', ctypes.c_int),  # 多头冻结
        ('ShortFrozen', ctypes.c_int),  # 空头冻结
        ('LongFrozenAmount', ctypes.c_double),  # 开仓冻结金额
        ('ShortFrozenAmount', ctypes.c_double),  # 开仓冻结金额
        ('OpenVolume', ctypes.c_int),  # 开仓量
        ('CloseVolume', ctypes.c_int),  # 平仓量
        ('OpenAmount', ctypes.c_double),  # 开仓金额
        ('CloseAmount', ctypes.c_double),  # 平仓金额
        ('PositionCost', ctypes.c_double),  # 持仓成本
        ('PreMargin', ctypes.c_double),  # 上次占用的保证金
        ('UseMargin', ctypes.c_double),  # 占用的保证金
        ('FrozenMargin', ctypes.c_double),  # 冻结的保证金
        ('FrozenCash', ctypes.c_double),  # 冻结的资金
        ('FrozenCommission', ctypes.c_double),  # 冻结的手续费
        ('CashIn', ctypes.c_double),  # 资金差额
        ('Commission', ctypes.c_double),  # 手续费
        ('CloseProfit', ctypes.c_double),  # 平仓盈亏
        ('PositionProfit', ctypes.c_double),  # 持仓盈亏
        ('PreSettlementPrice', ctypes.c_double),  # 上次结算价
        ('SettlementPrice', ctypes.c_double),  # 本次结算价
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('OpenCost', ctypes.c_double),  # 开仓成本
        ('ExchangeMargin', ctypes.c_double),  # 交易所保证金
        ('CombPosition', ctypes.c_int),  # 组合成交形成的持仓
        ('CombLongFrozen', ctypes.c_int),  # 组合多头冻结
        ('CombShortFrozen', ctypes.c_int),  # 组合空头冻结
        ('CloseProfitByDate', ctypes.c_double),  # 逐日盯市平仓盈亏
        ('CloseProfitByTrade', ctypes.c_double),  # 逐笔对冲平仓盈亏
        ('TodayPosition', ctypes.c_int),  # 今日持仓
        ('MarginRateByMoney', ctypes.c_double),  # 保证金率
        ('MarginRateByVolume', ctypes.c_double),  # 保证金率(按手数)
        ('StrikeFrozen', ctypes.c_int),  # 执行冻结
        ('StrikeFrozenAmount', ctypes.c_double),  # 执行冻结金额
        ('AbandonFrozen', ctypes.c_int),  # 放弃执行冻结
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('YdStrikeFrozen', ctypes.c_int),  # 执行冻结的昨仓
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('PositionCostOffset', ctypes.c_double),  # 持仓成本差值
        ('TasPosition', ctypes.c_int),  # tas持仓手数
        ('TasPositionCost', ctypes.c_double),  # tas持仓成本
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', BrokerID: str = '', InvestorID: str = '', PosiDirection: str = '', HedgeFlag: str = '', PositionDate: str = '', YdPosition: int = 0, Position: int = 0,
                 LongFrozen: int = 0, ShortFrozen: int = 0, LongFrozenAmount: float = 0.0, ShortFrozenAmount: float = 0.0, OpenVolume: int = 0, CloseVolume: int = 0, OpenAmount: float = 0.0,
                 CloseAmount: float = 0.0, PositionCost: float = 0.0, PreMargin: float = 0.0, UseMargin: float = 0.0, FrozenMargin: float = 0.0, FrozenCash: float = 0.0, FrozenCommission: float = 0.0,
                 CashIn: float = 0.0, Commission: float = 0.0, CloseProfit: float = 0.0, PositionProfit: float = 0.0, PreSettlementPrice: float = 0.0, SettlementPrice: float = 0.0,
                 TradingDay: str = '', SettlementID: int = 0, OpenCost: float = 0.0, ExchangeMargin: float = 0.0, CombPosition: int = 0, CombLongFrozen: int = 0, CombShortFrozen: int = 0,
                 CloseProfitByDate: float = 0.0, CloseProfitByTrade: float = 0.0, TodayPosition: int = 0, MarginRateByMoney: float = 0.0, MarginRateByVolume: float = 0.0, StrikeFrozen: int = 0,
                 StrikeFrozenAmount: float = 0.0, AbandonFrozen: int = 0, ExchangeID: str = '', YdStrikeFrozen: int = 0, InvestUnitID: str = '', PositionCostOffset: float = 0.0, TasPosition: int = 0,
                 TasPositionCost: float = 0.0, InstrumentID: str = ''):
        super(SyncingInvestorPositionField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.PositionDate = self._to_bytes(PositionDate)
        self.YdPosition = int(YdPosition)
        self.Position = int(Position)
        self.LongFrozen = int(LongFrozen)
        self.ShortFrozen = int(ShortFrozen)
        self.LongFrozenAmount = float(LongFrozenAmount)
        self.ShortFrozenAmount = float(ShortFrozenAmount)
        self.OpenVolume = int(OpenVolume)
        self.CloseVolume = int(CloseVolume)
        self.OpenAmount = float(OpenAmount)
        self.CloseAmount = float(CloseAmount)
        self.PositionCost = float(PositionCost)
        self.PreMargin = float(PreMargin)
        self.UseMargin = float(UseMargin)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.CloseProfit = float(CloseProfit)
        self.PositionProfit = float(PositionProfit)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OpenCost = float(OpenCost)
        self.ExchangeMargin = float(ExchangeMargin)
        self.CombPosition = int(CombPosition)
        self.CombLongFrozen = int(CombLongFrozen)
        self.CombShortFrozen = int(CombShortFrozen)
        self.CloseProfitByDate = float(CloseProfitByDate)
        self.CloseProfitByTrade = float(CloseProfitByTrade)
        self.TodayPosition = int(TodayPosition)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.StrikeFrozen = int(StrikeFrozen)
        self.StrikeFrozenAmount = float(StrikeFrozenAmount)
        self.AbandonFrozen = int(AbandonFrozen)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.YdStrikeFrozen = int(YdStrikeFrozen)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.PositionCostOffset = float(PositionCostOffset)
        self.TasPosition = int(TasPosition)
        self.TasPositionCost = float(TasPositionCost)
        self.InstrumentID = self._to_bytes(InstrumentID)


class SyncingInstrumentMarginRateField(Base):
    """正在同步中的合约保证金率"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('LongMarginRatioByMoney', ctypes.c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', ctypes.c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', ctypes.c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', ctypes.c_double),  # 空头保证金费
        ('IsRelative', ctypes.c_int),  # 是否相对交易所收取
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', HedgeFlag: str = '', LongMarginRatioByMoney: float = 0.0,
                 LongMarginRatioByVolume: float = 0.0, ShortMarginRatioByMoney: float = 0.0, ShortMarginRatioByVolume: float = 0.0, IsRelative: int = 0, InstrumentID: str = ''):
        super(SyncingInstrumentMarginRateField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)
        self.InstrumentID = self._to_bytes(InstrumentID)


class SyncingInstrumentCommissionRateField(Base):
    """正在同步中的合约手续费率"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', ctypes.c_double),  # 开仓手续费率
        ('OpenRatioByVolume', ctypes.c_double),  # 开仓手续费
        ('CloseRatioByMoney', ctypes.c_double),  # 平仓手续费率
        ('CloseRatioByVolume', ctypes.c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', ctypes.c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', ctypes.c_double),  # 平今手续费
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', OpenRatioByMoney: float = 0.0, OpenRatioByVolume: float = 0.0,
                 CloseRatioByMoney: float = 0.0, CloseRatioByVolume: float = 0.0, CloseTodayRatioByMoney: float = 0.0, CloseTodayRatioByVolume: float = 0.0, InstrumentID: str = ''):
        super(SyncingInstrumentCommissionRateField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.InstrumentID = self._to_bytes(InstrumentID)


class SyncingInstrumentTradingRightField(Base):
    """正在同步中的合约交易权限"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('TradingRight', ctypes.c_char),  # 交易权限
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', TradingRight: str = '', InstrumentID: str = ''):
        super(SyncingInstrumentTradingRightField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.TradingRight = self._to_bytes(TradingRight)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryOrderField(Base):
    """查询报单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('InsertTimeStart', ctypes.c_char * 9),  # 开始时间
        ('InsertTimeEnd', ctypes.c_char * 9),  # 结束时间
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', OrderSysID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '',
                 InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryTradeField(Base):
    """查询成交"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TradeID', ctypes.c_char * 21),  # 成交编号
        ('TradeTimeStart', ctypes.c_char * 9),  # 开始时间
        ('TradeTimeEnd', ctypes.c_char * 9),  # 结束时间
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', TradeID: str = '', TradeTimeStart: str = '', TradeTimeEnd: str = '', InvestUnitID: str = '',
                 InstrumentID: str = ''):
        super(QryTradeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TradeID = self._to_bytes(TradeID)
        self.TradeTimeStart = self._to_bytes(TradeTimeStart)
        self.TradeTimeEnd = self._to_bytes(TradeTimeEnd)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryInvestorPositionField(Base):
    """查询投资者持仓"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryInvestorPositionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryTradingAccountField(Base):
    """查询资金账户"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('BizType', ctypes.c_char),  # 业务类型
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', CurrencyID: str = '', BizType: str = '', AccountID: str = ''):
        super(QryTradingAccountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.BizType = self._to_bytes(BizType)
        self.AccountID = self._to_bytes(AccountID)


class QryInvestorField(Base):
    """查询投资者"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = ''):
        super(QryInvestorField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class QryTradingCodeField(Base):
    """查询交易编码"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('ClientIDType', ctypes.c_char),  # 交易编码类型
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExchangeID: str = '', ClientID: str = '', ClientIDType: str = '', InvestUnitID: str = ''):
        super(QryTradingCodeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ClientID = self._to_bytes(ClientID)
        self.ClientIDType = self._to_bytes(ClientIDType)
        self.InvestUnitID = self._to_bytes(InvestUnitID)


class QryInvestorGroupField(Base):
    """查询投资者组"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
    ]

    def __init__(self, BrokerID: str = ''):
        super(QryInvestorGroupField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class QryInstrumentMarginRateField(Base):
    """查询合约保证金率"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', HedgeFlag: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryInstrumentMarginRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryInstrumentCommissionRateField(Base):
    """查询手续费率"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryInstrumentCommissionRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryInstrumentTradingRightField(Base):
    """查询合约交易权限"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', InstrumentID: str = ''):
        super(QryInstrumentTradingRightField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryBrokerField(Base):
    """查询经纪公司"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
    ]

    def __init__(self, BrokerID: str = ''):
        super(QryBrokerField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class QryTraderField(Base):
    """查询交易员"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
    ]

    def __init__(self, ExchangeID: str = '', ParticipantID: str = '', TraderID: str = ''):
        super(QryTraderField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.TraderID = self._to_bytes(TraderID)


class QrySuperUserFunctionField(Base):
    """查询管理用户功能权限"""
    _fields_ = [
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, UserID: str = ''):
        super(QrySuperUserFunctionField, self).__init__()
        self.UserID = self._to_bytes(UserID)


class QryUserSessionField(Base):
    """查询用户会话"""
    _fields_ = [
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, FrontID: int = 0, SessionID: int = 0, BrokerID: str = '', UserID: str = ''):
        super(QryUserSessionField, self).__init__()
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class QryPartBrokerField(Base):
    """查询经纪公司会员代码"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
    ]

    def __init__(self, ExchangeID: str = '', BrokerID: str = '', ParticipantID: str = ''):
        super(QryPartBrokerField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.ParticipantID = self._to_bytes(ParticipantID)


class QryFrontStatusField(Base):
    """查询前置状态"""
    _fields_ = [
        ('FrontID', ctypes.c_int),  # 前置编号
    ]

    def __init__(self, FrontID: int = 0):
        super(QryFrontStatusField, self).__init__()
        self.FrontID = int(FrontID)


class QryExchangeOrderField(Base):
    """查询交易所报单"""
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, ParticipantID: str = '', ClientID: str = '', reserve1: str = '', ExchangeID: str = '', TraderID: str = '', ExchangeInstID: str = ''):
        super(QryExchangeOrderField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class QryOrderActionField(Base):
    """查询报单操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExchangeID: str = ''):
        super(QryOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class QryExchangeOrderActionField(Base):
    """查询交易所报单操作"""
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
    ]

    def __init__(self, ParticipantID: str = '', ClientID: str = '', ExchangeID: str = '', TraderID: str = ''):
        super(QryExchangeOrderActionField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class QrySuperUserField(Base):
    """查询管理用户"""
    _fields_ = [
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, UserID: str = ''):
        super(QrySuperUserField, self).__init__()
        self.UserID = self._to_bytes(UserID)


class QryExchangeField(Base):
    """查询交易所"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
    ]

    def __init__(self, ExchangeID: str = ''):
        super(QryExchangeField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)


class QryProductField(Base):
    """查询产品"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ProductClass', ctypes.c_char),  # 产品类型
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ProductID', ctypes.c_char * 81),  # 产品代码
    ]

    def __init__(self, reserve1: str = '', ProductClass: str = '', ExchangeID: str = '', ProductID: str = ''):
        super(QryProductField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.ProductClass = self._to_bytes(ProductClass)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProductID = self._to_bytes(ProductID)


class QryInstrumentField(Base):
    """查询合约"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('reserve3', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('ProductID', ctypes.c_char * 81),  # 产品代码
    ]

    def __init__(self, reserve1: str = '', ExchangeID: str = '', reserve2: str = '', reserve3: str = '', InstrumentID: str = '', ExchangeInstID: str = '', ProductID: str = ''):
        super(QryInstrumentField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve2 = self._to_bytes(reserve2)
        self.reserve3 = self._to_bytes(reserve3)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.ProductID = self._to_bytes(ProductID)


class QryDepthMarketDataField(Base):
    """查询行情"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', ExchangeID: str = '', InstrumentID: str = ''):
        super(QryDepthMarketDataField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryBrokerUserField(Base):
    """查询经纪公司用户"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = ''):
        super(QryBrokerUserField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class QryBrokerUserFunctionField(Base):
    """查询经纪公司用户权限"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = ''):
        super(QryBrokerUserFunctionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class QryTraderOfferField(Base):
    """查询交易员报盘机"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
    ]

    def __init__(self, ExchangeID: str = '', ParticipantID: str = '', TraderID: str = ''):
        super(QryTraderOfferField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.TraderID = self._to_bytes(TraderID)


class QrySyncDepositField(Base):
    """查询出入金流水"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('DepositSeqNo', ctypes.c_char * 15),  # 出入金流水号
    ]

    def __init__(self, BrokerID: str = '', DepositSeqNo: str = ''):
        super(QrySyncDepositField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.DepositSeqNo = self._to_bytes(DepositSeqNo)


class QrySettlementInfoField(Base):
    """查询投资者结算结果"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', TradingDay: str = '', AccountID: str = '', CurrencyID: str = ''):
        super(QrySettlementInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.TradingDay = self._to_bytes(TradingDay)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class QryExchangeMarginRateField(Base):
    """查询交易所保证金率"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', reserve1: str = '', HedgeFlag: str = '', ExchangeID: str = '', InstrumentID: str = ''):
        super(QryExchangeMarginRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.reserve1 = self._to_bytes(reserve1)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryExchangeMarginRateAdjustField(Base):
    """查询交易所调整保证金率"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', reserve1: str = '', HedgeFlag: str = '', InstrumentID: str = ''):
        super(QryExchangeMarginRateAdjustField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.reserve1 = self._to_bytes(reserve1)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryExchangeRateField(Base):
    """查询汇率"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('FromCurrencyID', ctypes.c_char * 4),  # 源币种
        ('ToCurrencyID', ctypes.c_char * 4),  # 目标币种
    ]

    def __init__(self, BrokerID: str = '', FromCurrencyID: str = '', ToCurrencyID: str = ''):
        super(QryExchangeRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.FromCurrencyID = self._to_bytes(FromCurrencyID)
        self.ToCurrencyID = self._to_bytes(ToCurrencyID)


class QrySyncFundMortgageField(Base):
    """查询货币质押流水"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('MortgageSeqNo', ctypes.c_char * 15),  # 货币质押流水号
    ]

    def __init__(self, BrokerID: str = '', MortgageSeqNo: str = ''):
        super(QrySyncFundMortgageField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.MortgageSeqNo = self._to_bytes(MortgageSeqNo)


class QryHisOrderField(Base):
    """查询报单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('InsertTimeStart', ctypes.c_char * 9),  # 开始时间
        ('InsertTimeEnd', ctypes.c_char * 9),  # 结束时间
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', OrderSysID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '',
                 TradingDay: str = '', SettlementID: int = 0, InstrumentID: str = ''):
        super(QryHisOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class OptionInstrMiniMarginField(Base):
    """当前期权合约最小保证金"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('MinMargin', ctypes.c_double),  # 单位（手）期权合约最小保证金
        ('ValueMethod', ctypes.c_char),  # 取值方式
        ('IsRelative', ctypes.c_int),  # 是否跟随交易所收取
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', MinMargin: float = 0.0, ValueMethod: str = '', IsRelative: int = 0,
                 InstrumentID: str = ''):
        super(OptionInstrMiniMarginField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.MinMargin = float(MinMargin)
        self.ValueMethod = self._to_bytes(ValueMethod)
        self.IsRelative = int(IsRelative)
        self.InstrumentID = self._to_bytes(InstrumentID)


class OptionInstrMarginAdjustField(Base):
    """当前期权合约保证金调整系数"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('SShortMarginRatioByMoney', ctypes.c_double),  # 投机空头保证金调整系数
        ('SShortMarginRatioByVolume', ctypes.c_double),  # 投机空头保证金调整系数
        ('HShortMarginRatioByMoney', ctypes.c_double),  # 保值空头保证金调整系数
        ('HShortMarginRatioByVolume', ctypes.c_double),  # 保值空头保证金调整系数
        ('AShortMarginRatioByMoney', ctypes.c_double),  # 套利空头保证金调整系数
        ('AShortMarginRatioByVolume', ctypes.c_double),  # 套利空头保证金调整系数
        ('IsRelative', ctypes.c_int),  # 是否跟随交易所收取
        ('MShortMarginRatioByMoney', ctypes.c_double),  # 做市商空头保证金调整系数
        ('MShortMarginRatioByVolume', ctypes.c_double),  # 做市商空头保证金调整系数
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', SShortMarginRatioByMoney: float = 0.0, SShortMarginRatioByVolume: float = 0.0,
                 HShortMarginRatioByMoney: float = 0.0, HShortMarginRatioByVolume: float = 0.0, AShortMarginRatioByMoney: float = 0.0, AShortMarginRatioByVolume: float = 0.0, IsRelative: int = 0,
                 MShortMarginRatioByMoney: float = 0.0, MShortMarginRatioByVolume: float = 0.0, InstrumentID: str = ''):
        super(OptionInstrMarginAdjustField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.SShortMarginRatioByMoney = float(SShortMarginRatioByMoney)
        self.SShortMarginRatioByVolume = float(SShortMarginRatioByVolume)
        self.HShortMarginRatioByMoney = float(HShortMarginRatioByMoney)
        self.HShortMarginRatioByVolume = float(HShortMarginRatioByVolume)
        self.AShortMarginRatioByMoney = float(AShortMarginRatioByMoney)
        self.AShortMarginRatioByVolume = float(AShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)
        self.MShortMarginRatioByMoney = float(MShortMarginRatioByMoney)
        self.MShortMarginRatioByVolume = float(MShortMarginRatioByVolume)
        self.InstrumentID = self._to_bytes(InstrumentID)


class OptionInstrCommRateField(Base):
    """当前期权合约手续费的详细内容"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', ctypes.c_double),  # 开仓手续费率
        ('OpenRatioByVolume', ctypes.c_double),  # 开仓手续费
        ('CloseRatioByMoney', ctypes.c_double),  # 平仓手续费率
        ('CloseRatioByVolume', ctypes.c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', ctypes.c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', ctypes.c_double),  # 平今手续费
        ('StrikeRatioByMoney', ctypes.c_double),  # 执行手续费率
        ('StrikeRatioByVolume', ctypes.c_double),  # 执行手续费
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', OpenRatioByMoney: float = 0.0, OpenRatioByVolume: float = 0.0,
                 CloseRatioByMoney: float = 0.0, CloseRatioByVolume: float = 0.0, CloseTodayRatioByMoney: float = 0.0, CloseTodayRatioByVolume: float = 0.0, StrikeRatioByMoney: float = 0.0,
                 StrikeRatioByVolume: float = 0.0, ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(OptionInstrCommRateField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.StrikeRatioByMoney = float(StrikeRatioByMoney)
        self.StrikeRatioByVolume = float(StrikeRatioByVolume)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class OptionInstrTradeCostField(Base):
    """期权交易成本"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('FixedMargin', ctypes.c_double),  # 期权合约保证金不变部分
        ('MiniMargin', ctypes.c_double),  # 期权合约最小保证金
        ('Royalty', ctypes.c_double),  # 期权合约权利金
        ('ExchFixedMargin', ctypes.c_double),  # 交易所期权合约保证金不变部分
        ('ExchMiniMargin', ctypes.c_double),  # 交易所期权合约最小保证金
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', HedgeFlag: str = '', FixedMargin: float = 0.0, MiniMargin: float = 0.0, Royalty: float = 0.0,
                 ExchFixedMargin: float = 0.0, ExchMiniMargin: float = 0.0, ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(OptionInstrTradeCostField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.FixedMargin = float(FixedMargin)
        self.MiniMargin = float(MiniMargin)
        self.Royalty = float(Royalty)
        self.ExchFixedMargin = float(ExchFixedMargin)
        self.ExchMiniMargin = float(ExchMiniMargin)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryOptionInstrTradeCostField(Base):
    """期权交易成本查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('InputPrice', ctypes.c_double),  # 期权合约报价
        ('UnderlyingPrice', ctypes.c_double),  # 标的价格,填0则用昨结算价
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', HedgeFlag: str = '', InputPrice: float = 0.0, UnderlyingPrice: float = 0.0, ExchangeID: str = '',
                 InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryOptionInstrTradeCostField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.InputPrice = float(InputPrice)
        self.UnderlyingPrice = float(UnderlyingPrice)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryOptionInstrCommRateField(Base):
    """期权手续费率查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryOptionInstrCommRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class IndexPriceField(Base):
    """股指现货指数"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ClosePrice', ctypes.c_double),  # 指数现货收盘价
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', reserve1: str = '', ClosePrice: float = 0.0, InstrumentID: str = ''):
        super(IndexPriceField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ClosePrice = float(ClosePrice)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InputExecOrderField(Base):
    """输入的执行宣告"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExecOrderRef', ctypes.c_char * 13),  # 执行宣告引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Volume', ctypes.c_int),  # 数量
        ('RequestID', ctypes.c_int),  # 请求编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OffsetFlag', ctypes.c_char),  # 开平标志
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ActionType', ctypes.c_char),  # 执行类型
        ('PosiDirection', ctypes.c_char),  # 保留头寸申请的持仓方向
        ('ReservePositionFlag', ctypes.c_char),  # 期权行权后是否保留期货头寸的标记,该字段已废弃
        ('CloseFlag', ctypes.c_char),  # 期权行权后生成的头寸是否自动平仓
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('ClientID', ctypes.c_char * 11),  # 交易编码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExecOrderRef: str = '', UserID: str = '', Volume: int = 0, RequestID: int = 0, BusinessUnit: str = '',
                 OffsetFlag: str = '', HedgeFlag: str = '', ActionType: str = '', PosiDirection: str = '', ReservePositionFlag: str = '', CloseFlag: str = '', ExchangeID: str = '',
                 InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', ClientID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(InputExecOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.UserID = self._to_bytes(UserID)
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionType = self._to_bytes(ActionType)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.ReservePositionFlag = self._to_bytes(ReservePositionFlag)
        self.CloseFlag = self._to_bytes(CloseFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class InputExecOrderActionField(Base):
    """输入执行宣告操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExecOrderActionRef', ctypes.c_int),  # 执行宣告操作引用
        ('ExecOrderRef', ctypes.c_char * 13),  # 执行宣告引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ExecOrderSysID', ctypes.c_char * 21),  # 执行宣告操作编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExecOrderActionRef: int = 0, ExecOrderRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '',
                 ExecOrderSysID: str = '', ActionFlag: str = '', UserID: str = '', reserve1: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '',
                 IPAddress: str = ''):
        super(InputExecOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExecOrderActionRef = int(ExecOrderActionRef)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.UserID = self._to_bytes(UserID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class ExecOrderField(Base):
    """执行宣告"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExecOrderRef', ctypes.c_char * 13),  # 执行宣告引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Volume', ctypes.c_int),  # 数量
        ('RequestID', ctypes.c_int),  # 请求编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OffsetFlag', ctypes.c_char),  # 开平标志
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ActionType', ctypes.c_char),  # 执行类型
        ('PosiDirection', ctypes.c_char),  # 保留头寸申请的持仓方向
        ('ReservePositionFlag', ctypes.c_char),  # 期权行权后是否保留期货头寸的标记,该字段已废弃
        ('CloseFlag', ctypes.c_char),  # 期权行权后生成的头寸是否自动平仓
        ('ExecOrderLocalID', ctypes.c_char * 13),  # 本地执行宣告编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderSubmitStatus', ctypes.c_char),  # 执行宣告提交状态
        ('NotifySequence', ctypes.c_int),  # 报单提示序号
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('ExecOrderSysID', ctypes.c_char * 21),  # 执行宣告编号
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 插入时间
        ('CancelTime', ctypes.c_char * 9),  # 撤销时间
        ('ExecResult', ctypes.c_char),  # 执行结果
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('ActiveUserID', ctypes.c_char * 16),  # 操作用户代码
        ('BrokerExecOrderSeq', ctypes.c_int),  # 经纪公司报单编号
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('reserve3', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExecOrderRef: str = '', UserID: str = '', Volume: int = 0, RequestID: int = 0, BusinessUnit: str = '',
                 OffsetFlag: str = '', HedgeFlag: str = '', ActionType: str = '', PosiDirection: str = '', ReservePositionFlag: str = '', CloseFlag: str = '', ExecOrderLocalID: str = '',
                 ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '', reserve2: str = '', TraderID: str = '', InstallID: int = 0, OrderSubmitStatus: str = '', NotifySequence: int = 0,
                 TradingDay: str = '', SettlementID: int = 0, ExecOrderSysID: str = '', InsertDate: str = '', InsertTime: str = '', CancelTime: str = '', ExecResult: str = '',
                 ClearingPartID: str = '', SequenceNo: int = 0, FrontID: int = 0, SessionID: int = 0, UserProductInfo: str = '', StatusMsg: str = '', ActiveUserID: str = '',
                 BrokerExecOrderSeq: int = 0, BranchID: str = '', InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', reserve3: str = '', MacAddress: str = '', InstrumentID: str = '',
                 ExchangeInstID: str = '', IPAddress: str = ''):
        super(ExecOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.UserID = self._to_bytes(UserID)
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionType = self._to_bytes(ActionType)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.ReservePositionFlag = self._to_bytes(ReservePositionFlag)
        self.CloseFlag = self._to_bytes(CloseFlag)
        self.ExecOrderLocalID = self._to_bytes(ExecOrderLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ExecResult = self._to_bytes(ExecResult)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerExecOrderSeq = int(BrokerExecOrderSeq)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.reserve3 = self._to_bytes(reserve3)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class ExecOrderActionField(Base):
    """执行宣告操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExecOrderActionRef', ctypes.c_int),  # 执行宣告操作引用
        ('ExecOrderRef', ctypes.c_char * 13),  # 执行宣告引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ExecOrderSysID', ctypes.c_char * 21),  # 执行宣告操作编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('ExecOrderLocalID', ctypes.c_char * 13),  # 本地执行宣告编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('ActionType', ctypes.c_char),  # 执行类型
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExecOrderActionRef: int = 0, ExecOrderRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '',
                 ExecOrderSysID: str = '', ActionFlag: str = '', ActionDate: str = '', ActionTime: str = '', TraderID: str = '', InstallID: int = 0, ExecOrderLocalID: str = '',
                 ActionLocalID: str = '', ParticipantID: str = '', ClientID: str = '', BusinessUnit: str = '', OrderActionStatus: str = '', UserID: str = '', ActionType: str = '', StatusMsg: str = '',
                 reserve1: str = '', BranchID: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(ExecOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExecOrderActionRef = int(ExecOrderActionRef)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ExecOrderLocalID = self._to_bytes(ExecOrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.ActionType = self._to_bytes(ActionType)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.reserve1 = self._to_bytes(reserve1)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryExecOrderField(Base):
    """执行宣告查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ExecOrderSysID', ctypes.c_char * 21),  # 执行宣告编号
        ('InsertTimeStart', ctypes.c_char * 9),  # 开始时间
        ('InsertTimeEnd', ctypes.c_char * 9),  # 结束时间
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', ExecOrderSysID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '',
                 InstrumentID: str = ''):
        super(QryExecOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)
        self.InstrumentID = self._to_bytes(InstrumentID)


class ExchangeExecOrderField(Base):
    """交易所执行宣告信息"""
    _fields_ = [
        ('Volume', ctypes.c_int),  # 数量
        ('RequestID', ctypes.c_int),  # 请求编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OffsetFlag', ctypes.c_char),  # 开平标志
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ActionType', ctypes.c_char),  # 执行类型
        ('PosiDirection', ctypes.c_char),  # 保留头寸申请的持仓方向
        ('ReservePositionFlag', ctypes.c_char),  # 期权行权后是否保留期货头寸的标记,该字段已废弃
        ('CloseFlag', ctypes.c_char),  # 期权行权后生成的头寸是否自动平仓
        ('ExecOrderLocalID', ctypes.c_char * 13),  # 本地执行宣告编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderSubmitStatus', ctypes.c_char),  # 执行宣告提交状态
        ('NotifySequence', ctypes.c_int),  # 报单提示序号
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('ExecOrderSysID', ctypes.c_char * 21),  # 执行宣告编号
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 插入时间
        ('CancelTime', ctypes.c_char * 9),  # 撤销时间
        ('ExecResult', ctypes.c_char),  # 执行结果
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, Volume: int = 0, RequestID: int = 0, BusinessUnit: str = '', OffsetFlag: str = '', HedgeFlag: str = '', ActionType: str = '', PosiDirection: str = '',
                 ReservePositionFlag: str = '', CloseFlag: str = '', ExecOrderLocalID: str = '', ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '', reserve1: str = '',
                 TraderID: str = '', InstallID: int = 0, OrderSubmitStatus: str = '', NotifySequence: int = 0, TradingDay: str = '', SettlementID: int = 0, ExecOrderSysID: str = '',
                 InsertDate: str = '', InsertTime: str = '', CancelTime: str = '', ExecResult: str = '', ClearingPartID: str = '', SequenceNo: int = 0, BranchID: str = '', reserve2: str = '',
                 MacAddress: str = '', ExchangeInstID: str = '', IPAddress: str = ''):
        super(ExchangeExecOrderField, self).__init__()
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionType = self._to_bytes(ActionType)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.ReservePositionFlag = self._to_bytes(ReservePositionFlag)
        self.CloseFlag = self._to_bytes(CloseFlag)
        self.ExecOrderLocalID = self._to_bytes(ExecOrderLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ExecResult = self._to_bytes(ExecResult)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.BranchID = self._to_bytes(BranchID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryExchangeExecOrderField(Base):
    """交易所执行宣告查询"""
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, ParticipantID: str = '', ClientID: str = '', reserve1: str = '', ExchangeID: str = '', TraderID: str = '', ExchangeInstID: str = ''):
        super(QryExchangeExecOrderField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class QryExecOrderActionField(Base):
    """执行宣告操作查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExchangeID: str = ''):
        super(QryExecOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class ExchangeExecOrderActionField(Base):
    """交易所执行宣告操作"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ExecOrderSysID', ctypes.c_char * 21),  # 执行宣告操作编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('ExecOrderLocalID', ctypes.c_char * 13),  # 本地执行宣告编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('ActionType', ctypes.c_char),  # 执行类型
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('Volume', ctypes.c_int),  # 数量
        ('IPAddress', ctypes.c_char * 33),  # IP地址
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, ExchangeID: str = '', ExecOrderSysID: str = '', ActionFlag: str = '', ActionDate: str = '', ActionTime: str = '', TraderID: str = '', InstallID: int = 0,
                 ExecOrderLocalID: str = '', ActionLocalID: str = '', ParticipantID: str = '', ClientID: str = '', BusinessUnit: str = '', OrderActionStatus: str = '', UserID: str = '',
                 ActionType: str = '', BranchID: str = '', reserve1: str = '', MacAddress: str = '', reserve2: str = '', Volume: int = 0, IPAddress: str = '', ExchangeInstID: str = ''):
        super(ExchangeExecOrderActionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ExecOrderLocalID = self._to_bytes(ExecOrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.ActionType = self._to_bytes(ActionType)
        self.BranchID = self._to_bytes(BranchID)
        self.reserve1 = self._to_bytes(reserve1)
        self.MacAddress = self._to_bytes(MacAddress)
        self.reserve2 = self._to_bytes(reserve2)
        self.Volume = int(Volume)
        self.IPAddress = self._to_bytes(IPAddress)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class QryExchangeExecOrderActionField(Base):
    """交易所执行宣告操作查询"""
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
    ]

    def __init__(self, ParticipantID: str = '', ClientID: str = '', ExchangeID: str = '', TraderID: str = ''):
        super(QryExchangeExecOrderActionField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class ErrExecOrderField(Base):
    """错误执行宣告"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExecOrderRef', ctypes.c_char * 13),  # 执行宣告引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Volume', ctypes.c_int),  # 数量
        ('RequestID', ctypes.c_int),  # 请求编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OffsetFlag', ctypes.c_char),  # 开平标志
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ActionType', ctypes.c_char),  # 执行类型
        ('PosiDirection', ctypes.c_char),  # 保留头寸申请的持仓方向
        ('ReservePositionFlag', ctypes.c_char),  # 期权行权后是否保留期货头寸的标记,该字段已废弃
        ('CloseFlag', ctypes.c_char),  # 期权行权后生成的头寸是否自动平仓
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('ClientID', ctypes.c_char * 11),  # 交易编码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExecOrderRef: str = '', UserID: str = '', Volume: int = 0, RequestID: int = 0, BusinessUnit: str = '',
                 OffsetFlag: str = '', HedgeFlag: str = '', ActionType: str = '', PosiDirection: str = '', ReservePositionFlag: str = '', CloseFlag: str = '', ExchangeID: str = '',
                 InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', ClientID: str = '', reserve2: str = '', MacAddress: str = '', ErrorID: int = 0, ErrorMsg: str = '',
                 InstrumentID: str = '', IPAddress: str = ''):
        super(ErrExecOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.UserID = self._to_bytes(UserID)
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionType = self._to_bytes(ActionType)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.ReservePositionFlag = self._to_bytes(ReservePositionFlag)
        self.CloseFlag = self._to_bytes(CloseFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryErrExecOrderField(Base):
    """查询错误执行宣告"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = ''):
        super(QryErrExecOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class ErrExecOrderActionField(Base):
    """错误执行宣告操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExecOrderActionRef', ctypes.c_int),  # 执行宣告操作引用
        ('ExecOrderRef', ctypes.c_char * 13),  # 执行宣告引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ExecOrderSysID', ctypes.c_char * 21),  # 执行宣告操作编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExecOrderActionRef: int = 0, ExecOrderRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '',
                 ExecOrderSysID: str = '', ActionFlag: str = '', UserID: str = '', reserve1: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', ErrorID: int = 0,
                 ErrorMsg: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(ErrExecOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExecOrderActionRef = int(ExecOrderActionRef)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.UserID = self._to_bytes(UserID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryErrExecOrderActionField(Base):
    """查询错误执行宣告操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = ''):
        super(QryErrExecOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class OptionInstrTradingRightField(Base):
    """投资者期权合约交易权限"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('Direction', ctypes.c_char),  # 买卖方向
        ('TradingRight', ctypes.c_char),  # 交易权限
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', Direction: str = '', TradingRight: str = '', InstrumentID: str = ''):
        super(OptionInstrTradingRightField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Direction = self._to_bytes(Direction)
        self.TradingRight = self._to_bytes(TradingRight)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryOptionInstrTradingRightField(Base):
    """查询期权合约交易权限"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('Direction', ctypes.c_char),  # 买卖方向
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', Direction: str = '', InstrumentID: str = ''):
        super(QryOptionInstrTradingRightField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.Direction = self._to_bytes(Direction)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InputForQuoteField(Base):
    """输入的询价"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ForQuoteRef', ctypes.c_char * 13),  # 询价引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ForQuoteRef: str = '', UserID: str = '', ExchangeID: str = '', InvestUnitID: str = '', reserve2: str = '',
                 MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(InputForQuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ForQuoteRef = self._to_bytes(ForQuoteRef)
        self.UserID = self._to_bytes(UserID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class ForQuoteField(Base):
    """询价"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ForQuoteRef', ctypes.c_char * 13),  # 询价引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('ForQuoteLocalID', ctypes.c_char * 13),  # 本地询价编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 插入时间
        ('ForQuoteStatus', ctypes.c_char),  # 询价状态
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('ActiveUserID', ctypes.c_char * 16),  # 操作用户代码
        ('BrokerForQutoSeq', ctypes.c_int),  # 经纪公司询价编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve3', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ForQuoteRef: str = '', UserID: str = '', ForQuoteLocalID: str = '', ExchangeID: str = '', ParticipantID: str = '',
                 ClientID: str = '', reserve2: str = '', TraderID: str = '', InstallID: int = 0, InsertDate: str = '', InsertTime: str = '', ForQuoteStatus: str = '', FrontID: int = 0,
                 SessionID: int = 0, StatusMsg: str = '', ActiveUserID: str = '', BrokerForQutoSeq: int = 0, InvestUnitID: str = '', reserve3: str = '', MacAddress: str = '', InstrumentID: str = '',
                 ExchangeInstID: str = '', IPAddress: str = ''):
        super(ForQuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ForQuoteRef = self._to_bytes(ForQuoteRef)
        self.UserID = self._to_bytes(UserID)
        self.ForQuoteLocalID = self._to_bytes(ForQuoteLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.ForQuoteStatus = self._to_bytes(ForQuoteStatus)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerForQutoSeq = int(BrokerForQutoSeq)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve3 = self._to_bytes(reserve3)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryForQuoteField(Base):
    """询价查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InsertTimeStart', ctypes.c_char * 9),  # 开始时间
        ('InsertTimeEnd', ctypes.c_char * 9),  # 结束时间
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '', InvestUnitID: str = '',
                 InstrumentID: str = ''):
        super(QryForQuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class ExchangeForQuoteField(Base):
    """交易所询价信息"""
    _fields_ = [
        ('ForQuoteLocalID', ctypes.c_char * 13),  # 本地询价编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 插入时间
        ('ForQuoteStatus', ctypes.c_char),  # 询价状态
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, ForQuoteLocalID: str = '', ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '', reserve1: str = '', TraderID: str = '', InstallID: int = 0, InsertDate: str = '',
                 InsertTime: str = '', ForQuoteStatus: str = '', reserve2: str = '', MacAddress: str = '', ExchangeInstID: str = '', IPAddress: str = ''):
        super(ExchangeForQuoteField, self).__init__()
        self.ForQuoteLocalID = self._to_bytes(ForQuoteLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.ForQuoteStatus = self._to_bytes(ForQuoteStatus)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryExchangeForQuoteField(Base):
    """交易所询价查询"""
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, ParticipantID: str = '', ClientID: str = '', reserve1: str = '', ExchangeID: str = '', TraderID: str = '', ExchangeInstID: str = ''):
        super(QryExchangeForQuoteField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class InputQuoteField(Base):
    """输入的报价"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('QuoteRef', ctypes.c_char * 13),  # 报价引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('AskPrice', ctypes.c_double),  # 卖价格
        ('BidPrice', ctypes.c_double),  # 买价格
        ('AskVolume', ctypes.c_int),  # 卖数量
        ('BidVolume', ctypes.c_int),  # 买数量
        ('RequestID', ctypes.c_int),  # 请求编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('AskOffsetFlag', ctypes.c_char),  # 卖开平标志
        ('BidOffsetFlag', ctypes.c_char),  # 买开平标志
        ('AskHedgeFlag', ctypes.c_char),  # 卖投机套保标志
        ('BidHedgeFlag', ctypes.c_char),  # 买投机套保标志
        ('AskOrderRef', ctypes.c_char * 13),  # 衍生卖报单引用
        ('BidOrderRef', ctypes.c_char * 13),  # 衍生买报单引用
        ('ForQuoteSysID', ctypes.c_char * 21),  # 应价编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('ClientID', ctypes.c_char * 11),  # 交易编码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
        ('ReplaceSysID', ctypes.c_char * 21),  # 被顶单编号
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', QuoteRef: str = '', UserID: str = '', AskPrice: float = 0.0, BidPrice: float = 0.0, AskVolume: int = 0,
                 BidVolume: int = 0, RequestID: int = 0, BusinessUnit: str = '', AskOffsetFlag: str = '', BidOffsetFlag: str = '', AskHedgeFlag: str = '', BidHedgeFlag: str = '',
                 AskOrderRef: str = '', BidOrderRef: str = '', ForQuoteSysID: str = '', ExchangeID: str = '', InvestUnitID: str = '', ClientID: str = '', reserve2: str = '', MacAddress: str = '',
                 InstrumentID: str = '', IPAddress: str = '', ReplaceSysID: str = ''):
        super(InputQuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.QuoteRef = self._to_bytes(QuoteRef)
        self.UserID = self._to_bytes(UserID)
        self.AskPrice = float(AskPrice)
        self.BidPrice = float(BidPrice)
        self.AskVolume = int(AskVolume)
        self.BidVolume = int(BidVolume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.AskOffsetFlag = self._to_bytes(AskOffsetFlag)
        self.BidOffsetFlag = self._to_bytes(BidOffsetFlag)
        self.AskHedgeFlag = self._to_bytes(AskHedgeFlag)
        self.BidHedgeFlag = self._to_bytes(BidHedgeFlag)
        self.AskOrderRef = self._to_bytes(AskOrderRef)
        self.BidOrderRef = self._to_bytes(BidOrderRef)
        self.ForQuoteSysID = self._to_bytes(ForQuoteSysID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.ReplaceSysID = self._to_bytes(ReplaceSysID)


class InputQuoteActionField(Base):
    """输入报价操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('QuoteActionRef', ctypes.c_int),  # 报价操作引用
        ('QuoteRef', ctypes.c_char * 13),  # 报价引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('QuoteSysID', ctypes.c_char * 21),  # 报价操作编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('ClientID', ctypes.c_char * 11),  # 交易编码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', QuoteActionRef: int = 0, QuoteRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '',
                 QuoteSysID: str = '', ActionFlag: str = '', UserID: str = '', reserve1: str = '', InvestUnitID: str = '', ClientID: str = '', reserve2: str = '', MacAddress: str = '',
                 InstrumentID: str = '', IPAddress: str = ''):
        super(InputQuoteActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.QuoteActionRef = int(QuoteActionRef)
        self.QuoteRef = self._to_bytes(QuoteRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.UserID = self._to_bytes(UserID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class QuoteField(Base):
    """报价"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('QuoteRef', ctypes.c_char * 13),  # 报价引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('AskPrice', ctypes.c_double),  # 卖价格
        ('BidPrice', ctypes.c_double),  # 买价格
        ('AskVolume', ctypes.c_int),  # 卖数量
        ('BidVolume', ctypes.c_int),  # 买数量
        ('RequestID', ctypes.c_int),  # 请求编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('AskOffsetFlag', ctypes.c_char),  # 卖开平标志
        ('BidOffsetFlag', ctypes.c_char),  # 买开平标志
        ('AskHedgeFlag', ctypes.c_char),  # 卖投机套保标志
        ('BidHedgeFlag', ctypes.c_char),  # 买投机套保标志
        ('QuoteLocalID', ctypes.c_char * 13),  # 本地报价编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('NotifySequence', ctypes.c_int),  # 报价提示序号
        ('OrderSubmitStatus', ctypes.c_char),  # 报价提交状态
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('QuoteSysID', ctypes.c_char * 21),  # 报价编号
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 插入时间
        ('CancelTime', ctypes.c_char * 9),  # 撤销时间
        ('QuoteStatus', ctypes.c_char),  # 报价状态
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('AskOrderSysID', ctypes.c_char * 21),  # 卖方报单编号
        ('BidOrderSysID', ctypes.c_char * 21),  # 买方报单编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('ActiveUserID', ctypes.c_char * 16),  # 操作用户代码
        ('BrokerQuoteSeq', ctypes.c_int),  # 经纪公司报价编号
        ('AskOrderRef', ctypes.c_char * 13),  # 衍生卖报单引用
        ('BidOrderRef', ctypes.c_char * 13),  # 衍生买报单引用
        ('ForQuoteSysID', ctypes.c_char * 21),  # 应价编号
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('reserve3', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
        ('ReplaceSysID', ctypes.c_char * 21),  # 被顶单编号
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', QuoteRef: str = '', UserID: str = '', AskPrice: float = 0.0, BidPrice: float = 0.0, AskVolume: int = 0,
                 BidVolume: int = 0, RequestID: int = 0, BusinessUnit: str = '', AskOffsetFlag: str = '', BidOffsetFlag: str = '', AskHedgeFlag: str = '', BidHedgeFlag: str = '',
                 QuoteLocalID: str = '', ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '', reserve2: str = '', TraderID: str = '', InstallID: int = 0, NotifySequence: int = 0,
                 OrderSubmitStatus: str = '', TradingDay: str = '', SettlementID: int = 0, QuoteSysID: str = '', InsertDate: str = '', InsertTime: str = '', CancelTime: str = '',
                 QuoteStatus: str = '', ClearingPartID: str = '', SequenceNo: int = 0, AskOrderSysID: str = '', BidOrderSysID: str = '', FrontID: int = 0, SessionID: int = 0,
                 UserProductInfo: str = '', StatusMsg: str = '', ActiveUserID: str = '', BrokerQuoteSeq: int = 0, AskOrderRef: str = '', BidOrderRef: str = '', ForQuoteSysID: str = '',
                 BranchID: str = '', InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', reserve3: str = '', MacAddress: str = '', InstrumentID: str = '', ExchangeInstID: str = '',
                 IPAddress: str = '', ReplaceSysID: str = ''):
        super(QuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.QuoteRef = self._to_bytes(QuoteRef)
        self.UserID = self._to_bytes(UserID)
        self.AskPrice = float(AskPrice)
        self.BidPrice = float(BidPrice)
        self.AskVolume = int(AskVolume)
        self.BidVolume = int(BidVolume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.AskOffsetFlag = self._to_bytes(AskOffsetFlag)
        self.BidOffsetFlag = self._to_bytes(BidOffsetFlag)
        self.AskHedgeFlag = self._to_bytes(AskHedgeFlag)
        self.BidHedgeFlag = self._to_bytes(BidHedgeFlag)
        self.QuoteLocalID = self._to_bytes(QuoteLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.NotifySequence = int(NotifySequence)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.QuoteStatus = self._to_bytes(QuoteStatus)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.AskOrderSysID = self._to_bytes(AskOrderSysID)
        self.BidOrderSysID = self._to_bytes(BidOrderSysID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerQuoteSeq = int(BrokerQuoteSeq)
        self.AskOrderRef = self._to_bytes(AskOrderRef)
        self.BidOrderRef = self._to_bytes(BidOrderRef)
        self.ForQuoteSysID = self._to_bytes(ForQuoteSysID)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.reserve3 = self._to_bytes(reserve3)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.ReplaceSysID = self._to_bytes(ReplaceSysID)


class QuoteActionField(Base):
    """报价操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('QuoteActionRef', ctypes.c_int),  # 报价操作引用
        ('QuoteRef', ctypes.c_char * 13),  # 报价引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('QuoteSysID', ctypes.c_char * 21),  # 报价操作编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('QuoteLocalID', ctypes.c_char * 13),  # 本地报价编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', QuoteActionRef: int = 0, QuoteRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '',
                 QuoteSysID: str = '', ActionFlag: str = '', ActionDate: str = '', ActionTime: str = '', TraderID: str = '', InstallID: int = 0, QuoteLocalID: str = '', ActionLocalID: str = '',
                 ParticipantID: str = '', ClientID: str = '', BusinessUnit: str = '', OrderActionStatus: str = '', UserID: str = '', StatusMsg: str = '', reserve1: str = '', BranchID: str = '',
                 InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(QuoteActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.QuoteActionRef = int(QuoteActionRef)
        self.QuoteRef = self._to_bytes(QuoteRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.QuoteLocalID = self._to_bytes(QuoteLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.reserve1 = self._to_bytes(reserve1)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryQuoteField(Base):
    """报价查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('QuoteSysID', ctypes.c_char * 21),  # 报价编号
        ('InsertTimeStart', ctypes.c_char * 9),  # 开始时间
        ('InsertTimeEnd', ctypes.c_char * 9),  # 结束时间
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', QuoteSysID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '',
                 InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryQuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class ExchangeQuoteField(Base):
    """交易所报价信息"""
    _fields_ = [
        ('AskPrice', ctypes.c_double),  # 卖价格
        ('BidPrice', ctypes.c_double),  # 买价格
        ('AskVolume', ctypes.c_int),  # 卖数量
        ('BidVolume', ctypes.c_int),  # 买数量
        ('RequestID', ctypes.c_int),  # 请求编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('AskOffsetFlag', ctypes.c_char),  # 卖开平标志
        ('BidOffsetFlag', ctypes.c_char),  # 买开平标志
        ('AskHedgeFlag', ctypes.c_char),  # 卖投机套保标志
        ('BidHedgeFlag', ctypes.c_char),  # 买投机套保标志
        ('QuoteLocalID', ctypes.c_char * 13),  # 本地报价编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('NotifySequence', ctypes.c_int),  # 报价提示序号
        ('OrderSubmitStatus', ctypes.c_char),  # 报价提交状态
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('QuoteSysID', ctypes.c_char * 21),  # 报价编号
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 插入时间
        ('CancelTime', ctypes.c_char * 9),  # 撤销时间
        ('QuoteStatus', ctypes.c_char),  # 报价状态
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('AskOrderSysID', ctypes.c_char * 21),  # 卖方报单编号
        ('BidOrderSysID', ctypes.c_char * 21),  # 买方报单编号
        ('ForQuoteSysID', ctypes.c_char * 21),  # 应价编号
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, AskPrice: float = 0.0, BidPrice: float = 0.0, AskVolume: int = 0, BidVolume: int = 0, RequestID: int = 0, BusinessUnit: str = '', AskOffsetFlag: str = '',
                 BidOffsetFlag: str = '', AskHedgeFlag: str = '', BidHedgeFlag: str = '', QuoteLocalID: str = '', ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '', reserve1: str = '',
                 TraderID: str = '', InstallID: int = 0, NotifySequence: int = 0, OrderSubmitStatus: str = '', TradingDay: str = '', SettlementID: int = 0, QuoteSysID: str = '', InsertDate: str = '',
                 InsertTime: str = '', CancelTime: str = '', QuoteStatus: str = '', ClearingPartID: str = '', SequenceNo: int = 0, AskOrderSysID: str = '', BidOrderSysID: str = '',
                 ForQuoteSysID: str = '', BranchID: str = '', reserve2: str = '', MacAddress: str = '', ExchangeInstID: str = '', IPAddress: str = ''):
        super(ExchangeQuoteField, self).__init__()
        self.AskPrice = float(AskPrice)
        self.BidPrice = float(BidPrice)
        self.AskVolume = int(AskVolume)
        self.BidVolume = int(BidVolume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.AskOffsetFlag = self._to_bytes(AskOffsetFlag)
        self.BidOffsetFlag = self._to_bytes(BidOffsetFlag)
        self.AskHedgeFlag = self._to_bytes(AskHedgeFlag)
        self.BidHedgeFlag = self._to_bytes(BidHedgeFlag)
        self.QuoteLocalID = self._to_bytes(QuoteLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.NotifySequence = int(NotifySequence)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.QuoteStatus = self._to_bytes(QuoteStatus)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.AskOrderSysID = self._to_bytes(AskOrderSysID)
        self.BidOrderSysID = self._to_bytes(BidOrderSysID)
        self.ForQuoteSysID = self._to_bytes(ForQuoteSysID)
        self.BranchID = self._to_bytes(BranchID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryExchangeQuoteField(Base):
    """交易所报价查询"""
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, ParticipantID: str = '', ClientID: str = '', reserve1: str = '', ExchangeID: str = '', TraderID: str = '', ExchangeInstID: str = ''):
        super(QryExchangeQuoteField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class QryQuoteActionField(Base):
    """报价操作查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExchangeID: str = ''):
        super(QryQuoteActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class ExchangeQuoteActionField(Base):
    """交易所报价操作"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('QuoteSysID', ctypes.c_char * 21),  # 报价操作编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('QuoteLocalID', ctypes.c_char * 13),  # 本地报价编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, ExchangeID: str = '', QuoteSysID: str = '', ActionFlag: str = '', ActionDate: str = '', ActionTime: str = '', TraderID: str = '', InstallID: int = 0, QuoteLocalID: str = '',
                 ActionLocalID: str = '', ParticipantID: str = '', ClientID: str = '', BusinessUnit: str = '', OrderActionStatus: str = '', UserID: str = '', reserve1: str = '', MacAddress: str = '',
                 IPAddress: str = ''):
        super(ExchangeQuoteActionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.QuoteLocalID = self._to_bytes(QuoteLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.reserve1 = self._to_bytes(reserve1)
        self.MacAddress = self._to_bytes(MacAddress)
        self.IPAddress = self._to_bytes(IPAddress)


class QryExchangeQuoteActionField(Base):
    """交易所报价操作查询"""
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
    ]

    def __init__(self, ParticipantID: str = '', ClientID: str = '', ExchangeID: str = '', TraderID: str = ''):
        super(QryExchangeQuoteActionField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class OptionInstrDeltaField(Base):
    """期权合约delta值"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('Delta', ctypes.c_double),  # Delta值
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', Delta: float = 0.0, InstrumentID: str = ''):
        super(OptionInstrDeltaField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Delta = float(Delta)
        self.InstrumentID = self._to_bytes(InstrumentID)


class ForQuoteRspField(Base):
    """发给做市商的询价请求"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ForQuoteSysID', ctypes.c_char * 21),  # 询价编号
        ('ForQuoteTime', ctypes.c_char * 9),  # 询价时间
        ('ActionDay', ctypes.c_char * 9),  # 业务日期
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, TradingDay: str = '', reserve1: str = '', ForQuoteSysID: str = '', ForQuoteTime: str = '', ActionDay: str = '', ExchangeID: str = '', InstrumentID: str = ''):
        super(ForQuoteRspField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.reserve1 = self._to_bytes(reserve1)
        self.ForQuoteSysID = self._to_bytes(ForQuoteSysID)
        self.ForQuoteTime = self._to_bytes(ForQuoteTime)
        self.ActionDay = self._to_bytes(ActionDay)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class StrikeOffsetField(Base):
    """当前期权合约执行偏移值的详细内容"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('Offset', ctypes.c_double),  # 执行偏移值
        ('OffsetType', ctypes.c_char),  # 执行偏移类型
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', Offset: float = 0.0, OffsetType: str = '', InstrumentID: str = ''):
        super(StrikeOffsetField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Offset = float(Offset)
        self.OffsetType = self._to_bytes(OffsetType)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryStrikeOffsetField(Base):
    """期权执行偏移值查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', InstrumentID: str = ''):
        super(QryStrikeOffsetField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InputBatchOrderActionField(Base):
    """输入批量报单操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OrderActionRef', ctypes.c_int),  # 报单操作引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', OrderActionRef: int = 0, RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '', UserID: str = '',
                 InvestUnitID: str = '', reserve1: str = '', MacAddress: str = '', IPAddress: str = ''):
        super(InputBatchOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.UserID = self._to_bytes(UserID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve1 = self._to_bytes(reserve1)
        self.MacAddress = self._to_bytes(MacAddress)
        self.IPAddress = self._to_bytes(IPAddress)


class BatchOrderActionField(Base):
    """批量报单操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OrderActionRef', ctypes.c_int),  # 报单操作引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', OrderActionRef: int = 0, RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '', ActionDate: str = '',
                 ActionTime: str = '', TraderID: str = '', InstallID: int = 0, ActionLocalID: str = '', ParticipantID: str = '', ClientID: str = '', BusinessUnit: str = '',
                 OrderActionStatus: str = '', UserID: str = '', StatusMsg: str = '', InvestUnitID: str = '', reserve1: str = '', MacAddress: str = '', IPAddress: str = ''):
        super(BatchOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve1 = self._to_bytes(reserve1)
        self.MacAddress = self._to_bytes(MacAddress)
        self.IPAddress = self._to_bytes(IPAddress)


class ExchangeBatchOrderActionField(Base):
    """交易所批量报单操作"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, ExchangeID: str = '', ActionDate: str = '', ActionTime: str = '', TraderID: str = '', InstallID: int = 0, ActionLocalID: str = '', ParticipantID: str = '', ClientID: str = '',
                 BusinessUnit: str = '', OrderActionStatus: str = '', UserID: str = '', reserve1: str = '', MacAddress: str = '', IPAddress: str = ''):
        super(ExchangeBatchOrderActionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.reserve1 = self._to_bytes(reserve1)
        self.MacAddress = self._to_bytes(MacAddress)
        self.IPAddress = self._to_bytes(IPAddress)


class QryBatchOrderActionField(Base):
    """查询批量报单操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExchangeID: str = ''):
        super(QryBatchOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class CombInstrumentGuardField(Base):
    """组合合约安全系数"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('GuarantRatio', ctypes.c_double),  #
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', reserve1: str = '', GuarantRatio: float = 0.0, ExchangeID: str = '', InstrumentID: str = ''):
        super(CombInstrumentGuardField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.reserve1 = self._to_bytes(reserve1)
        self.GuarantRatio = float(GuarantRatio)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryCombInstrumentGuardField(Base):
    """组合合约安全系数查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', reserve1: str = '', ExchangeID: str = '', InstrumentID: str = ''):
        super(QryCombInstrumentGuardField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InputCombActionField(Base):
    """输入的申请组合"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('CombActionRef', ctypes.c_char * 13),  # 组合引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Direction', ctypes.c_char),  # 买卖方向
        ('Volume', ctypes.c_int),  # 数量
        ('CombDirection', ctypes.c_char),  # 组合指令方向
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', CombActionRef: str = '', UserID: str = '', Direction: str = '', Volume: int = 0, CombDirection: str = '',
                 HedgeFlag: str = '', ExchangeID: str = '', reserve2: str = '', MacAddress: str = '', InvestUnitID: str = '', FrontID: int = 0, SessionID: int = 0, InstrumentID: str = '',
                 IPAddress: str = ''):
        super(InputCombActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.CombActionRef = self._to_bytes(CombActionRef)
        self.UserID = self._to_bytes(UserID)
        self.Direction = self._to_bytes(Direction)
        self.Volume = int(Volume)
        self.CombDirection = self._to_bytes(CombDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class CombActionField(Base):
    """申请组合"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('CombActionRef', ctypes.c_char * 13),  # 组合引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Direction', ctypes.c_char),  # 买卖方向
        ('Volume', ctypes.c_int),  # 数量
        ('CombDirection', ctypes.c_char),  # 组合指令方向
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ActionLocalID', ctypes.c_char * 13),  # 本地申请组合编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('ActionStatus', ctypes.c_char),  # 组合状态
        ('NotifySequence', ctypes.c_int),  # 报单提示序号
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('reserve3', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('ComTradeID', ctypes.c_char * 21),  # 组合编号
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', CombActionRef: str = '', UserID: str = '', Direction: str = '', Volume: int = 0, CombDirection: str = '',
                 HedgeFlag: str = '', ActionLocalID: str = '', ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '', reserve2: str = '', TraderID: str = '', InstallID: int = 0,
                 ActionStatus: str = '', NotifySequence: int = 0, TradingDay: str = '', SettlementID: int = 0, SequenceNo: int = 0, FrontID: int = 0, SessionID: int = 0, UserProductInfo: str = '',
                 StatusMsg: str = '', reserve3: str = '', MacAddress: str = '', ComTradeID: str = '', BranchID: str = '', InvestUnitID: str = '', InstrumentID: str = '', ExchangeInstID: str = '',
                 IPAddress: str = ''):
        super(CombActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.CombActionRef = self._to_bytes(CombActionRef)
        self.UserID = self._to_bytes(UserID)
        self.Direction = self._to_bytes(Direction)
        self.Volume = int(Volume)
        self.CombDirection = self._to_bytes(CombDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ActionStatus = self._to_bytes(ActionStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.reserve3 = self._to_bytes(reserve3)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ComTradeID = self._to_bytes(ComTradeID)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryCombActionField(Base):
    """申请组合查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryCombActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class ExchangeCombActionField(Base):
    """交易所申请组合信息"""
    _fields_ = [
        ('Direction', ctypes.c_char),  # 买卖方向
        ('Volume', ctypes.c_int),  # 数量
        ('CombDirection', ctypes.c_char),  # 组合指令方向
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ActionLocalID', ctypes.c_char * 13),  # 本地申请组合编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('ActionStatus', ctypes.c_char),  # 组合状态
        ('NotifySequence', ctypes.c_int),  # 报单提示序号
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('ComTradeID', ctypes.c_char * 21),  # 组合编号
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, Direction: str = '', Volume: int = 0, CombDirection: str = '', HedgeFlag: str = '', ActionLocalID: str = '', ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '',
                 reserve1: str = '', TraderID: str = '', InstallID: int = 0, ActionStatus: str = '', NotifySequence: int = 0, TradingDay: str = '', SettlementID: int = 0, SequenceNo: int = 0,
                 reserve2: str = '', MacAddress: str = '', ComTradeID: str = '', BranchID: str = '', ExchangeInstID: str = '', IPAddress: str = ''):
        super(ExchangeCombActionField, self).__init__()
        self.Direction = self._to_bytes(Direction)
        self.Volume = int(Volume)
        self.CombDirection = self._to_bytes(CombDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ActionStatus = self._to_bytes(ActionStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.SequenceNo = int(SequenceNo)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ComTradeID = self._to_bytes(ComTradeID)
        self.BranchID = self._to_bytes(BranchID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryExchangeCombActionField(Base):
    """交易所申请组合查询"""
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, ParticipantID: str = '', ClientID: str = '', reserve1: str = '', ExchangeID: str = '', TraderID: str = '', ExchangeInstID: str = ''):
        super(QryExchangeCombActionField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class ProductExchRateField(Base):
    """产品报价汇率"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('QuoteCurrencyID', ctypes.c_char * 4),  # 报价币种类型
        ('ExchangeRate', ctypes.c_double),  # 汇率
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ProductID', ctypes.c_char * 81),  # 产品代码
    ]

    def __init__(self, reserve1: str = '', QuoteCurrencyID: str = '', ExchangeRate: float = 0.0, ExchangeID: str = '', ProductID: str = ''):
        super(ProductExchRateField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.QuoteCurrencyID = self._to_bytes(QuoteCurrencyID)
        self.ExchangeRate = float(ExchangeRate)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProductID = self._to_bytes(ProductID)


class QryProductExchRateField(Base):
    """产品报价汇率查询"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ProductID', ctypes.c_char * 81),  # 产品代码
    ]

    def __init__(self, reserve1: str = '', ExchangeID: str = '', ProductID: str = ''):
        super(QryProductExchRateField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProductID = self._to_bytes(ProductID)


class QryForQuoteParamField(Base):
    """查询询价价差参数"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', reserve1: str = '', ExchangeID: str = '', InstrumentID: str = ''):
        super(QryForQuoteParamField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class ForQuoteParamField(Base):
    """询价价差参数"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('LastPrice', ctypes.c_double),  # 最新价
        ('PriceInterval', ctypes.c_double),  # 价差
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', reserve1: str = '', ExchangeID: str = '', LastPrice: float = 0.0, PriceInterval: float = 0.0, InstrumentID: str = ''):
        super(ForQuoteParamField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.LastPrice = float(LastPrice)
        self.PriceInterval = float(PriceInterval)
        self.InstrumentID = self._to_bytes(InstrumentID)


class MMOptionInstrCommRateField(Base):
    """当前做市商期权合约手续费的详细内容"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', ctypes.c_double),  # 开仓手续费率
        ('OpenRatioByVolume', ctypes.c_double),  # 开仓手续费
        ('CloseRatioByMoney', ctypes.c_double),  # 平仓手续费率
        ('CloseRatioByVolume', ctypes.c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', ctypes.c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', ctypes.c_double),  # 平今手续费
        ('StrikeRatioByMoney', ctypes.c_double),  # 执行手续费率
        ('StrikeRatioByVolume', ctypes.c_double),  # 执行手续费
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', OpenRatioByMoney: float = 0.0, OpenRatioByVolume: float = 0.0,
                 CloseRatioByMoney: float = 0.0, CloseRatioByVolume: float = 0.0, CloseTodayRatioByMoney: float = 0.0, CloseTodayRatioByVolume: float = 0.0, StrikeRatioByMoney: float = 0.0,
                 StrikeRatioByVolume: float = 0.0, InstrumentID: str = ''):
        super(MMOptionInstrCommRateField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.StrikeRatioByMoney = float(StrikeRatioByMoney)
        self.StrikeRatioByVolume = float(StrikeRatioByVolume)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryMMOptionInstrCommRateField(Base):
    """做市商期权手续费率查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', InstrumentID: str = ''):
        super(QryMMOptionInstrCommRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InstrumentID = self._to_bytes(InstrumentID)


class MMInstrumentCommissionRateField(Base):
    """做市商合约手续费率"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', ctypes.c_double),  # 开仓手续费率
        ('OpenRatioByVolume', ctypes.c_double),  # 开仓手续费
        ('CloseRatioByMoney', ctypes.c_double),  # 平仓手续费率
        ('CloseRatioByVolume', ctypes.c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', ctypes.c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', ctypes.c_double),  # 平今手续费
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', OpenRatioByMoney: float = 0.0, OpenRatioByVolume: float = 0.0,
                 CloseRatioByMoney: float = 0.0, CloseRatioByVolume: float = 0.0, CloseTodayRatioByMoney: float = 0.0, CloseTodayRatioByVolume: float = 0.0, InstrumentID: str = ''):
        super(MMInstrumentCommissionRateField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryMMInstrumentCommissionRateField(Base):
    """查询做市商合约手续费率"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', InstrumentID: str = ''):
        super(QryMMInstrumentCommissionRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InstrumentOrderCommRateField(Base):
    """当前报单手续费的详细内容"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('OrderCommByVolume', ctypes.c_double),  # 报单手续费
        ('OrderActionCommByVolume', ctypes.c_double),  # 撤单手续费
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('OrderCommByTrade', ctypes.c_double),  # 报单手续费
        ('OrderActionCommByTrade', ctypes.c_double),  # 撤单手续费
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', HedgeFlag: str = '', OrderCommByVolume: float = 0.0, OrderActionCommByVolume: float = 0.0,
                 ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = '', OrderCommByTrade: float = 0.0, OrderActionCommByTrade: float = 0.0):
        super(InstrumentOrderCommRateField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.OrderCommByVolume = float(OrderCommByVolume)
        self.OrderActionCommByVolume = float(OrderActionCommByVolume)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.OrderCommByTrade = float(OrderCommByTrade)
        self.OrderActionCommByTrade = float(OrderActionCommByTrade)


class QryInstrumentOrderCommRateField(Base):
    """报单手续费率查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', InstrumentID: str = ''):
        super(QryInstrumentOrderCommRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InstrumentID = self._to_bytes(InstrumentID)


class TradeParamField(Base):
    """交易参数"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('TradeParamID', ctypes.c_char),  # 参数代码
        ('TradeParamValue', ctypes.c_char * 256),  # 参数代码值
        ('Memo', ctypes.c_char * 161),  # 备注
    ]

    def __init__(self, BrokerID: str = '', TradeParamID: str = '', TradeParamValue: str = '', Memo: str = ''):
        super(TradeParamField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.TradeParamID = self._to_bytes(TradeParamID)
        self.TradeParamValue = self._to_bytes(TradeParamValue)
        self.Memo = self._to_bytes(Memo)


class InstrumentMarginRateULField(Base):
    """合约保证金率调整"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('LongMarginRatioByMoney', ctypes.c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', ctypes.c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', ctypes.c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', ctypes.c_double),  # 空头保证金费
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', HedgeFlag: str = '', LongMarginRatioByMoney: float = 0.0,
                 LongMarginRatioByVolume: float = 0.0, ShortMarginRatioByMoney: float = 0.0, ShortMarginRatioByVolume: float = 0.0, InstrumentID: str = ''):
        super(InstrumentMarginRateULField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.InstrumentID = self._to_bytes(InstrumentID)


class FutureLimitPosiParamField(Base):
    """期货持仓限制参数"""
    _fields_ = [
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('SpecOpenVolume', ctypes.c_int),  # 当日投机开仓数量限制
        ('ArbiOpenVolume', ctypes.c_int),  # 当日套利开仓数量限制
        ('OpenVolume', ctypes.c_int),  # 当日投机+套利开仓数量限制
        ('ProductID', ctypes.c_char * 81),  # 产品代码
    ]

    def __init__(self, InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', reserve1: str = '', SpecOpenVolume: int = 0, ArbiOpenVolume: int = 0, OpenVolume: int = 0,
                 ProductID: str = ''):
        super(FutureLimitPosiParamField, self).__init__()
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.SpecOpenVolume = int(SpecOpenVolume)
        self.ArbiOpenVolume = int(ArbiOpenVolume)
        self.OpenVolume = int(OpenVolume)
        self.ProductID = self._to_bytes(ProductID)


class LoginForbiddenIPField(Base):
    """禁止登录IP"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, reserve1: str = '', IPAddress: str = ''):
        super(LoginForbiddenIPField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.IPAddress = self._to_bytes(IPAddress)


class IPListField(Base):
    """IP列表"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('IsWhite', ctypes.c_int),  # 是否白名单
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, reserve1: str = '', IsWhite: int = 0, IPAddress: str = ''):
        super(IPListField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.IsWhite = int(IsWhite)
        self.IPAddress = self._to_bytes(IPAddress)


class InputOptionSelfCloseField(Base):
    """输入的期权自对冲"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('OptionSelfCloseRef', ctypes.c_char * 13),  # 期权自对冲引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Volume', ctypes.c_int),  # 数量
        ('RequestID', ctypes.c_int),  # 请求编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('OptSelfCloseFlag', ctypes.c_char),  # 期权行权的头寸是否自对冲
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('ClientID', ctypes.c_char * 11),  # 交易编码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OptionSelfCloseRef: str = '', UserID: str = '', Volume: int = 0, RequestID: int = 0, BusinessUnit: str = '',
                 HedgeFlag: str = '', OptSelfCloseFlag: str = '', ExchangeID: str = '', InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', ClientID: str = '', reserve2: str = '',
                 MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(InputOptionSelfCloseField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.OptionSelfCloseRef = self._to_bytes(OptionSelfCloseRef)
        self.UserID = self._to_bytes(UserID)
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.OptSelfCloseFlag = self._to_bytes(OptSelfCloseFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class InputOptionSelfCloseActionField(Base):
    """输入期权自对冲操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OptionSelfCloseActionRef', ctypes.c_int),  # 期权自对冲操作引用
        ('OptionSelfCloseRef', ctypes.c_char * 13),  # 期权自对冲引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OptionSelfCloseSysID', ctypes.c_char * 21),  # 期权自对冲操作编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', OptionSelfCloseActionRef: int = 0, OptionSelfCloseRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0,
                 ExchangeID: str = '', OptionSelfCloseSysID: str = '', ActionFlag: str = '', UserID: str = '', reserve1: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '',
                 InstrumentID: str = '', IPAddress: str = ''):
        super(InputOptionSelfCloseActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OptionSelfCloseActionRef = int(OptionSelfCloseActionRef)
        self.OptionSelfCloseRef = self._to_bytes(OptionSelfCloseRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OptionSelfCloseSysID = self._to_bytes(OptionSelfCloseSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.UserID = self._to_bytes(UserID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class OptionSelfCloseField(Base):
    """期权自对冲"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('OptionSelfCloseRef', ctypes.c_char * 13),  # 期权自对冲引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Volume', ctypes.c_int),  # 数量
        ('RequestID', ctypes.c_int),  # 请求编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('OptSelfCloseFlag', ctypes.c_char),  # 期权行权的头寸是否自对冲
        ('OptionSelfCloseLocalID', ctypes.c_char * 13),  # 本地期权自对冲编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderSubmitStatus', ctypes.c_char),  # 期权自对冲提交状态
        ('NotifySequence', ctypes.c_int),  # 报单提示序号
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('OptionSelfCloseSysID', ctypes.c_char * 21),  # 期权自对冲编号
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 插入时间
        ('CancelTime', ctypes.c_char * 9),  # 撤销时间
        ('ExecResult', ctypes.c_char),  # 自对冲结果
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('ActiveUserID', ctypes.c_char * 16),  # 操作用户代码
        ('BrokerOptionSelfCloseSeq', ctypes.c_int),  # 经纪公司报单编号
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('reserve3', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OptionSelfCloseRef: str = '', UserID: str = '', Volume: int = 0, RequestID: int = 0, BusinessUnit: str = '',
                 HedgeFlag: str = '', OptSelfCloseFlag: str = '', OptionSelfCloseLocalID: str = '', ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '', reserve2: str = '',
                 TraderID: str = '', InstallID: int = 0, OrderSubmitStatus: str = '', NotifySequence: int = 0, TradingDay: str = '', SettlementID: int = 0, OptionSelfCloseSysID: str = '',
                 InsertDate: str = '', InsertTime: str = '', CancelTime: str = '', ExecResult: str = '', ClearingPartID: str = '', SequenceNo: int = 0, FrontID: int = 0, SessionID: int = 0,
                 UserProductInfo: str = '', StatusMsg: str = '', ActiveUserID: str = '', BrokerOptionSelfCloseSeq: int = 0, BranchID: str = '', InvestUnitID: str = '', AccountID: str = '',
                 CurrencyID: str = '', reserve3: str = '', MacAddress: str = '', InstrumentID: str = '', ExchangeInstID: str = '', IPAddress: str = ''):
        super(OptionSelfCloseField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.OptionSelfCloseRef = self._to_bytes(OptionSelfCloseRef)
        self.UserID = self._to_bytes(UserID)
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.OptSelfCloseFlag = self._to_bytes(OptSelfCloseFlag)
        self.OptionSelfCloseLocalID = self._to_bytes(OptionSelfCloseLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OptionSelfCloseSysID = self._to_bytes(OptionSelfCloseSysID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ExecResult = self._to_bytes(ExecResult)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerOptionSelfCloseSeq = int(BrokerOptionSelfCloseSeq)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.reserve3 = self._to_bytes(reserve3)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class OptionSelfCloseActionField(Base):
    """期权自对冲操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OptionSelfCloseActionRef', ctypes.c_int),  # 期权自对冲操作引用
        ('OptionSelfCloseRef', ctypes.c_char * 13),  # 期权自对冲引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OptionSelfCloseSysID', ctypes.c_char * 21),  # 期权自对冲操作编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OptionSelfCloseLocalID', ctypes.c_char * 13),  # 本地期权自对冲编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', OptionSelfCloseActionRef: int = 0, OptionSelfCloseRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0,
                 ExchangeID: str = '', OptionSelfCloseSysID: str = '', ActionFlag: str = '', ActionDate: str = '', ActionTime: str = '', TraderID: str = '', InstallID: int = 0,
                 OptionSelfCloseLocalID: str = '', ActionLocalID: str = '', ParticipantID: str = '', ClientID: str = '', BusinessUnit: str = '', OrderActionStatus: str = '', UserID: str = '',
                 StatusMsg: str = '', reserve1: str = '', BranchID: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(OptionSelfCloseActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OptionSelfCloseActionRef = int(OptionSelfCloseActionRef)
        self.OptionSelfCloseRef = self._to_bytes(OptionSelfCloseRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OptionSelfCloseSysID = self._to_bytes(OptionSelfCloseSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OptionSelfCloseLocalID = self._to_bytes(OptionSelfCloseLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.reserve1 = self._to_bytes(reserve1)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryOptionSelfCloseField(Base):
    """期权自对冲查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OptionSelfCloseSysID', ctypes.c_char * 21),  # 期权自对冲编号
        ('InsertTimeStart', ctypes.c_char * 9),  # 开始时间
        ('InsertTimeEnd', ctypes.c_char * 9),  # 结束时间
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', OptionSelfCloseSysID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '',
                 InstrumentID: str = ''):
        super(QryOptionSelfCloseField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OptionSelfCloseSysID = self._to_bytes(OptionSelfCloseSysID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)
        self.InstrumentID = self._to_bytes(InstrumentID)


class ExchangeOptionSelfCloseField(Base):
    """交易所期权自对冲信息"""
    _fields_ = [
        ('Volume', ctypes.c_int),  # 数量
        ('RequestID', ctypes.c_int),  # 请求编号
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('OptSelfCloseFlag', ctypes.c_char),  # 期权行权的头寸是否自对冲
        ('OptionSelfCloseLocalID', ctypes.c_char * 13),  # 本地期权自对冲编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderSubmitStatus', ctypes.c_char),  # 期权自对冲提交状态
        ('NotifySequence', ctypes.c_int),  # 报单提示序号
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('OptionSelfCloseSysID', ctypes.c_char * 21),  # 期权自对冲编号
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 插入时间
        ('CancelTime', ctypes.c_char * 9),  # 撤销时间
        ('ExecResult', ctypes.c_char),  # 自对冲结果
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, Volume: int = 0, RequestID: int = 0, BusinessUnit: str = '', HedgeFlag: str = '', OptSelfCloseFlag: str = '', OptionSelfCloseLocalID: str = '', ExchangeID: str = '',
                 ParticipantID: str = '', ClientID: str = '', reserve1: str = '', TraderID: str = '', InstallID: int = 0, OrderSubmitStatus: str = '', NotifySequence: int = 0, TradingDay: str = '',
                 SettlementID: int = 0, OptionSelfCloseSysID: str = '', InsertDate: str = '', InsertTime: str = '', CancelTime: str = '', ExecResult: str = '', ClearingPartID: str = '',
                 SequenceNo: int = 0, BranchID: str = '', reserve2: str = '', MacAddress: str = '', ExchangeInstID: str = '', IPAddress: str = ''):
        super(ExchangeOptionSelfCloseField, self).__init__()
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.OptSelfCloseFlag = self._to_bytes(OptSelfCloseFlag)
        self.OptionSelfCloseLocalID = self._to_bytes(OptionSelfCloseLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve1 = self._to_bytes(reserve1)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OptionSelfCloseSysID = self._to_bytes(OptionSelfCloseSysID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ExecResult = self._to_bytes(ExecResult)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.BranchID = self._to_bytes(BranchID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryOptionSelfCloseActionField(Base):
    """期权自对冲操作查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExchangeID: str = ''):
        super(QryOptionSelfCloseActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class ExchangeOptionSelfCloseActionField(Base):
    """交易所期权自对冲操作"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OptionSelfCloseSysID', ctypes.c_char * 21),  # 期权自对冲操作编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OptionSelfCloseLocalID', ctypes.c_char * 13),  # 本地期权自对冲编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('OptSelfCloseFlag', ctypes.c_char),  # 期权行权的头寸是否自对冲
        ('IPAddress', ctypes.c_char * 33),  # IP地址
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, ExchangeID: str = '', OptionSelfCloseSysID: str = '', ActionFlag: str = '', ActionDate: str = '', ActionTime: str = '', TraderID: str = '', InstallID: int = 0,
                 OptionSelfCloseLocalID: str = '', ActionLocalID: str = '', ParticipantID: str = '', ClientID: str = '', BusinessUnit: str = '', OrderActionStatus: str = '', UserID: str = '',
                 BranchID: str = '', reserve1: str = '', MacAddress: str = '', reserve2: str = '', OptSelfCloseFlag: str = '', IPAddress: str = '', ExchangeInstID: str = ''):
        super(ExchangeOptionSelfCloseActionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OptionSelfCloseSysID = self._to_bytes(OptionSelfCloseSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OptionSelfCloseLocalID = self._to_bytes(OptionSelfCloseLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.BranchID = self._to_bytes(BranchID)
        self.reserve1 = self._to_bytes(reserve1)
        self.MacAddress = self._to_bytes(MacAddress)
        self.reserve2 = self._to_bytes(reserve2)
        self.OptSelfCloseFlag = self._to_bytes(OptSelfCloseFlag)
        self.IPAddress = self._to_bytes(IPAddress)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class SyncDelaySwapField(Base):
    """延时换汇同步"""
    _fields_ = [
        ('DelaySwapSeqNo', ctypes.c_char * 15),  # 换汇流水号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('FromCurrencyID', ctypes.c_char * 4),  # 源币种
        ('FromAmount', ctypes.c_double),  # 源金额
        ('FromFrozenSwap', ctypes.c_double),  # 源换汇冻结金额(可用冻结)
        ('FromRemainSwap', ctypes.c_double),  # 源剩余换汇额度(可提冻结)
        ('ToCurrencyID', ctypes.c_char * 4),  # 目标币种
        ('ToAmount', ctypes.c_double),  # 目标金额
        ('IsManualSwap', ctypes.c_int),  # 是否手工换汇
        ('IsAllRemainSetZero', ctypes.c_int),  # 是否将所有外币的剩余换汇额度设置为0
    ]

    def __init__(self, DelaySwapSeqNo: str = '', BrokerID: str = '', InvestorID: str = '', FromCurrencyID: str = '', FromAmount: float = 0.0, FromFrozenSwap: float = 0.0, FromRemainSwap: float = 0.0,
                 ToCurrencyID: str = '', ToAmount: float = 0.0, IsManualSwap: int = 0, IsAllRemainSetZero: int = 0):
        super(SyncDelaySwapField, self).__init__()
        self.DelaySwapSeqNo = self._to_bytes(DelaySwapSeqNo)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.FromCurrencyID = self._to_bytes(FromCurrencyID)
        self.FromAmount = float(FromAmount)
        self.FromFrozenSwap = float(FromFrozenSwap)
        self.FromRemainSwap = float(FromRemainSwap)
        self.ToCurrencyID = self._to_bytes(ToCurrencyID)
        self.ToAmount = float(ToAmount)
        self.IsManualSwap = int(IsManualSwap)
        self.IsAllRemainSetZero = int(IsAllRemainSetZero)


class QrySyncDelaySwapField(Base):
    """查询延时换汇同步"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('DelaySwapSeqNo', ctypes.c_char * 15),  # 延时换汇流水号
    ]

    def __init__(self, BrokerID: str = '', DelaySwapSeqNo: str = ''):
        super(QrySyncDelaySwapField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.DelaySwapSeqNo = self._to_bytes(DelaySwapSeqNo)


class InvestUnitField(Base):
    """投资单元"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InvestorUnitName', ctypes.c_char * 81),  # 投资者单元名称
        ('InvestorGroupID', ctypes.c_char * 13),  # 投资者分组代码
        ('CommModelID', ctypes.c_char * 13),  # 手续费率模板代码
        ('MarginModelID', ctypes.c_char * 13),  # 保证金率模板代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', InvestUnitID: str = '', InvestorUnitName: str = '', InvestorGroupID: str = '', CommModelID: str = '', MarginModelID: str = '',
                 AccountID: str = '', CurrencyID: str = ''):
        super(InvestUnitField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InvestorUnitName = self._to_bytes(InvestorUnitName)
        self.InvestorGroupID = self._to_bytes(InvestorGroupID)
        self.CommModelID = self._to_bytes(CommModelID)
        self.MarginModelID = self._to_bytes(MarginModelID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class QryInvestUnitField(Base):
    """查询投资单元"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', InvestUnitID: str = ''):
        super(QryInvestUnitField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)


class SecAgentCheckModeField(Base):
    """二级代理商资金校验模式"""
    _fields_ = [
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('CurrencyID', ctypes.c_char * 4),  # 币种
        ('BrokerSecAgentID', ctypes.c_char * 13),  # 境外中介机构资金帐号
        ('CheckSelfAccount', ctypes.c_int),  # 是否需要校验自己的资金账户
    ]

    def __init__(self, InvestorID: str = '', BrokerID: str = '', CurrencyID: str = '', BrokerSecAgentID: str = '', CheckSelfAccount: int = 0):
        super(SecAgentCheckModeField, self).__init__()
        self.InvestorID = self._to_bytes(InvestorID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.BrokerSecAgentID = self._to_bytes(BrokerSecAgentID)
        self.CheckSelfAccount = int(CheckSelfAccount)


class SecAgentTradeInfoField(Base):
    """二级代理商信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('BrokerSecAgentID', ctypes.c_char * 13),  # 境外中介机构资金帐号
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('LongCustomerName', ctypes.c_char * 161),  # 二级代理商姓名
    ]

    def __init__(self, BrokerID: str = '', BrokerSecAgentID: str = '', InvestorID: str = '', LongCustomerName: str = ''):
        super(SecAgentTradeInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerSecAgentID = self._to_bytes(BrokerSecAgentID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class MarketDataField(Base):
    """市场行情"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('LastPrice', ctypes.c_double),  # 最新价
        ('PreSettlementPrice', ctypes.c_double),  # 上次结算价
        ('PreClosePrice', ctypes.c_double),  # 昨收盘
        ('PreOpenInterest', ctypes.c_double),  # 昨持仓量
        ('OpenPrice', ctypes.c_double),  # 今开盘
        ('HighestPrice', ctypes.c_double),  # 最高价
        ('LowestPrice', ctypes.c_double),  # 最低价
        ('Volume', ctypes.c_int),  # 数量
        ('Turnover', ctypes.c_double),  # 成交金额
        ('OpenInterest', ctypes.c_double),  # 持仓量
        ('ClosePrice', ctypes.c_double),  # 今收盘
        ('SettlementPrice', ctypes.c_double),  # 本次结算价
        ('UpperLimitPrice', ctypes.c_double),  # 涨停板价
        ('LowerLimitPrice', ctypes.c_double),  # 跌停板价
        ('PreDelta', ctypes.c_double),  # 昨虚实度
        ('CurrDelta', ctypes.c_double),  # 今虚实度
        ('UpdateTime', ctypes.c_char * 9),  # 最后修改时间
        ('UpdateMillisec', ctypes.c_int),  # 最后修改毫秒
        ('ActionDay', ctypes.c_char * 9),  # 业务日期
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, TradingDay: str = '', reserve1: str = '', ExchangeID: str = '', reserve2: str = '', LastPrice: float = 0.0, PreSettlementPrice: float = 0.0, PreClosePrice: float = 0.0,
                 PreOpenInterest: float = 0.0, OpenPrice: float = 0.0, HighestPrice: float = 0.0, LowestPrice: float = 0.0, Volume: int = 0, Turnover: float = 0.0, OpenInterest: float = 0.0,
                 ClosePrice: float = 0.0, SettlementPrice: float = 0.0, UpperLimitPrice: float = 0.0, LowerLimitPrice: float = 0.0, PreDelta: float = 0.0, CurrDelta: float = 0.0, UpdateTime: str = '',
                 UpdateMillisec: int = 0, ActionDay: str = '', InstrumentID: str = '', ExchangeInstID: str = ''):
        super(MarketDataField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve2 = self._to_bytes(reserve2)
        self.LastPrice = float(LastPrice)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)
        self.ClosePrice = float(ClosePrice)
        self.SettlementPrice = float(SettlementPrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.PreDelta = float(PreDelta)
        self.CurrDelta = float(CurrDelta)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.UpdateMillisec = int(UpdateMillisec)
        self.ActionDay = self._to_bytes(ActionDay)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class MarketDataBaseField(Base):
    """行情基础属性"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('PreSettlementPrice', ctypes.c_double),  # 上次结算价
        ('PreClosePrice', ctypes.c_double),  # 昨收盘
        ('PreOpenInterest', ctypes.c_double),  # 昨持仓量
        ('PreDelta', ctypes.c_double),  # 昨虚实度
    ]

    def __init__(self, TradingDay: str = '', PreSettlementPrice: float = 0.0, PreClosePrice: float = 0.0, PreOpenInterest: float = 0.0, PreDelta: float = 0.0):
        super(MarketDataBaseField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.PreDelta = float(PreDelta)


class MarketDataStaticField(Base):
    """行情静态属性"""
    _fields_ = [
        ('OpenPrice', ctypes.c_double),  # 今开盘
        ('HighestPrice', ctypes.c_double),  # 最高价
        ('LowestPrice', ctypes.c_double),  # 最低价
        ('ClosePrice', ctypes.c_double),  # 今收盘
        ('UpperLimitPrice', ctypes.c_double),  # 涨停板价
        ('LowerLimitPrice', ctypes.c_double),  # 跌停板价
        ('SettlementPrice', ctypes.c_double),  # 本次结算价
        ('CurrDelta', ctypes.c_double),  # 今虚实度
    ]

    def __init__(self, OpenPrice: float = 0.0, HighestPrice: float = 0.0, LowestPrice: float = 0.0, ClosePrice: float = 0.0, UpperLimitPrice: float = 0.0, LowerLimitPrice: float = 0.0,
                 SettlementPrice: float = 0.0, CurrDelta: float = 0.0):
        super(MarketDataStaticField, self).__init__()
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.ClosePrice = float(ClosePrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.CurrDelta = float(CurrDelta)


class MarketDataLastMatchField(Base):
    """行情最新成交属性"""
    _fields_ = [
        ('LastPrice', ctypes.c_double),  # 最新价
        ('Volume', ctypes.c_int),  # 数量
        ('Turnover', ctypes.c_double),  # 成交金额
        ('OpenInterest', ctypes.c_double),  # 持仓量
    ]

    def __init__(self, LastPrice: float = 0.0, Volume: int = 0, Turnover: float = 0.0, OpenInterest: float = 0.0):
        super(MarketDataLastMatchField, self).__init__()
        self.LastPrice = float(LastPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)


class MarketDataBestPriceField(Base):
    """行情最优价属性"""
    _fields_ = [
        ('BidPrice1', ctypes.c_double),  # 申买价一
        ('BidVolume1', ctypes.c_int),  # 申买量一
        ('AskPrice1', ctypes.c_double),  # 申卖价一
        ('AskVolume1', ctypes.c_int),  # 申卖量一
    ]

    def __init__(self, BidPrice1: float = 0.0, BidVolume1: int = 0, AskPrice1: float = 0.0, AskVolume1: int = 0):
        super(MarketDataBestPriceField, self).__init__()
        self.BidPrice1 = float(BidPrice1)
        self.BidVolume1 = int(BidVolume1)
        self.AskPrice1 = float(AskPrice1)
        self.AskVolume1 = int(AskVolume1)


class MarketDataBid23Field(Base):
    """行情申买二、三属性"""
    _fields_ = [
        ('BidPrice2', ctypes.c_double),  # 申买价二
        ('BidVolume2', ctypes.c_int),  # 申买量二
        ('BidPrice3', ctypes.c_double),  # 申买价三
        ('BidVolume3', ctypes.c_int),  # 申买量三
    ]

    def __init__(self, BidPrice2: float = 0.0, BidVolume2: int = 0, BidPrice3: float = 0.0, BidVolume3: int = 0):
        super(MarketDataBid23Field, self).__init__()
        self.BidPrice2 = float(BidPrice2)
        self.BidVolume2 = int(BidVolume2)
        self.BidPrice3 = float(BidPrice3)
        self.BidVolume3 = int(BidVolume3)


class MarketDataAsk23Field(Base):
    """行情申卖二、三属性"""
    _fields_ = [
        ('AskPrice2', ctypes.c_double),  # 申卖价二
        ('AskVolume2', ctypes.c_int),  # 申卖量二
        ('AskPrice3', ctypes.c_double),  # 申卖价三
        ('AskVolume3', ctypes.c_int),  # 申卖量三
    ]

    def __init__(self, AskPrice2: float = 0.0, AskVolume2: int = 0, AskPrice3: float = 0.0, AskVolume3: int = 0):
        super(MarketDataAsk23Field, self).__init__()
        self.AskPrice2 = float(AskPrice2)
        self.AskVolume2 = int(AskVolume2)
        self.AskPrice3 = float(AskPrice3)
        self.AskVolume3 = int(AskVolume3)


class MarketDataBid45Field(Base):
    """行情申买四、五属性"""
    _fields_ = [
        ('BidPrice4', ctypes.c_double),  # 申买价四
        ('BidVolume4', ctypes.c_int),  # 申买量四
        ('BidPrice5', ctypes.c_double),  # 申买价五
        ('BidVolume5', ctypes.c_int),  # 申买量五
    ]

    def __init__(self, BidPrice4: float = 0.0, BidVolume4: int = 0, BidPrice5: float = 0.0, BidVolume5: int = 0):
        super(MarketDataBid45Field, self).__init__()
        self.BidPrice4 = float(BidPrice4)
        self.BidVolume4 = int(BidVolume4)
        self.BidPrice5 = float(BidPrice5)
        self.BidVolume5 = int(BidVolume5)


class MarketDataAsk45Field(Base):
    """行情申卖四、五属性"""
    _fields_ = [
        ('AskPrice4', ctypes.c_double),  # 申卖价四
        ('AskVolume4', ctypes.c_int),  # 申卖量四
        ('AskPrice5', ctypes.c_double),  # 申卖价五
        ('AskVolume5', ctypes.c_int),  # 申卖量五
    ]

    def __init__(self, AskPrice4: float = 0.0, AskVolume4: int = 0, AskPrice5: float = 0.0, AskVolume5: int = 0):
        super(MarketDataAsk45Field, self).__init__()
        self.AskPrice4 = float(AskPrice4)
        self.AskVolume4 = int(AskVolume4)
        self.AskPrice5 = float(AskPrice5)
        self.AskVolume5 = int(AskVolume5)


class MarketDataUpdateTimeField(Base):
    """行情更新时间属性"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('UpdateTime', ctypes.c_char * 9),  # 最后修改时间
        ('UpdateMillisec', ctypes.c_int),  # 最后修改毫秒
        ('ActionDay', ctypes.c_char * 9),  # 业务日期
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', UpdateTime: str = '', UpdateMillisec: int = 0, ActionDay: str = '', InstrumentID: str = ''):
        super(MarketDataUpdateTimeField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.UpdateMillisec = int(UpdateMillisec)
        self.ActionDay = self._to_bytes(ActionDay)
        self.InstrumentID = self._to_bytes(InstrumentID)


class MarketDataBandingPriceField(Base):
    """行情上下带价"""
    _fields_ = [
        ('BandingUpperPrice', ctypes.c_double),  # 上带价
        ('BandingLowerPrice', ctypes.c_double),  # 下带价
    ]

    def __init__(self, BandingUpperPrice: float = 0.0, BandingLowerPrice: float = 0.0):
        super(MarketDataBandingPriceField, self).__init__()
        self.BandingUpperPrice = float(BandingUpperPrice)
        self.BandingLowerPrice = float(BandingLowerPrice)


class MarketDataExchangeField(Base):
    """行情交易所代码属性"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
    ]

    def __init__(self, ExchangeID: str = ''):
        super(MarketDataExchangeField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)


class SpecificInstrumentField(Base):
    """指定的合约"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, reserve1: str = '', InstrumentID: str = ''):
        super(SpecificInstrumentField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InstrumentStatusField(Base):
    """合约状态"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('SettlementGroupID', ctypes.c_char * 9),  # 结算组代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentStatus', ctypes.c_char),  # 合约交易状态
        ('TradingSegmentSN', ctypes.c_int),  # 交易阶段编号
        ('EnterTime', ctypes.c_char * 9),  # 进入本状态时间
        ('EnterReason', ctypes.c_char),  # 进入本状态原因
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, ExchangeID: str = '', reserve1: str = '', SettlementGroupID: str = '', reserve2: str = '', InstrumentStatus: str = '', TradingSegmentSN: int = 0, EnterTime: str = '',
                 EnterReason: str = '', ExchangeInstID: str = '', InstrumentID: str = ''):
        super(InstrumentStatusField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve1 = self._to_bytes(reserve1)
        self.SettlementGroupID = self._to_bytes(SettlementGroupID)
        self.reserve2 = self._to_bytes(reserve2)
        self.InstrumentStatus = self._to_bytes(InstrumentStatus)
        self.TradingSegmentSN = int(TradingSegmentSN)
        self.EnterTime = self._to_bytes(EnterTime)
        self.EnterReason = self._to_bytes(EnterReason)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryInstrumentStatusField(Base):
    """查询合约状态"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
    ]

    def __init__(self, ExchangeID: str = '', reserve1: str = '', ExchangeInstID: str = ''):
        super(QryInstrumentStatusField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class InvestorAccountField(Base):
    """投资者账户"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', AccountID: str = '', CurrencyID: str = ''):
        super(InvestorAccountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class PositionProfitAlgorithmField(Base):
    """浮动盈亏算法"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Algorithm', ctypes.c_char),  # 盈亏算法
        ('Memo', ctypes.c_char * 161),  # 备注
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', AccountID: str = '', Algorithm: str = '', Memo: str = '', CurrencyID: str = ''):
        super(PositionProfitAlgorithmField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.Algorithm = self._to_bytes(Algorithm)
        self.Memo = self._to_bytes(Memo)
        self.CurrencyID = self._to_bytes(CurrencyID)


class DiscountField(Base):
    """会员资金折扣"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('Discount', ctypes.c_double),  # 资金折扣比例
    ]

    def __init__(self, BrokerID: str = '', InvestorRange: str = '', InvestorID: str = '', Discount: float = 0.0):
        super(DiscountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Discount = float(Discount)


class QryTransferBankField(Base):
    """查询转帐银行"""
    _fields_ = [
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBrchID', ctypes.c_char * 5),  # 银行分中心代码
    ]

    def __init__(self, BankID: str = '', BankBrchID: str = ''):
        super(QryTransferBankField, self).__init__()
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)


class TransferBankField(Base):
    """转帐银行"""
    _fields_ = [
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBrchID', ctypes.c_char * 5),  # 银行分中心代码
        ('BankName', ctypes.c_char * 101),  # 银行名称
        ('IsActive', ctypes.c_int),  # 是否活跃
    ]

    def __init__(self, BankID: str = '', BankBrchID: str = '', BankName: str = '', IsActive: int = 0):
        super(TransferBankField, self).__init__()
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)
        self.BankName = self._to_bytes(BankName)
        self.IsActive = int(IsActive)


class QryInvestorPositionDetailField(Base):
    """查询投资者持仓明细"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryInvestorPositionDetailField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InvestorPositionDetailField(Base):
    """投资者持仓明细"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('Direction', ctypes.c_char),  # 买卖
        ('OpenDate', ctypes.c_char * 9),  # 开仓日期
        ('TradeID', ctypes.c_char * 21),  # 成交编号
        ('Volume', ctypes.c_int),  # 数量
        ('OpenPrice', ctypes.c_double),  # 开仓价
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('TradeType', ctypes.c_char),  # 成交类型
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('CloseProfitByDate', ctypes.c_double),  # 逐日盯市平仓盈亏
        ('CloseProfitByTrade', ctypes.c_double),  # 逐笔对冲平仓盈亏
        ('PositionProfitByDate', ctypes.c_double),  # 逐日盯市持仓盈亏
        ('PositionProfitByTrade', ctypes.c_double),  # 逐笔对冲持仓盈亏
        ('Margin', ctypes.c_double),  # 投资者保证金
        ('ExchMargin', ctypes.c_double),  # 交易所保证金
        ('MarginRateByMoney', ctypes.c_double),  # 保证金率
        ('MarginRateByVolume', ctypes.c_double),  # 保证金率(按手数)
        ('LastSettlementPrice', ctypes.c_double),  # 昨结算价
        ('SettlementPrice', ctypes.c_double),  # 结算价
        ('CloseVolume', ctypes.c_int),  # 平仓量
        ('CloseAmount', ctypes.c_double),  # 平仓金额
        ('TimeFirstVolume', ctypes.c_int),  # 先开先平剩余数量
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('SpecPosiType', ctypes.c_char),  # 特殊持仓标志
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('CombInstrumentID', ctypes.c_char * 81),  # 组合合约代码
    ]

    def __init__(self, reserve1: str = '', BrokerID: str = '', InvestorID: str = '', HedgeFlag: str = '', Direction: str = '', OpenDate: str = '', TradeID: str = '', Volume: int = 0,
                 OpenPrice: float = 0.0, TradingDay: str = '', SettlementID: int = 0, TradeType: str = '', reserve2: str = '', ExchangeID: str = '', CloseProfitByDate: float = 0.0,
                 CloseProfitByTrade: float = 0.0, PositionProfitByDate: float = 0.0, PositionProfitByTrade: float = 0.0, Margin: float = 0.0, ExchMargin: float = 0.0, MarginRateByMoney: float = 0.0,
                 MarginRateByVolume: float = 0.0, LastSettlementPrice: float = 0.0, SettlementPrice: float = 0.0, CloseVolume: int = 0, CloseAmount: float = 0.0, TimeFirstVolume: int = 0,
                 InvestUnitID: str = '', SpecPosiType: str = '', InstrumentID: str = '', CombInstrumentID: str = ''):
        super(InvestorPositionDetailField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Direction = self._to_bytes(Direction)
        self.OpenDate = self._to_bytes(OpenDate)
        self.TradeID = self._to_bytes(TradeID)
        self.Volume = int(Volume)
        self.OpenPrice = float(OpenPrice)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.TradeType = self._to_bytes(TradeType)
        self.reserve2 = self._to_bytes(reserve2)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.CloseProfitByDate = float(CloseProfitByDate)
        self.CloseProfitByTrade = float(CloseProfitByTrade)
        self.PositionProfitByDate = float(PositionProfitByDate)
        self.PositionProfitByTrade = float(PositionProfitByTrade)
        self.Margin = float(Margin)
        self.ExchMargin = float(ExchMargin)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.LastSettlementPrice = float(LastSettlementPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.CloseVolume = int(CloseVolume)
        self.CloseAmount = float(CloseAmount)
        self.TimeFirstVolume = int(TimeFirstVolume)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.SpecPosiType = self._to_bytes(SpecPosiType)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)


class TradingAccountPasswordField(Base):
    """资金账户口令域"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 密码
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', AccountID: str = '', Password: str = '', CurrencyID: str = ''):
        super(TradingAccountPasswordField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.CurrencyID = self._to_bytes(CurrencyID)


class MDTraderOfferField(Base):
    """交易所行情报盘机"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('Password', ctypes.c_char * 41),  # 密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('TraderConnectStatus', ctypes.c_char),  # 交易所交易员连接状态
        ('ConnectRequestDate', ctypes.c_char * 9),  # 发出连接请求的日期
        ('ConnectRequestTime', ctypes.c_char * 9),  # 发出连接请求的时间
        ('LastReportDate', ctypes.c_char * 9),  # 上次报告日期
        ('LastReportTime', ctypes.c_char * 9),  # 上次报告时间
        ('ConnectDate', ctypes.c_char * 9),  # 完成连接日期
        ('ConnectTime', ctypes.c_char * 9),  # 完成连接时间
        ('StartDate', ctypes.c_char * 9),  # 启动日期
        ('StartTime', ctypes.c_char * 9),  # 启动时间
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('MaxTradeID', ctypes.c_char * 21),  # 本席位最大成交编号
        ('MaxOrderMessageReference', ctypes.c_char * 7),  # 本席位最大报单备拷
        ('OrderCancelAlg', ctypes.c_char),  # 撤单时选择席位算法
    ]

    def __init__(self, ExchangeID: str = '', TraderID: str = '', ParticipantID: str = '', Password: str = '', InstallID: int = 0, OrderLocalID: str = '', TraderConnectStatus: str = '',
                 ConnectRequestDate: str = '', ConnectRequestTime: str = '', LastReportDate: str = '', LastReportTime: str = '', ConnectDate: str = '', ConnectTime: str = '', StartDate: str = '',
                 StartTime: str = '', TradingDay: str = '', BrokerID: str = '', MaxTradeID: str = '', MaxOrderMessageReference: str = '', OrderCancelAlg: str = ''):
        super(MDTraderOfferField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.TraderConnectStatus = self._to_bytes(TraderConnectStatus)
        self.ConnectRequestDate = self._to_bytes(ConnectRequestDate)
        self.ConnectRequestTime = self._to_bytes(ConnectRequestTime)
        self.LastReportDate = self._to_bytes(LastReportDate)
        self.LastReportTime = self._to_bytes(LastReportTime)
        self.ConnectDate = self._to_bytes(ConnectDate)
        self.ConnectTime = self._to_bytes(ConnectTime)
        self.StartDate = self._to_bytes(StartDate)
        self.StartTime = self._to_bytes(StartTime)
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.MaxTradeID = self._to_bytes(MaxTradeID)
        self.MaxOrderMessageReference = self._to_bytes(MaxOrderMessageReference)
        self.OrderCancelAlg = self._to_bytes(OrderCancelAlg)


class QryMDTraderOfferField(Base):
    """查询行情报盘机"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
    ]

    def __init__(self, ExchangeID: str = '', ParticipantID: str = '', TraderID: str = ''):
        super(QryMDTraderOfferField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.TraderID = self._to_bytes(TraderID)


class QryNoticeField(Base):
    """查询客户通知"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
    ]

    def __init__(self, BrokerID: str = ''):
        super(QryNoticeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class NoticeField(Base):
    """客户通知"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('Content', ctypes.c_char * 501),  # 消息正文
        ('SequenceLabel', ctypes.c_char * 2),  # 经纪公司通知内容序列号
    ]

    def __init__(self, BrokerID: str = '', Content: str = '', SequenceLabel: str = ''):
        super(NoticeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.Content = self._to_bytes(Content)
        self.SequenceLabel = self._to_bytes(SequenceLabel)


class UserRightField(Base):
    """用户权限"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('UserRightType', ctypes.c_char),  # 客户权限类型
        ('IsForbidden', ctypes.c_int),  # 是否禁止
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', UserRightType: str = '', IsForbidden: int = 0):
        super(UserRightField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserRightType = self._to_bytes(UserRightType)
        self.IsForbidden = int(IsForbidden)


class QrySettlementInfoConfirmField(Base):
    """查询结算信息确认域"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', AccountID: str = '', CurrencyID: str = ''):
        super(QrySettlementInfoConfirmField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class LoadSettlementInfoField(Base):
    """装载结算信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
    ]

    def __init__(self, BrokerID: str = ''):
        super(LoadSettlementInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class BrokerWithdrawAlgorithmField(Base):
    """经纪公司可提资金算法表"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('WithdrawAlgorithm', ctypes.c_char),  # 可提资金算法
        ('UsingRatio', ctypes.c_double),  # 资金使用率
        ('IncludeCloseProfit', ctypes.c_char),  # 可提是否包含平仓盈利
        ('AllWithoutTrade', ctypes.c_char),  # 本日无仓且无成交客户是否受可提比例限制
        ('AvailIncludeCloseProfit', ctypes.c_char),  # 可用是否包含平仓盈利
        ('IsBrokerUserEvent', ctypes.c_int),  # 是否启用用户事件
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('FundMortgageRatio', ctypes.c_double),  # 货币质押比率
        ('BalanceAlgorithm', ctypes.c_char),  # 权益算法
    ]

    def __init__(self, BrokerID: str = '', WithdrawAlgorithm: str = '', UsingRatio: float = 0.0, IncludeCloseProfit: str = '', AllWithoutTrade: str = '', AvailIncludeCloseProfit: str = '',
                 IsBrokerUserEvent: int = 0, CurrencyID: str = '', FundMortgageRatio: float = 0.0, BalanceAlgorithm: str = ''):
        super(BrokerWithdrawAlgorithmField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.WithdrawAlgorithm = self._to_bytes(WithdrawAlgorithm)
        self.UsingRatio = float(UsingRatio)
        self.IncludeCloseProfit = self._to_bytes(IncludeCloseProfit)
        self.AllWithoutTrade = self._to_bytes(AllWithoutTrade)
        self.AvailIncludeCloseProfit = self._to_bytes(AvailIncludeCloseProfit)
        self.IsBrokerUserEvent = int(IsBrokerUserEvent)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.FundMortgageRatio = float(FundMortgageRatio)
        self.BalanceAlgorithm = self._to_bytes(BalanceAlgorithm)


class TradingAccountPasswordUpdateV1Field(Base):
    """资金账户口令变更域"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OldPassword', ctypes.c_char * 41),  # 原来的口令
        ('NewPassword', ctypes.c_char * 41),  # 新的口令
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', OldPassword: str = '', NewPassword: str = ''):
        super(TradingAccountPasswordUpdateV1Field, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OldPassword = self._to_bytes(OldPassword)
        self.NewPassword = self._to_bytes(NewPassword)


class TradingAccountPasswordUpdateField(Base):
    """资金账户口令变更域"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('OldPassword', ctypes.c_char * 41),  # 原来的口令
        ('NewPassword', ctypes.c_char * 41),  # 新的口令
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', AccountID: str = '', OldPassword: str = '', NewPassword: str = '', CurrencyID: str = ''):
        super(TradingAccountPasswordUpdateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.OldPassword = self._to_bytes(OldPassword)
        self.NewPassword = self._to_bytes(NewPassword)
        self.CurrencyID = self._to_bytes(CurrencyID)


class QryCombinationLegField(Base):
    """查询组合合约分腿"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('LegID', ctypes.c_int),  # 单腿编号
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('CombInstrumentID', ctypes.c_char * 81),  # 组合合约代码
        ('LegInstrumentID', ctypes.c_char * 81),  # 单腿合约代码
    ]

    def __init__(self, reserve1: str = '', LegID: int = 0, reserve2: str = '', CombInstrumentID: str = '', LegInstrumentID: str = ''):
        super(QryCombinationLegField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.LegID = int(LegID)
        self.reserve2 = self._to_bytes(reserve2)
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)
        self.LegInstrumentID = self._to_bytes(LegInstrumentID)


class QrySyncStatusField(Base):
    """查询组合合约分腿"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
    ]

    def __init__(self, TradingDay: str = ''):
        super(QrySyncStatusField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)


class CombinationLegField(Base):
    """组合交易合约的单腿"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('LegID', ctypes.c_int),  # 单腿编号
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('Direction', ctypes.c_char),  # 买卖方向
        ('LegMultiple', ctypes.c_int),  # 单腿乘数
        ('ImplyLevel', ctypes.c_int),  # 派生层数
        ('CombInstrumentID', ctypes.c_char * 81),  # 组合合约代码
        ('LegInstrumentID', ctypes.c_char * 81),  # 单腿合约代码
    ]

    def __init__(self, reserve1: str = '', LegID: int = 0, reserve2: str = '', Direction: str = '', LegMultiple: int = 0, ImplyLevel: int = 0, CombInstrumentID: str = '', LegInstrumentID: str = ''):
        super(CombinationLegField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.LegID = int(LegID)
        self.reserve2 = self._to_bytes(reserve2)
        self.Direction = self._to_bytes(Direction)
        self.LegMultiple = int(LegMultiple)
        self.ImplyLevel = int(ImplyLevel)
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)
        self.LegInstrumentID = self._to_bytes(LegInstrumentID)


class SyncStatusField(Base):
    """数据同步状态"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('DataSyncStatus', ctypes.c_char),  # 数据同步状态
    ]

    def __init__(self, TradingDay: str = '', DataSyncStatus: str = ''):
        super(SyncStatusField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.DataSyncStatus = self._to_bytes(DataSyncStatus)


class QryLinkManField(Base):
    """查询联系人"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = ''):
        super(QryLinkManField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class LinkManField(Base):
    """联系人"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('PersonType', ctypes.c_char),  # 联系人类型
        ('IdentifiedCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('PersonName', ctypes.c_char * 81),  # 名称
        ('Telephone', ctypes.c_char * 41),  # 联系电话
        ('Address', ctypes.c_char * 101),  # 通讯地址
        ('ZipCode', ctypes.c_char * 7),  # 邮政编码
        ('Priority', ctypes.c_int),  # 优先级
        ('UOAZipCode', ctypes.c_char * 11),  # 开户邮政编码
        ('PersonFullName', ctypes.c_char * 101),  # 全称
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', PersonType: str = '', IdentifiedCardType: str = '', IdentifiedCardNo: str = '', PersonName: str = '', Telephone: str = '',
                 Address: str = '', ZipCode: str = '', Priority: int = 0, UOAZipCode: str = '', PersonFullName: str = ''):
        super(LinkManField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.PersonType = self._to_bytes(PersonType)
        self.IdentifiedCardType = self._to_bytes(IdentifiedCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.PersonName = self._to_bytes(PersonName)
        self.Telephone = self._to_bytes(Telephone)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Priority = int(Priority)
        self.UOAZipCode = self._to_bytes(UOAZipCode)
        self.PersonFullName = self._to_bytes(PersonFullName)


class QryBrokerUserEventField(Base):
    """查询经纪公司用户事件"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('UserEventType', ctypes.c_char),  # 用户事件类型
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', UserEventType: str = ''):
        super(QryBrokerUserEventField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserEventType = self._to_bytes(UserEventType)


class BrokerUserEventField(Base):
    """查询经纪公司用户事件"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('UserEventType', ctypes.c_char),  # 用户事件类型
        ('EventSequenceNo', ctypes.c_int),  # 用户事件序号
        ('EventDate', ctypes.c_char * 9),  # 事件发生日期
        ('EventTime', ctypes.c_char * 9),  # 事件发生时间
        ('UserEventInfo', ctypes.c_char * 1025),  # 用户事件信息
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', UserEventType: str = '', EventSequenceNo: int = 0, EventDate: str = '', EventTime: str = '', UserEventInfo: str = '', InvestorID: str = '',
                 reserve1: str = '', InstrumentID: str = ''):
        super(BrokerUserEventField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserEventType = self._to_bytes(UserEventType)
        self.EventSequenceNo = int(EventSequenceNo)
        self.EventDate = self._to_bytes(EventDate)
        self.EventTime = self._to_bytes(EventTime)
        self.UserEventInfo = self._to_bytes(UserEventInfo)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryContractBankField(Base):
    """查询签约银行请求"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBrchID', ctypes.c_char * 5),  # 银行分中心代码
    ]

    def __init__(self, BrokerID: str = '', BankID: str = '', BankBrchID: str = ''):
        super(QryContractBankField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)


class ContractBankField(Base):
    """查询签约银行响应"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBrchID', ctypes.c_char * 5),  # 银行分中心代码
        ('BankName', ctypes.c_char * 101),  # 银行名称
    ]

    def __init__(self, BrokerID: str = '', BankID: str = '', BankBrchID: str = '', BankName: str = ''):
        super(ContractBankField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)
        self.BankName = self._to_bytes(BankName)


class InvestorPositionCombineDetailField(Base):
    """投资者组合持仓明细"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('OpenDate', ctypes.c_char * 9),  # 开仓日期
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ComTradeID', ctypes.c_char * 21),  # 组合编号
        ('TradeID', ctypes.c_char * 21),  # 撮合编号
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('Direction', ctypes.c_char),  # 买卖
        ('TotalAmt', ctypes.c_int),  # 持仓量
        ('Margin', ctypes.c_double),  # 投资者保证金
        ('ExchMargin', ctypes.c_double),  # 交易所保证金
        ('MarginRateByMoney', ctypes.c_double),  # 保证金率
        ('MarginRateByVolume', ctypes.c_double),  # 保证金率(按手数)
        ('LegID', ctypes.c_int),  # 单腿编号
        ('LegMultiple', ctypes.c_int),  # 单腿乘数
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('TradeGroupID', ctypes.c_int),  # 成交组号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('CombInstrumentID', ctypes.c_char * 81),  # 组合持仓合约编码
    ]

    def __init__(self, TradingDay: str = '', OpenDate: str = '', ExchangeID: str = '', SettlementID: int = 0, BrokerID: str = '', InvestorID: str = '', ComTradeID: str = '', TradeID: str = '',
                 reserve1: str = '', HedgeFlag: str = '', Direction: str = '', TotalAmt: int = 0, Margin: float = 0.0, ExchMargin: float = 0.0, MarginRateByMoney: float = 0.0,
                 MarginRateByVolume: float = 0.0, LegID: int = 0, LegMultiple: int = 0, reserve2: str = '', TradeGroupID: int = 0, InvestUnitID: str = '', InstrumentID: str = '',
                 CombInstrumentID: str = ''):
        super(InvestorPositionCombineDetailField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.OpenDate = self._to_bytes(OpenDate)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.SettlementID = int(SettlementID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ComTradeID = self._to_bytes(ComTradeID)
        self.TradeID = self._to_bytes(TradeID)
        self.reserve1 = self._to_bytes(reserve1)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Direction = self._to_bytes(Direction)
        self.TotalAmt = int(TotalAmt)
        self.Margin = float(Margin)
        self.ExchMargin = float(ExchMargin)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.LegID = int(LegID)
        self.LegMultiple = int(LegMultiple)
        self.reserve2 = self._to_bytes(reserve2)
        self.TradeGroupID = int(TradeGroupID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)


class ParkedOrderField(Base):
    """预埋单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('OrderRef', ctypes.c_char * 13),  # 报单引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('OrderPriceType', ctypes.c_char),  # 报单价格条件
        ('Direction', ctypes.c_char),  # 买卖方向
        ('CombOffsetFlag', ctypes.c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', ctypes.c_char * 5),  # 组合投机套保标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeTotalOriginal', ctypes.c_int),  # 数量
        ('TimeCondition', ctypes.c_char),  # 有效期类型
        ('GTDDate', ctypes.c_char * 9),  # GTD日期
        ('VolumeCondition', ctypes.c_char),  # 成交量类型
        ('MinVolume', ctypes.c_int),  # 最小成交量
        ('ContingentCondition', ctypes.c_char),  # 触发条件
        ('StopPrice', ctypes.c_double),  # 止损价
        ('ForceCloseReason', ctypes.c_char),  # 强平原因
        ('IsAutoSuspend', ctypes.c_int),  # 自动挂起标志
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('RequestID', ctypes.c_int),  # 请求编号
        ('UserForceClose', ctypes.c_int),  # 用户强评标志
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParkedOrderID', ctypes.c_char * 13),  # 预埋报单编号
        ('UserType', ctypes.c_char),  # 用户类型
        ('Status', ctypes.c_char),  # 预埋单状态
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('IsSwapOrder', ctypes.c_int),  # 互换单标志
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('ClientID', ctypes.c_char * 11),  # 交易编码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OrderRef: str = '', UserID: str = '', OrderPriceType: str = '', Direction: str = '', CombOffsetFlag: str = '',
                 CombHedgeFlag: str = '', LimitPrice: float = 0.0, VolumeTotalOriginal: int = 0, TimeCondition: str = '', GTDDate: str = '', VolumeCondition: str = '', MinVolume: int = 0,
                 ContingentCondition: str = '', StopPrice: float = 0.0, ForceCloseReason: str = '', IsAutoSuspend: int = 0, BusinessUnit: str = '', RequestID: int = 0, UserForceClose: int = 0,
                 ExchangeID: str = '', ParkedOrderID: str = '', UserType: str = '', Status: str = '', ErrorID: int = 0, ErrorMsg: str = '', IsSwapOrder: int = 0, AccountID: str = '',
                 CurrencyID: str = '', ClientID: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(ParkedOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParkedOrderID = self._to_bytes(ParkedOrderID)
        self.UserType = self._to_bytes(UserType)
        self.Status = self._to_bytes(Status)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.IsSwapOrder = int(IsSwapOrder)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class ParkedOrderActionField(Base):
    """输入预埋单操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OrderActionRef', ctypes.c_int),  # 报单操作引用
        ('OrderRef', ctypes.c_char * 13),  # 报单引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeChange', ctypes.c_int),  # 数量变化
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ParkedOrderActionID', ctypes.c_char * 13),  # 预埋撤单单编号
        ('UserType', ctypes.c_char),  # 用户类型
        ('Status', ctypes.c_char),  # 预埋撤单状态
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', OrderActionRef: int = 0, OrderRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '',
                 OrderSysID: str = '', ActionFlag: str = '', LimitPrice: float = 0.0, VolumeChange: int = 0, UserID: str = '', reserve1: str = '', ParkedOrderActionID: str = '', UserType: str = '',
                 Status: str = '', ErrorID: int = 0, ErrorMsg: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(ParkedOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = self._to_bytes(OrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.UserID = self._to_bytes(UserID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ParkedOrderActionID = self._to_bytes(ParkedOrderActionID)
        self.UserType = self._to_bytes(UserType)
        self.Status = self._to_bytes(Status)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryParkedOrderField(Base):
    """查询预埋单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryParkedOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryParkedOrderActionField(Base):
    """查询预埋撤单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryParkedOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class RemoveParkedOrderField(Base):
    """删除预埋单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ParkedOrderID', ctypes.c_char * 13),  # 预埋报单编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ParkedOrderID: str = '', InvestUnitID: str = ''):
        super(RemoveParkedOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ParkedOrderID = self._to_bytes(ParkedOrderID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)


class RemoveParkedOrderActionField(Base):
    """删除预埋撤单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ParkedOrderActionID', ctypes.c_char * 13),  # 预埋撤单编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ParkedOrderActionID: str = '', InvestUnitID: str = ''):
        super(RemoveParkedOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ParkedOrderActionID = self._to_bytes(ParkedOrderActionID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)


class InvestorWithdrawAlgorithmField(Base):
    """经纪公司可提资金算法表"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('UsingRatio', ctypes.c_double),  # 可提资金比例
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('FundMortgageRatio', ctypes.c_double),  # 货币质押比率
    ]

    def __init__(self, BrokerID: str = '', InvestorRange: str = '', InvestorID: str = '', UsingRatio: float = 0.0, CurrencyID: str = '', FundMortgageRatio: float = 0.0):
        super(InvestorWithdrawAlgorithmField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.InvestorID = self._to_bytes(InvestorID)
        self.UsingRatio = float(UsingRatio)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.FundMortgageRatio = float(FundMortgageRatio)


class QryInvestorPositionCombineDetailField(Base):
    """查询组合持仓明细"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('CombInstrumentID', ctypes.c_char * 81),  # 组合持仓合约编码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', CombInstrumentID: str = ''):
        super(QryInvestorPositionCombineDetailField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)


class MarketDataAveragePriceField(Base):
    """成交均价"""
    _fields_ = [
        ('AveragePrice', ctypes.c_double),  # 当日均价
    ]

    def __init__(self, AveragePrice: float = 0.0):
        super(MarketDataAveragePriceField, self).__init__()
        self.AveragePrice = float(AveragePrice)


class VerifyInvestorPasswordField(Base):
    """校验投资者密码"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('Password', ctypes.c_char * 41),  # 密码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', Password: str = ''):
        super(VerifyInvestorPasswordField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Password = self._to_bytes(Password)


class UserIPField(Base):
    """用户IP"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('IPAddress', ctypes.c_char * 33),  # IP地址
        ('IPMask', ctypes.c_char * 33),  # IP地址掩码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', reserve1: str = '', reserve2: str = '', MacAddress: str = '', IPAddress: str = '', IPMask: str = ''):
        super(UserIPField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.reserve1 = self._to_bytes(reserve1)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.IPAddress = self._to_bytes(IPAddress)
        self.IPMask = self._to_bytes(IPMask)


class TradingNoticeInfoField(Base):
    """用户事件通知信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('SendTime', ctypes.c_char * 9),  # 发送时间
        ('FieldContent', ctypes.c_char * 501),  # 消息正文
        ('SequenceSeries', ctypes.c_short),  # 序列系列号
        ('SequenceNo', ctypes.c_int),  # 序列号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', SendTime: str = '', FieldContent: str = '', SequenceSeries: int = 0, SequenceNo: int = 0, InvestUnitID: str = ''):
        super(TradingNoticeInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.SendTime = self._to_bytes(SendTime)
        self.FieldContent = self._to_bytes(FieldContent)
        self.SequenceSeries = int(SequenceSeries)
        self.SequenceNo = int(SequenceNo)
        self.InvestUnitID = self._to_bytes(InvestUnitID)


class TradingNoticeField(Base):
    """用户事件通知"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('SequenceSeries', ctypes.c_short),  # 序列系列号
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('SendTime', ctypes.c_char * 9),  # 发送时间
        ('SequenceNo', ctypes.c_int),  # 序列号
        ('FieldContent', ctypes.c_char * 501),  # 消息正文
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
    ]

    def __init__(self, BrokerID: str = '', InvestorRange: str = '', InvestorID: str = '', SequenceSeries: int = 0, UserID: str = '', SendTime: str = '', SequenceNo: int = 0, FieldContent: str = '',
                 InvestUnitID: str = ''):
        super(TradingNoticeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.InvestorID = self._to_bytes(InvestorID)
        self.SequenceSeries = int(SequenceSeries)
        self.UserID = self._to_bytes(UserID)
        self.SendTime = self._to_bytes(SendTime)
        self.SequenceNo = int(SequenceNo)
        self.FieldContent = self._to_bytes(FieldContent)
        self.InvestUnitID = self._to_bytes(InvestUnitID)


class QryTradingNoticeField(Base):
    """查询交易事件通知"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', InvestUnitID: str = ''):
        super(QryTradingNoticeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)


class QryErrOrderField(Base):
    """查询错误报单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = ''):
        super(QryErrOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class ErrOrderField(Base):
    """错误报单"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('OrderRef', ctypes.c_char * 13),  # 报单引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('OrderPriceType', ctypes.c_char),  # 报单价格条件
        ('Direction', ctypes.c_char),  # 买卖方向
        ('CombOffsetFlag', ctypes.c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', ctypes.c_char * 5),  # 组合投机套保标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeTotalOriginal', ctypes.c_int),  # 数量
        ('TimeCondition', ctypes.c_char),  # 有效期类型
        ('GTDDate', ctypes.c_char * 9),  # GTD日期
        ('VolumeCondition', ctypes.c_char),  # 成交量类型
        ('MinVolume', ctypes.c_int),  # 最小成交量
        ('ContingentCondition', ctypes.c_char),  # 触发条件
        ('StopPrice', ctypes.c_double),  # 止损价
        ('ForceCloseReason', ctypes.c_char),  # 强平原因
        ('IsAutoSuspend', ctypes.c_int),  # 自动挂起标志
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('RequestID', ctypes.c_int),  # 请求编号
        ('UserForceClose', ctypes.c_int),  # 用户强评标志
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('IsSwapOrder', ctypes.c_int),  # 互换单标志
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('ClientID', ctypes.c_char * 11),  # 交易编码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OrderRef: str = '', UserID: str = '', OrderPriceType: str = '', Direction: str = '', CombOffsetFlag: str = '',
                 CombHedgeFlag: str = '', LimitPrice: float = 0.0, VolumeTotalOriginal: int = 0, TimeCondition: str = '', GTDDate: str = '', VolumeCondition: str = '', MinVolume: int = 0,
                 ContingentCondition: str = '', StopPrice: float = 0.0, ForceCloseReason: str = '', IsAutoSuspend: int = 0, BusinessUnit: str = '', RequestID: int = 0, UserForceClose: int = 0,
                 ErrorID: int = 0, ErrorMsg: str = '', IsSwapOrder: int = 0, ExchangeID: str = '', InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', ClientID: str = '',
                 reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        super(ErrOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.IsSwapOrder = int(IsSwapOrder)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class ErrorConditionalOrderField(Base):
    """查询错误报单操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('OrderRef', ctypes.c_char * 13),  # 报单引用
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('OrderPriceType', ctypes.c_char),  # 报单价格条件
        ('Direction', ctypes.c_char),  # 买卖方向
        ('CombOffsetFlag', ctypes.c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', ctypes.c_char * 5),  # 组合投机套保标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeTotalOriginal', ctypes.c_int),  # 数量
        ('TimeCondition', ctypes.c_char),  # 有效期类型
        ('GTDDate', ctypes.c_char * 9),  # GTD日期
        ('VolumeCondition', ctypes.c_char),  # 成交量类型
        ('MinVolume', ctypes.c_int),  # 最小成交量
        ('ContingentCondition', ctypes.c_char),  # 触发条件
        ('StopPrice', ctypes.c_double),  # 止损价
        ('ForceCloseReason', ctypes.c_char),  # 强平原因
        ('IsAutoSuspend', ctypes.c_int),  # 自动挂起标志
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('RequestID', ctypes.c_int),  # 请求编号
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderSubmitStatus', ctypes.c_char),  # 报单提交状态
        ('NotifySequence', ctypes.c_int),  # 报单提示序号
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('OrderSource', ctypes.c_char),  # 报单来源
        ('OrderStatus', ctypes.c_char),  # 报单状态
        ('OrderType', ctypes.c_char),  # 报单类型
        ('VolumeTraded', ctypes.c_int),  # 今成交数量
        ('VolumeTotal', ctypes.c_int),  # 剩余数量
        ('InsertDate', ctypes.c_char * 9),  # 报单日期
        ('InsertTime', ctypes.c_char * 9),  # 委托时间
        ('ActiveTime', ctypes.c_char * 9),  # 激活时间
        ('SuspendTime', ctypes.c_char * 9),  # 挂起时间
        ('UpdateTime', ctypes.c_char * 9),  # 最后修改时间
        ('CancelTime', ctypes.c_char * 9),  # 撤销时间
        ('ActiveTraderID', ctypes.c_char * 21),  # 最后修改交易所交易员代码
        ('ClearingPartID', ctypes.c_char * 11),  # 结算会员编号
        ('SequenceNo', ctypes.c_int),  # 序号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('UserForceClose', ctypes.c_int),  # 用户强评标志
        ('ActiveUserID', ctypes.c_char * 16),  # 操作用户代码
        ('BrokerOrderSeq', ctypes.c_int),  # 经纪公司报单编号
        ('RelativeOrderSysID', ctypes.c_char * 21),  # 相关报单
        ('ZCETotalTradedVolume', ctypes.c_int),  # 郑商所成交数量
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('IsSwapOrder', ctypes.c_int),  # 互换单标志
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('AccountID', ctypes.c_char * 13),  # 资金账号
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('reserve3', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OrderRef: str = '', UserID: str = '', OrderPriceType: str = '', Direction: str = '', CombOffsetFlag: str = '',
                 CombHedgeFlag: str = '', LimitPrice: float = 0.0, VolumeTotalOriginal: int = 0, TimeCondition: str = '', GTDDate: str = '', VolumeCondition: str = '', MinVolume: int = 0,
                 ContingentCondition: str = '', StopPrice: float = 0.0, ForceCloseReason: str = '', IsAutoSuspend: int = 0, BusinessUnit: str = '', RequestID: int = 0, OrderLocalID: str = '',
                 ExchangeID: str = '', ParticipantID: str = '', ClientID: str = '', reserve2: str = '', TraderID: str = '', InstallID: int = 0, OrderSubmitStatus: str = '', NotifySequence: int = 0,
                 TradingDay: str = '', SettlementID: int = 0, OrderSysID: str = '', OrderSource: str = '', OrderStatus: str = '', OrderType: str = '', VolumeTraded: int = 0, VolumeTotal: int = 0,
                 InsertDate: str = '', InsertTime: str = '', ActiveTime: str = '', SuspendTime: str = '', UpdateTime: str = '', CancelTime: str = '', ActiveTraderID: str = '',
                 ClearingPartID: str = '', SequenceNo: int = 0, FrontID: int = 0, SessionID: int = 0, UserProductInfo: str = '', StatusMsg: str = '', UserForceClose: int = 0, ActiveUserID: str = '',
                 BrokerOrderSeq: int = 0, RelativeOrderSysID: str = '', ZCETotalTradedVolume: int = 0, ErrorID: int = 0, ErrorMsg: str = '', IsSwapOrder: int = 0, BranchID: str = '',
                 InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', reserve3: str = '', MacAddress: str = '', InstrumentID: str = '', ExchangeInstID: str = '', IPAddress: str = ''):
        super(ErrorConditionalOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.reserve2 = self._to_bytes(reserve2)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.OrderSource = self._to_bytes(OrderSource)
        self.OrderStatus = self._to_bytes(OrderStatus)
        self.OrderType = self._to_bytes(OrderType)
        self.VolumeTraded = int(VolumeTraded)
        self.VolumeTotal = int(VolumeTotal)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.ActiveTime = self._to_bytes(ActiveTime)
        self.SuspendTime = self._to_bytes(SuspendTime)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ActiveTraderID = self._to_bytes(ActiveTraderID)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.UserForceClose = int(UserForceClose)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerOrderSeq = int(BrokerOrderSeq)
        self.RelativeOrderSysID = self._to_bytes(RelativeOrderSysID)
        self.ZCETotalTradedVolume = int(ZCETotalTradedVolume)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.IsSwapOrder = int(IsSwapOrder)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.reserve3 = self._to_bytes(reserve3)
        self.MacAddress = self._to_bytes(MacAddress)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryErrOrderActionField(Base):
    """查询错误报单操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = ''):
        super(QryErrOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class ErrOrderActionField(Base):
    """错误报单操作"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OrderActionRef', ctypes.c_int),  # 报单操作引用
        ('OrderRef', ctypes.c_char * 13),  # 报单引用
        ('RequestID', ctypes.c_int),  # 请求编号
        ('FrontID', ctypes.c_int),  # 前置编号
        ('SessionID', ctypes.c_int),  # 会话编号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('OrderSysID', ctypes.c_char * 21),  # 报单编号
        ('ActionFlag', ctypes.c_char),  # 操作标志
        ('LimitPrice', ctypes.c_double),  # 价格
        ('VolumeChange', ctypes.c_int),  # 数量变化
        ('ActionDate', ctypes.c_char * 9),  # 操作日期
        ('ActionTime', ctypes.c_char * 9),  # 操作时间
        ('TraderID', ctypes.c_char * 21),  # 交易所交易员代码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('OrderLocalID', ctypes.c_char * 13),  # 本地报单编号
        ('ActionLocalID', ctypes.c_char * 13),  # 操作本地编号
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ClientID', ctypes.c_char * 11),  # 客户代码
        ('BusinessUnit', ctypes.c_char * 21),  # 业务单元
        ('OrderActionStatus', ctypes.c_char),  # 报单操作状态
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('StatusMsg', ctypes.c_char * 81),  # 状态信息
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('BranchID', ctypes.c_char * 9),  # 营业部编号
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('reserve2', ctypes.c_char * 16),  # 保留的无效字段
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', OrderActionRef: int = 0, OrderRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '',
                 OrderSysID: str = '', ActionFlag: str = '', LimitPrice: float = 0.0, VolumeChange: int = 0, ActionDate: str = '', ActionTime: str = '', TraderID: str = '', InstallID: int = 0,
                 OrderLocalID: str = '', ActionLocalID: str = '', ParticipantID: str = '', ClientID: str = '', BusinessUnit: str = '', OrderActionStatus: str = '', UserID: str = '',
                 StatusMsg: str = '', reserve1: str = '', BranchID: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', ErrorID: int = 0, ErrorMsg: str = '',
                 InstrumentID: str = '', IPAddress: str = ''):
        super(ErrOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = self._to_bytes(OrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.reserve1 = self._to_bytes(reserve1)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.reserve2 = self._to_bytes(reserve2)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryExchangeSequenceField(Base):
    """查询交易所状态"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
    ]

    def __init__(self, ExchangeID: str = ''):
        super(QryExchangeSequenceField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)


class ExchangeSequenceField(Base):
    """交易所状态"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('SequenceNo', ctypes.c_int),  # 序号
        ('MarketStatus', ctypes.c_char),  # 合约交易状态
    ]

    def __init__(self, ExchangeID: str = '', SequenceNo: int = 0, MarketStatus: str = ''):
        super(ExchangeSequenceField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.SequenceNo = int(SequenceNo)
        self.MarketStatus = self._to_bytes(MarketStatus)


class QryMaxOrderVolumeWithPriceField(Base):
    """根据价格查询最大报单数量"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('Direction', ctypes.c_char),  # 买卖方向
        ('OffsetFlag', ctypes.c_char),  # 开平标志
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('MaxVolume', ctypes.c_int),  # 最大允许报单数量
        ('Price', ctypes.c_double),  # 报单价格
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', Direction: str = '', OffsetFlag: str = '', HedgeFlag: str = '', MaxVolume: int = 0, Price: float = 0.0,
                 ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryMaxOrderVolumeWithPriceField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.Direction = self._to_bytes(Direction)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.MaxVolume = int(MaxVolume)
        self.Price = float(Price)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryBrokerTradingParamsField(Base):
    """查询经纪公司交易参数"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', CurrencyID: str = '', AccountID: str = ''):
        super(QryBrokerTradingParamsField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.AccountID = self._to_bytes(AccountID)


class BrokerTradingParamsField(Base):
    """经纪公司交易参数"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('MarginPriceType', ctypes.c_char),  # 保证金价格类型
        ('Algorithm', ctypes.c_char),  # 盈亏算法
        ('AvailIncludeCloseProfit', ctypes.c_char),  # 可用是否包含平仓盈利
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('OptionRoyaltyPriceType', ctypes.c_char),  # 期权权利金价格类型
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', MarginPriceType: str = '', Algorithm: str = '', AvailIncludeCloseProfit: str = '', CurrencyID: str = '',
                 OptionRoyaltyPriceType: str = '', AccountID: str = ''):
        super(BrokerTradingParamsField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.MarginPriceType = self._to_bytes(MarginPriceType)
        self.Algorithm = self._to_bytes(Algorithm)
        self.AvailIncludeCloseProfit = self._to_bytes(AvailIncludeCloseProfit)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.OptionRoyaltyPriceType = self._to_bytes(OptionRoyaltyPriceType)
        self.AccountID = self._to_bytes(AccountID)


class QryBrokerTradingAlgosField(Base):
    """查询经纪公司交易算法"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', ExchangeID: str = '', reserve1: str = '', InstrumentID: str = ''):
        super(QryBrokerTradingAlgosField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InstrumentID = self._to_bytes(InstrumentID)


class BrokerTradingAlgosField(Base):
    """经纪公司交易算法"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('HandlePositionAlgoID', ctypes.c_char),  # 持仓处理算法编号
        ('FindMarginRateAlgoID', ctypes.c_char),  # 寻找保证金率算法编号
        ('HandleTradingAccountAlgoID', ctypes.c_char),  # 资金处理算法编号
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', ExchangeID: str = '', reserve1: str = '', HandlePositionAlgoID: str = '', FindMarginRateAlgoID: str = '', HandleTradingAccountAlgoID: str = '',
                 InstrumentID: str = ''):
        super(BrokerTradingAlgosField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve1 = self._to_bytes(reserve1)
        self.HandlePositionAlgoID = self._to_bytes(HandlePositionAlgoID)
        self.FindMarginRateAlgoID = self._to_bytes(FindMarginRateAlgoID)
        self.HandleTradingAccountAlgoID = self._to_bytes(HandleTradingAccountAlgoID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QueryBrokerDepositField(Base):
    """查询经纪公司资金"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
    ]

    def __init__(self, BrokerID: str = '', ExchangeID: str = ''):
        super(QueryBrokerDepositField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class BrokerDepositField(Base):
    """经纪公司资金"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日期
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ParticipantID', ctypes.c_char * 11),  # 会员代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('PreBalance', ctypes.c_double),  # 上次结算准备金
        ('CurrMargin', ctypes.c_double),  # 当前保证金总额
        ('CloseProfit', ctypes.c_double),  # 平仓盈亏
        ('Balance', ctypes.c_double),  # 期货结算准备金
        ('Deposit', ctypes.c_double),  # 入金金额
        ('Withdraw', ctypes.c_double),  # 出金金额
        ('Available', ctypes.c_double),  # 可提资金
        ('Reserve', ctypes.c_double),  # 基本准备金
        ('FrozenMargin', ctypes.c_double),  # 冻结的保证金
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', ParticipantID: str = '', ExchangeID: str = '', PreBalance: float = 0.0, CurrMargin: float = 0.0, CloseProfit: float = 0.0,
                 Balance: float = 0.0, Deposit: float = 0.0, Withdraw: float = 0.0, Available: float = 0.0, Reserve: float = 0.0, FrozenMargin: float = 0.0):
        super(BrokerDepositField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.PreBalance = float(PreBalance)
        self.CurrMargin = float(CurrMargin)
        self.CloseProfit = float(CloseProfit)
        self.Balance = float(Balance)
        self.Deposit = float(Deposit)
        self.Withdraw = float(Withdraw)
        self.Available = float(Available)
        self.Reserve = float(Reserve)
        self.FrozenMargin = float(FrozenMargin)


class QryCFMMCBrokerKeyField(Base):
    """查询保证金监管系统经纪公司密钥"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
    ]

    def __init__(self, BrokerID: str = ''):
        super(QryCFMMCBrokerKeyField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class CFMMCBrokerKeyField(Base):
    """保证金监管系统经纪公司密钥"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ParticipantID', ctypes.c_char * 11),  # 经纪公司统一编码
        ('CreateDate', ctypes.c_char * 9),  # 密钥生成日期
        ('CreateTime', ctypes.c_char * 9),  # 密钥生成时间
        ('KeyID', ctypes.c_int),  # 密钥编号
        ('CurrentKey', ctypes.c_char * 21),  # 动态密钥
        ('KeyKind', ctypes.c_char),  # 动态密钥类型
    ]

    def __init__(self, BrokerID: str = '', ParticipantID: str = '', CreateDate: str = '', CreateTime: str = '', KeyID: int = 0, CurrentKey: str = '', KeyKind: str = ''):
        super(CFMMCBrokerKeyField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.CreateDate = self._to_bytes(CreateDate)
        self.CreateTime = self._to_bytes(CreateTime)
        self.KeyID = int(KeyID)
        self.CurrentKey = self._to_bytes(CurrentKey)
        self.KeyKind = self._to_bytes(KeyKind)


class CFMMCTradingAccountKeyField(Base):
    """保证金监管系统经纪公司资金账户密钥"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ParticipantID', ctypes.c_char * 11),  # 经纪公司统一编码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('KeyID', ctypes.c_int),  # 密钥编号
        ('CurrentKey', ctypes.c_char * 21),  # 动态密钥
    ]

    def __init__(self, BrokerID: str = '', ParticipantID: str = '', AccountID: str = '', KeyID: int = 0, CurrentKey: str = ''):
        super(CFMMCTradingAccountKeyField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.AccountID = self._to_bytes(AccountID)
        self.KeyID = int(KeyID)
        self.CurrentKey = self._to_bytes(CurrentKey)


class QryCFMMCTradingAccountKeyField(Base):
    """请求查询保证金监管系统经纪公司资金账户密钥"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = ''):
        super(QryCFMMCTradingAccountKeyField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class BrokerUserOTPParamField(Base):
    """用户动态令牌参数"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('OTPVendorsID', ctypes.c_char * 2),  # 动态令牌提供商
        ('SerialNumber', ctypes.c_char * 17),  # 动态令牌序列号
        ('AuthKey', ctypes.c_char * 41),  # 令牌密钥
        ('LastDrift', ctypes.c_int),  # 漂移值
        ('LastSuccess', ctypes.c_int),  # 成功值
        ('OTPType', ctypes.c_char),  # 动态令牌类型
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', OTPVendorsID: str = '', SerialNumber: str = '', AuthKey: str = '', LastDrift: int = 0, LastSuccess: int = 0, OTPType: str = ''):
        super(BrokerUserOTPParamField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.OTPVendorsID = self._to_bytes(OTPVendorsID)
        self.SerialNumber = self._to_bytes(SerialNumber)
        self.AuthKey = self._to_bytes(AuthKey)
        self.LastDrift = int(LastDrift)
        self.LastSuccess = int(LastSuccess)
        self.OTPType = self._to_bytes(OTPType)


class ManualSyncBrokerUserOTPField(Base):
    """手工同步用户动态令牌"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('OTPType', ctypes.c_char),  # 动态令牌类型
        ('FirstOTP', ctypes.c_char * 41),  # 第一个动态密码
        ('SecondOTP', ctypes.c_char * 41),  # 第二个动态密码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', OTPType: str = '', FirstOTP: str = '', SecondOTP: str = ''):
        super(ManualSyncBrokerUserOTPField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.OTPType = self._to_bytes(OTPType)
        self.FirstOTP = self._to_bytes(FirstOTP)
        self.SecondOTP = self._to_bytes(SecondOTP)


class CommRateModelField(Base):
    """投资者手续费率模板"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('CommModelID', ctypes.c_char * 13),  # 手续费率模板代码
        ('CommModelName', ctypes.c_char * 161),  # 模板名称
    ]

    def __init__(self, BrokerID: str = '', CommModelID: str = '', CommModelName: str = ''):
        super(CommRateModelField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.CommModelID = self._to_bytes(CommModelID)
        self.CommModelName = self._to_bytes(CommModelName)


class QryCommRateModelField(Base):
    """请求查询投资者手续费率模板"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('CommModelID', ctypes.c_char * 13),  # 手续费率模板代码
    ]

    def __init__(self, BrokerID: str = '', CommModelID: str = ''):
        super(QryCommRateModelField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.CommModelID = self._to_bytes(CommModelID)


class MarginModelField(Base):
    """投资者保证金率模板"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('MarginModelID', ctypes.c_char * 13),  # 保证金率模板代码
        ('MarginModelName', ctypes.c_char * 161),  # 模板名称
    ]

    def __init__(self, BrokerID: str = '', MarginModelID: str = '', MarginModelName: str = ''):
        super(MarginModelField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.MarginModelID = self._to_bytes(MarginModelID)
        self.MarginModelName = self._to_bytes(MarginModelName)


class QryMarginModelField(Base):
    """请求查询投资者保证金率模板"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('MarginModelID', ctypes.c_char * 13),  # 保证金率模板代码
    ]

    def __init__(self, BrokerID: str = '', MarginModelID: str = ''):
        super(QryMarginModelField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.MarginModelID = self._to_bytes(MarginModelID)


class EWarrantOffsetField(Base):
    """仓单折抵信息"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日期
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('Direction', ctypes.c_char),  # 买卖方向
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('Volume', ctypes.c_int),  # 数量
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', InvestorID: str = '', ExchangeID: str = '', reserve1: str = '', Direction: str = '', HedgeFlag: str = '', Volume: int = 0,
                 InvestUnitID: str = '', InstrumentID: str = ''):
        super(EWarrantOffsetField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve1 = self._to_bytes(reserve1)
        self.Direction = self._to_bytes(Direction)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Volume = int(Volume)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryEWarrantOffsetField(Base):
    """查询仓单折抵信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExchangeID: str = '', reserve1: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        super(QryEWarrantOffsetField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryInvestorProductGroupMarginField(Base):
    """查询投资者品种/跨品种保证金"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('ProductGroupID', ctypes.c_char * 81),  # 品种/跨品种标示
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', HedgeFlag: str = '', ExchangeID: str = '', InvestUnitID: str = '', ProductGroupID: str = ''):
        super(QryInvestorProductGroupMarginField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.reserve1 = self._to_bytes(reserve1)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.ProductGroupID = self._to_bytes(ProductGroupID)


class InvestorProductGroupMarginField(Base):
    """投资者品种/跨品种保证金"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('FrozenMargin', ctypes.c_double),  # 冻结的保证金
        ('LongFrozenMargin', ctypes.c_double),  # 多头冻结的保证金
        ('ShortFrozenMargin', ctypes.c_double),  # 空头冻结的保证金
        ('UseMargin', ctypes.c_double),  # 占用的保证金
        ('LongUseMargin', ctypes.c_double),  # 多头保证金
        ('ShortUseMargin', ctypes.c_double),  # 空头保证金
        ('ExchMargin', ctypes.c_double),  # 交易所保证金
        ('LongExchMargin', ctypes.c_double),  # 交易所多头保证金
        ('ShortExchMargin', ctypes.c_double),  # 交易所空头保证金
        ('CloseProfit', ctypes.c_double),  # 平仓盈亏
        ('FrozenCommission', ctypes.c_double),  # 冻结的手续费
        ('Commission', ctypes.c_double),  # 手续费
        ('FrozenCash', ctypes.c_double),  # 冻结的资金
        ('CashIn', ctypes.c_double),  # 资金差额
        ('PositionProfit', ctypes.c_double),  # 持仓盈亏
        ('OffsetAmount', ctypes.c_double),  # 折抵总金额
        ('LongOffsetAmount', ctypes.c_double),  # 多头折抵总金额
        ('ShortOffsetAmount', ctypes.c_double),  # 空头折抵总金额
        ('ExchOffsetAmount', ctypes.c_double),  # 交易所折抵总金额
        ('LongExchOffsetAmount', ctypes.c_double),  # 交易所多头折抵总金额
        ('ShortExchOffsetAmount', ctypes.c_double),  # 交易所空头折抵总金额
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('ProductGroupID', ctypes.c_char * 81),  # 品种/跨品种标示
    ]

    def __init__(self, reserve1: str = '', BrokerID: str = '', InvestorID: str = '', TradingDay: str = '', SettlementID: int = 0, FrozenMargin: float = 0.0, LongFrozenMargin: float = 0.0,
                 ShortFrozenMargin: float = 0.0, UseMargin: float = 0.0, LongUseMargin: float = 0.0, ShortUseMargin: float = 0.0, ExchMargin: float = 0.0, LongExchMargin: float = 0.0,
                 ShortExchMargin: float = 0.0, CloseProfit: float = 0.0, FrozenCommission: float = 0.0, Commission: float = 0.0, FrozenCash: float = 0.0, CashIn: float = 0.0,
                 PositionProfit: float = 0.0, OffsetAmount: float = 0.0, LongOffsetAmount: float = 0.0, ShortOffsetAmount: float = 0.0, ExchOffsetAmount: float = 0.0,
                 LongExchOffsetAmount: float = 0.0, ShortExchOffsetAmount: float = 0.0, HedgeFlag: str = '', ExchangeID: str = '', InvestUnitID: str = '', ProductGroupID: str = ''):
        super(InvestorProductGroupMarginField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.FrozenMargin = float(FrozenMargin)
        self.LongFrozenMargin = float(LongFrozenMargin)
        self.ShortFrozenMargin = float(ShortFrozenMargin)
        self.UseMargin = float(UseMargin)
        self.LongUseMargin = float(LongUseMargin)
        self.ShortUseMargin = float(ShortUseMargin)
        self.ExchMargin = float(ExchMargin)
        self.LongExchMargin = float(LongExchMargin)
        self.ShortExchMargin = float(ShortExchMargin)
        self.CloseProfit = float(CloseProfit)
        self.FrozenCommission = float(FrozenCommission)
        self.Commission = float(Commission)
        self.FrozenCash = float(FrozenCash)
        self.CashIn = float(CashIn)
        self.PositionProfit = float(PositionProfit)
        self.OffsetAmount = float(OffsetAmount)
        self.LongOffsetAmount = float(LongOffsetAmount)
        self.ShortOffsetAmount = float(ShortOffsetAmount)
        self.ExchOffsetAmount = float(ExchOffsetAmount)
        self.LongExchOffsetAmount = float(LongExchOffsetAmount)
        self.ShortExchOffsetAmount = float(ShortExchOffsetAmount)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.ProductGroupID = self._to_bytes(ProductGroupID)


class QueryCFMMCTradingAccountTokenField(Base):
    """查询监控中心用户令牌"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', InvestUnitID: str = ''):
        super(QueryCFMMCTradingAccountTokenField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)


class CFMMCTradingAccountTokenField(Base):
    """监控中心用户令牌"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('ParticipantID', ctypes.c_char * 11),  # 经纪公司统一编码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('KeyID', ctypes.c_int),  # 密钥编号
        ('Token', ctypes.c_char * 21),  # 动态令牌
    ]

    def __init__(self, BrokerID: str = '', ParticipantID: str = '', AccountID: str = '', KeyID: int = 0, Token: str = ''):
        super(CFMMCTradingAccountTokenField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.AccountID = self._to_bytes(AccountID)
        self.KeyID = int(KeyID)
        self.Token = self._to_bytes(Token)


class QryProductGroupField(Base):
    """查询产品组"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ProductID', ctypes.c_char * 81),  # 产品代码
    ]

    def __init__(self, reserve1: str = '', ExchangeID: str = '', ProductID: str = ''):
        super(QryProductGroupField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProductID = self._to_bytes(ProductID)


class ProductGroupField(Base):
    """投资者品种/跨品种保证金产品组"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('reserve2', ctypes.c_char * 31),  # 保留的无效字段
        ('ProductID', ctypes.c_char * 81),  # 产品代码
        ('ProductGroupID', ctypes.c_char * 81),  # 产品组代码
    ]

    def __init__(self, reserve1: str = '', ExchangeID: str = '', reserve2: str = '', ProductID: str = '', ProductGroupID: str = ''):
        super(ProductGroupField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.reserve2 = self._to_bytes(reserve2)
        self.ProductID = self._to_bytes(ProductID)
        self.ProductGroupID = self._to_bytes(ProductGroupID)


class BulletinField(Base):
    """交易所公告"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BulletinID', ctypes.c_int),  # 公告编号
        ('SequenceNo', ctypes.c_int),  # 序列号
        ('NewsType', ctypes.c_char * 3),  # 公告类型
        ('NewsUrgency', ctypes.c_char),  # 紧急程度
        ('SendTime', ctypes.c_char * 9),  # 发送时间
        ('Abstract', ctypes.c_char * 81),  # 消息摘要
        ('ComeFrom', ctypes.c_char * 21),  # 消息来源
        ('Content', ctypes.c_char * 501),  # 消息正文
        ('URLLink', ctypes.c_char * 201),  # WEB地址
        ('MarketID', ctypes.c_char * 31),  # 市场代码
    ]

    def __init__(self, ExchangeID: str = '', TradingDay: str = '', BulletinID: int = 0, SequenceNo: int = 0, NewsType: str = '', NewsUrgency: str = '', SendTime: str = '', Abstract: str = '',
                 ComeFrom: str = '', Content: str = '', URLLink: str = '', MarketID: str = ''):
        super(BulletinField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TradingDay = self._to_bytes(TradingDay)
        self.BulletinID = int(BulletinID)
        self.SequenceNo = int(SequenceNo)
        self.NewsType = self._to_bytes(NewsType)
        self.NewsUrgency = self._to_bytes(NewsUrgency)
        self.SendTime = self._to_bytes(SendTime)
        self.Abstract = self._to_bytes(Abstract)
        self.ComeFrom = self._to_bytes(ComeFrom)
        self.Content = self._to_bytes(Content)
        self.URLLink = self._to_bytes(URLLink)
        self.MarketID = self._to_bytes(MarketID)


class QryBulletinField(Base):
    """查询交易所公告"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('BulletinID', ctypes.c_int),  # 公告编号
        ('SequenceNo', ctypes.c_int),  # 序列号
        ('NewsType', ctypes.c_char * 3),  # 公告类型
        ('NewsUrgency', ctypes.c_char),  # 紧急程度
    ]

    def __init__(self, ExchangeID: str = '', BulletinID: int = 0, SequenceNo: int = 0, NewsType: str = '', NewsUrgency: str = ''):
        super(QryBulletinField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.BulletinID = int(BulletinID)
        self.SequenceNo = int(SequenceNo)
        self.NewsType = self._to_bytes(NewsType)
        self.NewsUrgency = self._to_bytes(NewsUrgency)


class MulticastInstrumentField(Base):
    """MulticastInstrument"""
    _fields_ = [
        ('TopicID', ctypes.c_int),  # 主题号
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentNo', ctypes.c_int),  # 合约编号
        ('CodePrice', ctypes.c_double),  # 基准价
        ('VolumeMultiple', ctypes.c_int),  # 合约数量乘数
        ('PriceTick', ctypes.c_double),  # 最小变动价位
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, TopicID: int = 0, reserve1: str = '', InstrumentNo: int = 0, CodePrice: float = 0.0, VolumeMultiple: int = 0, PriceTick: float = 0.0, InstrumentID: str = ''):
        super(MulticastInstrumentField, self).__init__()
        self.TopicID = int(TopicID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InstrumentNo = int(InstrumentNo)
        self.CodePrice = float(CodePrice)
        self.VolumeMultiple = int(VolumeMultiple)
        self.PriceTick = float(PriceTick)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryMulticastInstrumentField(Base):
    """QryMulticastInstrument"""
    _fields_ = [
        ('TopicID', ctypes.c_int),  # 主题号
        ('reserve1', ctypes.c_char * 31),  # 保留的无效字段
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, TopicID: int = 0, reserve1: str = '', InstrumentID: str = ''):
        super(QryMulticastInstrumentField, self).__init__()
        self.TopicID = int(TopicID)
        self.reserve1 = self._to_bytes(reserve1)
        self.InstrumentID = self._to_bytes(InstrumentID)


class AppIDAuthAssignField(Base):
    """App客户端权限分配"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AppID', ctypes.c_char * 33),  # App代码
        ('DRIdentityID', ctypes.c_int),  # 交易中心代码
    ]

    def __init__(self, BrokerID: str = '', AppID: str = '', DRIdentityID: int = 0):
        super(AppIDAuthAssignField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AppID = self._to_bytes(AppID)
        self.DRIdentityID = int(DRIdentityID)


class ReqOpenAccountField(Base):
    """转帐开户请求"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('Gender', ctypes.c_char),  # 性别
        ('CountryCode', ctypes.c_char * 21),  # 国家代码
        ('CustType', ctypes.c_char),  # 客户类型
        ('Address', ctypes.c_char * 101),  # 地址
        ('ZipCode', ctypes.c_char * 7),  # 邮编
        ('Telephone', ctypes.c_char * 41),  # 电话号码
        ('MobilePhone', ctypes.c_char * 21),  # 手机
        ('Fax', ctypes.c_char * 41),  # 传真
        ('EMail', ctypes.c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', ctypes.c_char),  # 资金账户状态
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('CashExchangeCode', ctypes.c_char),  # 汇钞标志
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('TID', ctypes.c_int),  # 交易ID
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', Gender: str = '',
                 CountryCode: str = '', CustType: str = '', Address: str = '', ZipCode: str = '', Telephone: str = '', MobilePhone: str = '', Fax: str = '', EMail: str = '',
                 MoneyAccountStatus: str = '', BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', InstallID: int = 0, VerifyCertNoFlag: str = '',
                 CurrencyID: str = '', CashExchangeCode: str = '', Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '',
                 BankSecuAcc: str = '', BankPwdFlag: str = '', SecuPwdFlag: str = '', OperNo: str = '', TID: int = 0, UserID: str = '', LongCustomerName: str = ''):
        super(ReqOpenAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.CashExchangeCode = self._to_bytes(CashExchangeCode)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.TID = int(TID)
        self.UserID = self._to_bytes(UserID)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ReqCancelAccountField(Base):
    """转帐销户请求"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('Gender', ctypes.c_char),  # 性别
        ('CountryCode', ctypes.c_char * 21),  # 国家代码
        ('CustType', ctypes.c_char),  # 客户类型
        ('Address', ctypes.c_char * 101),  # 地址
        ('ZipCode', ctypes.c_char * 7),  # 邮编
        ('Telephone', ctypes.c_char * 41),  # 电话号码
        ('MobilePhone', ctypes.c_char * 21),  # 手机
        ('Fax', ctypes.c_char * 41),  # 传真
        ('EMail', ctypes.c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', ctypes.c_char),  # 资金账户状态
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('CashExchangeCode', ctypes.c_char),  # 汇钞标志
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('TID', ctypes.c_int),  # 交易ID
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', Gender: str = '',
                 CountryCode: str = '', CustType: str = '', Address: str = '', ZipCode: str = '', Telephone: str = '', MobilePhone: str = '', Fax: str = '', EMail: str = '',
                 MoneyAccountStatus: str = '', BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', InstallID: int = 0, VerifyCertNoFlag: str = '',
                 CurrencyID: str = '', CashExchangeCode: str = '', Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '',
                 BankSecuAcc: str = '', BankPwdFlag: str = '', SecuPwdFlag: str = '', OperNo: str = '', TID: int = 0, UserID: str = '', LongCustomerName: str = ''):
        super(ReqCancelAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.CashExchangeCode = self._to_bytes(CashExchangeCode)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.TID = int(TID)
        self.UserID = self._to_bytes(UserID)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ReqChangeAccountField(Base):
    """变更银行账户请求"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('Gender', ctypes.c_char),  # 性别
        ('CountryCode', ctypes.c_char * 21),  # 国家代码
        ('CustType', ctypes.c_char),  # 客户类型
        ('Address', ctypes.c_char * 101),  # 地址
        ('ZipCode', ctypes.c_char * 7),  # 邮编
        ('Telephone', ctypes.c_char * 41),  # 电话号码
        ('MobilePhone', ctypes.c_char * 21),  # 手机
        ('Fax', ctypes.c_char * 41),  # 传真
        ('EMail', ctypes.c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', ctypes.c_char),  # 资金账户状态
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('NewBankAccount', ctypes.c_char * 41),  # 新银行帐号
        ('NewBankPassWord', ctypes.c_char * 41),  # 新银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('InstallID', ctypes.c_int),  # 安装编号
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('TID', ctypes.c_int),  # 交易ID
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', Gender: str = '',
                 CountryCode: str = '', CustType: str = '', Address: str = '', ZipCode: str = '', Telephone: str = '', MobilePhone: str = '', Fax: str = '', EMail: str = '',
                 MoneyAccountStatus: str = '', BankAccount: str = '', BankPassWord: str = '', NewBankAccount: str = '', NewBankPassWord: str = '', AccountID: str = '', Password: str = '',
                 BankAccType: str = '', InstallID: int = 0, VerifyCertNoFlag: str = '', CurrencyID: str = '', BrokerIDByBank: str = '', BankPwdFlag: str = '', SecuPwdFlag: str = '', TID: int = 0,
                 Digest: str = '', LongCustomerName: str = ''):
        super(ReqChangeAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.NewBankAccount = self._to_bytes(NewBankAccount)
        self.NewBankPassWord = self._to_bytes(NewBankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.BankAccType = self._to_bytes(BankAccType)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.TID = int(TID)
        self.Digest = self._to_bytes(Digest)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ReqTransferField(Base):
    """转账请求"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustType', ctypes.c_char),  # 客户类型
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('FutureSerial', ctypes.c_int),  # 期货公司流水号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('TradeAmount', ctypes.c_double),  # 转帐金额
        ('FutureFetchAmount', ctypes.c_double),  # 期货可取金额
        ('FeePayFlag', ctypes.c_char),  # 费用支付标志
        ('CustFee', ctypes.c_double),  # 应收客户费用
        ('BrokerFee', ctypes.c_double),  # 应收期货公司费用
        ('Message', ctypes.c_char * 129),  # 发送方给接收方的消息
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('TransferStatus', ctypes.c_char),  # 转账交易状态
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', CustType: str = '',
                 BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', InstallID: int = 0, FutureSerial: int = 0, UserID: str = '', VerifyCertNoFlag: str = '',
                 CurrencyID: str = '', TradeAmount: float = 0.0, FutureFetchAmount: float = 0.0, FeePayFlag: str = '', CustFee: float = 0.0, BrokerFee: float = 0.0, Message: str = '',
                 Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '', BankSecuAcc: str = '', BankPwdFlag: str = '', SecuPwdFlag: str = '',
                 OperNo: str = '', RequestID: int = 0, TID: int = 0, TransferStatus: str = '', LongCustomerName: str = ''):
        super(ReqTransferField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = self._to_bytes(FeePayFlag)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = self._to_bytes(Message)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = self._to_bytes(TransferStatus)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class RspTransferField(Base):
    """银行发起银行资金转期货响应"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustType', ctypes.c_char),  # 客户类型
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('FutureSerial', ctypes.c_int),  # 期货公司流水号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('TradeAmount', ctypes.c_double),  # 转帐金额
        ('FutureFetchAmount', ctypes.c_double),  # 期货可取金额
        ('FeePayFlag', ctypes.c_char),  # 费用支付标志
        ('CustFee', ctypes.c_double),  # 应收客户费用
        ('BrokerFee', ctypes.c_double),  # 应收期货公司费用
        ('Message', ctypes.c_char * 129),  # 发送方给接收方的消息
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('TransferStatus', ctypes.c_char),  # 转账交易状态
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', CustType: str = '',
                 BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', InstallID: int = 0, FutureSerial: int = 0, UserID: str = '', VerifyCertNoFlag: str = '',
                 CurrencyID: str = '', TradeAmount: float = 0.0, FutureFetchAmount: float = 0.0, FeePayFlag: str = '', CustFee: float = 0.0, BrokerFee: float = 0.0, Message: str = '',
                 Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '', BankSecuAcc: str = '', BankPwdFlag: str = '', SecuPwdFlag: str = '',
                 OperNo: str = '', RequestID: int = 0, TID: int = 0, TransferStatus: str = '', ErrorID: int = 0, ErrorMsg: str = '', LongCustomerName: str = ''):
        super(RspTransferField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = self._to_bytes(FeePayFlag)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = self._to_bytes(Message)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = self._to_bytes(TransferStatus)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ReqRepealField(Base):
    """冲正请求"""
    _fields_ = [
        ('RepealTimeInterval', ctypes.c_int),  # 冲正时间间隔
        ('RepealedTimes', ctypes.c_int),  # 已经冲正次数
        ('BankRepealFlag', ctypes.c_char),  # 银行冲正标志
        ('BrokerRepealFlag', ctypes.c_char),  # 期商冲正标志
        ('PlateRepealSerial', ctypes.c_int),  # 被冲正平台流水号
        ('BankRepealSerial', ctypes.c_char * 13),  # 被冲正银行流水号
        ('FutureRepealSerial', ctypes.c_int),  # 被冲正期货流水号
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustType', ctypes.c_char),  # 客户类型
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('FutureSerial', ctypes.c_int),  # 期货公司流水号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('TradeAmount', ctypes.c_double),  # 转帐金额
        ('FutureFetchAmount', ctypes.c_double),  # 期货可取金额
        ('FeePayFlag', ctypes.c_char),  # 费用支付标志
        ('CustFee', ctypes.c_double),  # 应收客户费用
        ('BrokerFee', ctypes.c_double),  # 应收期货公司费用
        ('Message', ctypes.c_char * 129),  # 发送方给接收方的消息
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('TransferStatus', ctypes.c_char),  # 转账交易状态
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, RepealTimeInterval: int = 0, RepealedTimes: int = 0, BankRepealFlag: str = '', BrokerRepealFlag: str = '', PlateRepealSerial: int = 0, BankRepealSerial: str = '',
                 FutureRepealSerial: int = 0, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '',
                 BankSerial: str = '', TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '',
                 CustType: str = '', BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', InstallID: int = 0, FutureSerial: int = 0, UserID: str = '',
                 VerifyCertNoFlag: str = '', CurrencyID: str = '', TradeAmount: float = 0.0, FutureFetchAmount: float = 0.0, FeePayFlag: str = '', CustFee: float = 0.0, BrokerFee: float = 0.0,
                 Message: str = '', Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '', BankSecuAcc: str = '', BankPwdFlag: str = '',
                 SecuPwdFlag: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, TransferStatus: str = '', LongCustomerName: str = ''):
        super(ReqRepealField, self).__init__()
        self.RepealTimeInterval = int(RepealTimeInterval)
        self.RepealedTimes = int(RepealedTimes)
        self.BankRepealFlag = self._to_bytes(BankRepealFlag)
        self.BrokerRepealFlag = self._to_bytes(BrokerRepealFlag)
        self.PlateRepealSerial = int(PlateRepealSerial)
        self.BankRepealSerial = self._to_bytes(BankRepealSerial)
        self.FutureRepealSerial = int(FutureRepealSerial)
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = self._to_bytes(FeePayFlag)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = self._to_bytes(Message)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = self._to_bytes(TransferStatus)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class RspRepealField(Base):
    """冲正响应"""
    _fields_ = [
        ('RepealTimeInterval', ctypes.c_int),  # 冲正时间间隔
        ('RepealedTimes', ctypes.c_int),  # 已经冲正次数
        ('BankRepealFlag', ctypes.c_char),  # 银行冲正标志
        ('BrokerRepealFlag', ctypes.c_char),  # 期商冲正标志
        ('PlateRepealSerial', ctypes.c_int),  # 被冲正平台流水号
        ('BankRepealSerial', ctypes.c_char * 13),  # 被冲正银行流水号
        ('FutureRepealSerial', ctypes.c_int),  # 被冲正期货流水号
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustType', ctypes.c_char),  # 客户类型
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('FutureSerial', ctypes.c_int),  # 期货公司流水号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('TradeAmount', ctypes.c_double),  # 转帐金额
        ('FutureFetchAmount', ctypes.c_double),  # 期货可取金额
        ('FeePayFlag', ctypes.c_char),  # 费用支付标志
        ('CustFee', ctypes.c_double),  # 应收客户费用
        ('BrokerFee', ctypes.c_double),  # 应收期货公司费用
        ('Message', ctypes.c_char * 129),  # 发送方给接收方的消息
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('TransferStatus', ctypes.c_char),  # 转账交易状态
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, RepealTimeInterval: int = 0, RepealedTimes: int = 0, BankRepealFlag: str = '', BrokerRepealFlag: str = '', PlateRepealSerial: int = 0, BankRepealSerial: str = '',
                 FutureRepealSerial: int = 0, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '',
                 BankSerial: str = '', TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '',
                 CustType: str = '', BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', InstallID: int = 0, FutureSerial: int = 0, UserID: str = '',
                 VerifyCertNoFlag: str = '', CurrencyID: str = '', TradeAmount: float = 0.0, FutureFetchAmount: float = 0.0, FeePayFlag: str = '', CustFee: float = 0.0, BrokerFee: float = 0.0,
                 Message: str = '', Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '', BankSecuAcc: str = '', BankPwdFlag: str = '',
                 SecuPwdFlag: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, TransferStatus: str = '', ErrorID: int = 0, ErrorMsg: str = '', LongCustomerName: str = ''):
        super(RspRepealField, self).__init__()
        self.RepealTimeInterval = int(RepealTimeInterval)
        self.RepealedTimes = int(RepealedTimes)
        self.BankRepealFlag = self._to_bytes(BankRepealFlag)
        self.BrokerRepealFlag = self._to_bytes(BrokerRepealFlag)
        self.PlateRepealSerial = int(PlateRepealSerial)
        self.BankRepealSerial = self._to_bytes(BankRepealSerial)
        self.FutureRepealSerial = int(FutureRepealSerial)
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = self._to_bytes(FeePayFlag)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = self._to_bytes(Message)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = self._to_bytes(TransferStatus)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ReqQueryAccountField(Base):
    """查询账户信息请求"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustType', ctypes.c_char),  # 客户类型
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('FutureSerial', ctypes.c_int),  # 期货公司流水号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', CustType: str = '',
                 BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', FutureSerial: int = 0, InstallID: int = 0, UserID: str = '', VerifyCertNoFlag: str = '',
                 CurrencyID: str = '', Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '', BankSecuAcc: str = '', BankPwdFlag: str = '',
                 SecuPwdFlag: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, LongCustomerName: str = ''):
        super(ReqQueryAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.FutureSerial = int(FutureSerial)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class RspQueryAccountField(Base):
    """查询账户信息响应"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustType', ctypes.c_char),  # 客户类型
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('FutureSerial', ctypes.c_int),  # 期货公司流水号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('BankUseAmount', ctypes.c_double),  # 银行可用金额
        ('BankFetchAmount', ctypes.c_double),  # 银行可取金额
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', CustType: str = '',
                 BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', FutureSerial: int = 0, InstallID: int = 0, UserID: str = '', VerifyCertNoFlag: str = '',
                 CurrencyID: str = '', Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '', BankSecuAcc: str = '', BankPwdFlag: str = '',
                 SecuPwdFlag: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, BankUseAmount: float = 0.0, BankFetchAmount: float = 0.0, LongCustomerName: str = ''):
        super(RspQueryAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.FutureSerial = int(FutureSerial)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.BankUseAmount = float(BankUseAmount)
        self.BankFetchAmount = float(BankFetchAmount)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class FutureSignIOField(Base):
    """期商签到签退"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, InstallID: int = 0, UserID: str = '', Digest: str = '', CurrencyID: str = '',
                 DeviceID: str = '', BrokerIDByBank: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0):
        super(FutureSignIOField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)


class RspFutureSignInField(Base):
    """期商签到响应"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('PinKey', ctypes.c_char * 129),  # PIN密钥
        ('MacKey', ctypes.c_char * 129),  # MAC密钥
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, InstallID: int = 0, UserID: str = '', Digest: str = '', CurrencyID: str = '',
                 DeviceID: str = '', BrokerIDByBank: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, ErrorID: int = 0, ErrorMsg: str = '', PinKey: str = '', MacKey: str = ''):
        super(RspFutureSignInField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.PinKey = self._to_bytes(PinKey)
        self.MacKey = self._to_bytes(MacKey)


class ReqFutureSignOutField(Base):
    """期商签退请求"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, InstallID: int = 0, UserID: str = '', Digest: str = '', CurrencyID: str = '',
                 DeviceID: str = '', BrokerIDByBank: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0):
        super(ReqFutureSignOutField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)


class RspFutureSignOutField(Base):
    """期商签退响应"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, InstallID: int = 0, UserID: str = '', Digest: str = '', CurrencyID: str = '',
                 DeviceID: str = '', BrokerIDByBank: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, ErrorID: int = 0, ErrorMsg: str = ''):
        super(RspFutureSignOutField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class ReqQueryTradeResultBySerialField(Base):
    """查询指定流水号的交易结果请求"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('Reference', ctypes.c_int),  # 流水号
        ('RefrenceIssureType', ctypes.c_char),  # 本流水号发布者的机构类型
        ('RefrenceIssure', ctypes.c_char * 36),  # 本流水号发布者机构编码
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustType', ctypes.c_char),  # 客户类型
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('TradeAmount', ctypes.c_double),  # 转帐金额
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, Reference: int = 0, RefrenceIssureType: str = '', RefrenceIssure: str = '',
                 CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', CustType: str = '', BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '',
                 CurrencyID: str = '', TradeAmount: float = 0.0, Digest: str = '', LongCustomerName: str = ''):
        super(ReqQueryTradeResultBySerialField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.Reference = int(Reference)
        self.RefrenceIssureType = self._to_bytes(RefrenceIssureType)
        self.RefrenceIssure = self._to_bytes(RefrenceIssure)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.Digest = self._to_bytes(Digest)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class RspQueryTradeResultBySerialField(Base):
    """查询指定流水号的交易结果响应"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('Reference', ctypes.c_int),  # 流水号
        ('RefrenceIssureType', ctypes.c_char),  # 本流水号发布者的机构类型
        ('RefrenceIssure', ctypes.c_char * 36),  # 本流水号发布者机构编码
        ('OriginReturnCode', ctypes.c_char * 7),  # 原始返回代码
        ('OriginDescrInfoForReturnCode', ctypes.c_char * 129),  # 原始返回码描述
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('TradeAmount', ctypes.c_double),  # 转帐金额
        ('Digest', ctypes.c_char * 36),  # 摘要
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, ErrorID: int = 0, ErrorMsg: str = '', Reference: int = 0, RefrenceIssureType: str = '',
                 RefrenceIssure: str = '', OriginReturnCode: str = '', OriginDescrInfoForReturnCode: str = '', BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '',
                 CurrencyID: str = '', TradeAmount: float = 0.0, Digest: str = ''):
        super(RspQueryTradeResultBySerialField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.Reference = int(Reference)
        self.RefrenceIssureType = self._to_bytes(RefrenceIssureType)
        self.RefrenceIssure = self._to_bytes(RefrenceIssure)
        self.OriginReturnCode = self._to_bytes(OriginReturnCode)
        self.OriginDescrInfoForReturnCode = self._to_bytes(OriginDescrInfoForReturnCode)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.Digest = self._to_bytes(Digest)


class ReqDayEndFileReadyField(Base):
    """日终文件就绪请求"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('FileBusinessCode', ctypes.c_char),  # 文件业务功能
        ('Digest', ctypes.c_char * 36),  # 摘要
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, FileBusinessCode: str = '', Digest: str = ''):
        super(ReqDayEndFileReadyField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.FileBusinessCode = self._to_bytes(FileBusinessCode)
        self.Digest = self._to_bytes(Digest)


class ReturnResultField(Base):
    """返回结果"""
    _fields_ = [
        ('ReturnCode', ctypes.c_char * 7),  # 返回代码
        ('DescrInfoForReturnCode', ctypes.c_char * 129),  # 返回码描述
    ]

    def __init__(self, ReturnCode: str = '', DescrInfoForReturnCode: str = ''):
        super(ReturnResultField, self).__init__()
        self.ReturnCode = self._to_bytes(ReturnCode)
        self.DescrInfoForReturnCode = self._to_bytes(DescrInfoForReturnCode)


class VerifyFuturePasswordField(Base):
    """验证期货资金密码"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('TID', ctypes.c_int),  # 交易ID
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, AccountID: str = '', Password: str = '', BankAccount: str = '', BankPassWord: str = '',
                 InstallID: int = 0, TID: int = 0, CurrencyID: str = ''):
        super(VerifyFuturePasswordField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.InstallID = int(InstallID)
        self.TID = int(TID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class VerifyCustInfoField(Base):
    """验证客户信息"""
    _fields_ = [
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustType', ctypes.c_char),  # 客户类型
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', CustType: str = '', LongCustomerName: str = ''):
        super(VerifyCustInfoField, self).__init__()
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class VerifyFuturePasswordAndCustInfoField(Base):
    """验证期货资金密码和客户信息"""
    _fields_ = [
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustType', ctypes.c_char),  # 客户类型
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', CustType: str = '', AccountID: str = '', Password: str = '', CurrencyID: str = '',
                 LongCustomerName: str = ''):
        super(VerifyFuturePasswordAndCustInfoField, self).__init__()
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class DepositResultInformField(Base):
    """验证期货资金密码和客户信息"""
    _fields_ = [
        ('DepositSeqNo', ctypes.c_char * 15),  # 出入金流水号，该流水号为银期报盘返回的流水号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('Deposit', ctypes.c_double),  # 入金金额
        ('RequestID', ctypes.c_int),  # 请求编号
        ('ReturnCode', ctypes.c_char * 7),  # 返回代码
        ('DescrInfoForReturnCode', ctypes.c_char * 129),  # 返回码描述
    ]

    def __init__(self, DepositSeqNo: str = '', BrokerID: str = '', InvestorID: str = '', Deposit: float = 0.0, RequestID: int = 0, ReturnCode: str = '', DescrInfoForReturnCode: str = ''):
        super(DepositResultInformField, self).__init__()
        self.DepositSeqNo = self._to_bytes(DepositSeqNo)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Deposit = float(Deposit)
        self.RequestID = int(RequestID)
        self.ReturnCode = self._to_bytes(ReturnCode)
        self.DescrInfoForReturnCode = self._to_bytes(DescrInfoForReturnCode)


class ReqSyncKeyField(Base):
    """交易核心向银期报盘发出密钥同步请求"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('Message', ctypes.c_char * 129),  # 交易核心给银期报盘的消息
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, InstallID: int = 0, UserID: str = '', Message: str = '', DeviceID: str = '',
                 BrokerIDByBank: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0):
        super(ReqSyncKeyField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Message = self._to_bytes(Message)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)


class RspSyncKeyField(Base):
    """交易核心向银期报盘发出密钥同步响应"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('Message', ctypes.c_char * 129),  # 交易核心给银期报盘的消息
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, InstallID: int = 0, UserID: str = '', Message: str = '', DeviceID: str = '',
                 BrokerIDByBank: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, ErrorID: int = 0, ErrorMsg: str = ''):
        super(RspSyncKeyField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Message = self._to_bytes(Message)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class NotifyQueryAccountField(Base):
    """查询账户信息通知"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustType', ctypes.c_char),  # 客户类型
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('FutureSerial', ctypes.c_int),  # 期货公司流水号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('BankUseAmount', ctypes.c_double),  # 银行可用金额
        ('BankFetchAmount', ctypes.c_double),  # 银行可取金额
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', CustType: str = '',
                 BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', FutureSerial: int = 0, InstallID: int = 0, UserID: str = '', VerifyCertNoFlag: str = '',
                 CurrencyID: str = '', Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '', BankSecuAcc: str = '', BankPwdFlag: str = '',
                 SecuPwdFlag: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, BankUseAmount: float = 0.0, BankFetchAmount: float = 0.0, ErrorID: int = 0, ErrorMsg: str = '',
                 LongCustomerName: str = ''):
        super(NotifyQueryAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.FutureSerial = int(FutureSerial)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.BankUseAmount = float(BankUseAmount)
        self.BankFetchAmount = float(BankFetchAmount)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class TransferSerialField(Base):
    """银期转账交易流水表"""
    _fields_ = [
        ('PlateSerial', ctypes.c_int),  # 平台流水号
        ('TradeDate', ctypes.c_char * 9),  # 交易发起方日期
        ('TradingDay', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('TradeCode', ctypes.c_char * 7),  # 交易代码
        ('SessionID', ctypes.c_int),  # 会话编号
        ('BankID', ctypes.c_char * 4),  # 银行编码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构编码
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('BrokerID', ctypes.c_char * 11),  # 期货公司编码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('FutureAccType', ctypes.c_char),  # 期货公司帐号类型
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('FutureSerial', ctypes.c_int),  # 期货公司流水号
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('TradeAmount', ctypes.c_double),  # 交易金额
        ('CustFee', ctypes.c_double),  # 应收客户费用
        ('BrokerFee', ctypes.c_double),  # 应收期货公司费用
        ('AvailabilityFlag', ctypes.c_char),  # 有效标志
        ('OperatorCode', ctypes.c_char * 17),  # 操作员
        ('BankNewAccount', ctypes.c_char * 41),  # 新银行帐号
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
    ]

    def __init__(self, PlateSerial: int = 0, TradeDate: str = '', TradingDay: str = '', TradeTime: str = '', TradeCode: str = '', SessionID: int = 0, BankID: str = '', BankBranchID: str = '',
                 BankAccType: str = '', BankAccount: str = '', BankSerial: str = '', BrokerID: str = '', BrokerBranchID: str = '', FutureAccType: str = '', AccountID: str = '', InvestorID: str = '',
                 FutureSerial: int = 0, IdCardType: str = '', IdentifiedCardNo: str = '', CurrencyID: str = '', TradeAmount: float = 0.0, CustFee: float = 0.0, BrokerFee: float = 0.0,
                 AvailabilityFlag: str = '', OperatorCode: str = '', BankNewAccount: str = '', ErrorID: int = 0, ErrorMsg: str = ''):
        super(TransferSerialField, self).__init__()
        self.PlateSerial = int(PlateSerial)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradingDay = self._to_bytes(TradingDay)
        self.TradeTime = self._to_bytes(TradeTime)
        self.TradeCode = self._to_bytes(TradeCode)
        self.SessionID = int(SessionID)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BankAccType = self._to_bytes(BankAccType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankSerial = self._to_bytes(BankSerial)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.FutureAccType = self._to_bytes(FutureAccType)
        self.AccountID = self._to_bytes(AccountID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.FutureSerial = int(FutureSerial)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.AvailabilityFlag = self._to_bytes(AvailabilityFlag)
        self.OperatorCode = self._to_bytes(OperatorCode)
        self.BankNewAccount = self._to_bytes(BankNewAccount)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class QryTransferSerialField(Base):
    """请求查询转帐流水"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('BankID', ctypes.c_char * 4),  # 银行编码
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', AccountID: str = '', BankID: str = '', CurrencyID: str = ''):
        super(QryTransferSerialField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.BankID = self._to_bytes(BankID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class NotifyFutureSignInField(Base):
    """期商签到通知"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('PinKey', ctypes.c_char * 129),  # PIN密钥
        ('MacKey', ctypes.c_char * 129),  # MAC密钥
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, InstallID: int = 0, UserID: str = '', Digest: str = '', CurrencyID: str = '',
                 DeviceID: str = '', BrokerIDByBank: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, ErrorID: int = 0, ErrorMsg: str = '', PinKey: str = '', MacKey: str = ''):
        super(NotifyFutureSignInField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.PinKey = self._to_bytes(PinKey)
        self.MacKey = self._to_bytes(MacKey)


class NotifyFutureSignOutField(Base):
    """期商签退通知"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, InstallID: int = 0, UserID: str = '', Digest: str = '', CurrencyID: str = '',
                 DeviceID: str = '', BrokerIDByBank: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, ErrorID: int = 0, ErrorMsg: str = ''):
        super(NotifyFutureSignOutField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class NotifySyncKeyField(Base):
    """交易核心向银期报盘发出密钥同步处理结果的通知"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('InstallID', ctypes.c_int),  # 安装编号
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('Message', ctypes.c_char * 129),  # 交易核心给银期报盘的消息
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('RequestID', ctypes.c_int),  # 请求编号
        ('TID', ctypes.c_int),  # 交易ID
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, InstallID: int = 0, UserID: str = '', Message: str = '', DeviceID: str = '',
                 BrokerIDByBank: str = '', OperNo: str = '', RequestID: int = 0, TID: int = 0, ErrorID: int = 0, ErrorMsg: str = ''):
        super(NotifySyncKeyField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Message = self._to_bytes(Message)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class QryAccountregisterField(Base):
    """请求查询银期签约关系"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('BankID', ctypes.c_char * 4),  # 银行编码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构编码
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', AccountID: str = '', BankID: str = '', BankBranchID: str = '', CurrencyID: str = ''):
        super(QryAccountregisterField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class AccountregisterField(Base):
    """客户开销户信息表"""
    _fields_ = [
        ('TradeDay', ctypes.c_char * 9),  # 交易日期
        ('BankID', ctypes.c_char * 4),  # 银行编码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构编码
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BrokerID', ctypes.c_char * 11),  # 期货公司编码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期货公司分支机构编码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('OpenOrDestroy', ctypes.c_char),  # 开销户类别
        ('RegDate', ctypes.c_char * 9),  # 签约日期
        ('OutDate', ctypes.c_char * 9),  # 解约日期
        ('TID', ctypes.c_int),  # 交易ID
        ('CustType', ctypes.c_char),  # 客户类型
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeDay: str = '', BankID: str = '', BankBranchID: str = '', BankAccount: str = '', BrokerID: str = '', BrokerBranchID: str = '', AccountID: str = '', IdCardType: str = '',
                 IdentifiedCardNo: str = '', CustomerName: str = '', CurrencyID: str = '', OpenOrDestroy: str = '', RegDate: str = '', OutDate: str = '', TID: int = 0, CustType: str = '',
                 BankAccType: str = '', LongCustomerName: str = ''):
        super(AccountregisterField, self).__init__()
        self.TradeDay = self._to_bytes(TradeDay)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.AccountID = self._to_bytes(AccountID)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustomerName = self._to_bytes(CustomerName)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.OpenOrDestroy = self._to_bytes(OpenOrDestroy)
        self.RegDate = self._to_bytes(RegDate)
        self.OutDate = self._to_bytes(OutDate)
        self.TID = int(TID)
        self.CustType = self._to_bytes(CustType)
        self.BankAccType = self._to_bytes(BankAccType)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class OpenAccountField(Base):
    """银期开户信息"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('Gender', ctypes.c_char),  # 性别
        ('CountryCode', ctypes.c_char * 21),  # 国家代码
        ('CustType', ctypes.c_char),  # 客户类型
        ('Address', ctypes.c_char * 101),  # 地址
        ('ZipCode', ctypes.c_char * 7),  # 邮编
        ('Telephone', ctypes.c_char * 41),  # 电话号码
        ('MobilePhone', ctypes.c_char * 21),  # 手机
        ('Fax', ctypes.c_char * 41),  # 传真
        ('EMail', ctypes.c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', ctypes.c_char),  # 资金账户状态
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('CashExchangeCode', ctypes.c_char),  # 汇钞标志
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('TID', ctypes.c_int),  # 交易ID
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', Gender: str = '',
                 CountryCode: str = '', CustType: str = '', Address: str = '', ZipCode: str = '', Telephone: str = '', MobilePhone: str = '', Fax: str = '', EMail: str = '',
                 MoneyAccountStatus: str = '', BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', InstallID: int = 0, VerifyCertNoFlag: str = '',
                 CurrencyID: str = '', CashExchangeCode: str = '', Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '',
                 BankSecuAcc: str = '', BankPwdFlag: str = '', SecuPwdFlag: str = '', OperNo: str = '', TID: int = 0, UserID: str = '', ErrorID: int = 0, ErrorMsg: str = '',
                 LongCustomerName: str = ''):
        super(OpenAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.CashExchangeCode = self._to_bytes(CashExchangeCode)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.TID = int(TID)
        self.UserID = self._to_bytes(UserID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class CancelAccountField(Base):
    """银期销户信息"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('Gender', ctypes.c_char),  # 性别
        ('CountryCode', ctypes.c_char * 21),  # 国家代码
        ('CustType', ctypes.c_char),  # 客户类型
        ('Address', ctypes.c_char * 101),  # 地址
        ('ZipCode', ctypes.c_char * 7),  # 邮编
        ('Telephone', ctypes.c_char * 41),  # 电话号码
        ('MobilePhone', ctypes.c_char * 21),  # 手机
        ('Fax', ctypes.c_char * 41),  # 传真
        ('EMail', ctypes.c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', ctypes.c_char),  # 资金账户状态
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('CashExchangeCode', ctypes.c_char),  # 汇钞标志
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('DeviceID', ctypes.c_char * 3),  # 渠道标志
        ('BankSecuAccType', ctypes.c_char),  # 期货单位帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', ctypes.c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('OperNo', ctypes.c_char * 17),  # 交易柜员
        ('TID', ctypes.c_int),  # 交易ID
        ('UserID', ctypes.c_char * 16),  # 用户标识
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', Gender: str = '',
                 CountryCode: str = '', CustType: str = '', Address: str = '', ZipCode: str = '', Telephone: str = '', MobilePhone: str = '', Fax: str = '', EMail: str = '',
                 MoneyAccountStatus: str = '', BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', InstallID: int = 0, VerifyCertNoFlag: str = '',
                 CurrencyID: str = '', CashExchangeCode: str = '', Digest: str = '', BankAccType: str = '', DeviceID: str = '', BankSecuAccType: str = '', BrokerIDByBank: str = '',
                 BankSecuAcc: str = '', BankPwdFlag: str = '', SecuPwdFlag: str = '', OperNo: str = '', TID: int = 0, UserID: str = '', ErrorID: int = 0, ErrorMsg: str = '',
                 LongCustomerName: str = ''):
        super(CancelAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.CashExchangeCode = self._to_bytes(CashExchangeCode)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.TID = int(TID)
        self.UserID = self._to_bytes(UserID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ChangeAccountField(Base):
    """银期变更银行账号信息"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 51),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('Gender', ctypes.c_char),  # 性别
        ('CountryCode', ctypes.c_char * 21),  # 国家代码
        ('CustType', ctypes.c_char),  # 客户类型
        ('Address', ctypes.c_char * 101),  # 地址
        ('ZipCode', ctypes.c_char * 7),  # 邮编
        ('Telephone', ctypes.c_char * 41),  # 电话号码
        ('MobilePhone', ctypes.c_char * 21),  # 手机
        ('Fax', ctypes.c_char * 41),  # 传真
        ('EMail', ctypes.c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', ctypes.c_char),  # 资金账户状态
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('NewBankAccount', ctypes.c_char * 41),  # 新银行帐号
        ('NewBankPassWord', ctypes.c_char * 41),  # 新银行密码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('InstallID', ctypes.c_int),  # 安装编号
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('BankPwdFlag', ctypes.c_char),  # 银行密码标志
        ('SecuPwdFlag', ctypes.c_char),  # 期货资金密码核对标志
        ('TID', ctypes.c_int),  # 交易ID
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
        ('LongCustomerName', ctypes.c_char * 161),  # 长客户姓名
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', Gender: str = '',
                 CountryCode: str = '', CustType: str = '', Address: str = '', ZipCode: str = '', Telephone: str = '', MobilePhone: str = '', Fax: str = '', EMail: str = '',
                 MoneyAccountStatus: str = '', BankAccount: str = '', BankPassWord: str = '', NewBankAccount: str = '', NewBankPassWord: str = '', AccountID: str = '', Password: str = '',
                 BankAccType: str = '', InstallID: int = 0, VerifyCertNoFlag: str = '', CurrencyID: str = '', BrokerIDByBank: str = '', BankPwdFlag: str = '', SecuPwdFlag: str = '', TID: int = 0,
                 Digest: str = '', ErrorID: int = 0, ErrorMsg: str = '', LongCustomerName: str = ''):
        super(ChangeAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.NewBankAccount = self._to_bytes(NewBankAccount)
        self.NewBankPassWord = self._to_bytes(NewBankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.BankAccType = self._to_bytes(BankAccType)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.TID = int(TID)
        self.Digest = self._to_bytes(Digest)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class SecAgentACIDMapField(Base):
    """二级代理操作员银期权限"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('AccountID', ctypes.c_char * 13),  # 资金账户
        ('CurrencyID', ctypes.c_char * 4),  # 币种
        ('BrokerSecAgentID', ctypes.c_char * 13),  # 境外中介机构资金帐号
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', AccountID: str = '', CurrencyID: str = '', BrokerSecAgentID: str = ''):
        super(SecAgentACIDMapField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.BrokerSecAgentID = self._to_bytes(BrokerSecAgentID)


class QrySecAgentACIDMapField(Base):
    """二级代理操作员银期权限查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('AccountID', ctypes.c_char * 13),  # 资金账户
        ('CurrencyID', ctypes.c_char * 4),  # 币种
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', AccountID: str = '', CurrencyID: str = ''):
        super(QrySecAgentACIDMapField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class UserRightsAssignField(Base):
    """灾备中心交易权限"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 应用单元代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('DRIdentityID', ctypes.c_int),  # 交易中心代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', DRIdentityID: int = 0):
        super(UserRightsAssignField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.DRIdentityID = int(DRIdentityID)


class BrokerUserRightAssignField(Base):
    """经济公司是否有在本标示的交易权限"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 应用单元代码
        ('DRIdentityID', ctypes.c_int),  # 交易中心代码
        ('Tradeable', ctypes.c_int),  # 能否交易
    ]

    def __init__(self, BrokerID: str = '', DRIdentityID: int = 0, Tradeable: int = 0):
        super(BrokerUserRightAssignField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.DRIdentityID = int(DRIdentityID)
        self.Tradeable = int(Tradeable)


class DRTransferField(Base):
    """灾备交易转换报文"""
    _fields_ = [
        ('OrigDRIdentityID', ctypes.c_int),  # 原交易中心代码
        ('DestDRIdentityID', ctypes.c_int),  # 目标交易中心代码
        ('OrigBrokerID', ctypes.c_char * 11),  # 原应用单元代码
        ('DestBrokerID', ctypes.c_char * 11),  # 目标易用单元代码
    ]

    def __init__(self, OrigDRIdentityID: int = 0, DestDRIdentityID: int = 0, OrigBrokerID: str = '', DestBrokerID: str = ''):
        super(DRTransferField, self).__init__()
        self.OrigDRIdentityID = int(OrigDRIdentityID)
        self.DestDRIdentityID = int(DestDRIdentityID)
        self.OrigBrokerID = self._to_bytes(OrigBrokerID)
        self.DestBrokerID = self._to_bytes(DestBrokerID)


class FensUserInfoField(Base):
    """Fens用户信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('LoginMode', ctypes.c_char),  # 登录模式
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', LoginMode: str = ''):
        super(FensUserInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.LoginMode = self._to_bytes(LoginMode)


class CurrTransferIdentityField(Base):
    """当前银期所属交易中心"""
    _fields_ = [
        ('IdentityID', ctypes.c_int),  # 交易中心代码
    ]

    def __init__(self, IdentityID: int = 0):
        super(CurrTransferIdentityField, self).__init__()
        self.IdentityID = int(IdentityID)


class LoginForbiddenUserField(Base):
    """禁止登录用户"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', reserve1: str = '', IPAddress: str = ''):
        super(LoginForbiddenUserField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.reserve1 = self._to_bytes(reserve1)
        self.IPAddress = self._to_bytes(IPAddress)


class QryLoginForbiddenUserField(Base):
    """查询禁止登录用户"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = ''):
        super(QryLoginForbiddenUserField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class TradingAccountReserveField(Base):
    """资金账户基本准备金"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Reserve', ctypes.c_double),  # 基本准备金
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', AccountID: str = '', Reserve: float = 0.0, CurrencyID: str = ''):
        super(TradingAccountReserveField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.Reserve = float(Reserve)
        self.CurrencyID = self._to_bytes(CurrencyID)


class QryLoginForbiddenIPField(Base):
    """查询禁止登录IP"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, reserve1: str = '', IPAddress: str = ''):
        super(QryLoginForbiddenIPField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.IPAddress = self._to_bytes(IPAddress)


class QryIPListField(Base):
    """查询IP列表"""
    _fields_ = [
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, reserve1: str = '', IPAddress: str = ''):
        super(QryIPListField, self).__init__()
        self.reserve1 = self._to_bytes(reserve1)
        self.IPAddress = self._to_bytes(IPAddress)


class QryUserRightsAssignField(Base):
    """查询用户下单权限分配表"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 应用单元代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = ''):
        super(QryUserRightsAssignField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class ReserveOpenAccountConfirmField(Base):
    """银期预约开户确认请求"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 161),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('Gender', ctypes.c_char),  # 性别
        ('CountryCode', ctypes.c_char * 21),  # 国家代码
        ('CustType', ctypes.c_char),  # 客户类型
        ('Address', ctypes.c_char * 101),  # 地址
        ('ZipCode', ctypes.c_char * 7),  # 邮编
        ('Telephone', ctypes.c_char * 41),  # 电话号码
        ('MobilePhone', ctypes.c_char * 21),  # 手机
        ('Fax', ctypes.c_char * 41),  # 传真
        ('EMail', ctypes.c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', ctypes.c_char),  # 资金账户状态 
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('TID', ctypes.c_int),  # 交易ID
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('Password', ctypes.c_char * 41),  # 期货密码
        ('BankReserveOpenSeq', ctypes.c_char * 13),  # 预约开户银行流水号
        ('BookDate', ctypes.c_char * 9),  # 预约开户日期
        ('BookPsw', ctypes.c_char * 41),  # 预约开户验证密码
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', Gender: str = '',
                 CountryCode: str = '', CustType: str = '', Address: str = '', ZipCode: str = '', Telephone: str = '', MobilePhone: str = '', Fax: str = '', EMail: str = '',
                 MoneyAccountStatus: str = '', BankAccount: str = '', BankPassWord: str = '', InstallID: int = 0, VerifyCertNoFlag: str = '', CurrencyID: str = '', Digest: str = '',
                 BankAccType: str = '', BrokerIDByBank: str = '', TID: int = 0, AccountID: str = '', Password: str = '', BankReserveOpenSeq: str = '', BookDate: str = '', BookPsw: str = '',
                 ErrorID: int = 0, ErrorMsg: str = ''):
        super(ReserveOpenAccountConfirmField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.TID = int(TID)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.BankReserveOpenSeq = self._to_bytes(BankReserveOpenSeq)
        self.BookDate = self._to_bytes(BookDate)
        self.BookPsw = self._to_bytes(BookPsw)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class ReserveOpenAccountField(Base):
    """银期预约开户"""
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),  # 业务功能码
        ('BankID', ctypes.c_char * 4),  # 银行代码
        ('BankBranchID', ctypes.c_char * 5),  # 银行分支机构代码
        ('BrokerID', ctypes.c_char * 11),  # 期商代码
        ('BrokerBranchID', ctypes.c_char * 31),  # 期商分支机构代码
        ('TradeDate', ctypes.c_char * 9),  # 交易日期
        ('TradeTime', ctypes.c_char * 9),  # 交易时间
        ('BankSerial', ctypes.c_char * 13),  # 银行流水号
        ('TradingDay', ctypes.c_char * 9),  # 交易系统日期
        ('PlateSerial', ctypes.c_int),  # 银期平台消息流水号
        ('LastFragment', ctypes.c_char),  # 最后分片标志
        ('SessionID', ctypes.c_int),  # 会话号
        ('CustomerName', ctypes.c_char * 161),  # 客户姓名
        ('IdCardType', ctypes.c_char),  # 证件类型
        ('IdentifiedCardNo', ctypes.c_char * 51),  # 证件号码
        ('Gender', ctypes.c_char),  # 性别
        ('CountryCode', ctypes.c_char * 21),  # 国家代码
        ('CustType', ctypes.c_char),  # 客户类型
        ('Address', ctypes.c_char * 101),  # 地址
        ('ZipCode', ctypes.c_char * 7),  # 邮编
        ('Telephone', ctypes.c_char * 41),  # 电话号码
        ('MobilePhone', ctypes.c_char * 21),  # 手机
        ('Fax', ctypes.c_char * 41),  # 传真
        ('EMail', ctypes.c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', ctypes.c_char),  # 资金账户状态
        ('BankAccount', ctypes.c_char * 41),  # 银行帐号
        ('BankPassWord', ctypes.c_char * 41),  # 银行密码
        ('InstallID', ctypes.c_int),  # 安装编号
        ('VerifyCertNoFlag', ctypes.c_char),  # 验证客户证件号码标志
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('Digest', ctypes.c_char * 36),  # 摘要
        ('BankAccType', ctypes.c_char),  # 银行帐号类型
        ('BrokerIDByBank', ctypes.c_char * 33),  # 期货公司银行编码
        ('TID', ctypes.c_int),  # 交易ID
        ('ReserveOpenAccStas', ctypes.c_char),  # 预约开户状态
        ('ErrorID', ctypes.c_int),  # 错误代码
        ('ErrorMsg', ctypes.c_char * 81),  # 错误信息
    ]

    def __init__(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '',
                 TradingDay: str = '', PlateSerial: int = 0, LastFragment: str = '', SessionID: int = 0, CustomerName: str = '', IdCardType: str = '', IdentifiedCardNo: str = '', Gender: str = '',
                 CountryCode: str = '', CustType: str = '', Address: str = '', ZipCode: str = '', Telephone: str = '', MobilePhone: str = '', Fax: str = '', EMail: str = '',
                 MoneyAccountStatus: str = '', BankAccount: str = '', BankPassWord: str = '', InstallID: int = 0, VerifyCertNoFlag: str = '', CurrencyID: str = '', Digest: str = '',
                 BankAccType: str = '', BrokerIDByBank: str = '', TID: int = 0, ReserveOpenAccStas: str = '', ErrorID: int = 0, ErrorMsg: str = ''):
        super(ReserveOpenAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.TID = int(TID)
        self.ReserveOpenAccStas = self._to_bytes(ReserveOpenAccStas)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class AccountPropertyField(Base):
    """银行账户属性"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('BankID', ctypes.c_char * 4),  # 银行统一标识类型
        ('BankAccount', ctypes.c_char * 41),  # 银行账户
        ('OpenName', ctypes.c_char * 101),  # 银行账户的开户人名称
        ('OpenBank', ctypes.c_char * 101),  # 银行账户的开户行
        ('IsActive', ctypes.c_int),  # 是否活跃
        ('AccountSourceType', ctypes.c_char),  # 账户来源
        ('OpenDate', ctypes.c_char * 9),  # 开户日期
        ('CancelDate', ctypes.c_char * 9),  # 注销日期
        ('OperatorID', ctypes.c_char * 65),  # 录入员代码
        ('OperateDate', ctypes.c_char * 9),  # 录入日期
        ('OperateTime', ctypes.c_char * 9),  # 录入时间
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
    ]

    def __init__(self, BrokerID: str = '', AccountID: str = '', BankID: str = '', BankAccount: str = '', OpenName: str = '', OpenBank: str = '', IsActive: int = 0, AccountSourceType: str = '',
                 OpenDate: str = '', CancelDate: str = '', OperatorID: str = '', OperateDate: str = '', OperateTime: str = '', CurrencyID: str = ''):
        super(AccountPropertyField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.BankID = self._to_bytes(BankID)
        self.BankAccount = self._to_bytes(BankAccount)
        self.OpenName = self._to_bytes(OpenName)
        self.OpenBank = self._to_bytes(OpenBank)
        self.IsActive = int(IsActive)
        self.AccountSourceType = self._to_bytes(AccountSourceType)
        self.OpenDate = self._to_bytes(OpenDate)
        self.CancelDate = self._to_bytes(CancelDate)
        self.OperatorID = self._to_bytes(OperatorID)
        self.OperateDate = self._to_bytes(OperateDate)
        self.OperateTime = self._to_bytes(OperateTime)
        self.CurrencyID = self._to_bytes(CurrencyID)


class QryCurrDRIdentityField(Base):
    """查询当前交易中心"""
    _fields_ = [
        ('DRIdentityID', ctypes.c_int),  # 交易中心代码
    ]

    def __init__(self, DRIdentityID: int = 0):
        super(QryCurrDRIdentityField, self).__init__()
        self.DRIdentityID = int(DRIdentityID)


class CurrDRIdentityField(Base):
    """当前交易中心"""
    _fields_ = [
        ('DRIdentityID', ctypes.c_int),  # 交易中心代码
    ]

    def __init__(self, DRIdentityID: int = 0):
        super(CurrDRIdentityField, self).__init__()
        self.DRIdentityID = int(DRIdentityID)


class QrySecAgentCheckModeField(Base):
    """查询二级代理商资金校验模式"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = ''):
        super(QrySecAgentCheckModeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class QrySecAgentTradeInfoField(Base):
    """查询二级代理商信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('BrokerSecAgentID', ctypes.c_char * 13),  # 境外中介机构资金帐号
    ]

    def __init__(self, BrokerID: str = '', BrokerSecAgentID: str = ''):
        super(QrySecAgentTradeInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerSecAgentID = self._to_bytes(BrokerSecAgentID)


class ReqUserAuthMethodField(Base):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', UserID: str = ''):
        super(ReqUserAuthMethodField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class RspUserAuthMethodField(Base):
    """用户发出获取安全安全登陆方法回复"""
    _fields_ = [
        ('UsableAuthMethod', ctypes.c_int),  # 当前可以用的认证模式
    ]

    def __init__(self, UsableAuthMethod: int = 0):
        super(RspUserAuthMethodField, self).__init__()
        self.UsableAuthMethod = int(UsableAuthMethod)


class ReqGenUserCaptchaField(Base):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', UserID: str = ''):
        super(ReqGenUserCaptchaField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class RspGenUserCaptchaField(Base):
    """生成的图片验证码信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('CaptchaInfoLen', ctypes.c_int),  # 图片信息长度
        ('CaptchaInfo', ctypes.c_char * 2561),  # 图片信息
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', CaptchaInfoLen: int = 0, CaptchaInfo: str = ''):
        super(RspGenUserCaptchaField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.CaptchaInfoLen = int(CaptchaInfoLen)
        self.CaptchaInfo = self._to_bytes(CaptchaInfo)


class ReqGenUserTextField(Base):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', UserID: str = ''):
        super(ReqGenUserTextField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class RspGenUserTextField(Base):
    """短信验证码生成的回复"""
    _fields_ = [
        ('UserTextSeq', ctypes.c_int),  # 短信验证码序号
    ]

    def __init__(self, UserTextSeq: int = 0):
        super(RspGenUserTextField, self).__init__()
        self.UserTextSeq = int(UserTextSeq)


class ReqUserLoginWithCaptchaField(Base):
    """用户发出带图形验证码的登录请求请求"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Password', ctypes.c_char * 41),  # 密码
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', ctypes.c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', ctypes.c_char * 11),  # 协议信息
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('LoginRemark', ctypes.c_char * 36),  # 登录备注
        ('Captcha', ctypes.c_char * 41),  # 图形验证码的文字内容
        ('ClientIPPort', ctypes.c_int),  # 终端IP端口
        ('ClientIPAddress', ctypes.c_char * 33),  # 终端IP地址
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', UserID: str = '', Password: str = '', UserProductInfo: str = '', InterfaceProductInfo: str = '', ProtocolInfo: str = '',
                 MacAddress: str = '', reserve1: str = '', LoginRemark: str = '', Captcha: str = '', ClientIPPort: int = 0, ClientIPAddress: str = ''):
        super(ReqUserLoginWithCaptchaField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.Password = self._to_bytes(Password)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.InterfaceProductInfo = self._to_bytes(InterfaceProductInfo)
        self.ProtocolInfo = self._to_bytes(ProtocolInfo)
        self.MacAddress = self._to_bytes(MacAddress)
        self.reserve1 = self._to_bytes(reserve1)
        self.LoginRemark = self._to_bytes(LoginRemark)
        self.Captcha = self._to_bytes(Captcha)
        self.ClientIPPort = int(ClientIPPort)
        self.ClientIPAddress = self._to_bytes(ClientIPAddress)


class ReqUserLoginWithTextField(Base):
    """用户发出带短信验证码的登录请求请求"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Password', ctypes.c_char * 41),  # 密码
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', ctypes.c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', ctypes.c_char * 11),  # 协议信息
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('LoginRemark', ctypes.c_char * 36),  # 登录备注
        ('Text', ctypes.c_char * 41),  # 短信验证码文字内容
        ('ClientIPPort', ctypes.c_int),  # 终端IP端口
        ('ClientIPAddress', ctypes.c_char * 33),  # 终端IP地址
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', UserID: str = '', Password: str = '', UserProductInfo: str = '', InterfaceProductInfo: str = '', ProtocolInfo: str = '',
                 MacAddress: str = '', reserve1: str = '', LoginRemark: str = '', Text: str = '', ClientIPPort: int = 0, ClientIPAddress: str = ''):
        super(ReqUserLoginWithTextField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.Password = self._to_bytes(Password)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.InterfaceProductInfo = self._to_bytes(InterfaceProductInfo)
        self.ProtocolInfo = self._to_bytes(ProtocolInfo)
        self.MacAddress = self._to_bytes(MacAddress)
        self.reserve1 = self._to_bytes(reserve1)
        self.LoginRemark = self._to_bytes(LoginRemark)
        self.Text = self._to_bytes(Text)
        self.ClientIPPort = int(ClientIPPort)
        self.ClientIPAddress = self._to_bytes(ClientIPAddress)


class ReqUserLoginWithOTPField(Base):
    """用户发出带动态验证码的登录请求请求"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Password', ctypes.c_char * 41),  # 密码
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', ctypes.c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', ctypes.c_char * 11),  # 协议信息
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('LoginRemark', ctypes.c_char * 36),  # 登录备注
        ('OTPPassword', ctypes.c_char * 41),  # OTP密码
        ('ClientIPPort', ctypes.c_int),  # 终端IP端口
        ('ClientIPAddress', ctypes.c_char * 33),  # 终端IP地址
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', UserID: str = '', Password: str = '', UserProductInfo: str = '', InterfaceProductInfo: str = '', ProtocolInfo: str = '',
                 MacAddress: str = '', reserve1: str = '', LoginRemark: str = '', OTPPassword: str = '', ClientIPPort: int = 0, ClientIPAddress: str = ''):
        super(ReqUserLoginWithOTPField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.Password = self._to_bytes(Password)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.InterfaceProductInfo = self._to_bytes(InterfaceProductInfo)
        self.ProtocolInfo = self._to_bytes(ProtocolInfo)
        self.MacAddress = self._to_bytes(MacAddress)
        self.reserve1 = self._to_bytes(reserve1)
        self.LoginRemark = self._to_bytes(LoginRemark)
        self.OTPPassword = self._to_bytes(OTPPassword)
        self.ClientIPPort = int(ClientIPPort)
        self.ClientIPAddress = self._to_bytes(ClientIPAddress)


class ReqApiHandshakeField(Base):
    """api握手请求"""
    _fields_ = [
        ('CryptoKeyVersion', ctypes.c_char * 31),  # api与front通信密钥版本号
    ]

    def __init__(self, CryptoKeyVersion: str = ''):
        super(ReqApiHandshakeField, self).__init__()
        self.CryptoKeyVersion = self._to_bytes(CryptoKeyVersion)


class RspApiHandshakeField(Base):
    """front发给api的握手回复"""
    _fields_ = [
        ('FrontHandshakeDataLen', ctypes.c_int),  # 握手回复数据长度
        ('FrontHandshakeData', ctypes.c_char * 301),  # 握手回复数据
        ('IsApiAuthEnabled', ctypes.c_int),  # API认证是否开启
    ]

    def __init__(self, FrontHandshakeDataLen: int = 0, FrontHandshakeData: str = '', IsApiAuthEnabled: int = 0):
        super(RspApiHandshakeField, self).__init__()
        self.FrontHandshakeDataLen = int(FrontHandshakeDataLen)
        self.FrontHandshakeData = self._to_bytes(FrontHandshakeData)
        self.IsApiAuthEnabled = int(IsApiAuthEnabled)


class ReqVerifyApiKeyField(Base):
    """api给front的验证key的请求"""
    _fields_ = [
        ('ApiHandshakeDataLen', ctypes.c_int),  # 握手回复数据长度
        ('ApiHandshakeData', ctypes.c_char * 301),  # 握手回复数据
    ]

    def __init__(self, ApiHandshakeDataLen: int = 0, ApiHandshakeData: str = ''):
        super(ReqVerifyApiKeyField, self).__init__()
        self.ApiHandshakeDataLen = int(ApiHandshakeDataLen)
        self.ApiHandshakeData = self._to_bytes(ApiHandshakeData)


class DepartmentUserField(Base):
    """操作员组织架构关系"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', InvestorRange: str = '', InvestorID: str = ''):
        super(DepartmentUserField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.InvestorID = self._to_bytes(InvestorID)


class QueryFreqField(Base):
    """查询频率，每秒查询比数"""
    _fields_ = [
        ('QueryFreq', ctypes.c_int),  # 查询频率
    ]

    def __init__(self, QueryFreq: int = 0):
        super(QueryFreqField, self).__init__()
        self.QueryFreq = int(QueryFreq)


class AuthForbiddenIPField(Base):
    """禁止认证IP"""
    _fields_ = [
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, IPAddress: str = ''):
        super(AuthForbiddenIPField, self).__init__()
        self.IPAddress = self._to_bytes(IPAddress)


class QryAuthForbiddenIPField(Base):
    """查询禁止认证IP"""
    _fields_ = [
        ('IPAddress', ctypes.c_char * 33),  # IP地址
    ]

    def __init__(self, IPAddress: str = ''):
        super(QryAuthForbiddenIPField, self).__init__()
        self.IPAddress = self._to_bytes(IPAddress)


class SyncDelaySwapFrozenField(Base):
    """换汇可提冻结"""
    _fields_ = [
        ('DelaySwapSeqNo', ctypes.c_char * 15),  # 换汇流水号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('FromCurrencyID', ctypes.c_char * 4),  # 源币种
        ('FromRemainSwap', ctypes.c_double),  # 源剩余换汇额度(可提冻结)
        ('IsManualSwap', ctypes.c_int),  # 是否手工换汇
    ]

    def __init__(self, DelaySwapSeqNo: str = '', BrokerID: str = '', InvestorID: str = '', FromCurrencyID: str = '', FromRemainSwap: float = 0.0, IsManualSwap: int = 0):
        super(SyncDelaySwapFrozenField, self).__init__()
        self.DelaySwapSeqNo = self._to_bytes(DelaySwapSeqNo)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.FromCurrencyID = self._to_bytes(FromCurrencyID)
        self.FromRemainSwap = float(FromRemainSwap)
        self.IsManualSwap = int(IsManualSwap)


class UserSystemInfoField(Base):
    """用户系统信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('ClientSystemInfoLen', ctypes.c_int),  # 用户端系统内部信息长度
        ('ClientSystemInfo', ctypes.c_char * 273),  # 用户端系统内部信息
        ('reserve1', ctypes.c_char * 16),  # 保留的无效字段
        ('ClientIPPort', ctypes.c_int),  # 终端IP端口
        ('ClientLoginTime', ctypes.c_char * 9),  # 登录成功时间
        ('ClientAppID', ctypes.c_char * 33),  # App代码
        ('ClientPublicIP', ctypes.c_char * 33),  # 用户公网IP
        ('ClientLoginRemark', ctypes.c_char * 151),  # 客户登录备注2
    ]

    def __init__(self, BrokerID: str = '', UserID: str = '', ClientSystemInfoLen: int = 0, ClientSystemInfo: str = '', reserve1: str = '', ClientIPPort: int = 0, ClientLoginTime: str = '',
                 ClientAppID: str = '', ClientPublicIP: str = '', ClientLoginRemark: str = ''):
        super(UserSystemInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.ClientSystemInfoLen = int(ClientSystemInfoLen)
        self.ClientSystemInfo = self._to_bytes(ClientSystemInfo)
        self.reserve1 = self._to_bytes(reserve1)
        self.ClientIPPort = int(ClientIPPort)
        self.ClientLoginTime = self._to_bytes(ClientLoginTime)
        self.ClientAppID = self._to_bytes(ClientAppID)
        self.ClientPublicIP = self._to_bytes(ClientPublicIP)
        self.ClientLoginRemark = self._to_bytes(ClientLoginRemark)


class AuthUserIDField(Base):
    """终端用户绑定信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AppID', ctypes.c_char * 33),  # App代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('AuthType', ctypes.c_char),  # 校验类型
    ]

    def __init__(self, BrokerID: str = '', AppID: str = '', UserID: str = '', AuthType: str = ''):
        super(AuthUserIDField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AppID = self._to_bytes(AppID)
        self.UserID = self._to_bytes(UserID)
        self.AuthType = self._to_bytes(AuthType)


class AuthIPField(Base):
    """用户IP绑定信息"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AppID', ctypes.c_char * 33),  # App代码
        ('IPAddress', ctypes.c_char * 33),  # 用户代码
    ]

    def __init__(self, BrokerID: str = '', AppID: str = '', IPAddress: str = ''):
        super(AuthIPField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AppID = self._to_bytes(AppID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryClassifiedInstrumentField(Base):
    """查询分类合约"""
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('ProductID', ctypes.c_char * 81),  # 产品代码
        ('TradingType', ctypes.c_char),  # 合约交易状态
        ('ClassType', ctypes.c_char),  # 合约分类类型
    ]

    def __init__(self, InstrumentID: str = '', ExchangeID: str = '', ExchangeInstID: str = '', ProductID: str = '', TradingType: str = '', ClassType: str = ''):
        super(QryClassifiedInstrumentField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.ProductID = self._to_bytes(ProductID)
        self.TradingType = self._to_bytes(TradingType)
        self.ClassType = self._to_bytes(ClassType)


class QryCombPromotionParamField(Base):
    """查询组合优惠比例"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, ExchangeID: str = '', InstrumentID: str = ''):
        super(QryCombPromotionParamField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class CombPromotionParamField(Base):
    """组合优惠比例"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('CombHedgeFlag', ctypes.c_char * 5),  # 投机套保标志
        ('Xparameter', ctypes.c_double),  # 期权组合保证金比例
    ]

    def __init__(self, ExchangeID: str = '', InstrumentID: str = '', CombHedgeFlag: str = '', Xparameter: float = 0.0):
        super(CombPromotionParamField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.Xparameter = float(Xparameter)


class ReqUserLoginSCField(Base):
    """国密用户登录请求"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('UserID', ctypes.c_char * 16),  # 用户代码
        ('Password', ctypes.c_char * 41),  # 密码
        ('UserProductInfo', ctypes.c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', ctypes.c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', ctypes.c_char * 11),  # 协议信息
        ('MacAddress', ctypes.c_char * 21),  # Mac地址
        ('OneTimePassword', ctypes.c_char * 41),  # 动态密码
        ('ClientIPAddress', ctypes.c_char * 33),  # 终端IP地址
        ('LoginRemark', ctypes.c_char * 36),  # 登录备注
        ('ClientIPPort', ctypes.c_int),  # 终端IP端口
        ('AuthCode', ctypes.c_char * 17),  # 认证码
        ('AppID', ctypes.c_char * 33),  # App代码
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', UserID: str = '', Password: str = '', UserProductInfo: str = '', InterfaceProductInfo: str = '', ProtocolInfo: str = '',
                 MacAddress: str = '', OneTimePassword: str = '', ClientIPAddress: str = '', LoginRemark: str = '', ClientIPPort: int = 0, AuthCode: str = '', AppID: str = ''):
        super(ReqUserLoginSCField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.Password = self._to_bytes(Password)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.InterfaceProductInfo = self._to_bytes(InterfaceProductInfo)
        self.ProtocolInfo = self._to_bytes(ProtocolInfo)
        self.MacAddress = self._to_bytes(MacAddress)
        self.OneTimePassword = self._to_bytes(OneTimePassword)
        self.ClientIPAddress = self._to_bytes(ClientIPAddress)
        self.LoginRemark = self._to_bytes(LoginRemark)
        self.ClientIPPort = int(ClientIPPort)
        self.AuthCode = self._to_bytes(AuthCode)
        self.AppID = self._to_bytes(AppID)


class QryRiskSettleInvstPositionField(Base):
    """投资者风险结算持仓查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', InstrumentID: str = ''):
        super(QryRiskSettleInvstPositionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryRiskSettleProductStatusField(Base):
    """风险结算产品查询"""
    _fields_ = [
        ('ProductID', ctypes.c_char * 81),  # 产品代码
    ]

    def __init__(self, ProductID: str = ''):
        super(QryRiskSettleProductStatusField, self).__init__()
        self.ProductID = self._to_bytes(ProductID)


class RiskSettleInvstPositionField(Base):
    """投资者风险结算持仓"""
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('PosiDirection', ctypes.c_char),  # 持仓多空方向
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('PositionDate', ctypes.c_char),  # 持仓日期
        ('YdPosition', ctypes.c_int),  # 上日持仓
        ('Position', ctypes.c_int),  # 今日持仓
        ('LongFrozen', ctypes.c_int),  # 多头冻结
        ('ShortFrozen', ctypes.c_int),  # 空头冻结
        ('LongFrozenAmount', ctypes.c_double),  # 开仓冻结金额
        ('ShortFrozenAmount', ctypes.c_double),  # 开仓冻结金额
        ('OpenVolume', ctypes.c_int),  # 开仓量
        ('CloseVolume', ctypes.c_int),  # 平仓量
        ('OpenAmount', ctypes.c_double),  # 开仓金额
        ('CloseAmount', ctypes.c_double),  # 平仓金额
        ('PositionCost', ctypes.c_double),  # 持仓成本
        ('PreMargin', ctypes.c_double),  # 上次占用的保证金
        ('UseMargin', ctypes.c_double),  # 占用的保证金
        ('FrozenMargin', ctypes.c_double),  # 冻结的保证金
        ('FrozenCash', ctypes.c_double),  # 冻结的资金
        ('FrozenCommission', ctypes.c_double),  # 冻结的手续费
        ('CashIn', ctypes.c_double),  # 资金差额
        ('Commission', ctypes.c_double),  # 手续费
        ('CloseProfit', ctypes.c_double),  # 平仓盈亏
        ('PositionProfit', ctypes.c_double),  # 持仓盈亏
        ('PreSettlementPrice', ctypes.c_double),  # 上次结算价
        ('SettlementPrice', ctypes.c_double),  # 本次结算价
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('OpenCost', ctypes.c_double),  # 开仓成本
        ('ExchangeMargin', ctypes.c_double),  # 交易所保证金
        ('CombPosition', ctypes.c_int),  # 组合成交形成的持仓
        ('CombLongFrozen', ctypes.c_int),  # 组合多头冻结
        ('CombShortFrozen', ctypes.c_int),  # 组合空头冻结
        ('CloseProfitByDate', ctypes.c_double),  # 逐日盯市平仓盈亏
        ('CloseProfitByTrade', ctypes.c_double),  # 逐笔对冲平仓盈亏
        ('TodayPosition', ctypes.c_int),  # 今日持仓
        ('MarginRateByMoney', ctypes.c_double),  # 保证金率
        ('MarginRateByVolume', ctypes.c_double),  # 保证金率(按手数)
        ('StrikeFrozen', ctypes.c_int),  # 执行冻结
        ('StrikeFrozenAmount', ctypes.c_double),  # 执行冻结金额
        ('AbandonFrozen', ctypes.c_int),  # 放弃执行冻结
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('YdStrikeFrozen', ctypes.c_int),  # 执行冻结的昨仓
        ('InvestUnitID', ctypes.c_char * 17),  # 投资单元代码
        ('PositionCostOffset', ctypes.c_double),  # 持仓成本差值
        ('TasPosition', ctypes.c_int),  # tas持仓手数
        ('TasPositionCost', ctypes.c_double),  # tas持仓成本
    ]

    def __init__(self, InstrumentID: str = '', BrokerID: str = '', InvestorID: str = '', PosiDirection: str = '', HedgeFlag: str = '', PositionDate: str = '', YdPosition: int = 0, Position: int = 0,
                 LongFrozen: int = 0, ShortFrozen: int = 0, LongFrozenAmount: float = 0.0, ShortFrozenAmount: float = 0.0, OpenVolume: int = 0, CloseVolume: int = 0, OpenAmount: float = 0.0,
                 CloseAmount: float = 0.0, PositionCost: float = 0.0, PreMargin: float = 0.0, UseMargin: float = 0.0, FrozenMargin: float = 0.0, FrozenCash: float = 0.0, FrozenCommission: float = 0.0,
                 CashIn: float = 0.0, Commission: float = 0.0, CloseProfit: float = 0.0, PositionProfit: float = 0.0, PreSettlementPrice: float = 0.0, SettlementPrice: float = 0.0,
                 TradingDay: str = '', SettlementID: int = 0, OpenCost: float = 0.0, ExchangeMargin: float = 0.0, CombPosition: int = 0, CombLongFrozen: int = 0, CombShortFrozen: int = 0,
                 CloseProfitByDate: float = 0.0, CloseProfitByTrade: float = 0.0, TodayPosition: int = 0, MarginRateByMoney: float = 0.0, MarginRateByVolume: float = 0.0, StrikeFrozen: int = 0,
                 StrikeFrozenAmount: float = 0.0, AbandonFrozen: int = 0, ExchangeID: str = '', YdStrikeFrozen: int = 0, InvestUnitID: str = '', PositionCostOffset: float = 0.0, TasPosition: int = 0,
                 TasPositionCost: float = 0.0):
        super(RiskSettleInvstPositionField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.PositionDate = self._to_bytes(PositionDate)
        self.YdPosition = int(YdPosition)
        self.Position = int(Position)
        self.LongFrozen = int(LongFrozen)
        self.ShortFrozen = int(ShortFrozen)
        self.LongFrozenAmount = float(LongFrozenAmount)
        self.ShortFrozenAmount = float(ShortFrozenAmount)
        self.OpenVolume = int(OpenVolume)
        self.CloseVolume = int(CloseVolume)
        self.OpenAmount = float(OpenAmount)
        self.CloseAmount = float(CloseAmount)
        self.PositionCost = float(PositionCost)
        self.PreMargin = float(PreMargin)
        self.UseMargin = float(UseMargin)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.CloseProfit = float(CloseProfit)
        self.PositionProfit = float(PositionProfit)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OpenCost = float(OpenCost)
        self.ExchangeMargin = float(ExchangeMargin)
        self.CombPosition = int(CombPosition)
        self.CombLongFrozen = int(CombLongFrozen)
        self.CombShortFrozen = int(CombShortFrozen)
        self.CloseProfitByDate = float(CloseProfitByDate)
        self.CloseProfitByTrade = float(CloseProfitByTrade)
        self.TodayPosition = int(TodayPosition)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.StrikeFrozen = int(StrikeFrozen)
        self.StrikeFrozenAmount = float(StrikeFrozenAmount)
        self.AbandonFrozen = int(AbandonFrozen)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.YdStrikeFrozen = int(YdStrikeFrozen)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.PositionCostOffset = float(PositionCostOffset)
        self.TasPosition = int(TasPosition)
        self.TasPositionCost = float(TasPositionCost)


class RiskSettleProductStatusField(Base):
    """风险品种"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ProductID', ctypes.c_char * 81),  # 产品编号
        ('ProductStatus', ctypes.c_char),  # 产品结算状态
    ]

    def __init__(self, ExchangeID: str = '', ProductID: str = '', ProductStatus: str = ''):
        super(RiskSettleProductStatusField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProductID = self._to_bytes(ProductID)
        self.ProductStatus = self._to_bytes(ProductStatus)


class SyncDeltaInfoField(Base):
    """风险结算追平信息"""
    _fields_ = [
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
        ('SyncDeltaStatus', ctypes.c_char),  # 追平状态
        ('SyncDescription', ctypes.c_char * 257),  # 追平描述
        ('IsOnlyTrdDelta', ctypes.c_int),  # 是否只有资金追平
    ]

    def __init__(self, SyncDeltaSequenceNo: int = 0, SyncDeltaStatus: str = '', SyncDescription: str = '', IsOnlyTrdDelta: int = 0):
        super(SyncDeltaInfoField, self).__init__()
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)
        self.SyncDeltaStatus = self._to_bytes(SyncDeltaStatus)
        self.SyncDescription = self._to_bytes(SyncDescription)
        self.IsOnlyTrdDelta = int(IsOnlyTrdDelta)


class SyncDeltaProductStatusField(Base):
    """风险结算追平产品信息"""
    _fields_ = [
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ProductID', ctypes.c_char * 81),  # 产品代码
        ('ProductStatus', ctypes.c_char),  # 是否允许交易
    ]

    def __init__(self, SyncDeltaSequenceNo: int = 0, ExchangeID: str = '', ProductID: str = '', ProductStatus: str = ''):
        super(SyncDeltaProductStatusField, self).__init__()
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProductID = self._to_bytes(ProductID)
        self.ProductStatus = self._to_bytes(ProductStatus)


class SyncDeltaInvstPosDtlField(Base):
    """风险结算追平持仓明细"""
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('Direction', ctypes.c_char),  # 买卖
        ('OpenDate', ctypes.c_char * 9),  # 开仓日期
        ('TradeID', ctypes.c_char * 21),  # 成交编号
        ('Volume', ctypes.c_int),  # 数量
        ('OpenPrice', ctypes.c_double),  # 开仓价
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('TradeType', ctypes.c_char),  # 成交类型
        ('CombInstrumentID', ctypes.c_char * 81),  # 组合合约代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('CloseProfitByDate', ctypes.c_double),  # 逐日盯市平仓盈亏
        ('CloseProfitByTrade', ctypes.c_double),  # 逐笔对冲平仓盈亏
        ('PositionProfitByDate', ctypes.c_double),  # 逐日盯市持仓盈亏
        ('PositionProfitByTrade', ctypes.c_double),  # 逐笔对冲持仓盈亏
        ('Margin', ctypes.c_double),  # 投资者保证金
        ('ExchMargin', ctypes.c_double),  # 交易所保证金
        ('MarginRateByMoney', ctypes.c_double),  # 保证金率
        ('MarginRateByVolume', ctypes.c_double),  # 保证金率(按手数)
        ('LastSettlementPrice', ctypes.c_double),  # 昨结算价
        ('SettlementPrice', ctypes.c_double),  # 结算价
        ('CloseVolume', ctypes.c_int),  # 平仓量
        ('CloseAmount', ctypes.c_double),  # 平仓金额
        ('TimeFirstVolume', ctypes.c_int),  # 先开先平剩余数量
        ('SpecPosiType', ctypes.c_char),  # 特殊持仓标志
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, InstrumentID: str = '', BrokerID: str = '', InvestorID: str = '', HedgeFlag: str = '', Direction: str = '', OpenDate: str = '', TradeID: str = '', Volume: int = 0,
                 OpenPrice: float = 0.0, TradingDay: str = '', SettlementID: int = 0, TradeType: str = '', CombInstrumentID: str = '', ExchangeID: str = '', CloseProfitByDate: float = 0.0,
                 CloseProfitByTrade: float = 0.0, PositionProfitByDate: float = 0.0, PositionProfitByTrade: float = 0.0, Margin: float = 0.0, ExchMargin: float = 0.0, MarginRateByMoney: float = 0.0,
                 MarginRateByVolume: float = 0.0, LastSettlementPrice: float = 0.0, SettlementPrice: float = 0.0, CloseVolume: int = 0, CloseAmount: float = 0.0, TimeFirstVolume: int = 0,
                 SpecPosiType: str = '', ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaInvstPosDtlField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Direction = self._to_bytes(Direction)
        self.OpenDate = self._to_bytes(OpenDate)
        self.TradeID = self._to_bytes(TradeID)
        self.Volume = int(Volume)
        self.OpenPrice = float(OpenPrice)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.TradeType = self._to_bytes(TradeType)
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.CloseProfitByDate = float(CloseProfitByDate)
        self.CloseProfitByTrade = float(CloseProfitByTrade)
        self.PositionProfitByDate = float(PositionProfitByDate)
        self.PositionProfitByTrade = float(PositionProfitByTrade)
        self.Margin = float(Margin)
        self.ExchMargin = float(ExchMargin)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.LastSettlementPrice = float(LastSettlementPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.CloseVolume = int(CloseVolume)
        self.CloseAmount = float(CloseAmount)
        self.TimeFirstVolume = int(TimeFirstVolume)
        self.SpecPosiType = self._to_bytes(SpecPosiType)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaInvstPosCombDtlField(Base):
    """风险结算追平组合持仓明细"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('OpenDate', ctypes.c_char * 9),  # 开仓日期
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ComTradeID', ctypes.c_char * 21),  # 组合编号
        ('TradeID', ctypes.c_char * 21),  # 撮合编号
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('Direction', ctypes.c_char),  # 买卖
        ('TotalAmt', ctypes.c_int),  # 持仓量
        ('Margin', ctypes.c_double),  # 投资者保证金
        ('ExchMargin', ctypes.c_double),  # 交易所保证金
        ('MarginRateByMoney', ctypes.c_double),  # 保证金率
        ('MarginRateByVolume', ctypes.c_double),  # 保证金率(按手数)
        ('LegID', ctypes.c_int),  # 单腿编号
        ('LegMultiple', ctypes.c_int),  # 单腿乘数
        ('TradeGroupID', ctypes.c_int),  # 成交组号
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, TradingDay: str = '', OpenDate: str = '', ExchangeID: str = '', SettlementID: int = 0, BrokerID: str = '', InvestorID: str = '', ComTradeID: str = '', TradeID: str = '',
                 InstrumentID: str = '', HedgeFlag: str = '', Direction: str = '', TotalAmt: int = 0, Margin: float = 0.0, ExchMargin: float = 0.0, MarginRateByMoney: float = 0.0,
                 MarginRateByVolume: float = 0.0, LegID: int = 0, LegMultiple: int = 0, TradeGroupID: int = 0, ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaInvstPosCombDtlField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.OpenDate = self._to_bytes(OpenDate)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.SettlementID = int(SettlementID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ComTradeID = self._to_bytes(ComTradeID)
        self.TradeID = self._to_bytes(TradeID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Direction = self._to_bytes(Direction)
        self.TotalAmt = int(TotalAmt)
        self.Margin = float(Margin)
        self.ExchMargin = float(ExchMargin)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.LegID = int(LegID)
        self.LegMultiple = int(LegMultiple)
        self.TradeGroupID = int(TradeGroupID)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaTradingAccountField(Base):
    """风险结算追平资金"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('AccountID', ctypes.c_char * 13),  # 投资者帐号
        ('PreMortgage', ctypes.c_double),  # 上次质押金额
        ('PreCredit', ctypes.c_double),  # 上次信用额度
        ('PreDeposit', ctypes.c_double),  # 上次存款额
        ('PreBalance', ctypes.c_double),  # 上次结算准备金
        ('PreMargin', ctypes.c_double),  # 上次占用的保证金
        ('InterestBase', ctypes.c_double),  # 利息基数
        ('Interest', ctypes.c_double),  # 利息收入
        ('Deposit', ctypes.c_double),  # 入金金额
        ('Withdraw', ctypes.c_double),  # 出金金额
        ('FrozenMargin', ctypes.c_double),  # 冻结的保证金
        ('FrozenCash', ctypes.c_double),  # 冻结的资金
        ('FrozenCommission', ctypes.c_double),  # 冻结的手续费
        ('CurrMargin', ctypes.c_double),  # 当前保证金总额
        ('CashIn', ctypes.c_double),  # 资金差额
        ('Commission', ctypes.c_double),  # 手续费
        ('CloseProfit', ctypes.c_double),  # 平仓盈亏
        ('PositionProfit', ctypes.c_double),  # 持仓盈亏
        ('Balance', ctypes.c_double),  # 期货结算准备金
        ('Available', ctypes.c_double),  # 可用资金
        ('WithdrawQuota', ctypes.c_double),  # 可取资金
        ('Reserve', ctypes.c_double),  # 基本准备金
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('SettlementID', ctypes.c_int),  # 结算编号
        ('Credit', ctypes.c_double),  # 信用额度
        ('Mortgage', ctypes.c_double),  # 质押金额
        ('ExchangeMargin', ctypes.c_double),  # 交易所保证金
        ('DeliveryMargin', ctypes.c_double),  # 投资者交割保证金
        ('ExchangeDeliveryMargin', ctypes.c_double),  # 交易所交割保证金
        ('ReserveBalance', ctypes.c_double),  # 保底期货结算准备金
        ('CurrencyID', ctypes.c_char * 4),  # 币种代码
        ('PreFundMortgageIn', ctypes.c_double),  # 上次货币质入金额
        ('PreFundMortgageOut', ctypes.c_double),  # 上次货币质出金额
        ('FundMortgageIn', ctypes.c_double),  # 货币质入金额
        ('FundMortgageOut', ctypes.c_double),  # 货币质出金额
        ('FundMortgageAvailable', ctypes.c_double),  # 货币质押余额
        ('MortgageableFund', ctypes.c_double),  # 可质押货币金额
        ('SpecProductMargin', ctypes.c_double),  # 特殊产品占用保证金
        ('SpecProductFrozenMargin', ctypes.c_double),  # 特殊产品冻结保证金
        ('SpecProductCommission', ctypes.c_double),  # 特殊产品手续费
        ('SpecProductFrozenCommission', ctypes.c_double),  # 特殊产品冻结手续费
        ('SpecProductPositionProfit', ctypes.c_double),  # 特殊产品持仓盈亏
        ('SpecProductCloseProfit', ctypes.c_double),  # 特殊产品平仓盈亏
        ('SpecProductPositionProfitByAlg', ctypes.c_double),  # 根据持仓盈亏算法计算的特殊产品持仓盈亏
        ('SpecProductExchangeMargin', ctypes.c_double),  # 特殊产品交易所保证金
        ('FrozenSwap', ctypes.c_double),  # 延时换汇冻结金额
        ('RemainSwap', ctypes.c_double),  # 剩余换汇额度
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, BrokerID: str = '', AccountID: str = '', PreMortgage: float = 0.0, PreCredit: float = 0.0, PreDeposit: float = 0.0, PreBalance: float = 0.0, PreMargin: float = 0.0,
                 InterestBase: float = 0.0, Interest: float = 0.0, Deposit: float = 0.0, Withdraw: float = 0.0, FrozenMargin: float = 0.0, FrozenCash: float = 0.0, FrozenCommission: float = 0.0,
                 CurrMargin: float = 0.0, CashIn: float = 0.0, Commission: float = 0.0, CloseProfit: float = 0.0, PositionProfit: float = 0.0, Balance: float = 0.0, Available: float = 0.0,
                 WithdrawQuota: float = 0.0, Reserve: float = 0.0, TradingDay: str = '', SettlementID: int = 0, Credit: float = 0.0, Mortgage: float = 0.0, ExchangeMargin: float = 0.0,
                 DeliveryMargin: float = 0.0, ExchangeDeliveryMargin: float = 0.0, ReserveBalance: float = 0.0, CurrencyID: str = '', PreFundMortgageIn: float = 0.0, PreFundMortgageOut: float = 0.0,
                 FundMortgageIn: float = 0.0, FundMortgageOut: float = 0.0, FundMortgageAvailable: float = 0.0, MortgageableFund: float = 0.0, SpecProductMargin: float = 0.0,
                 SpecProductFrozenMargin: float = 0.0, SpecProductCommission: float = 0.0, SpecProductFrozenCommission: float = 0.0, SpecProductPositionProfit: float = 0.0,
                 SpecProductCloseProfit: float = 0.0, SpecProductPositionProfitByAlg: float = 0.0, SpecProductExchangeMargin: float = 0.0, FrozenSwap: float = 0.0, RemainSwap: float = 0.0,
                 SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaTradingAccountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.PreMortgage = float(PreMortgage)
        self.PreCredit = float(PreCredit)
        self.PreDeposit = float(PreDeposit)
        self.PreBalance = float(PreBalance)
        self.PreMargin = float(PreMargin)
        self.InterestBase = float(InterestBase)
        self.Interest = float(Interest)
        self.Deposit = float(Deposit)
        self.Withdraw = float(Withdraw)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CurrMargin = float(CurrMargin)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.CloseProfit = float(CloseProfit)
        self.PositionProfit = float(PositionProfit)
        self.Balance = float(Balance)
        self.Available = float(Available)
        self.WithdrawQuota = float(WithdrawQuota)
        self.Reserve = float(Reserve)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.Credit = float(Credit)
        self.Mortgage = float(Mortgage)
        self.ExchangeMargin = float(ExchangeMargin)
        self.DeliveryMargin = float(DeliveryMargin)
        self.ExchangeDeliveryMargin = float(ExchangeDeliveryMargin)
        self.ReserveBalance = float(ReserveBalance)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.PreFundMortgageIn = float(PreFundMortgageIn)
        self.PreFundMortgageOut = float(PreFundMortgageOut)
        self.FundMortgageIn = float(FundMortgageIn)
        self.FundMortgageOut = float(FundMortgageOut)
        self.FundMortgageAvailable = float(FundMortgageAvailable)
        self.MortgageableFund = float(MortgageableFund)
        self.SpecProductMargin = float(SpecProductMargin)
        self.SpecProductFrozenMargin = float(SpecProductFrozenMargin)
        self.SpecProductCommission = float(SpecProductCommission)
        self.SpecProductFrozenCommission = float(SpecProductFrozenCommission)
        self.SpecProductPositionProfit = float(SpecProductPositionProfit)
        self.SpecProductCloseProfit = float(SpecProductCloseProfit)
        self.SpecProductPositionProfitByAlg = float(SpecProductPositionProfitByAlg)
        self.SpecProductExchangeMargin = float(SpecProductExchangeMargin)
        self.FrozenSwap = float(FrozenSwap)
        self.RemainSwap = float(RemainSwap)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaInitInvstMarginField(Base):
    """投资者风险结算总保证金"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('LastRiskTotalInvstMargin', ctypes.c_double),  # 追平前总风险保证金
        ('LastRiskTotalExchMargin', ctypes.c_double),  # 追平前交易所总风险保证金
        ('ThisSyncInvstMargin', ctypes.c_double),  # 本次追平品种总保证金
        ('ThisSyncExchMargin', ctypes.c_double),  # 本次追平品种交易所总保证金
        ('RemainRiskInvstMargin', ctypes.c_double),  # 本次未追平品种总保证金
        ('RemainRiskExchMargin', ctypes.c_double),  # 本次未追平品种交易所总保证金
        ('LastRiskSpecTotalInvstMargin', ctypes.c_double),  # 追平前总特殊产品风险保证金
        ('LastRiskSpecTotalExchMargin', ctypes.c_double),  # 追平前总特殊产品交易所风险保证金
        ('ThisSyncSpecInvstMargin', ctypes.c_double),  # 本次追平品种特殊产品总保证金
        ('ThisSyncSpecExchMargin', ctypes.c_double),  # 本次追平品种特殊产品交易所总保证金
        ('RemainRiskSpecInvstMargin', ctypes.c_double),  # 本次未追平品种特殊产品总保证金
        ('RemainRiskSpecExchMargin', ctypes.c_double),  # 本次未追平品种特殊产品交易所总保证金
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', LastRiskTotalInvstMargin: float = 0.0, LastRiskTotalExchMargin: float = 0.0, ThisSyncInvstMargin: float = 0.0,
                 ThisSyncExchMargin: float = 0.0, RemainRiskInvstMargin: float = 0.0, RemainRiskExchMargin: float = 0.0, LastRiskSpecTotalInvstMargin: float = 0.0,
                 LastRiskSpecTotalExchMargin: float = 0.0, ThisSyncSpecInvstMargin: float = 0.0, ThisSyncSpecExchMargin: float = 0.0, RemainRiskSpecInvstMargin: float = 0.0,
                 RemainRiskSpecExchMargin: float = 0.0, SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaInitInvstMarginField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.LastRiskTotalInvstMargin = float(LastRiskTotalInvstMargin)
        self.LastRiskTotalExchMargin = float(LastRiskTotalExchMargin)
        self.ThisSyncInvstMargin = float(ThisSyncInvstMargin)
        self.ThisSyncExchMargin = float(ThisSyncExchMargin)
        self.RemainRiskInvstMargin = float(RemainRiskInvstMargin)
        self.RemainRiskExchMargin = float(RemainRiskExchMargin)
        self.LastRiskSpecTotalInvstMargin = float(LastRiskSpecTotalInvstMargin)
        self.LastRiskSpecTotalExchMargin = float(LastRiskSpecTotalExchMargin)
        self.ThisSyncSpecInvstMargin = float(ThisSyncSpecInvstMargin)
        self.ThisSyncSpecExchMargin = float(ThisSyncSpecExchMargin)
        self.RemainRiskSpecInvstMargin = float(RemainRiskSpecInvstMargin)
        self.RemainRiskSpecExchMargin = float(RemainRiskSpecExchMargin)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaDceCombInstrumentField(Base):
    """风险结算追平组合优先级"""
    _fields_ = [
        ('CombInstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('TradeGroupID', ctypes.c_int),  # 成交组号
        ('CombHedgeFlag', ctypes.c_char),  # 投机套保标志
        ('CombinationType', ctypes.c_char),  # 组合类型
        ('Direction', ctypes.c_char),  # 买卖
        ('ProductID', ctypes.c_char * 81),  # 产品代码
        ('Xparameter', ctypes.c_double),  # 期权组合保证金比例
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, CombInstrumentID: str = '', ExchangeID: str = '', ExchangeInstID: str = '', TradeGroupID: int = 0, CombHedgeFlag: str = '', CombinationType: str = '', Direction: str = '',
                 ProductID: str = '', Xparameter: float = 0.0, ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaDceCombInstrumentField, self).__init__()
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TradeGroupID = int(TradeGroupID)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.CombinationType = self._to_bytes(CombinationType)
        self.Direction = self._to_bytes(Direction)
        self.ProductID = self._to_bytes(ProductID)
        self.Xparameter = float(Xparameter)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaInvstMarginRateField(Base):
    """风险结算追平投资者期货保证金率"""
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('LongMarginRatioByMoney', ctypes.c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', ctypes.c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', ctypes.c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', ctypes.c_double),  # 空头保证金费
        ('IsRelative', ctypes.c_int),  # 是否相对交易所收取
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, InstrumentID: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', HedgeFlag: str = '', LongMarginRatioByMoney: float = 0.0,
                 LongMarginRatioByVolume: float = 0.0, ShortMarginRatioByMoney: float = 0.0, ShortMarginRatioByVolume: float = 0.0, IsRelative: int = 0, ActionDirection: str = '',
                 SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaInvstMarginRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaExchMarginRateField(Base):
    """风险结算追平交易所期货保证金率"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('LongMarginRatioByMoney', ctypes.c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', ctypes.c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', ctypes.c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', ctypes.c_double),  # 空头保证金费
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, BrokerID: str = '', InstrumentID: str = '', HedgeFlag: str = '', LongMarginRatioByMoney: float = 0.0, LongMarginRatioByVolume: float = 0.0, ShortMarginRatioByMoney: float = 0.0,
                 ShortMarginRatioByVolume: float = 0.0, ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaExchMarginRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaOptExchMarginField(Base):
    """风险结算追平中金现货期权交易所保证金率"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('SShortMarginRatioByMoney', ctypes.c_double),  # 投机空头保证金调整系数
        ('SShortMarginRatioByVolume', ctypes.c_double),  # 投机空头保证金调整系数
        ('HShortMarginRatioByMoney', ctypes.c_double),  # 保值空头保证金调整系数
        ('HShortMarginRatioByVolume', ctypes.c_double),  # 保值空头保证金调整系数
        ('AShortMarginRatioByMoney', ctypes.c_double),  # 套利空头保证金调整系数
        ('AShortMarginRatioByVolume', ctypes.c_double),  # 套利空头保证金调整系数
        ('MShortMarginRatioByMoney', ctypes.c_double),  # 做市商空头保证金调整系数
        ('MShortMarginRatioByVolume', ctypes.c_double),  # 做市商空头保证金调整系数
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, BrokerID: str = '', InstrumentID: str = '', SShortMarginRatioByMoney: float = 0.0, SShortMarginRatioByVolume: float = 0.0, HShortMarginRatioByMoney: float = 0.0,
                 HShortMarginRatioByVolume: float = 0.0, AShortMarginRatioByMoney: float = 0.0, AShortMarginRatioByVolume: float = 0.0, MShortMarginRatioByMoney: float = 0.0,
                 MShortMarginRatioByVolume: float = 0.0, ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaOptExchMarginField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.SShortMarginRatioByMoney = float(SShortMarginRatioByMoney)
        self.SShortMarginRatioByVolume = float(SShortMarginRatioByVolume)
        self.HShortMarginRatioByMoney = float(HShortMarginRatioByMoney)
        self.HShortMarginRatioByVolume = float(HShortMarginRatioByVolume)
        self.AShortMarginRatioByMoney = float(AShortMarginRatioByMoney)
        self.AShortMarginRatioByVolume = float(AShortMarginRatioByVolume)
        self.MShortMarginRatioByMoney = float(MShortMarginRatioByMoney)
        self.MShortMarginRatioByVolume = float(MShortMarginRatioByVolume)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaOptInvstMarginField(Base):
    """风险结算追平中金现货期权投资者保证金率"""
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('SShortMarginRatioByMoney', ctypes.c_double),  # 投机空头保证金调整系数
        ('SShortMarginRatioByVolume', ctypes.c_double),  # 投机空头保证金调整系数
        ('HShortMarginRatioByMoney', ctypes.c_double),  # 保值空头保证金调整系数
        ('HShortMarginRatioByVolume', ctypes.c_double),  # 保值空头保证金调整系数
        ('AShortMarginRatioByMoney', ctypes.c_double),  # 套利空头保证金调整系数
        ('AShortMarginRatioByVolume', ctypes.c_double),  # 套利空头保证金调整系数
        ('IsRelative', ctypes.c_int),  # 是否跟随交易所收取
        ('MShortMarginRatioByMoney', ctypes.c_double),  # 做市商空头保证金调整系数
        ('MShortMarginRatioByVolume', ctypes.c_double),  # 做市商空头保证金调整系数
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, InstrumentID: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', SShortMarginRatioByMoney: float = 0.0, SShortMarginRatioByVolume: float = 0.0,
                 HShortMarginRatioByMoney: float = 0.0, HShortMarginRatioByVolume: float = 0.0, AShortMarginRatioByMoney: float = 0.0, AShortMarginRatioByVolume: float = 0.0, IsRelative: int = 0,
                 MShortMarginRatioByMoney: float = 0.0, MShortMarginRatioByVolume: float = 0.0, ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaOptInvstMarginField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.SShortMarginRatioByMoney = float(SShortMarginRatioByMoney)
        self.SShortMarginRatioByVolume = float(SShortMarginRatioByVolume)
        self.HShortMarginRatioByMoney = float(HShortMarginRatioByMoney)
        self.HShortMarginRatioByVolume = float(HShortMarginRatioByVolume)
        self.AShortMarginRatioByMoney = float(AShortMarginRatioByMoney)
        self.AShortMarginRatioByVolume = float(AShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)
        self.MShortMarginRatioByMoney = float(MShortMarginRatioByMoney)
        self.MShortMarginRatioByVolume = float(MShortMarginRatioByVolume)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaInvstMarginRateULField(Base):
    """风险结算追平期权标的调整保证金率"""
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('LongMarginRatioByMoney', ctypes.c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', ctypes.c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', ctypes.c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', ctypes.c_double),  # 空头保证金费
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, InstrumentID: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', HedgeFlag: str = '', LongMarginRatioByMoney: float = 0.0,
                 LongMarginRatioByVolume: float = 0.0, ShortMarginRatioByMoney: float = 0.0, ShortMarginRatioByVolume: float = 0.0, ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaInvstMarginRateULField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaOptInvstCommRateField(Base):
    """风险结算追平期权手续费率"""
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', ctypes.c_double),  # 开仓手续费率
        ('OpenRatioByVolume', ctypes.c_double),  # 开仓手续费
        ('CloseRatioByMoney', ctypes.c_double),  # 平仓手续费率
        ('CloseRatioByVolume', ctypes.c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', ctypes.c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', ctypes.c_double),  # 平今手续费
        ('StrikeRatioByMoney', ctypes.c_double),  # 执行手续费率
        ('StrikeRatioByVolume', ctypes.c_double),  # 执行手续费
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, InstrumentID: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', OpenRatioByMoney: float = 0.0, OpenRatioByVolume: float = 0.0,
                 CloseRatioByMoney: float = 0.0, CloseRatioByVolume: float = 0.0, CloseTodayRatioByMoney: float = 0.0, CloseTodayRatioByVolume: float = 0.0, StrikeRatioByMoney: float = 0.0,
                 StrikeRatioByVolume: float = 0.0, ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaOptInvstCommRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.StrikeRatioByMoney = float(StrikeRatioByMoney)
        self.StrikeRatioByVolume = float(StrikeRatioByVolume)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaInvstCommRateField(Base):
    """风险结算追平期货手续费率"""
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', ctypes.c_double),  # 开仓手续费率
        ('OpenRatioByVolume', ctypes.c_double),  # 开仓手续费
        ('CloseRatioByMoney', ctypes.c_double),  # 平仓手续费率
        ('CloseRatioByVolume', ctypes.c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', ctypes.c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', ctypes.c_double),  # 平今手续费
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, InstrumentID: str = '', InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', OpenRatioByMoney: float = 0.0, OpenRatioByVolume: float = 0.0,
                 CloseRatioByMoney: float = 0.0, CloseRatioByVolume: float = 0.0, CloseTodayRatioByMoney: float = 0.0, CloseTodayRatioByVolume: float = 0.0, ActionDirection: str = '',
                 SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaInvstCommRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaProductExchRateField(Base):
    """风险结算追平交叉汇率"""
    _fields_ = [
        ('ProductID', ctypes.c_char * 81),  # 产品代码
        ('QuoteCurrencyID', ctypes.c_char * 4),  # 报价币种类型
        ('ExchangeRate', ctypes.c_double),  # 汇率
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, ProductID: str = '', QuoteCurrencyID: str = '', ExchangeRate: float = 0.0, ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaProductExchRateField, self).__init__()
        self.ProductID = self._to_bytes(ProductID)
        self.QuoteCurrencyID = self._to_bytes(QuoteCurrencyID)
        self.ExchangeRate = float(ExchangeRate)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaDepthMarketDataField(Base):
    """风险结算追平行情"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ExchangeInstID', ctypes.c_char * 81),  # 合约在交易所的代码
        ('LastPrice', ctypes.c_double),  # 最新价
        ('PreSettlementPrice', ctypes.c_double),  # 上次结算价
        ('PreClosePrice', ctypes.c_double),  # 昨收盘
        ('PreOpenInterest', ctypes.c_double),  # 昨持仓量
        ('OpenPrice', ctypes.c_double),  # 今开盘
        ('HighestPrice', ctypes.c_double),  # 最高价
        ('LowestPrice', ctypes.c_double),  # 最低价
        ('Volume', ctypes.c_int),  # 数量
        ('Turnover', ctypes.c_double),  # 成交金额
        ('OpenInterest', ctypes.c_double),  # 持仓量
        ('ClosePrice', ctypes.c_double),  # 今收盘
        ('SettlementPrice', ctypes.c_double),  # 本次结算价
        ('UpperLimitPrice', ctypes.c_double),  # 涨停板价
        ('LowerLimitPrice', ctypes.c_double),  # 跌停板价
        ('PreDelta', ctypes.c_double),  # 昨虚实度
        ('CurrDelta', ctypes.c_double),  # 今虚实度
        ('UpdateTime', ctypes.c_char * 9),  # 最后修改时间
        ('UpdateMillisec', ctypes.c_int),  # 最后修改毫秒
        ('BidPrice1', ctypes.c_double),  # 申买价一
        ('BidVolume1', ctypes.c_int),  # 申买量一
        ('AskPrice1', ctypes.c_double),  # 申卖价一
        ('AskVolume1', ctypes.c_int),  # 申卖量一
        ('BidPrice2', ctypes.c_double),  # 申买价二
        ('BidVolume2', ctypes.c_int),  # 申买量二
        ('AskPrice2', ctypes.c_double),  # 申卖价二
        ('AskVolume2', ctypes.c_int),  # 申卖量二
        ('BidPrice3', ctypes.c_double),  # 申买价三
        ('BidVolume3', ctypes.c_int),  # 申买量三
        ('AskPrice3', ctypes.c_double),  # 申卖价三
        ('AskVolume3', ctypes.c_int),  # 申卖量三
        ('BidPrice4', ctypes.c_double),  # 申买价四
        ('BidVolume4', ctypes.c_int),  # 申买量四
        ('AskPrice4', ctypes.c_double),  # 申卖价四
        ('AskVolume4', ctypes.c_int),  # 申卖量四
        ('BidPrice5', ctypes.c_double),  # 申买价五
        ('BidVolume5', ctypes.c_int),  # 申买量五
        ('AskPrice5', ctypes.c_double),  # 申卖价五
        ('AskVolume5', ctypes.c_int),  # 申卖量五
        ('AveragePrice', ctypes.c_double),  # 当日均价
        ('ActionDay', ctypes.c_char * 9),  # 业务日期
        ('BandingUpperPrice', ctypes.c_double),  # 上带价
        ('BandingLowerPrice', ctypes.c_double),  # 下带价
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, TradingDay: str = '', InstrumentID: str = '', ExchangeID: str = '', ExchangeInstID: str = '', LastPrice: float = 0.0, PreSettlementPrice: float = 0.0,
                 PreClosePrice: float = 0.0, PreOpenInterest: float = 0.0, OpenPrice: float = 0.0, HighestPrice: float = 0.0, LowestPrice: float = 0.0, Volume: int = 0, Turnover: float = 0.0,
                 OpenInterest: float = 0.0, ClosePrice: float = 0.0, SettlementPrice: float = 0.0, UpperLimitPrice: float = 0.0, LowerLimitPrice: float = 0.0, PreDelta: float = 0.0,
                 CurrDelta: float = 0.0, UpdateTime: str = '', UpdateMillisec: int = 0, BidPrice1: float = 0.0, BidVolume1: int = 0, AskPrice1: float = 0.0, AskVolume1: int = 0,
                 BidPrice2: float = 0.0, BidVolume2: int = 0, AskPrice2: float = 0.0, AskVolume2: int = 0, BidPrice3: float = 0.0, BidVolume3: int = 0, AskPrice3: float = 0.0, AskVolume3: int = 0,
                 BidPrice4: float = 0.0, BidVolume4: int = 0, AskPrice4: float = 0.0, AskVolume4: int = 0, BidPrice5: float = 0.0, BidVolume5: int = 0, AskPrice5: float = 0.0, AskVolume5: int = 0,
                 AveragePrice: float = 0.0, ActionDay: str = '', BandingUpperPrice: float = 0.0, BandingLowerPrice: float = 0.0, ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaDepthMarketDataField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.LastPrice = float(LastPrice)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)
        self.ClosePrice = float(ClosePrice)
        self.SettlementPrice = float(SettlementPrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.PreDelta = float(PreDelta)
        self.CurrDelta = float(CurrDelta)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.UpdateMillisec = int(UpdateMillisec)
        self.BidPrice1 = float(BidPrice1)
        self.BidVolume1 = int(BidVolume1)
        self.AskPrice1 = float(AskPrice1)
        self.AskVolume1 = int(AskVolume1)
        self.BidPrice2 = float(BidPrice2)
        self.BidVolume2 = int(BidVolume2)
        self.AskPrice2 = float(AskPrice2)
        self.AskVolume2 = int(AskVolume2)
        self.BidPrice3 = float(BidPrice3)
        self.BidVolume3 = int(BidVolume3)
        self.AskPrice3 = float(AskPrice3)
        self.AskVolume3 = int(AskVolume3)
        self.BidPrice4 = float(BidPrice4)
        self.BidVolume4 = int(BidVolume4)
        self.AskPrice4 = float(AskPrice4)
        self.AskVolume4 = int(AskVolume4)
        self.BidPrice5 = float(BidPrice5)
        self.BidVolume5 = int(BidVolume5)
        self.AskPrice5 = float(AskPrice5)
        self.AskVolume5 = int(AskVolume5)
        self.AveragePrice = float(AveragePrice)
        self.ActionDay = self._to_bytes(ActionDay)
        self.BandingUpperPrice = float(BandingUpperPrice)
        self.BandingLowerPrice = float(BandingLowerPrice)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaIndexPriceField(Base):
    """风险结算追平现货指数"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ClosePrice', ctypes.c_double),  # 指数现货收盘价
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, BrokerID: str = '', InstrumentID: str = '', ClosePrice: float = 0.0, ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaIndexPriceField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ClosePrice = float(ClosePrice)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SyncDeltaEWarrantOffsetField(Base):
    """风险结算追平仓单折抵"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日期
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('Direction', ctypes.c_char),  # 买卖方向
        ('HedgeFlag', ctypes.c_char),  # 投机套保标志
        ('Volume', ctypes.c_int),  # 数量
        ('ActionDirection', ctypes.c_char),  # 操作标志
        ('SyncDeltaSequenceNo', ctypes.c_int),  # 追平序号
    ]

    def __init__(self, TradingDay: str = '', BrokerID: str = '', InvestorID: str = '', ExchangeID: str = '', InstrumentID: str = '', Direction: str = '', HedgeFlag: str = '', Volume: int = 0,
                 ActionDirection: str = '', SyncDeltaSequenceNo: int = 0):
        super(SyncDeltaEWarrantOffsetField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.Direction = self._to_bytes(Direction)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Volume = int(Volume)
        self.ActionDirection = self._to_bytes(ActionDirection)
        self.SyncDeltaSequenceNo = int(SyncDeltaSequenceNo)


class SPBMFutureParameterField(Base):
    """SPBM期货合约保证金参数"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ProdFamilyCode', ctypes.c_char * 81),  # 品种代码
        ('Cvf', ctypes.c_int),  # 期货合约因子
        ('TimeRange', ctypes.c_char),  # 阶段标识
        ('MarginRate', ctypes.c_double),  # 品种保证金标准
        ('LockRateX', ctypes.c_double),  # 期货合约内部对锁仓费率折扣比例
        ('AddOnRate', ctypes.c_double),  # 提高保证金标准
        ('PreSettlementPrice', ctypes.c_double),  # 昨结算价
    ]

    def __init__(self, TradingDay: str = '', ExchangeID: str = '', InstrumentID: str = '', ProdFamilyCode: str = '', Cvf: int = 0, TimeRange: str = '', MarginRate: float = 0.0, LockRateX: float = 0.0,
                 AddOnRate: float = 0.0, PreSettlementPrice: float = 0.0):
        super(SPBMFutureParameterField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ProdFamilyCode = self._to_bytes(ProdFamilyCode)
        self.Cvf = int(Cvf)
        self.TimeRange = self._to_bytes(TimeRange)
        self.MarginRate = float(MarginRate)
        self.LockRateX = float(LockRateX)
        self.AddOnRate = float(AddOnRate)
        self.PreSettlementPrice = float(PreSettlementPrice)


class SPBMOptionParameterField(Base):
    """SPBM期权合约保证金参数"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ProdFamilyCode', ctypes.c_char * 81),  # 品种代码
        ('Cvf', ctypes.c_int),  # 期权合约因子
        ('DownPrice', ctypes.c_double),  # 期权冲抵价格
        ('Delta', ctypes.c_double),  # Delta值
        ('SlimiDelta', ctypes.c_double),  # 卖方期权风险转换最低值
        ('PreSettlementPrice', ctypes.c_double),  # 昨结算价
    ]

    def __init__(self, TradingDay: str = '', ExchangeID: str = '', InstrumentID: str = '', ProdFamilyCode: str = '', Cvf: int = 0, DownPrice: float = 0.0, Delta: float = 0.0, SlimiDelta: float = 0.0,
                 PreSettlementPrice: float = 0.0):
        super(SPBMOptionParameterField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ProdFamilyCode = self._to_bytes(ProdFamilyCode)
        self.Cvf = int(Cvf)
        self.DownPrice = float(DownPrice)
        self.Delta = float(Delta)
        self.SlimiDelta = float(SlimiDelta)
        self.PreSettlementPrice = float(PreSettlementPrice)


class SPBMIntraParameterField(Base):
    """SPBM品种内对锁仓折扣参数"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ProdFamilyCode', ctypes.c_char * 81),  # 品种代码
        ('IntraRateY', ctypes.c_double),  # 品种内合约间对锁仓费率折扣比例
    ]

    def __init__(self, TradingDay: str = '', ExchangeID: str = '', ProdFamilyCode: str = '', IntraRateY: float = 0.0):
        super(SPBMIntraParameterField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProdFamilyCode = self._to_bytes(ProdFamilyCode)
        self.IntraRateY = float(IntraRateY)


class SPBMInterParameterField(Base):
    """SPBM跨品种抵扣参数"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('SpreadId', ctypes.c_int),  # 优先级
        ('InterRateZ', ctypes.c_double),  # 品种间对锁仓费率折扣比例
        ('Leg1ProdFamilyCode', ctypes.c_char * 81),  # 第一腿构成品种
        ('Leg2ProdFamilyCode', ctypes.c_char * 81),  # 第二腿构成品种
    ]

    def __init__(self, TradingDay: str = '', ExchangeID: str = '', SpreadId: int = 0, InterRateZ: float = 0.0, Leg1ProdFamilyCode: str = '', Leg2ProdFamilyCode: str = ''):
        super(SPBMInterParameterField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.SpreadId = int(SpreadId)
        self.InterRateZ = float(InterRateZ)
        self.Leg1ProdFamilyCode = self._to_bytes(Leg1ProdFamilyCode)
        self.Leg2ProdFamilyCode = self._to_bytes(Leg2ProdFamilyCode)


class SyncSPBMParameterEndField(Base):
    """同步SPBM参数结束"""
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),  # 交易日
    ]

    def __init__(self, TradingDay: str = ''):
        super(SyncSPBMParameterEndField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)


class QrySPBMFutureParameterField(Base):
    """SPBM期货合约保证金参数查询"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ProdFamilyCode', ctypes.c_char * 81),  # 品种代码
    ]

    def __init__(self, ExchangeID: str = '', InstrumentID: str = '', ProdFamilyCode: str = ''):
        super(QrySPBMFutureParameterField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ProdFamilyCode = self._to_bytes(ProdFamilyCode)


class QrySPBMOptionParameterField(Base):
    """SPBM期权合约保证金参数查询"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('InstrumentID', ctypes.c_char * 81),  # 合约代码
        ('ProdFamilyCode', ctypes.c_char * 81),  # 品种代码
    ]

    def __init__(self, ExchangeID: str = '', InstrumentID: str = '', ProdFamilyCode: str = ''):
        super(QrySPBMOptionParameterField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ProdFamilyCode = self._to_bytes(ProdFamilyCode)


class QrySPBMIntraParameterField(Base):
    """SPBM品种内对锁仓折扣参数查询"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('ProdFamilyCode', ctypes.c_char * 81),  # 品种代码
    ]

    def __init__(self, ExchangeID: str = '', ProdFamilyCode: str = ''):
        super(QrySPBMIntraParameterField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProdFamilyCode = self._to_bytes(ProdFamilyCode)


class QrySPBMInterParameterField(Base):
    """SPBM跨品种抵扣参数查询"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('Leg1ProdFamilyCode', ctypes.c_char * 81),  # 第一腿构成品种
        ('Leg2ProdFamilyCode', ctypes.c_char * 81),  # 第二腿构成品种
    ]

    def __init__(self, ExchangeID: str = '', Leg1ProdFamilyCode: str = '', Leg2ProdFamilyCode: str = ''):
        super(QrySPBMInterParameterField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.Leg1ProdFamilyCode = self._to_bytes(Leg1ProdFamilyCode)
        self.Leg2ProdFamilyCode = self._to_bytes(Leg2ProdFamilyCode)


class SPBMPortfDefinitionField(Base):
    """组合保证金套餐"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('PortfolioDefID', ctypes.c_int),  # 组合保证金套餐代码
        ('ProdFamilyCode', ctypes.c_char * 81),  # 品种代码
        ('IsSPBM', ctypes.c_int),  # 是否启用SPBM
    ]

    def __init__(self, ExchangeID: str = '', PortfolioDefID: int = 0, ProdFamilyCode: str = '', IsSPBM: int = 0):
        super(SPBMPortfDefinitionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.PortfolioDefID = int(PortfolioDefID)
        self.ProdFamilyCode = self._to_bytes(ProdFamilyCode)
        self.IsSPBM = int(IsSPBM)


class SPBMInvestorPortfDefField(Base):
    """投资者套餐选择"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('PortfolioDefID', ctypes.c_int),  # 组合保证金套餐代码
    ]

    def __init__(self, ExchangeID: str = '', BrokerID: str = '', InvestorID: str = '', PortfolioDefID: int = 0):
        super(SPBMInvestorPortfDefField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.PortfolioDefID = int(PortfolioDefID)


class InvestorPortfMarginRatioField(Base):
    """投资者新型组合保证金系数"""
    _fields_ = [
        ('InvestorRange', ctypes.c_char),  # 投资者范围
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('MarginRatio', ctypes.c_double),  # 会员对投资者收取的保证金和交易所对投资者收取的保证金的比例
    ]

    def __init__(self, InvestorRange: str = '', BrokerID: str = '', InvestorID: str = '', ExchangeID: str = '', MarginRatio: float = 0.0):
        super(InvestorPortfMarginRatioField, self).__init__()
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.MarginRatio = float(MarginRatio)


class QrySPBMPortfDefinitionField(Base):
    """组合保证金套餐查询"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('PortfolioDefID', ctypes.c_int),  # 组合保证金套餐代码
        ('ProdFamilyCode', ctypes.c_char * 81),  # 品种代码
    ]

    def __init__(self, ExchangeID: str = '', PortfolioDefID: int = 0, ProdFamilyCode: str = ''):
        super(QrySPBMPortfDefinitionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.PortfolioDefID = int(PortfolioDefID)
        self.ProdFamilyCode = self._to_bytes(ProdFamilyCode)


class QrySPBMInvestorPortfDefField(Base):
    """投资者套餐选择查询"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
    ]

    def __init__(self, ExchangeID: str = '', BrokerID: str = '', InvestorID: str = ''):
        super(QrySPBMInvestorPortfDefField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class QryInvestorPortfMarginRatioField(Base):
    """投资者新型组合保证金系数查询"""
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
    ]

    def __init__(self, BrokerID: str = '', InvestorID: str = '', ExchangeID: str = ''):
        super(QryInvestorPortfMarginRatioField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class InvestorProdSPBMDetailField(Base):
    """投资者产品SPBM明细"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ProdFamilyCode', ctypes.c_char * 81),  # 品种代码
        ('IntraInstrMargin', ctypes.c_double),  # 合约内对锁保证金
        ('BCollectingMargin', ctypes.c_double),  # 买归集保证金
        ('SCollectingMargin', ctypes.c_double),  # 卖归集保证金
        ('IntraProdMargin', ctypes.c_double),  # 品种内合约间对锁保证金
        ('NetMargin', ctypes.c_double),  # 净保证金
        ('InterProdMargin', ctypes.c_double),  # 产品间对锁保证金
        ('SingleMargin', ctypes.c_double),  # 裸保证金
        ('AddOnMargin', ctypes.c_double),  # 附加保证金
        ('DeliveryMargin', ctypes.c_double),  # 交割月保证金
        ('CallOptionMinRisk', ctypes.c_double),  # 看涨期权最低风险
        ('PutOptionMinRisk', ctypes.c_double),  # 看跌期权最低风险
        ('OptionMinRisk', ctypes.c_double),  # 卖方期权最低风险
        ('OptionValueOffset', ctypes.c_double),  # 买方期权冲抵价值
        ('OptionRoyalty', ctypes.c_double),  # 卖方期权权利金
        ('RealOptionValueOffset', ctypes.c_double),  # 价值冲抵
        ('Margin', ctypes.c_double),  # 保证金
        ('ExchMargin', ctypes.c_double),  # 交易所保证金
    ]

    def __init__(self, ExchangeID: str = '', BrokerID: str = '', InvestorID: str = '', ProdFamilyCode: str = '', IntraInstrMargin: float = 0.0, BCollectingMargin: float = 0.0,
                 SCollectingMargin: float = 0.0, IntraProdMargin: float = 0.0, NetMargin: float = 0.0, InterProdMargin: float = 0.0, SingleMargin: float = 0.0, AddOnMargin: float = 0.0,
                 DeliveryMargin: float = 0.0, CallOptionMinRisk: float = 0.0, PutOptionMinRisk: float = 0.0, OptionMinRisk: float = 0.0, OptionValueOffset: float = 0.0, OptionRoyalty: float = 0.0,
                 RealOptionValueOffset: float = 0.0, Margin: float = 0.0, ExchMargin: float = 0.0):
        super(InvestorProdSPBMDetailField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ProdFamilyCode = self._to_bytes(ProdFamilyCode)
        self.IntraInstrMargin = float(IntraInstrMargin)
        self.BCollectingMargin = float(BCollectingMargin)
        self.SCollectingMargin = float(SCollectingMargin)
        self.IntraProdMargin = float(IntraProdMargin)
        self.NetMargin = float(NetMargin)
        self.InterProdMargin = float(InterProdMargin)
        self.SingleMargin = float(SingleMargin)
        self.AddOnMargin = float(AddOnMargin)
        self.DeliveryMargin = float(DeliveryMargin)
        self.CallOptionMinRisk = float(CallOptionMinRisk)
        self.PutOptionMinRisk = float(PutOptionMinRisk)
        self.OptionMinRisk = float(OptionMinRisk)
        self.OptionValueOffset = float(OptionValueOffset)
        self.OptionRoyalty = float(OptionRoyalty)
        self.RealOptionValueOffset = float(RealOptionValueOffset)
        self.Margin = float(Margin)
        self.ExchMargin = float(ExchMargin)


class QryInvestorProdSPBMDetailField(Base):
    """投资者产品SPBM明细查询"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('ProdFamilyCode', ctypes.c_char * 81),  # 品种代码
    ]

    def __init__(self, ExchangeID: str = '', BrokerID: str = '', InvestorID: str = '', ProdFamilyCode: str = ''):
        super(QryInvestorProdSPBMDetailField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ProdFamilyCode = self._to_bytes(ProdFamilyCode)


class PortfTradeParamSettingField(Base):
    """组保交易参数设置"""
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),  # 交易所代码
        ('BrokerID', ctypes.c_char * 11),  # 经纪公司代码
        ('InvestorID', ctypes.c_char * 13),  # 投资者代码
        ('Portfolio', ctypes.c_char),  # 新型组保算法
        ('IsActionVerify', ctypes.c_int),  # 撤单是否验资
        ('IsCloseVerify', ctypes.c_int),  # 平仓是否验资
    ]

    def __init__(self, ExchangeID: str = '', BrokerID: str = '', InvestorID: str = '', Portfolio: str = '', IsActionVerify: int = 0, IsCloseVerify: int = 0):
        super(PortfTradeParamSettingField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Portfolio = self._to_bytes(Portfolio)
        self.IsActionVerify = int(IsActionVerify)
        self.IsCloseVerify = int(IsCloseVerify)
