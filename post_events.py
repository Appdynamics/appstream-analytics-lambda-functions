def post_events(region, stack):
    client = boto3.client('appstream',region_name=region, verify=False)
    apitoken = json.loads(get_secret('appapikey','eu-west-1'))['appapikey']
    appdurl = 'https://fra-ana-api.saas.appdynamics.com/events/publish/appstreamCloudWatch'
    appdaccount = json.loads(get_secret('appdaccount','eu-west-1'))['appdaccount']
    try:
        response = client.list_associated_fleets(StackName=stack)
        for key in response['Names']:
            fleet = key
        metrics =  [ "ActualCapacity", "InUseCapacity", "CapacityUtilization" ]
        for metric in metrics:
            payload = getCWMetric(region, fleet, metric)
            result = postToSchema(appdurl, json.dumps([payload]), appdaccount, apitoken)
            print (result)

    except Exception as e:
        #print(e.response['Error']['Message'])
        print e
        logger.error('something went wrong {}'.format(e))
    return "complete"
