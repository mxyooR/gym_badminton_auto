import logging
import os

import os

base_dir = os.getcwd()  # 使用当前工作目录
log_path = os.path.join(base_dir, 'log.log')




def setup_logger(log_file=log_path):
    """设置自定义日志记录器"""
    logger = logging.getLogger('custom_logger')
    logger.setLevel(logging.INFO)

    # 检查日志记录器是否已经有处理程序，避免重复记录
    if not any(isinstance(handler, logging.FileHandler) for handler in logger.handlers):
        formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # 文件处理程序，使用 UTF-8 编码写入文件
        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # 控制台处理程序
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        print(f"日志记录器已设置，日志文件: {log_file}")

def log_message(message):
    """记录日志信息"""
    logger = logging.getLogger('custom_logger')
    logger.info(message)

def clear_log():
    """清空日志文件"""
    print("日志path",log_path)
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write('')
    print("日志文件已清空")

