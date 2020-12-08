def getCWMetric(region, fleet, MetricName):
    cw = boto3.client('cloudwatch',region_name=region)
    response = cw.get_metric_statistics(
        Period=60,
        Namespace='AWS/AppStream',
        MetricName=MetricName,
        Dimensions=[
            {
                'Name': 'Fleet',
                'Value': fleet
            },
        ],
        StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=300),
        EndTime=datetime.datetime.utcnow(),
        # Period=123,
        Statistics=[
            'SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'
        ]
    )
    returnObj = {}
    returnObj['Average'] = round(float(response['Datapoints'][0]['Average']),2)
    returnObj['Fleet'] = fleet
    returnObj['Region'] = region
    returnObj['MetricName'] = MetricName
    returnObj['TimeStamp'] = datetime.datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S")
    return returnObj
