try:
    import ujson as json
except ImportError:
    import json
from pathlib import Path

DATABASE = Path() / "data" / "xiuxian"

class XiuConfig:

    def __init__(self):


        self.level = list(USERRANK.keys())
        self.level_up_cd = 60  # 突破CD(分钟)
        self.closing_exp = 30  # 闭关每分钟获取的修为
        self.closing_exp_upper_limit = 1.5  # 闭关获取修为上限（例如：1.5 下个境界的修为数*1.5）
        self.level_punishment_floor = 1  # 突破失败扣除修为，惩罚下限（百分比）
        self.level_punishment_limit = 10  # 突破失败扣除修为，惩罚上限(当前实例：10%)
        self.level_up_probability = 0.3  # 突破失败增加当前境界突破概率的比例
        self.sign_in_lingshi_lower_limit = 500  # 每日签到灵石下限
        self.sign_in_lingshi_upper_limit = 5000  # 每日签到灵石上限
        self.sign_in_xiuwei_lower_limit = 10000  # 每日签到修为下限
        self.sign_in_xiuwei_upper_limit = 100000  # 每日签到修为上限
        self.tou = 600 # 偷灵石惩罚
        self.tou_lower_limit = 200  # 偷灵石下限
        self.tou_upper_limit = 2000 # 偷灵石上限
        self.remake = 1000  # 重入仙途的消费
        self.sect_min_level = "渡劫境初期"  # 创建宗门的最低修为等级要求
        self.sect_create_cost = 25  # 创建宗门的最低修为等级要求
        self.user_info_cd = 10  # 我的修仙信息查询cd
        self.user_info_cd_msg = 5
        self.dufang_cd_msg = 5
        self.tou_cd = 5  # 偷灵石CD
        self.battle_boss_cd = 60  # 讨伐bossCD
        self.version = "xiuxian_1.1"

        self.sql_table = ["user_xiuxian", "user_cd", "sects", "back", "BuffInfo"]  # 数据库表校验
        self.sql_user_xiuxian = ["level_up_rate","sect_id","sect_position"
                                 ,"hp", "mp", "atk", "atkpractice", "sect_task",
                                "sect_contribution","sect_elixir_get", 
                                "blessed_spot_flag","blessed_spot_name"]   # 数据库字段校验
        self.sql_sects = ["sect_materials", "mainbuff", "secbuff", "elixir_room_level"]
        self.sql_buff = ["armor_buff", "atk_buff", "blessed_spot"]
        self.sql_back = ["bind_num"]
        self.img = True #是否全部转为简单图片发送

        # sql_table: ["user_xiuxian", "user_cd", "sects", "back", "BuffInfo"]  # 数据库表校验
        # sql_user_xiuxian: ["level_up_rate", "sect_id", "sect_position", "hp", "mp", "atk", "atkpractice",
        #                    "sect_task"]  # 数据库字段校验
        # sql_sects: ["sect_materials", "mainbuff", "secbuff"]



class JsonConfig:
    def __init__(self):
        self.config_jsonpath = DATABASE / "config.json"


    def read_data(self):
        """配置数据"""
        with open(self.config_jsonpath, 'r', encoding='utf-8') as e:
            data = json.load(e)
            return data

    def write_data(self, key, group_id=None):
        """
        说明：设置抢灵石开启或关闭
        参数：
            key：抢灵石1为开启，2为关闭
            key: 群聊1为开启，2为关闭
        """

        json_data = self.read_data()

        if key == 1:
            json_data['qiang'] = True
        if key == 2:
            json_data['qiang'] = False

        if key == 3 or key == 4:
            try:
                dd = json_data['group']
                if key == 4:
                    dd.append(group_id)
                if key == 3:
                    try:
                        dd.remove(group_id)
                    except ValueError:
                        print('删除数据失败')
                        return False
            except KeyError:
                json_data['group'] = [group_id]

        with open(self.config_jsonpath, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)

USERRANK = {
    '江湖好手':50,
    '练气境初期':49,
    '练气境中期':48,
    '练气境圆满':47,
    '筑基境初期':46,
    '筑基境中期':45,
    '筑基境圆满':44,
    '结丹境初期':43,
    '结丹境中期':42,
    '结丹境圆满':41,
    '元婴境初期':40,
    '元婴境中期':39,
    '元婴境圆满':38,
    '化神境初期':37,
    '化神境中期':36,
    '化神境圆满':35,
    '炼虚境初期':34,
    '炼虚境中期':33,
    '炼虚境圆满':32,
    '合体境初期':31,
    '合体境中期':30,
    '合体境圆满':29,
    '大乘境初期':28,
    '大乘境中期':27,
    '大乘境圆满':26,
    '渡劫境初期':25,
    '渡劫境中期':24,
    '渡劫境圆满':23,
    '半步真仙':22,
    '真仙境初期':21,
    '真仙境中期':20,
    '真仙境圆满':19,
    '金仙境初期':18,
    '金仙境中期':17,
    '金仙境圆满':16,
    '太乙境初期':15,
    '太乙境中期':14,
    '太乙境圆满':13,
    '悟道境':12,
}

if __name__ == '__main__':
    pathname = r""
    with open(pathname, 'r', encoding='utf-8') as e:
        data = json.load(e)

    key = 4


    if key == 1:
        data['qiang'] = True
    if key == 2:
        data['qiang'] = False
    if key == 3 or key == 4:
        try:
            dd = data['group']
            if key == 3:
                dd.append('223')
            if key == 4:
                try:
                    dd.remove('123')
                except ValueError:
                    print('bbbb')
        except KeyError:
            data['group'] = []

    with open(pathname, 'w', encoding='utf-8') as f:
        json.dump(data, f)
