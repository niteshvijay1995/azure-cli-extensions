# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_cosmosdb_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_cosmosdb_preview.vendored_sdks.cosmodb import CosmosDBManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   CosmosDBManagementClient)


def cf_database_account(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).database_accounts


def cf_database(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).database


def cf_collection(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).collection


def cf_collection_region(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).collection_region


def cf_database_account_region(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).database_account_region


def cf_percentile_source_target(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).percentile_source_target


def cf_percentile_target(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).percentile_target


def cf_percentile(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).percentile


def cf_collection_partition_region(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).collection_partition_region


def cf_collection_partition(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).collection_partition


def cf_partition_key_range_id(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).partition_key_range_id


def cf_partition_key_range_id_region(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).partition_key_range_id_region


def cf_graph_resource(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).graph_resources


def cf_sqlresource(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).sql_resources


def cf_mongo_dbresource(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).mongo_db_resources


def cf_table_resource(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).table_resources


def cf_cassandra_resource(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).cassandra_resources


def cf_gremlin_resource(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).gremlin_resources


def cf_cassandra_cluster(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).cassandra_clusters


def cf_cassandra_data_center(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).cassandra_data_centers


def cf_notebook_workspace(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).notebook_workspaces


def cf_private_endpoint_connection(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).private_endpoint_connections


def cf_private_link_resource(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).private_link_resources


def cf_restorable_database_account(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).restorable_database_accounts


def cf_restorable_sqldatabase(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).restorable_sql_databases


def cf_restorable_sqlcontainer(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).restorable_sql_containers


def cf_restorable_sqlresource(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).restorable_sql_resources


def cf_restorable_mongodb_database(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).restorable_mongodb_databases


def cf_restorable_mongodb_collection(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).restorable_mongodb_collections


def cf_restorable_mongodb_resource(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).restorable_mongodb_resources


def cf_service(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).service


def cf_data_transfer_job(cli_ctx, *_):
    return cf_cosmosdb_cl(cli_ctx).data_transfer_jobs
