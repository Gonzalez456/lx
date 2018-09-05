# import requests
# from hashlib import md5
# import os
# url = 'https://p9.pstatp.com/origin/32200003fa49157fc515'
# Headers = {
#         'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)'
# }
# request = requests.get(url, headers=Headers)
# con = request.content
#
# path = '{0}/{1}.{2}'.format(os.getcwd(),md5(con).hexdigest(),'jpg')
# if not os.path.exists(path):
#     with open(path,'wb') as f:
#         f.write(con)
# list = ['p9.pstatp.com\\/origin\\/32200003fa49157fc515',
#         'p1.pstatp.com\\/origin\\/32200003fa563c60b75f',
#         'p3.pstatp.com\\/origin\\/32200003fa5ca72aad5b',
#         'p3.pstatp.com\\/origin\\/32250003f82952d9e40f',
#         'p3.pstatp.com\\/origin\\/32250003f8371852a754',
#         'p3.pstatp.com\\/origin\\/321900041d6b9596fcf4']
# for i in range(len(list)):
#     print(list[i].replace('\\', ''))
for i in range(0,200,20):
    print(i)