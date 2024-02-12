import os
import dotenv
import json

dotenv.load_dotenv()

BASE_BODY1 = os.getenv('BASE_BODY')
BASE_HEADERS1 = os.getenv('BASE_HEADERS')
BASE_URL1 = os.getenv('BASE_URL')

print(BASE_URL1)
print(BASE_HEADERS1)
print(BASE_BODY1)
print(os.getcwd())

BASE_BODY = json.loads(str(os.getenv('BASE_BODY')))
BASE_HEADERS = json.loads(str(os.getenv('BASE_HEADERS')))
print(f'BASE_BODY= {BASE_BODY}')
