from bs4 import BeautifulSoup
import requests
import smtplib


class Tracker:
    def __init__(self,url):
        self.url=url
        #print(self.url)
    def track(self):
        params = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        response = requests.get(self.url, headers=params)
        response_text = response.text

        soup = BeautifulSoup(response_text, "html.parser")
        price = soup.find(name="span",class_="a-offscreen").getText()
        #print(soup.prettify())
        #print(price)
        split_price_symbol = price[1:]
        #print(split_price_symbol)
        remove_price_comma = split_price_symbol.replace(",", "")
        self.price_conversion = float(remove_price_comma)
        
        self.title = soup.find(id="productTitle").get_text()
        return self.title,self.price_conversion
        #print(title)
    
    def alert(self):
        message = f"{self.title} is now {self.BUY_PRICE}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            result = connection.login("kaustubh.tripathi6798@gmail.com","Maverick#679897!")
            connection.sendmail(
                from_addr="kaustubh.tripathi6798@gmail.com",
                to_addrs="dikshatanwar72@gmail.com",
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )

    
    def price_comparison(self):
        self.BUY_PRICE=2000
        if self.price_conversion < self.BUY_PRICE:
            self.alert()

url = "https://www.amazon.in/Wings-Wireless-Bluetooth-Earphones-Controls/dp/B08T96R3XJ/ref=sr_1_2?keywords=wings+phantom&qid=1645202890&sprefix=wings+%2Caps%2C261&sr=8-2"
track=Tracker(url)
track.track()
track.price_comparison()