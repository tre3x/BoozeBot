import bs4
import requests

def booze(tag, low, high):
    if(low == 0 and high == 0): link = 'https://www.spencers.in/catalogsearch/result/index/?cat=10664&q=' + tag
    else: link = 'https://www.spencers.in/catalogsearch/result/index/?cat=10664&price=' + low + '-' + high + '&q=' + tag

    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    output = []
    
    for ol in soup.find_all("ol", {"class":"products list items product-items"}):
        for li in ol.find_all(("li", {"class" : "item product product-item col-md-3 col-sm-3 col-xs-6"}) or ("li", {"class" : "item product product-item col-md-3 col-sm-3 col-xs-6 last_product"})):
            pricetag = []
            for a in li.find_all("a", {"class" : "product-item-link"}):
                pricetag.append(a.text.lstrip().rstrip())
            for span in li.find_all("span", {"class" : "price"}):
                pricetag.append(span.text)
            output.append(pricetag)
    if(len(output) > 0): output.pop(-1)
    return output
