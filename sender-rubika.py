from rubpy import Client
import asyncio

bot = Client(name="silent")

groups = [
    "g0FZp8o0c2953ddaa102aec72ca9ba82",
    "g0FZp8o0c2953ddaa102aec72ca9ba82",
    "g0FZp8o0c2953ddaa102aec72ca9ba82",
    "g0FZp8o0c2953ddaa102aec72ca9ba82",
    "g0DKivy0fa97db12fdc9383a491fb9bd"
]

async def send_message():
    while True:
        for group in groups:
            try:
                await bot.send_message(group, "سلام")
            except Exception as e:
                print(f"خطا در ارسال به گروه {group}: {e}")
            await asyncio.sleep(11)

async def main():
    await bot.start()
    await send_message()

if __name__ == "__main__":
    bot.run(main())