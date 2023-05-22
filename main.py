from dagster import asset, MultiPartitionsDefinition, MonthlyPartitionsDefinition, StaticPartitionsDefinition

small_code_list = ['a', 'b', 'c']

large_code_list = [f"a_{num}" for num in range(5000)]


@asset(partitions_def=MultiPartitionsDefinition(
    {
        "month": MonthlyPartitionsDefinition(start_date="2022-01-01"),
        "code": StaticPartitionsDefinition(small_code_list)
    }
))
def asset_small_static_partition():
    return [2, 3, 4]


@asset(partitions_def=MultiPartitionsDefinition(
    {
        "month": MonthlyPartitionsDefinition(start_date="2022-01-01"),
        "code": StaticPartitionsDefinition(large_code_list)
    }
))
def asset_large_static_partition():
    return [2, 3, 4]