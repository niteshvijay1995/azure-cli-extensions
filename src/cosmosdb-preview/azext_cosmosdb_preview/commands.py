# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-statements
from azure.cli.core.commands import CliCommandType
from azext_cosmosdb_preview._client_factory import (
    cf_cassandra_cluster,
    cf_cassandra_data_center,
    cf_graph_resources,
    cf_service,
    cf_data_transfer_job
)

from azure.cli.command_modules.cosmosdb._client_factory import (
    cf_cassandra_resources
)

from azext_cosmosdb_preview._format import (
    amc_node_status_table_format
)

def load_command_table(self, _):
    cosmosdb_graph_resources_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#GraphResourcesOperations.{}',
        client_factory=cf_graph_resources)

    cosmosdb_service_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#ServiceOperations.{}',
        client_factory=cf_service)

    cosmosdb_managed_cassandra_cluster_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#CassandraClustersOperations.{}',
        client_factory=cf_cassandra_cluster)

    cosmosdb_data_transfer_job = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.cosmodb.operations._data_transfer_jobs_operations#DataTransferJobsOperations.{}',
        client_factory=cf_data_transfer_job
    )

    cosmosdb_cassandra_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.cosmosdb.operations#CassandraResourcesOperations.{}',
        client_factory=cf_cassandra_resources)

    cosmosdb_managed_cassandra_datacenter_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#CassandraDataCentersOperations.{}',
        client_factory=cf_cassandra_data_center)

    with self.command_group('managed-cassandra cluster', cosmosdb_managed_cassandra_cluster_sdk, client_factory=cf_cassandra_cluster, is_preview=True) as g:
        g.custom_command('create', 'cli_cosmosdb_managed_cassandra_cluster_create', supports_no_wait=True)
        g.custom_command('update', 'cli_cosmosdb_managed_cassandra_cluster_update', supports_no_wait=True)
        g.custom_command('node-status', 'cli_cosmosdb_managed_cassandra_fetch_node_status', table_transformer=amc_node_status_table_format, supports_no_wait=True)
        g.custom_command('list', 'cli_cosmosdb_managed_cassandra_cluster_list')
        g.show_command('show', 'get')
        g.command('delete', 'begin_delete', confirmation=True, supports_no_wait=True)

    with self.command_group('managed-cassandra datacenter', cosmosdb_managed_cassandra_datacenter_sdk, client_factory=cf_cassandra_data_center, is_preview=True) as g:
        g.custom_command('create', 'cli_cosmosdb_managed_cassandra_datacenter_create', supports_no_wait=True)
        g.custom_command('update', 'cli_cosmosdb_managed_cassandra_datacenter_update', supports_no_wait=True)
        g.command('list', 'list')
        g.show_command('show', 'get')
        g.command('delete', 'begin_delete', confirmation=True, supports_no_wait=True)

    with self.command_group('cosmosdb graph', cosmosdb_graph_resources_sdk, client_factory=cf_graph_resources, is_preview=True) as g:
        g.custom_command('create', 'cli_cosmosdb_graph_create', supports_no_wait=True)
        g.custom_command('exists', 'cli_cosmosdb_graph_exists')
        g.command('list', 'list_graphs')
        g.show_command('show', 'get_graph')
        g.command('delete', 'begin_delete_graph_resource', confirmation=True, supports_no_wait=True)

    with self.command_group('cosmosdb service', cosmosdb_service_sdk, client_factory=cf_service, is_preview=True) as g:
        g.custom_command('create', 'cli_cosmosdb_service_create', supports_no_wait=True)
        g.custom_command('update', 'cli_cosmosdb_service_update', supports_no_wait=True)
        g.command('list', 'list')
        g.show_command('show', 'get')
        g.command('delete', 'begin_delete', confirmation=True, supports_no_wait=True)

    with self.command_group(
            'cosmosdb dts', cosmosdb_data_transfer_job, client_factory=cf_data_transfer_job
        ) as g:
            g.custom_command('export', 'cosmosdb_data_transfer_export_job')
            g.custom_command('import', 'cosmosdb_data_transfer_import_job')
            g.custom_command('copy', 'cosmosdb_data_transfer_copy_job')
            g.custom_command('list', 'cosmosdb_dts_list')
            g.custom_show_command('show', 'cosmosdb_dts_show')

    with self.command_group(
            'cosmosdb cassandra table', cosmosdb_cassandra_sdk, client_factory=cf_data_transfer_job
        ) as g:
            g.custom_command('export', 'cosmosdb_data_transfer_cassandra_export_job')

    with self.command_group(
            'cosmosdb cassandra table', cosmosdb_cassandra_sdk, client_factory=cf_data_transfer_job
        ) as g:
            g.custom_command('import', 'cosmosdb_data_transfer_cassandra_import_job')

    with self.command_group(
            'cosmosdb sql container', cosmosdb_data_transfer_job, client_factory=cf_data_transfer_job
        ) as g:
            g.custom_command('copy', 'cosmosdb_data_transfer_sql_copy_container')