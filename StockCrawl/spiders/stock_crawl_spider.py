from scrapy.spider import Spider
from scrapy.selector import Selector
from StockCrawl.items import StockcrawlItem
from test import dyurl
class StockCrawl(Spider):
  name ='Stock'
  start_urls = dyurl('a')
  def parse(self, res):
    hxs = Selector(res)
    items=[]
    asd = StockcrawlItem()
 #   item = StockcrawlItem
    for tr in hxs.xpath('//table[@width="880"]/tbody/tr[@class = "basic2"]'):     
        item = []
        tds = tr.xpath('td[@class="digit"]')
        item.append(tds[0].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip())
        item.append(tds[1].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip())
        item.append(tds[2].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip()) 
        item.append(tds[3].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip()) 
        item.append(tds[4].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip()) 
        item.append(tds[5].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip()) 
        item.append(tds[6].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip())
        item.append(tds[7].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip()) 
        item.append(tds[8].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip())
        item.append(tds[9].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip())
        item.append(tds[10].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip())
        item.append(tds[11].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip())
        item.append(tds[12].xpath('text()').extract()[0].replace(',', '').encode('utf-8').strip())
     
        items.append(item)
    asd['x'] = items
    return asd

   ## with open ('fuck.data', 'w') as f:
     #   f.write('%s\n' % items)
        #item = StockcrawlItem()
        #tds = tr.xpath('td')
        #item['x'] = tds[9].xpath('span/font/text()').extract()[0].encode('utf-8').strip()
        #item['y'] = tds[0].xpath('text()').extract()[0].encode('utf-8').strip()
        #if len(item['x']) == 0:
        #    item['x'] = 0
    #items.append(item)
    #return item
