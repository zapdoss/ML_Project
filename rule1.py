import requests
import json

def getVideosR1(id):
    tags=json.loads((requests.get("https://www.googleapis.com/youtube/v3/videos?key=AIzaSyCjXSaAJchstnrxGPXd9yR73kp4dIjjNU8&fields=items(snippet(title,description,tags))&part=snippet&id="+id)).content)["items"][0]["snippet"]["tags"]

    vids=[]

    searchRes=json.loads((requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&q="+tags[0]+"+"+tags[1]+"+"+tags[2]+"+"+tags[3]+"+"+tags[4]+"+"+tags[5]+"&key=AIzaSyCsrw2p5BxOKuKjjCn9NNMhYRra8amsboQ&type=video&pageToken=")).content)["items"]

    for i in range(min(25,len(searchRes))):
        if searchRes[i]["id"]["videoId"] != id:
            vids.append(searchRes[i]["id"]["videoId"])

    return vids

#print getVideosR1("0XL1NBUv2NU")