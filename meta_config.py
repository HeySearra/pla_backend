import re

DEBUG = True
CHAT_DEBUG = True

SPIDER_DATA_DIRNAME = '/home/pla_backend/pla_backend/spiders_data'
BULK_CREATE_BATCH_SIZE = 4096

HOST_IP = 'localhost'

CLS_PARSE_REG = re.compile(r"['](.*?)[']", re.S)

KB = 1 << 10
MB = KB * KB
GB = KB * MB
NOSQL_ID_LENGTH = 128

APPLY_status = (
    (0, '未处理'),
    (1, '未通过'),
    (2, '已通过'),
)

APPLY_type = (
    (0, '其他'),
    (1, '修改'),
    (2, '删除'),
    (3, '新增'),
    (4, '冒领'),
)

TIME_FMT = '%Y-%m-%d %H:%M:%S'

ROOT_SUFFIX = '' # '\'s root'

HELL_WORDS = ['哦', '呀', '啊', '嘤', '惹', '呢', '！', '哼', '~', '嗷', '嘻', '¿', '🐴', '🐋', '🐟']
