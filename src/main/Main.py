import Websocket
import time
import tools.TimeTools as TimeTools
import tools.ConsoleTools as ConsoleTools

# 变量
name = '"千樱 Cherrybot"'
connection = Websocket.Websocket(name)
check_in = '{"name":' + name + ',"type":"init","group":"idns_cn","country":"CN","lastMessageId":"' + str(
    connection.message_Id2) + '", "date":"' + str(
    TimeTools.getTimeStamp()) + '","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"}'


def run():
    try:
        ws_status = connection.websocketConnection()  # 连接ws
        if ws_status == 101:
            connection.sendFirstRequest(check_in)  # 注册bot的用户名和信息
            counter = 0
            while counter < 101:
                a = connection.getMessage()
                counter += 1  # 过滤历史消息
            while True:
                cut_message = connection.noticeMessage()
                text = connection.processMessage()
                if text is not None:
                    # print(text)
                    connection.sendMessage(text)
                time.sleep(0.05)
    except Exception:
        connection.ws.close()
        print(f"{ConsoleTools.console_colour('ERROR')}:发生错误，连接关闭。")
    finally:
        print(f"{ConsoleTools.console_colour('INFO')}:返回值 0。正在尝试重启:")
        return 0


if __name__ == "__main__":
    r = run()
    while r == 0:
        run()
