password = 'a123456'
while true:
    pwd = input('請施入密碼:')
    if pwd == password:
       print('登入成功')
       break
    else:
        x = x-1
        print('密碼錯誤!還有',x,'次機會!)
        if x == 0:
            break