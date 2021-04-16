import pytest
from api.api import Api
from tools.common_assert import common_assert
from tools.file_tool import FileTool
from tools.get_log import GetLog

log = GetLog.get_logger()


class Test01:
    # 1.实例化获取工具类对象
    tool = FileTool("sign.xlsx")

    # 2.读取excel-->将数据从excel中读取并写入到json中
    tool.read_excel()

    @pytest.mark.parametrize("case", tool.read_json())
    # 3.测试方法
    def test01(self, case):
        log.info("正在调用执行数据:{}".format(case))
        try:
            # 1.调用执行接口方法
            r = Api(case).run_method()
            print("响应数据为:", r.json())

            # 2.断言
            common_assert(r, case)

            # 3.将执行结果写入报告
            Test01.tool.write_excel(case.get("x_y"), "执行通过!")
        except Exception as e:
            Test01.tool.write_excel(case.get("x_y"), "执行失败! 原因:{}".format(e))
            log.error("错误,原因：{}".format(e))
            raise


# if __name__ == '__main__':
#     pytest.main()
