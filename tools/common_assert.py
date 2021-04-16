from tools.get_log import GetLog
log = GetLog.get_logger()


def common_assert(response, case):
    log.info("正在调用断言公共方法")
    # 获取响应数据
    result = response.json()
    print('result%s' % result)

    # 获取预期数据
    expect = case.get("expect")
    print('except%s' % expect)

    # 断言 code
    # assert result.get("status") == expect.get("status")

    # 断言 message
    # assert result.get("message") == expect.get("message")

    # 断言 status
    assert result.get("status") == expect.get("status"), "错误! 响应status:{} 预期status:{}".format(
        result.get("status"), expect.get("status"))

    assert result.get("message") == expect.get("message"), "错误! 响应message:{} 预期message:{}".format(
        result.get("message"), expect.get("message"))
