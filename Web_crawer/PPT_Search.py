import urllib.request as req
import bs4
import time


def GetData(url, target, num_page):

    Request = req.Request(url, headers = {
        'user-agent' :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'cookie' : 'GA1.2.1987286987.1623594711; _gid=GA1.2.558976360.1627289137; __cf_bm=25e99f513cf024479be0f4b98a3c48e864bd23c5-1627372881-1800-AZbR857Yn9ujH00vf9v6gER2hC+Ij6OX4HJKxzoyg+vFrYaaATSnI0w1AxcWAyoUdRk3LnXwtsQlS/cV6P2X6+U=; over18=1; _gat=1'
    })

    with req.urlopen(Request) as response :
        data = response.read().decode('utf-8')

    bs4data = bs4.BeautifulSoup(data, 'html.parser')
    titles = bs4data.find_all('div', class_= 'title')

    for title in titles:
        if title.a != None:
            if title.a.string.find(target) >= 0 :
                print('-----'*10 )
                print('Page.%d' %num_page) 
                print(title.a.string)
                print('https://www.ptt.cc/'+ title.a['href'])
                print('-----'*10+'\n')

    nextlink = bs4data.find('a', string= '‹ 上頁')
    return nextlink['href']


Again_variable = 'y'
while True :

    if Again_variable == 'Y' or Again_variable == 'y':
        
        times = int(input('Please tell me how much of pages you wanna search: '))
        target = str(input('Please tell me what title you wanna find: '))
        which_url = input('Which website is that you wanna search(1.Gossping/2.C_Chat)? (1/2) ')

        while True :

            if which_url == '1':
                url = 'https://www.ptt.cc/bbs/Gossiping/index.html' 
                break
            elif which_url == '2': 
                url = 'https://www.ptt.cc/bbs/C_Chat/index.html'
                break
            else:
                print('Wrong information that you give.')
                which_url = input('Which website is that you wanna search(1.Gossping/2.C_Chat)? (1/2) ')

        t1 = time.time()


        print('\n'*3)
        print('The results: ')


        # url = 'https://www.ptt.cc/bbs/Gossiping/index.html' 
        for t in range(1, times+1):
                url = 'https://www.ptt.cc' + GetData(url, target, t) 
            


        t2 = time.time()

        print('END','\n'*1)
        print('Total tims: %0.1f seconds' %(t2-t1))
        Again_variable = input('Would you wanna use this program again? (Y/N)')

    elif Again_variable == 'N' or Again_variable == 'n':
        break
    else: 
        print('Enter the wrong')
        Again_variable = input('Would you wanna use this program again? (Y/N)')

# print(titles)

