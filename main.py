import requests
import smtplib
from bs4 import BeautifulSoup

LINK = "https://www.amazon.in/Super-Rockerz-400-Bluetooth-Headphones/dp/B01FSYQ2A4/ref=sxin_15?asc_contentid=amzn1.osa.7da1aa2a-9edb-45fb-83be-54cc0852e82e.A21TJRUUN4KGV.en_IN&asc_contenttype=article&ascsubtag=amzn1.osa.7da1aa2a-9edb-45fb-83be-54cc0852e82e.A21TJRUUN4KGV.en_IN&creativeASIN=B01FSYQ2A4&crid=3DQ31LFGAGVUG&cv_ct_cx=headphones+with+mic&cv_ct_id=amzn1.osa.7da1aa2a-9edb-45fb-83be-54cc0852e82e.A21TJRUUN4KGV.en_IN&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-earns-comm&keywords=headphones+with+mic&linkCode=oas&pd_rd_i=B01FSYQ2A4&pd_rd_r=99f51eeb-33c3-4344-887d-6bf423bb17b4&pd_rd_w=TZi73&pd_rd_wg=q1s2l&pf_rd_p=31dc3369-28cf-4a1f-9aa0-314b513a6d1f&pf_rd_r=28QFQ3HN32772XE77MXE&qid=1645945372&sprefix=head%2Caps%2C592&sr=1-1-483c64d8-df78-4008-ae20-e69f683e58b1&tag=technologytoday-21"
CUTOFF_PRICE = 999

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

# Send a request to fetch HTML of the page.
response = requests.get(LINK, headers=header)

# Create a soup object
soup = BeautifulSoup(response.content, "lxml")

# Get the price of the item and converting the string amount to float.
price = float(soup.find(name="span", class_="a-price-whole").get_text())

# Get the title of the product.
title = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break")

# Remove extra spaces in the title using strip()
title = title.get_text().strip("        ")

# Compare the current price of the item with the cutoff price.
# If there is a price drop, send an email.
if price < CUTOFF_PRICE:
    connection = smtplib.SMTP(host=YOUR_SMTP_ADDRESS, port=587)
    connection.starttls()
    connection.login(user=YOUR_EMAIL, password=YOUR_PASSWORD)
    connection.sendmail(from_addr=YOUR_EMAIL,
                        to_addrs=YOUR_EMAIL,
                        msg=f"Subject:Amazon Price Drop Alert! \n\n {title} is now available at Rs.{price}.\n Buy now! Link: {LINK}")
    connection.close()
