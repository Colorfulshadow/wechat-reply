"""
@Author: Tianyi Zhang
@Date: 2025/1/17
@Description: 主要脚本
"""

import itchat

# 设置群名和要监听的用户名,若ID存在，名无效
target_room = ""
target_user = ""
# 获取群ID
room_id = None
user_id = None  # 我们会在启动时获取用户ID

# 获取指定群的群ID
def get_chatroom_id(room_name):
    chatrooms = itchat.get_chatrooms(update=True)
    for room in chatrooms:
        if target_room in room['NickName']:
            return room['UserName']
    return None

# 获取指定用户的ID
def get_user_id(username, chatroom_id):
    room = itchat.update_chatroom(chatroom_id, detailedMember=True)
    for member in room['MemberList']:
        if target_user in member['NickName']:
            return member['UserName']
    return None

@itchat.msg_register('Text', isGroupChat=True)
def text_reply(msg):
    global room_id
    global user_id

    if room_id is None:
        room_id = get_chatroom_id(target_room)
        if room_id is None:
            print(f"未找到群: {target_room}")
            return

    if user_id is None:
        user_id = get_user_id(target_user, room_id)
        if user_id is None:
            print(f"未找到: {target_user}")
            return

    if msg['FromUserName'] == room_id:
        if msg['ActualUserName'] == user_id:
            # 测试用途
            print(f"收到目标用户消息: {msg['Text']}")
            return msg['Text']

itchat.auto_login(hotReload=True)
itchat.run()