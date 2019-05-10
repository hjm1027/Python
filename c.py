import requests 
from bs4 import BeautifulSoup 
url = 'http://spoc.ccnu.edu.cn/starmoocHomepage' 
my_header = {'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36', } 
un = input('Username: ') 
pw = input('Password: ') 
data = { 'username': un, 'password': pw, 'lsession': 1 } 
Soj_session = requests.session() 
res = Soj_session.post(url + '/action.php?act=Login', data=data, headers=my_header)

res2 = Soj_session.get('http://spoc.ccnu.edu.cn/starmoocHomepage')   

