import function


filename_operations = "operations.json"
content = function.load_operations(filename_operations)

filter_operation = function.get_executed_operations(content)
sorted_operation = function.sorted_by_date(filter_operation)


for operation in sorted_operation[:5]:
    print(function.get_output_data(operation))