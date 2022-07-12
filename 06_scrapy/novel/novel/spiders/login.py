import scrapy

# option 1: override the start_requests method
# class LoginSpider(scrapy.Spider):
#     name = 'login'
#     allowed_domains = ['17k.com']
#     start_urls = ['https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919']
#
#     # override the start_requests method
#     def start_requests(self):
#         dic = {}
#         cookies = "GUID=8a7a2b6f-550a-46e3-a8dc-c47b969e8909; c_referer_17k=https://www.google.com/; _openId=ow-yN5u-1A_61aMgeQ0gYzmG1F-w; accessToken=nickname%3D%25E4%25B9%25A6%25E5%258F%258B7E5923W6J%26avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F12%252F32%252F55%252F97205532.jpg-88x88%253Fv%253D1656752124004%26id%3D97205532%26e%3D1672304124%26s%3D762171b7391aaf2d; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2297205532%22%2C%22%24device_id%22%3A%22181be132b5918f-025b9bcb7609ad-1c525635-2211840-181be132b5a9f3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%228a7a2b6f-550a-46e3-a8dc-c47b969e8909%22%7D"
#         # need key : value
#         for item in cookies.split("; "):
#             key, value = item.split("=")
#             dic[key] = value
#         for url in self.start_urls:
#             yield scrapy.Request(url, dont_filter=True, cookies=dic)
#
#     def parse(self, response, **kwargs):
#         print(response.text)

# option 2: Simulate login
class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['17k.com']
    start_urls = ['https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919']

    def start_requests(self):
        login_url = "https://passport.17k.com/ck/user/login"
        # option: 1
        yield scrapy.Request(
            url=login_url,
            method="POST",
            body="loginName=16538989670&password=q6035945",
            callback=self.login_success
        )
        # option 2:
        # yield scrapy.FormRequest(
        #     url=login_url,
        #     method="POST",
        #     formdata={
        #         "loginName": "16538989670",
        #         "password": "q6035945",
        #     },
        #     callback=self.login_success
        # )

    def login_success(self, resp, **kwargs):
        # print(resp.text)
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)

    def parse(self, response, **kwargs):
        print(response.text)
