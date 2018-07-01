#Converts your website URL to tiny URL

class TinyURL(object):
    i=0
    dictionary={}
    def tiny_url_encode(self,long_url):
        self.i=self.i+1
        self.dictionary[self.i]=long_url
        return "http://tinyurl.com/"+str(self.i)
    def tiny_url_decode(self,short_url):
        return self.dictionary[int(short_url.replace("http://tinyurl.com/",""))]
a=TinyURL()
print (a.tiny_url_encode("devsanghvifirstwebsiteever.com"))
print (a.tiny_url_encode("hemshahfirstwebsiteever.co.in"))
print (a.tiny_url_decode("http://tinyurl.com/1"))
print (a.tiny_url_decode("http://tinyurl.com/2"))

