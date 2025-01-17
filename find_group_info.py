"""
@Author: Tianyi Zhang
@Date: 2025/1/17
@Description: 用于查找群ID，保存群info
"""
import itchat
import json
from datetime import datetime

group_name_include = ""

itchat.auto_login(hotReload=True)
chatrooms = itchat.get_chatrooms(update=True)
target_groups_data = []
for chatroom in chatrooms:
    if group_name_include in chatroom['NickName']:
        print("群基本信息:")
        for key, value in chatroom.items():
            if isinstance(value, (list, dict)):
                print(f"{key}: [包含 {len(value)} 个元素]")
            else:
                print(f"{key}: {value}")
        print("=" * 50)
        target_groups_data.append(chatroom)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"group_data_{timestamp}.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(target_groups_data, f, ensure_ascii=False, indent=2)
print(f"\n数据已保存到文件: {filename}")

itchat.run()