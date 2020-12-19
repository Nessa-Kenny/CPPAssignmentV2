import boto3

dynamodb = boto3.resource('dynamodb')
#add table which has been created in dynmodb: Search_Table
dynamoTable = dynamodb.Table('Search_Table')
dynamoTable.put_item(

#table should contain title, keyword, s3 location to perform search
#key item is specified when creating the table
	Item={
