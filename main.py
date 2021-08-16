import datetime
now_time = datetime.datetime.now()

if __name__ == "__main__":
    print(f"Welcome to meet Vscode, it's {now_time.strftime('%Y年%m月%d日 %H时%M分%S秒')}")
