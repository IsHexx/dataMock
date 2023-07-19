"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Project : Demo
@File : mock.py
@Time : 2023/4/26 14:28
"""
import datetime
import random
import faker

from succutils.sucreditcode import CreditIdentifier


class MockData:

    def __init__(self):
        # Create a Faker instance once to avoid repeated initialization
        self.fake = faker.Faker(locale='zh_CN')
        # Create a CreditIdentifier instance once to avoid repeated initialization
        self.ci = CreditIdentifier()
        self.data = []

    def run_loop(self, method, n):
        """
        :param method: 方法名
        :param n: 循环次数
        :return: None
        """
        func = getattr(self, method)
        for i in range(n):
            self.data.append(func())
        return self.data

    def get_fixed_time(self):
        """
        :return:返回固定时间
        """
        time = datetime.datetime(year=2022, month=8, day=23, hour=10, minute=29, second=30)
        return time

    def get_today_date(self):
        """
        :return: 返回当日日期 格式：YYYY-MM-DD
        """
        date = datetime.date.today()
        return date

    def get_current_datetime(self):
        """
        :return: 返回当前时间 日期格式：YYYY-MM-DD H24:dd:ss
        """
        date = datetime.datetime.now().replace(microsecond=0)
        return date

    def generate_name(self):
        """
        :return:返回任意中文姓名
        """
        # Use the Faker instance instead of creating a new one
        return self.fake.name()

    def generate_phone_number(self):
        """
        :return: 返回中国电话号码
        """
        # Use the Faker instance instead of creating a new one
        data = self.fake.phone_number()
        return data

    def generate_random_float(self, n):
        """
        :return: 返回指定位数的小数
        """
        # Use the Faker instance instead of creating a new one
        return self.fake.pyfloat(left_digits=n, right_digits=2, positive=True)

    def generate_bank_card_number(self):
        """
        :return: 返回银行卡号
        """
        # Use the Faker instance instead of creating a new one
        return self.fake.credit_card_number()

    def generate_ssn(self):
        """
        :return: 返回身份证号码
        """
        # Use the Faker instance instead of creating a new one
        return self.fake.ssn()

    def generate_organization_code(self):
        """
        :return: 组织机构代码
        """
        # Use f-string instead of string concatenation for better readability and performance
        data = f"{random.randint(20000000, 99999999)}-{random.choice('123456789')}"
        return data

    def generate_credit_code(self):
        """
        :return: 统一社会信用代码
        """
        # Use the CreditIdentifier instance instead of creating a new one
        data = self.ci.gen_random_credit_code()
        return data["code"]

    def get_email(self):
        """
        :return: 邮箱
        """
        # Use the CreditIdentifier instance instead of creating a new one

        return self.fake.ascii_free_email()

    def generate_long_string(self):
        a = "超长字符串"
        return a


if __name__ == '__main__':
    # 创建一个DebugTalk的实例
    dt = MockData()
    # print(dt.run_loop("generate_random_float", 5))
    for i in range(100):
        print(dt.generate_organization_code())
