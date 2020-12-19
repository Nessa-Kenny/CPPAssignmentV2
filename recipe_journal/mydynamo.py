import boto3

dynamodb = boto3.resource('dynamodb')
#add table which has been created in dynamodb: Search_Table
dynamoTable = dynamodb.Table('Search_Table')
dynamoTable.put_item(

#key item is specified when creating the table

#table should contain entries for title, keyword, s3 location in order to perform search
#pull details when creating recipe in the html form on add_recipe.html
#	Item={
#	    'title' = t1
#	    'keyword' = k1
#	    's3_url' = s1
#	    }
