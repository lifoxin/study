from selenium import webdriver


d = webdriver.Chrome()
d.implicitly_wait(10)     #10s超时

d.set_window_position(20,40)   #虚拟一个页面可见
d.set_window_size(1100,700)

d.get("http://xxx.com")  #打开浏览器

d.find_element_by_id('username').send_keys('xxxx')               #输入账号密码
d.find_element_by_id('password_input').send_keys('xxxx')

d.find_element_by_id('login_button').click()        #点击登录
d.find_element_by_id('checkout_btn').click()        #点击签出


print("successful")
