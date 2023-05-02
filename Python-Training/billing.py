import boto3
import json
import pandas as pd
import openpyxl


# Set up the AWS credentials
session = boto3.Session(profile_name='default') # or specify your profile name
client = session.client('ce')

# Set up the start and end dates for the current month
start_date = '2023-04-01'
end_date = '2023-04-30'

# Retrieve the cost per service for the current month
result = client.get_cost_and_usage(
    TimePeriod={
        'Start': start_date,
        'End': end_date
    },
    Granularity='MONTHLY',
    Metrics=['UnblendedCost'],
    GroupBy=[
        {
            'Type': 'DIMENSION',
            'Key': 'SERVICE'
        },
    ]
)

# Create a Pandas dataframe from the data
data = []
for group in result['ResultsByTime'][0]['Groups']:
    service = group['Keys'][0]
    cost = group['Metrics']['UnblendedCost']['Amount']
    currency = group['Metrics']['UnblendedCost']['Unit']
    data.append({'Service': service, 'Cost': float(cost), 'Currency': currency})

df = pd.DataFrame(data)

# Export the dataframe to an Excel file
with pd.ExcelWriter('cost_per_service.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)

print(json.dumps(result, default= str,  indent=4))


# workbook = openpyxl.load_workbook('cost_per_service.xlsx')

# # Select the worksheet
# worksheet = workbook['Sheet1']

# # Find the row with the Amazon S3 service
# for row in worksheet.iter_rows(min_row=2):
#     service = row[0].value
#     if service == 'Amazon Simple Storage Service':
#         # Replace the cost in column 2 (B) with a new value
#         row[1].value = 500.0 # Replace with your desired cost

# # Save the workbook
# workbook.save('cost_per_service.xlsx')
