import boto3
from datetime import datetime, timedelta

def get_cost_data():
    client = boto3.client('ce', region_name='us-east-1')  # Cost Explorer Region

    end = datetime.today().date()
    start = end - timedelta(days=30)

    response = client.get_cost_and_usage(
        TimePeriod={'Start': start.isoformat(), 'End': end.isoformat()},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

    results = []
    for day in response['ResultsByTime']:
        for group in day['Groups']:
            results.append({
                'date': day['TimePeriod']['Start'],
                'service': group['Keys'][0],
                'cost': float(group['Metrics']['UnblendedCost']['Amount'])
            })
    return results
