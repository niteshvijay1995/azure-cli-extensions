# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long, too-many-statements


from azure.cli.core.commands.parameters import (
    get_resource_name_completion_list, name_type, get_enum_type, get_three_state_flag, get_location_type,
    tags_type,
    resource_group_name_type)

from azext_cosmosdb_preview._validators import (
    validate_gossip_certificates,
    validate_client_certificates,
    validate_seednodes,
    validate_node_count)

from azext_cosmosdb_preview.action import (
    AddDataTransferDataSource,
    AddDataTransferDataSink, AddCassandraTableAction, AddBlobContainerAction)

from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)

from azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.models import DefaultConsistencyLevel, DatabaseAccountKind, ServerVersion, BackupPolicyType


def load_arguments(self, _):
    from azure.cli.core.commands.parameters import tags_type

    # Managed Cassandra Cluster
    for scope in [
            'managed-cassandra cluster create',
            'managed-cassandra cluster update',
            'managed-cassandra cluster show',
            'managed-cassandra cluster delete',
            'managed-cassandra cluster node-status']:
        with self.argument_context(scope) as c:
            c.argument('cluster_name', options_list=['--cluster-name', '-c'], help="Cluster Name", required=True)

    # Managed Cassandra Cluster
    for scope in [
            'managed-cassandra cluster create',
            'managed-cassandra cluster update']:
        with self.argument_context(scope) as c:
            c.argument('tags', arg_type=tags_type)
            c.argument('external_gossip_certificates', nargs='+', validator=validate_gossip_certificates, options_list=['--external-gossip-certificates', '-e'], help="A list of certificates that the managed cassandra data center's should accept.")
            c.argument('cassandra_version', help="The version of Cassandra chosen.")
            c.argument('authentication_method', help="Authentication mode can be None or Cassandra. If None, no authentication will be required to connect to the Cassandra API. If Cassandra, then passwords will be used.")
            c.argument('hours_between_backups', help="The number of hours between backup attempts.")
            c.argument('repair_enabled', help="Enables automatic repair.")
            c.argument('client_certificates', nargs='+', validator=validate_client_certificates, help="If specified, enables client certificate authentication to the Cassandra API.")
            c.argument('gossip_certificates', help="A list of certificates that should be accepted by on-premise data centers.")
            c.argument('external_seed_nodes', nargs='+', validator=validate_seednodes, help="A list of ip addresses of the seed nodes of on-premise data centers.")
            c.argument('identity', help="Identity used to authenticate.")

    # Managed Cassandra Cluster
    with self.argument_context('managed-cassandra cluster create') as c:
        c.argument('location', options_list=['--location', '-l'], help="Azure Location of the Cluster", required=True)
        c.argument('delegated_management_subnet_id', options_list=['--delegated-management-subnet-id', '-s'], help="The resource id of a subnet where the ip address of the cassandra management server will be allocated. This subnet must have connectivity to the delegated_subnet_id subnet of each data center.", required=True)
        c.argument('initial_cassandra_admin_password', options_list=['--initial-cassandra-admin-password', '-i'], help="The intial password to be configured when a cluster is created for authentication_method Cassandra.")
        c.argument('restore_from_backup_id', help="The resource id of a backup. If provided on create, the backup will be used to prepopulate the cluster. The cluster data center count and node counts must match the backup.")
        c.argument('cluster_name_override', help="If a cluster must have a name that is not a valid azure resource name, this field can be specified to choose the Cassandra cluster name. Otherwise, the resource name will be used as the cluster name.")

    # Managed Cassandra Datacenter
    for scope in [
            'managed-cassandra datacenter create',
            'managed-cassandra datacenter update',
            'managed-cassandra datacenter show',
            'managed-cassandra datacenter delete']:
        with self.argument_context(scope) as c:
            c.argument('cluster_name', options_list=['--cluster-name', '-c'], help="Cluster Name", required=True)
            c.argument('data_center_name', options_list=['--data-center-name', '-d'], help="Datacenter Name", required=True)

    # Managed Cassandra Datacenter
    for scope in [
            'managed-cassandra datacenter create',
            'managed-cassandra datacenter update']:
        with self.argument_context(scope) as c:
            c.argument('node_count', options_list=['--node-count', '-n'], validator=validate_node_count, help="The number of Cassandra virtual machines in this data center. The minimum value is 3.")
            c.argument('base64_encoded_cassandra_yaml_fragment', options_list=['--base64-encoded-cassandra-yaml-fragment', '-b'], help="This is a Base64 encoded yaml file that is a subset of cassandra.yaml.  Supported fields will be honored and others will be ignored.")
            c.argument('data_center_location', options_list=['--data-center-location', '-l'], help="The region where the virtual machine for this data center will be located.")
            c.argument('delegated_subnet_id', options_list=['--delegated-subnet-id', '-s'], help="The resource id of a subnet where ip addresses of the Cassandra virtual machines will be allocated. This must be in the same region as data_center_location.")

    # Managed Cassandra Datacenter
    with self.argument_context('managed-cassandra datacenter create') as c:
        c.argument('data_center_location', options_list=['--data-center-location', '-l'], help="Azure Location of the Datacenter", required=True)
        c.argument('delegated_subnet_id', options_list=['--delegated-subnet-id', '-s'], help="The resource id of a subnet where ip addresses of the Cassandra virtual machines will be allocated. This must be in the same region as data_center_location.", required=True)
        c.argument('node_count', options_list=['--node-count', '-n'], validator=validate_node_count, help="The number of Cassandra virtual machines in this data center. The minimum value is 3.", required=True)

    # Managed Cassandra Datacenter
    with self.argument_context('managed-cassandra datacenter list') as c:
        c.argument('cluster_name', options_list=['--cluster-name', '-c'], help="Cluster Name", required=True)

    # Graph
    with self.argument_context('cosmosdb graph') as c:
        c.argument('account_name', completer=None, options_list=['--account-name', '-a'], help='Name of the Cosmos DB database account.', id_part=None)
        c.argument('resource_group_name', completer=None, options_list=['--resource-group-name', '-g'], help='Name of the resource group of the database account.', id_part=None)
        c.argument('graph_name', options_list=['--name', '-n'], help="Graph name")

    # Services
    with self.argument_context('cosmosdb service') as c:
        c.argument('account_name', completer=None, options_list=['--account-name', '-a'], help='Name of the Cosmos DB database account.', id_part=None)
        c.argument('resource_group_name', completer=None, options_list=['--resource-group-name', '-g'], help='Name of the resource group of the database account.', id_part=None)
        c.argument('service_kind', options_list=['--kind', '-k'], help="Service kind")
        c.argument('service_name', options_list=['--name', '-n'], help="Service Name.")
        c.argument('instance_count', options_list=['--count', '-c'], help="Instance Count.")
        c.argument('instance_size', options_list=['--size'], help="Instance Size. Possible values are: Cosmos.D4s, Cosmos.D8s, Cosmos.D16s etc")

    with self.argument_context('cosmosdb dts create2') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.')
        c.argument('job_name', type=str, help='Name of the Data Transfer Job')
        c.argument('source', action=AddDataTransferDataSource, nargs='+', help='Source component of Data Transfer job', arg_group='Component')
        c.argument('destination', action=AddDataTransferDataSink, nargs='+', help='Destination component of Data Transfer job', arg_group='Component')

    with self.argument_context('cosmosdb dts export') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, options_list=['--account-name', '-a'], help='Cosmos DB database account name.')
        c.argument('job_name', type=str, help='Name of the Data Transfer Job. A random job name will be generated if not passed.')
        c.argument('cassandra_table', nargs='+', action=AddCassandraTableAction, help='Data source cassandra table')
        c.argument('blob_container', nargs='+', action=AddBlobContainerAction, help='Data sink blob container')
        c.argument('worker_count', type=int, help='Worker count')

    with self.argument_context('cosmosdb dts import') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, options_list=['--account-name', '-a'], help='Cosmos DB database account name.')
        c.argument('job_name', type=str, help='Name of the Data Transfer Job. A random job name will be generated if not passed.')
        c.argument('cassandra_table', nargs='+', action=AddCassandraTableAction, help='Data sink cassandra table')
        c.argument('blob_container', nargs='+', action=AddBlobContainerAction, help='Data source blob container')
        c.argument('worker_count', type=int, help='Worker count')

    with self.argument_context('cosmosdb dts list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.')

    with self.argument_context('cosmosdb dts show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.', id_part='name')
        c.argument('job_name', type=str, help='Name of the Data Transfer Job', id_part='child_name_1')

    with self.argument_context('cosmosdb dts create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.')
        c.argument('job_name', type=str, help='Name of the Data Transfer Job')
        c.argument('job_create_parameters', type=validate_file_or_dict, help=' Expected value: '
                   'json-string/json-file/@json-file.')

    with self.argument_context('cosmosdb cassandra table export') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.')
        c.argument('job_name', type=str, help='Name of the Data Transfer Job')
        c.argument('keyspace_name', options_list=['--keyspace-name', '-k'], help="Keyspace name")
        c.argument('table_name', options_list=['--table-name'], help="Table name")
        c.argument('storage_container', options_list=['--storage-container', '-container'], help="Blob storage container name")
        c.argument('storage_url', options_list=['--storage-url'], help="Blob storage endpoint url")

    with self.argument_context('cosmosdb cassandra table import') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.')
        c.argument('job_name', type=str, help='Name of the Data Transfer Job')
        c.argument('keyspace_name', options_list=['--keyspace-name', '-k'], help="Keyspace name")
        c.argument('table_name', options_list=['--table-name'], help="Table name")
        c.argument('storage_container', options_list=['--storage-container', '-container'], help="Blob storage container name")
        c.argument('storage_url', options_list=['--storage-url'], help="Blob storage endpoint url")

    with self.argument_context('cosmosdb service list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.')

    with self.argument_context('cosmosdb service show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.', id_part='name')
        c.argument('service_name', options_list=['--service-name'], type=str, help='Cosmos DB service '
                   'name.', id_part='child_name_1')

    with self.argument_context('cosmosdb service create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.')
        c.argument('service_name', options_list=['--service-name'], type=str, help='Cosmos DB service '
                   'name.')
        c.argument('instance_size', arg_type=get_enum_type(['Cosmos.D4s', 'Cosmos.D8s', 'Cosmos.D16s']),
                   help='Instance type for the service.')
        c.argument('instance_count', type=int, help='Instance count for the service.')
        c.argument('service_type', arg_type=get_enum_type(['SqlDedicatedGateway', 'DataTransferService',
                                                           'GraphAPICompute']), help='ServiceType for the service.')

    with self.argument_context('cosmosdb service delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.', id_part='name')
        c.argument('service_name', options_list=['--service-name'], type=str, help='Cosmos DB service '
                   'name.', id_part='child_name_1')

    with self.argument_context('cosmosdb service wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', type=str, help='Cosmos DB database account name.', id_part='name')
        c.argument('service_name', options_list=['--service-name'], type=str, help='Cosmos DB service '
                   'name.', id_part='child_name_1')
