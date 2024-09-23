def delete_item_from_dynamo(ecr_repo_name, table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    try:
        delete_response = table.delete_item(Key={'ecr_repo_name': ecr_repo_name})
        if delete_response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"Item with ecr_repo_name '{ecr_repo_name}' deleted successfully.")
        else:
            print(f"Error deleting item: {delete_response}")
    except Exception as e:
        print(f"Error deleting item: {str(e)}")


def main(ecr_repo_name, table_name):
    try:
        abc()  # Call the function
        delete_records(ecr_repo_name, table_name)  # Delete records on success
    except Exception as e:
        print(f"Error executing function abc(): {str(e)}")
