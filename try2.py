import tweepy

auth = tweepy.OAuthHandler( "vkc9rhetQvsmKxIdsLICGVUJt", "aPuChtFao446UcECcwH7UeYoWU27wyLLH5WYOiVXPrSrP2adlw")
auth.set_access_token("708405043448442880-lsv6kLnJYbDraL0PhvNNRRxaYPErrEX", "NU8Mv6d3wfbiqqxGNgKuuU9pEMleNTAeJzxNCDwZv7mX1")

api = tweepy.API(auth)
fashion_image_twitts = api.search("fashion filter:images")
print fashion_image_twitts[0].entities