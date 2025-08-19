import os
import asyncio
import random
import telegram

# --- 从环境变量中读取配置，更安全 ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
TARGET_CHAT_ID = int(os.environ.get("TARGET_CHAT_ID"))
MESSAGE_TO_SEND = "/keng"

async def main():
    bot = telegram.Bot(token=BOT_TOKEN)
    print("Bot已启动，准备开始发送消息...")
    print(f"目标聊天ID: {TARGET_CHAT_ID}")

    while True:
        delay = random.uniform(1, 5)
        print(f"下次发送倒计时: {delay:.2f} 秒...")
        await asyncio.sleep(delay)
        
        try:
            await bot.send_message(chat_id=TARGET_CHAT_ID, text=MESSAGE_TO_SEND)
            print(f"消息 '{MESSAGE_TO_SEND}' 已发送。")
        except Exception as e:
            print(f"发送消息失败: {e}")

if __name__ == "__main__":
    # 首次运行时获取一下Chat ID的提示
    if not TARGET_CHAT_ID:
        print("错误: 环境变量 TARGET_CHAT_ID 未设置！")
    else:
        asyncio.run(main())
