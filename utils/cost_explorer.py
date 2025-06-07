import boto3
from datetime import datetime, timedelta

def get_cost_data():
    client = boto3.client('ce', region_name='us-east-1')
    sts = boto3.client('sts')

    end = datetime.today().date()
    start = end - timedelta(days=30)

    # Get AWS Account ID
    account_id = sts.get_caller_identity()['Account']

    # Get cost data grouped by service
    response = client.get_cost_and_usage(
        TimePeriod={'Start': start.isoformat(), 'End': end.isoformat()},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

    results = []
    total_cost = 0.0

    for day in response['ResultsByTime']:
        for group in day['Groups']:
            cost = float(group['Metrics']['UnblendedCost']['Amount'])
            total_cost += cost
            results.append({
                'date': day['TimePeriod']['Start'],
                'service': group['Keys'][0],
                'cost': cost
            })

    return {
        'data': results,
        'total_cost': total_cost,
        'start_date': start.isoformat(),
        'end_date': end.isoformat(),
        'account_id': account_id
    }
