import boto3
import json
import datetime
acm = boto3.client('acm')

response = acm.list_certificates(
    CertificateStatuses=[
      'ISSUED',
    ], 
)

for certificate in response['CertificateSummaryList']:
    expired_time = certificate['NotAfter']
    # current_time = datetime.datetime.today()
    # expired_time = certificate['NotAfter']
    # formatted_Expired_time = expired_time.strftime("%Y-%m-%d")
    # formatted_Current_time = current_time.strftime("%Y-%m-%d")
    # print(formatted_Expired_time)
    # print(formatted_Current_time)
    # expire_period = formatted_Current_time - formatted_Expired_time
    # print(expire_period)
    print(json.dumps(expired_time, default= str,  indent=4))
# print(json.dumps(response, default= str,  indent=4))
