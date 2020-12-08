def postToSchema(url, payload, accname, apikey):
    # proxies = {
    #     "http": "http://internal-Squid-Proxy-Loadbalancer-314698608.eu-west-1.elb.amazonaws.com:8080",
    #     "https": "http://internal-Squid-Proxy-Loadbalancer-314698608.eu-west-1.elb.amazonaws.com:8080"
    # }
    headers = {
      'X-Events-API-AccountName': accname,
      'X-Events-API-Key': apikey,
      'content-type': 'application/vnd.appd.events+json;v=2'
    }
    print (headers)
    print (payload)
    try:
        # r = requests.post(url=url, proxies=proxies, headers=headers, data=payload)
        r = requests.post(url=url, headers=headers, data=payload)
        # content = r.json()
        content = r
        # print content['factorResult']
        # print(content['factorResult'], end='')
        return content
    except Exception as e:
        # print ''
        print(str(e), end='')
        # decoding failed
        return str(e)
