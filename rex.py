import re

html = '<img src="/images/category.png"><img src="/images/js_framework.png">'
# 非贪婪匹配
rex = r'<img.*?src="(.*?)">'
print(re.findall(rex, html))

# 贪婪匹配（前img -> 后src）
rex2 = r'<img.*src="(.*?)">'
print(re.findall(rex2, html))
