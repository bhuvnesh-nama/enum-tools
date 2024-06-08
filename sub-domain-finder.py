import requests
from pathlib import Path

path = Path()/'report.txt'

def find_subdomain(domain):
    res = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
    return res.json()

def generate_report(data):
    file = open(path, 'w')
    file.write('')
    file.close()
    with open(path, 'a+') as file:
        for entry in data:
            file.write(f"{entry['name_value']}\n")

if __name__ == '__main__':
    try:
        domain = input('Enter domain : ')
        json_data = find_subdomain(domain=domain)
        generate_report(json_data)
        print(f'report generated successfully {path}')
    except Exception as e:
        print(f'error occured while processing your request {e}')
