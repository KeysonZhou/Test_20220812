import logging
from config.config import log_path

logger=logging.getLogger()
logger.setLevel(logging.INFO) ##定义日志器的级别
format=logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s ")
# '''
# format的格式：
# %(asctime)s  字符串形式的当前时间，默认格式为“2022-07-30”
# %(name)s     logger的名字
# %(levelname)s 文本日志的级别
# %(filename)s 调用日志的文件名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d  调用日志输出函数的语句所在的代码行
# %(message)s 用户输出的消息
# '''
f=logging.FileHandler(log_path,mode='a',encoding='utf-8')
f.setLevel(logging.INFO)
f.setFormatter(format)
logger.addHandler(f)