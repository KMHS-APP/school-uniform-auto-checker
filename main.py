import httpx
import toml
from datetime import datetime
import schedule
import time
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
User_Agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0'}


def main():
    now = datetime.now()

    with open('/user.toml', 'r') as f:
        user = toml.load(f)
        f.close()

    for i in user:
        data = {
            'entry.290613730_month': str(now.month),
            'entry.290613730_day': str(now.day),
            'entry.715331670': user[i]['class_number'],
            'entry.1292140636': user[i]['name'],
            'entry.792502709': '○',
            'entry.792502709_sentinel': '',
        }

        response = httpx.post(
            'https://docs.google.com/forms/d/e/1FAIpQLSeWfs5fKncHCanFnMwLtSFZqM48_itkB91a9rFdqvp086ASeA/formResponse',
            data=data,
            headers=User_Agent
        )

        if "응답이 기록되었습니다." in response.text:
            print("성공적으로 제출되었습니다.")
        else:
            print("제출에 실패했습니다.")
            print(response.text)
    
    return logging.info("Main function executed.")


def job():
    try:
        main()
    except Exception as e:
        logging.error(f"Error executing main function: {e}")


schedule.every().day.at("09:00").do(job)


if __name__ == '__main__':
    main()
    while True:
        schedule.run_pending()
        time.sleep(60)
