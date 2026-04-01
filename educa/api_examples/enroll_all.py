import requests

username = 'Ron'
password = 'Coffee.1'

base_url = 'http://127.0.0.1:8000/api/'
url = f'{base_url}courses/'
available_courses = []

print(f'Loading courses from {url}')
r = requests.get(url)
response = r.json()

# 判断返回格式
if isinstance(response, list):
    # 直接列表
    courses = response
    url = None
else:
    # 分页格式
    courses = response.get('results', [])
    url = response.get('next')

# 处理当前页课程
for course in courses:
    available_courses.append(course['title'])

# 如果有下一页，继续加载
while url:
    print(f'Loading courses from {url}')
    r = requests.get(url)
    response = r.json()
    courses = response.get('results', [])
    for course in courses:
        available_courses.append(course['title'])
    url = response.get('next')

print(f'Available courses: {", ".join(available_courses)}')