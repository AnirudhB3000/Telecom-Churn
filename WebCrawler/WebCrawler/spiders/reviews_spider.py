import scrapy
from ..items import WebcrawlerItem
from core.models import Reviews, Churn
from core.prediction import model_pred
from datetime import datetime
import re
from textblob import TextBlob

class ReviewSpider(scrapy.Spider):
    name = 'review'
    start_urls = [
        'https://www.trustpilot.com/review/jio.com'
    ]

    def parse(self, response):

        items = WebcrawlerItem()

        rw = response.css(".typography_color-black__5LYEn::text").extract()
        
        
        items['rw'] = rw
        yield {'titletext': items}

        #clean reviews:
        rw_updated = [x for x in rw if x != ' ']

        def is_date(string):
            date_formats = ["%B %d, %Y"]
            for date_format in date_formats:
                try:
                    datetime.strptime(string, date_format)
                    return True
                except ValueError:
                    pass
            return False

        def remove_dates(rw_updated):
            for element in rw_updated[:]:
                if re.match(r"([A-Z][a-z]+) (\d{1,2}), (\d{4})", element) and is_date(element):
                    rw_updated.remove(element)
            return rw_updated
            
        rw_updated = remove_dates(rw_updated)
        lenPos = 0
        lenNeg = 0
        positive_feedbacks = []
        negative_feedbacks = []
        for feedback in rw_updated:
            feedback_polarity = TextBlob(feedback).sentiment.polarity
            if feedback_polarity>0:
                positive_feedbacks.append(feedback)
                continue
            negative_feedbacks.append(feedback)
            lenPos = float(len(positive_feedbacks))
            lenNeg = float(len(negative_feedbacks))
            
            changePred = ((lenPos - lenNeg) / 10)
        
        finalMP = model_pred()
        z = finalMP
        finalChurnVal = (finalMP - (changePred))
        a = Churn(ModelPred = finalMP, Review = changePred, Final = finalChurnVal)
        a.save()
        b = Reviews(PlaintextReviews = rw_updated, PosFeedback = lenPos, NegFeedback = lenNeg, Alt = changePred)
        b.save()