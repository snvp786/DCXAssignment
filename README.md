Following steps were done to achieve the goal 
1.	Create a custom role with lambda function execution policy  - “DCXCustomLambdaexecutionRole”
2.	Created two new policies 
a.	S3writeonlyaccess 
b.	ReadParameterStore
3.	Attach the two new policies to the “DCXCustomLambdaexecutionRole” that will rights for the lambda function to Read from ParameterStore and Write to S3 bucket 
4.	Created a parameter “UserName” with value as “JohnDre” in System Manager’s parameter store 
5.	Created S3 bucket “dxcassignment” 
6.	CF template was created for lambda function for Python 3.6 (couple of options were tried – 
1. function zipped and stored in S3 bucket and referred to when executing the stack 
2. Zipfile Property inline in the CF template  

later was finalized as only cfresponse module required to send back response to CF supports Zipfile property inline 

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-lambda-function-code-cfnresponsemodule.html

#Results:

a)	Able to upload CF template for Lambda function, create a stack and deploy lambda function 
b)	Successful in creating o/p json document in S3 after invoking the function from console (can be done through CLI/ API gateway triggers) 


#Known Issues:

Unable to send response back to CF using CFNResponse module – getting the below error 

'ResponseURL': KeyError
Traceback (most recent call last):
File "/var/task/index.py", line 14, in lambda_handler
cfnresponse.send(event, context, cfnresponse.SUCCESS, jsondata, "CustomResourcePhysicalID")
File "/var/task/cfnresponse.py", line 15, in send
responseUrl = event['ResponseURL']
KeyError: 'ResponseURL'

