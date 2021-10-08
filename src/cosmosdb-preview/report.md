# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az cosmosdb|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az cosmosdb` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az cosmosdb||[commands](#CommandsIn)|
|az cosmosdb cassandra-cluster|CassandraClusters|[commands](#CommandsInCassandraClusters)|
|az cosmosdb cassandra-data-center|CassandraDataCenters|[commands](#CommandsInCassandraDataCenters)|
|az cosmosdb cassandra-resource|CassandraResources|[commands](#CommandsInCassandraResources)|
|az cosmosdb collection|Collection|[commands](#CommandsInCollection)|
|az cosmosdb collection-partition|CollectionPartition|[commands](#CommandsInCollectionPartition)|
|az cosmosdb collection-partition-region|CollectionPartitionRegion|[commands](#CommandsInCollectionPartitionRegion)|
|az cosmosdb collection-region|CollectionRegion|[commands](#CommandsInCollectionRegion)|
|az cosmosdb database|Database|[commands](#CommandsInDatabase)|
|az cosmosdb database-account|DatabaseAccounts|[commands](#CommandsInDatabaseAccounts)|
|az cosmosdb database-account-region|DatabaseAccountRegion|[commands](#CommandsInDatabaseAccountRegion)|
|az cosmosdb dts|DataTransferJobs|[commands](#CommandsInDataTransferJobs)|
|az cosmosdb graph-resource|GraphResources|[commands](#CommandsInGraphResources)|
|az cosmosdb gremlin-resource|GremlinResources|[commands](#CommandsInGremlinResources)|
|az cosmosdb mongo-db-resource|MongoDBResources|[commands](#CommandsInMongoDBResources)|
|az cosmosdb notebook-workspace|NotebookWorkspaces|[commands](#CommandsInNotebookWorkspaces)|
|az cosmosdb partition-key-range-id|PartitionKeyRangeId|[commands](#CommandsInPartitionKeyRangeId)|
|az cosmosdb partition-key-range-id-region|PartitionKeyRangeIdRegion|[commands](#CommandsInPartitionKeyRangeIdRegion)|
|az cosmosdb percentile|Percentile|[commands](#CommandsInPercentile)|
|az cosmosdb percentile-source-target|PercentileSourceTarget|[commands](#CommandsInPercentileSourceTarget)|
|az cosmosdb percentile-target|PercentileTarget|[commands](#CommandsInPercentileTarget)|
|az cosmosdb private-endpoint-connection|PrivateEndpointConnections|[commands](#CommandsInPrivateEndpointConnections)|
|az cosmosdb private-link-resource|PrivateLinkResources|[commands](#CommandsInPrivateLinkResources)|
|az cosmosdb restorable-database-account|RestorableDatabaseAccounts|[commands](#CommandsInRestorableDatabaseAccounts)|
|az cosmosdb restorable-mongodb-collection|RestorableMongodbCollections|[commands](#CommandsInRestorableMongodbCollections)|
|az cosmosdb restorable-mongodb-database|RestorableMongodbDatabases|[commands](#CommandsInRestorableMongodbDatabases)|
|az cosmosdb restorable-mongodb-resource|RestorableMongodbResources|[commands](#CommandsInRestorableMongodbResources)|
|az cosmosdb restorable-sql-container|RestorableSqlContainers|[commands](#CommandsInRestorableSqlContainers)|
|az cosmosdb restorable-sql-database|RestorableSqlDatabases|[commands](#CommandsInRestorableSqlDatabases)|
|az cosmosdb restorable-sql-resource|RestorableSqlResources|[commands](#CommandsInRestorableSqlResources)|
|az cosmosdb service|Service|[commands](#CommandsInService)|
|az cosmosdb sql-resource|SqlResources|[commands](#CommandsInSqlResources)|
|az cosmosdb table-resource|TableResources|[commands](#CommandsInTableResources)|

## COMMANDS
### <a name="CommandsIn">Commands in `az cosmosdb` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb location-get](#LocationGet)|LocationGet|[Parameters](#ParametersLocationGet)|[Example](#ExamplesLocationGet)|
|[az cosmosdb location-list](#LocationList)|LocationList|[Parameters](#ParametersLocationList)|[Example](#ExamplesLocationList)|

### <a name="CommandsInCassandraClusters">Commands in `az cosmosdb cassandra-cluster` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb cassandra-cluster list](#CassandraClustersListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersCassandraClustersListByResourceGroup)|[Example](#ExamplesCassandraClustersListByResourceGroup)|
|[az cosmosdb cassandra-cluster list](#CassandraClustersListBySubscription)|ListBySubscription|[Parameters](#ParametersCassandraClustersListBySubscription)|[Example](#ExamplesCassandraClustersListBySubscription)|
|[az cosmosdb cassandra-cluster show](#CassandraClustersGet)|Get|[Parameters](#ParametersCassandraClustersGet)|[Example](#ExamplesCassandraClustersGet)|
|[az cosmosdb cassandra-cluster update](#CassandraClustersUpdate)|Update|[Parameters](#ParametersCassandraClustersUpdate)|[Example](#ExamplesCassandraClustersUpdate)|
|[az cosmosdb cassandra-cluster delete](#CassandraClustersDelete)|Delete|[Parameters](#ParametersCassandraClustersDelete)|[Example](#ExamplesCassandraClustersDelete)|
|[az cosmosdb cassandra-cluster create-update](#CassandraClustersCreateUpdate)|CreateUpdate|[Parameters](#ParametersCassandraClustersCreateUpdate)|[Example](#ExamplesCassandraClustersCreateUpdate)|
|[az cosmosdb cassandra-cluster fetch-node-status](#CassandraClustersFetchNodeStatus)|FetchNodeStatus|[Parameters](#ParametersCassandraClustersFetchNodeStatus)|[Example](#ExamplesCassandraClustersFetchNodeStatus)|
|[az cosmosdb cassandra-cluster list-backup](#CassandraClustersListBackups)|ListBackups|[Parameters](#ParametersCassandraClustersListBackups)|[Example](#ExamplesCassandraClustersListBackups)|
|[az cosmosdb cassandra-cluster request-repair](#CassandraClustersRequestRepair)|RequestRepair|[Parameters](#ParametersCassandraClustersRequestRepair)|[Example](#ExamplesCassandraClustersRequestRepair)|
|[az cosmosdb cassandra-cluster show-backup](#CassandraClustersGetBackup)|GetBackup|[Parameters](#ParametersCassandraClustersGetBackup)|[Example](#ExamplesCassandraClustersGetBackup)|

### <a name="CommandsInCassandraDataCenters">Commands in `az cosmosdb cassandra-data-center` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb cassandra-data-center list](#CassandraDataCentersList)|List|[Parameters](#ParametersCassandraDataCentersList)|[Example](#ExamplesCassandraDataCentersList)|
|[az cosmosdb cassandra-data-center show](#CassandraDataCentersGet)|Get|[Parameters](#ParametersCassandraDataCentersGet)|[Example](#ExamplesCassandraDataCentersGet)|
|[az cosmosdb cassandra-data-center update](#CassandraDataCentersUpdate)|Update|[Parameters](#ParametersCassandraDataCentersUpdate)|[Example](#ExamplesCassandraDataCentersUpdate)|
|[az cosmosdb cassandra-data-center delete](#CassandraDataCentersDelete)|Delete|[Parameters](#ParametersCassandraDataCentersDelete)|[Example](#ExamplesCassandraDataCentersDelete)|
|[az cosmosdb cassandra-data-center create-update](#CassandraDataCentersCreateUpdate)|CreateUpdate|[Parameters](#ParametersCassandraDataCentersCreateUpdate)|[Example](#ExamplesCassandraDataCentersCreateUpdate)|

### <a name="CommandsInCassandraResources">Commands in `az cosmosdb cassandra-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb cassandra-resource create-update-cassandra-keyspace](#CassandraResourcesCreateUpdateCassandraKeyspace)|CreateUpdateCassandraKeyspace|[Parameters](#ParametersCassandraResourcesCreateUpdateCassandraKeyspace)|[Example](#ExamplesCassandraResourcesCreateUpdateCassandraKeyspace)|
|[az cosmosdb cassandra-resource create-update-cassandra-table](#CassandraResourcesCreateUpdateCassandraTable)|CreateUpdateCassandraTable|[Parameters](#ParametersCassandraResourcesCreateUpdateCassandraTable)|[Example](#ExamplesCassandraResourcesCreateUpdateCassandraTable)|
|[az cosmosdb cassandra-resource create-update-cassandra-view](#CassandraResourcesCreateUpdateCassandraView)|CreateUpdateCassandraView|[Parameters](#ParametersCassandraResourcesCreateUpdateCassandraView)|[Example](#ExamplesCassandraResourcesCreateUpdateCassandraView)|
|[az cosmosdb cassandra-resource delete-cassandra-keyspace](#CassandraResourcesDeleteCassandraKeyspace)|DeleteCassandraKeyspace|[Parameters](#ParametersCassandraResourcesDeleteCassandraKeyspace)|[Example](#ExamplesCassandraResourcesDeleteCassandraKeyspace)|
|[az cosmosdb cassandra-resource delete-cassandra-table](#CassandraResourcesDeleteCassandraTable)|DeleteCassandraTable|[Parameters](#ParametersCassandraResourcesDeleteCassandraTable)|[Example](#ExamplesCassandraResourcesDeleteCassandraTable)|
|[az cosmosdb cassandra-resource delete-cassandra-view](#CassandraResourcesDeleteCassandraView)|DeleteCassandraView|[Parameters](#ParametersCassandraResourcesDeleteCassandraView)|[Example](#ExamplesCassandraResourcesDeleteCassandraView)|
|[az cosmosdb cassandra-resource list-cassandra-keyspace](#CassandraResourcesListCassandraKeyspaces)|ListCassandraKeyspaces|[Parameters](#ParametersCassandraResourcesListCassandraKeyspaces)|[Example](#ExamplesCassandraResourcesListCassandraKeyspaces)|
|[az cosmosdb cassandra-resource list-cassandra-table](#CassandraResourcesListCassandraTables)|ListCassandraTables|[Parameters](#ParametersCassandraResourcesListCassandraTables)|[Example](#ExamplesCassandraResourcesListCassandraTables)|
|[az cosmosdb cassandra-resource list-cassandra-view](#CassandraResourcesListCassandraViews)|ListCassandraViews|[Parameters](#ParametersCassandraResourcesListCassandraViews)|[Example](#ExamplesCassandraResourcesListCassandraViews)|
|[az cosmosdb cassandra-resource migrate-cassandra-keyspace-to-autoscale](#CassandraResourcesMigrateCassandraKeyspaceToAutoscale)|MigrateCassandraKeyspaceToAutoscale|[Parameters](#ParametersCassandraResourcesMigrateCassandraKeyspaceToAutoscale)|[Example](#ExamplesCassandraResourcesMigrateCassandraKeyspaceToAutoscale)|
|[az cosmosdb cassandra-resource migrate-cassandra-keyspace-to-manual-throughput](#CassandraResourcesMigrateCassandraKeyspaceToManualThroughput)|MigrateCassandraKeyspaceToManualThroughput|[Parameters](#ParametersCassandraResourcesMigrateCassandraKeyspaceToManualThroughput)|[Example](#ExamplesCassandraResourcesMigrateCassandraKeyspaceToManualThroughput)|
|[az cosmosdb cassandra-resource migrate-cassandra-table-to-autoscale](#CassandraResourcesMigrateCassandraTableToAutoscale)|MigrateCassandraTableToAutoscale|[Parameters](#ParametersCassandraResourcesMigrateCassandraTableToAutoscale)|[Example](#ExamplesCassandraResourcesMigrateCassandraTableToAutoscale)|
|[az cosmosdb cassandra-resource migrate-cassandra-table-to-manual-throughput](#CassandraResourcesMigrateCassandraTableToManualThroughput)|MigrateCassandraTableToManualThroughput|[Parameters](#ParametersCassandraResourcesMigrateCassandraTableToManualThroughput)|[Example](#ExamplesCassandraResourcesMigrateCassandraTableToManualThroughput)|
|[az cosmosdb cassandra-resource migrate-cassandra-view-to-autoscale](#CassandraResourcesMigrateCassandraViewToAutoscale)|MigrateCassandraViewToAutoscale|[Parameters](#ParametersCassandraResourcesMigrateCassandraViewToAutoscale)|[Example](#ExamplesCassandraResourcesMigrateCassandraViewToAutoscale)|
|[az cosmosdb cassandra-resource migrate-cassandra-view-to-manual-throughput](#CassandraResourcesMigrateCassandraViewToManualThroughput)|MigrateCassandraViewToManualThroughput|[Parameters](#ParametersCassandraResourcesMigrateCassandraViewToManualThroughput)|[Example](#ExamplesCassandraResourcesMigrateCassandraViewToManualThroughput)|
|[az cosmosdb cassandra-resource show-cassandra-keyspace](#CassandraResourcesGetCassandraKeyspace)|GetCassandraKeyspace|[Parameters](#ParametersCassandraResourcesGetCassandraKeyspace)|[Example](#ExamplesCassandraResourcesGetCassandraKeyspace)|
|[az cosmosdb cassandra-resource show-cassandra-keyspace-throughput](#CassandraResourcesGetCassandraKeyspaceThroughput)|GetCassandraKeyspaceThroughput|[Parameters](#ParametersCassandraResourcesGetCassandraKeyspaceThroughput)|[Example](#ExamplesCassandraResourcesGetCassandraKeyspaceThroughput)|
|[az cosmosdb cassandra-resource show-cassandra-table](#CassandraResourcesGetCassandraTable)|GetCassandraTable|[Parameters](#ParametersCassandraResourcesGetCassandraTable)|[Example](#ExamplesCassandraResourcesGetCassandraTable)|
|[az cosmosdb cassandra-resource show-cassandra-table-throughput](#CassandraResourcesGetCassandraTableThroughput)|GetCassandraTableThroughput|[Parameters](#ParametersCassandraResourcesGetCassandraTableThroughput)|[Example](#ExamplesCassandraResourcesGetCassandraTableThroughput)|
|[az cosmosdb cassandra-resource show-cassandra-view](#CassandraResourcesGetCassandraView)|GetCassandraView|[Parameters](#ParametersCassandraResourcesGetCassandraView)|[Example](#ExamplesCassandraResourcesGetCassandraView)|
|[az cosmosdb cassandra-resource show-cassandra-view-throughput](#CassandraResourcesGetCassandraViewThroughput)|GetCassandraViewThroughput|[Parameters](#ParametersCassandraResourcesGetCassandraViewThroughput)|[Example](#ExamplesCassandraResourcesGetCassandraViewThroughput)|
|[az cosmosdb cassandra-resource update-cassandra-keyspace-throughput](#CassandraResourcesUpdateCassandraKeyspaceThroughput)|UpdateCassandraKeyspaceThroughput|[Parameters](#ParametersCassandraResourcesUpdateCassandraKeyspaceThroughput)|[Example](#ExamplesCassandraResourcesUpdateCassandraKeyspaceThroughput)|
|[az cosmosdb cassandra-resource update-cassandra-table-throughput](#CassandraResourcesUpdateCassandraTableThroughput)|UpdateCassandraTableThroughput|[Parameters](#ParametersCassandraResourcesUpdateCassandraTableThroughput)|[Example](#ExamplesCassandraResourcesUpdateCassandraTableThroughput)|
|[az cosmosdb cassandra-resource update-cassandra-view-throughput](#CassandraResourcesUpdateCassandraViewThroughput)|UpdateCassandraViewThroughput|[Parameters](#ParametersCassandraResourcesUpdateCassandraViewThroughput)|[Example](#ExamplesCassandraResourcesUpdateCassandraViewThroughput)|

### <a name="CommandsInCollection">Commands in `az cosmosdb collection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb collection list-metric](#CollectionListMetrics)|ListMetrics|[Parameters](#ParametersCollectionListMetrics)|[Example](#ExamplesCollectionListMetrics)|
|[az cosmosdb collection list-metric-definition](#CollectionListMetricDefinitions)|ListMetricDefinitions|[Parameters](#ParametersCollectionListMetricDefinitions)|[Example](#ExamplesCollectionListMetricDefinitions)|
|[az cosmosdb collection list-usage](#CollectionListUsages)|ListUsages|[Parameters](#ParametersCollectionListUsages)|[Example](#ExamplesCollectionListUsages)|

### <a name="CommandsInCollectionPartition">Commands in `az cosmosdb collection-partition` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb collection-partition list-metric](#CollectionPartitionListMetrics)|ListMetrics|[Parameters](#ParametersCollectionPartitionListMetrics)|[Example](#ExamplesCollectionPartitionListMetrics)|
|[az cosmosdb collection-partition list-usage](#CollectionPartitionListUsages)|ListUsages|[Parameters](#ParametersCollectionPartitionListUsages)|[Example](#ExamplesCollectionPartitionListUsages)|

### <a name="CommandsInCollectionPartitionRegion">Commands in `az cosmosdb collection-partition-region` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb collection-partition-region list-metric](#CollectionPartitionRegionListMetrics)|ListMetrics|[Parameters](#ParametersCollectionPartitionRegionListMetrics)|[Example](#ExamplesCollectionPartitionRegionListMetrics)|

### <a name="CommandsInCollectionRegion">Commands in `az cosmosdb collection-region` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb collection-region list-metric](#CollectionRegionListMetrics)|ListMetrics|[Parameters](#ParametersCollectionRegionListMetrics)|[Example](#ExamplesCollectionRegionListMetrics)|

### <a name="CommandsInDatabase">Commands in `az cosmosdb database` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb database list-metric](#DatabaseListMetrics)|ListMetrics|[Parameters](#ParametersDatabaseListMetrics)|[Example](#ExamplesDatabaseListMetrics)|
|[az cosmosdb database list-metric-definition](#DatabaseListMetricDefinitions)|ListMetricDefinitions|[Parameters](#ParametersDatabaseListMetricDefinitions)|[Example](#ExamplesDatabaseListMetricDefinitions)|
|[az cosmosdb database list-usage](#DatabaseListUsages)|ListUsages|[Parameters](#ParametersDatabaseListUsages)|[Example](#ExamplesDatabaseListUsages)|

### <a name="CommandsInDatabaseAccounts">Commands in `az cosmosdb database-account` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb database-account list](#DatabaseAccountsListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersDatabaseAccountsListByResourceGroup)|[Example](#ExamplesDatabaseAccountsListByResourceGroup)|
|[az cosmosdb database-account list](#DatabaseAccountsList)|List|[Parameters](#ParametersDatabaseAccountsList)|[Example](#ExamplesDatabaseAccountsList)|
|[az cosmosdb database-account show](#DatabaseAccountsGet)|Get|[Parameters](#ParametersDatabaseAccountsGet)|[Example](#ExamplesDatabaseAccountsGet)|
|[az cosmosdb database-account create](#DatabaseAccountsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersDatabaseAccountsCreateOrUpdate#Create)|[Example](#ExamplesDatabaseAccountsCreateOrUpdate#Create)|
|[az cosmosdb database-account update](#DatabaseAccountsUpdate)|Update|[Parameters](#ParametersDatabaseAccountsUpdate)|[Example](#ExamplesDatabaseAccountsUpdate)|
|[az cosmosdb database-account delete](#DatabaseAccountsDelete)|Delete|[Parameters](#ParametersDatabaseAccountsDelete)|[Example](#ExamplesDatabaseAccountsDelete)|
|[az cosmosdb database-account check-name-exist](#DatabaseAccountsCheckNameExists)|CheckNameExists|[Parameters](#ParametersDatabaseAccountsCheckNameExists)|[Example](#ExamplesDatabaseAccountsCheckNameExists)|
|[az cosmosdb database-account failover-priority-change](#DatabaseAccountsFailoverPriorityChange)|FailoverPriorityChange|[Parameters](#ParametersDatabaseAccountsFailoverPriorityChange)|[Example](#ExamplesDatabaseAccountsFailoverPriorityChange)|
|[az cosmosdb database-account list-connection-string](#DatabaseAccountsListConnectionStrings)|ListConnectionStrings|[Parameters](#ParametersDatabaseAccountsListConnectionStrings)|[Example](#ExamplesDatabaseAccountsListConnectionStrings)|
|[az cosmosdb database-account list-key](#DatabaseAccountsListKeys)|ListKeys|[Parameters](#ParametersDatabaseAccountsListKeys)|[Example](#ExamplesDatabaseAccountsListKeys)|
|[az cosmosdb database-account list-metric](#DatabaseAccountsListMetrics)|ListMetrics|[Parameters](#ParametersDatabaseAccountsListMetrics)|[Example](#ExamplesDatabaseAccountsListMetrics)|
|[az cosmosdb database-account list-metric-definition](#DatabaseAccountsListMetricDefinitions)|ListMetricDefinitions|[Parameters](#ParametersDatabaseAccountsListMetricDefinitions)|[Example](#ExamplesDatabaseAccountsListMetricDefinitions)|
|[az cosmosdb database-account list-read-only-key](#DatabaseAccountsListReadOnlyKeys)|ListReadOnlyKeys|[Parameters](#ParametersDatabaseAccountsListReadOnlyKeys)|[Example](#ExamplesDatabaseAccountsListReadOnlyKeys)|
|[az cosmosdb database-account list-usage](#DatabaseAccountsListUsages)|ListUsages|[Parameters](#ParametersDatabaseAccountsListUsages)|[Example](#ExamplesDatabaseAccountsListUsages)|
|[az cosmosdb database-account offline-region](#DatabaseAccountsOfflineRegion)|OfflineRegion|[Parameters](#ParametersDatabaseAccountsOfflineRegion)|[Example](#ExamplesDatabaseAccountsOfflineRegion)|
|[az cosmosdb database-account online-region](#DatabaseAccountsOnlineRegion)|OnlineRegion|[Parameters](#ParametersDatabaseAccountsOnlineRegion)|[Example](#ExamplesDatabaseAccountsOnlineRegion)|
|[az cosmosdb database-account regenerate-key](#DatabaseAccountsRegenerateKey)|RegenerateKey|[Parameters](#ParametersDatabaseAccountsRegenerateKey)|[Example](#ExamplesDatabaseAccountsRegenerateKey)|
|[az cosmosdb database-account show-read-only-key](#DatabaseAccountsGetReadOnlyKeys)|GetReadOnlyKeys|[Parameters](#ParametersDatabaseAccountsGetReadOnlyKeys)|[Example](#ExamplesDatabaseAccountsGetReadOnlyKeys)|

### <a name="CommandsInDatabaseAccountRegion">Commands in `az cosmosdb database-account-region` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb database-account-region list-metric](#DatabaseAccountRegionListMetrics)|ListMetrics|[Parameters](#ParametersDatabaseAccountRegionListMetrics)|[Example](#ExamplesDatabaseAccountRegionListMetrics)|

### <a name="CommandsInDataTransferJobs">Commands in `az cosmosdb dts` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb dts list](#DataTransferJobsListByDatabaseAccount)|ListByDatabaseAccount|[Parameters](#ParametersDataTransferJobsListByDatabaseAccount)|[Example](#ExamplesDataTransferJobsListByDatabaseAccount)|
|[az cosmosdb dts show](#DataTransferJobsGet)|Get|[Parameters](#ParametersDataTransferJobsGet)|[Example](#ExamplesDataTransferJobsGet)|
|[az cosmosdb dts create](#DataTransferJobsCreate)|Create|[Parameters](#ParametersDataTransferJobsCreate)|[Example](#ExamplesDataTransferJobsCreate)|

### <a name="CommandsInGraphResources">Commands in `az cosmosdb graph-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb graph-resource create-update-graph](#GraphResourcesCreateUpdateGraph)|CreateUpdateGraph|[Parameters](#ParametersGraphResourcesCreateUpdateGraph)|[Example](#ExamplesGraphResourcesCreateUpdateGraph)|
|[az cosmosdb graph-resource delete-graph-resource](#GraphResourcesDeleteGraphResource)|DeleteGraphResource|[Parameters](#ParametersGraphResourcesDeleteGraphResource)|[Example](#ExamplesGraphResourcesDeleteGraphResource)|
|[az cosmosdb graph-resource list-graph](#GraphResourcesListGraphs)|ListGraphs|[Parameters](#ParametersGraphResourcesListGraphs)|[Example](#ExamplesGraphResourcesListGraphs)|
|[az cosmosdb graph-resource show-graph](#GraphResourcesGetGraph)|GetGraph|[Parameters](#ParametersGraphResourcesGetGraph)|[Example](#ExamplesGraphResourcesGetGraph)|

### <a name="CommandsInGremlinResources">Commands in `az cosmosdb gremlin-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb gremlin-resource create-update-gremlin-database](#GremlinResourcesCreateUpdateGremlinDatabase)|CreateUpdateGremlinDatabase|[Parameters](#ParametersGremlinResourcesCreateUpdateGremlinDatabase)|[Example](#ExamplesGremlinResourcesCreateUpdateGremlinDatabase)|
|[az cosmosdb gremlin-resource create-update-gremlin-graph](#GremlinResourcesCreateUpdateGremlinGraph)|CreateUpdateGremlinGraph|[Parameters](#ParametersGremlinResourcesCreateUpdateGremlinGraph)|[Example](#ExamplesGremlinResourcesCreateUpdateGremlinGraph)|
|[az cosmosdb gremlin-resource delete-gremlin-database](#GremlinResourcesDeleteGremlinDatabase)|DeleteGremlinDatabase|[Parameters](#ParametersGremlinResourcesDeleteGremlinDatabase)|[Example](#ExamplesGremlinResourcesDeleteGremlinDatabase)|
|[az cosmosdb gremlin-resource delete-gremlin-graph](#GremlinResourcesDeleteGremlinGraph)|DeleteGremlinGraph|[Parameters](#ParametersGremlinResourcesDeleteGremlinGraph)|[Example](#ExamplesGremlinResourcesDeleteGremlinGraph)|
|[az cosmosdb gremlin-resource list-gremlin-database](#GremlinResourcesListGremlinDatabases)|ListGremlinDatabases|[Parameters](#ParametersGremlinResourcesListGremlinDatabases)|[Example](#ExamplesGremlinResourcesListGremlinDatabases)|
|[az cosmosdb gremlin-resource list-gremlin-graph](#GremlinResourcesListGremlinGraphs)|ListGremlinGraphs|[Parameters](#ParametersGremlinResourcesListGremlinGraphs)|[Example](#ExamplesGremlinResourcesListGremlinGraphs)|
|[az cosmosdb gremlin-resource migrate-gremlin-database-to-autoscale](#GremlinResourcesMigrateGremlinDatabaseToAutoscale)|MigrateGremlinDatabaseToAutoscale|[Parameters](#ParametersGremlinResourcesMigrateGremlinDatabaseToAutoscale)|[Example](#ExamplesGremlinResourcesMigrateGremlinDatabaseToAutoscale)|
|[az cosmosdb gremlin-resource migrate-gremlin-database-to-manual-throughput](#GremlinResourcesMigrateGremlinDatabaseToManualThroughput)|MigrateGremlinDatabaseToManualThroughput|[Parameters](#ParametersGremlinResourcesMigrateGremlinDatabaseToManualThroughput)|[Example](#ExamplesGremlinResourcesMigrateGremlinDatabaseToManualThroughput)|
|[az cosmosdb gremlin-resource migrate-gremlin-graph-to-autoscale](#GremlinResourcesMigrateGremlinGraphToAutoscale)|MigrateGremlinGraphToAutoscale|[Parameters](#ParametersGremlinResourcesMigrateGremlinGraphToAutoscale)|[Example](#ExamplesGremlinResourcesMigrateGremlinGraphToAutoscale)|
|[az cosmosdb gremlin-resource migrate-gremlin-graph-to-manual-throughput](#GremlinResourcesMigrateGremlinGraphToManualThroughput)|MigrateGremlinGraphToManualThroughput|[Parameters](#ParametersGremlinResourcesMigrateGremlinGraphToManualThroughput)|[Example](#ExamplesGremlinResourcesMigrateGremlinGraphToManualThroughput)|
|[az cosmosdb gremlin-resource show-gremlin-database](#GremlinResourcesGetGremlinDatabase)|GetGremlinDatabase|[Parameters](#ParametersGremlinResourcesGetGremlinDatabase)|[Example](#ExamplesGremlinResourcesGetGremlinDatabase)|
|[az cosmosdb gremlin-resource show-gremlin-database-throughput](#GremlinResourcesGetGremlinDatabaseThroughput)|GetGremlinDatabaseThroughput|[Parameters](#ParametersGremlinResourcesGetGremlinDatabaseThroughput)|[Example](#ExamplesGremlinResourcesGetGremlinDatabaseThroughput)|
|[az cosmosdb gremlin-resource show-gremlin-graph](#GremlinResourcesGetGremlinGraph)|GetGremlinGraph|[Parameters](#ParametersGremlinResourcesGetGremlinGraph)|[Example](#ExamplesGremlinResourcesGetGremlinGraph)|
|[az cosmosdb gremlin-resource show-gremlin-graph-throughput](#GremlinResourcesGetGremlinGraphThroughput)|GetGremlinGraphThroughput|[Parameters](#ParametersGremlinResourcesGetGremlinGraphThroughput)|[Example](#ExamplesGremlinResourcesGetGremlinGraphThroughput)|
|[az cosmosdb gremlin-resource update-gremlin-database-throughput](#GremlinResourcesUpdateGremlinDatabaseThroughput)|UpdateGremlinDatabaseThroughput|[Parameters](#ParametersGremlinResourcesUpdateGremlinDatabaseThroughput)|[Example](#ExamplesGremlinResourcesUpdateGremlinDatabaseThroughput)|
|[az cosmosdb gremlin-resource update-gremlin-graph-throughput](#GremlinResourcesUpdateGremlinGraphThroughput)|UpdateGremlinGraphThroughput|[Parameters](#ParametersGremlinResourcesUpdateGremlinGraphThroughput)|[Example](#ExamplesGremlinResourcesUpdateGremlinGraphThroughput)|

### <a name="CommandsInMongoDBResources">Commands in `az cosmosdb mongo-db-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb mongo-db-resource create-update-mongo-db-collection](#MongoDBResourcesCreateUpdateMongoDBCollection)|CreateUpdateMongoDBCollection|[Parameters](#ParametersMongoDBResourcesCreateUpdateMongoDBCollection)|[Example](#ExamplesMongoDBResourcesCreateUpdateMongoDBCollection)|
|[az cosmosdb mongo-db-resource create-update-mongo-db-database](#MongoDBResourcesCreateUpdateMongoDBDatabase)|CreateUpdateMongoDBDatabase|[Parameters](#ParametersMongoDBResourcesCreateUpdateMongoDBDatabase)|[Example](#ExamplesMongoDBResourcesCreateUpdateMongoDBDatabase)|
|[az cosmosdb mongo-db-resource delete-mongo-db-collection](#MongoDBResourcesDeleteMongoDBCollection)|DeleteMongoDBCollection|[Parameters](#ParametersMongoDBResourcesDeleteMongoDBCollection)|[Example](#ExamplesMongoDBResourcesDeleteMongoDBCollection)|
|[az cosmosdb mongo-db-resource delete-mongo-db-database](#MongoDBResourcesDeleteMongoDBDatabase)|DeleteMongoDBDatabase|[Parameters](#ParametersMongoDBResourcesDeleteMongoDBDatabase)|[Example](#ExamplesMongoDBResourcesDeleteMongoDBDatabase)|
|[az cosmosdb mongo-db-resource list-mongo-db-collection](#MongoDBResourcesListMongoDBCollections)|ListMongoDBCollections|[Parameters](#ParametersMongoDBResourcesListMongoDBCollections)|[Example](#ExamplesMongoDBResourcesListMongoDBCollections)|
|[az cosmosdb mongo-db-resource list-mongo-db-database](#MongoDBResourcesListMongoDBDatabases)|ListMongoDBDatabases|[Parameters](#ParametersMongoDBResourcesListMongoDBDatabases)|[Example](#ExamplesMongoDBResourcesListMongoDBDatabases)|
|[az cosmosdb mongo-db-resource migrate-mongo-db-collection-to-autoscale](#MongoDBResourcesMigrateMongoDBCollectionToAutoscale)|MigrateMongoDBCollectionToAutoscale|[Parameters](#ParametersMongoDBResourcesMigrateMongoDBCollectionToAutoscale)|[Example](#ExamplesMongoDBResourcesMigrateMongoDBCollectionToAutoscale)|
|[az cosmosdb mongo-db-resource migrate-mongo-db-collection-to-manual-throughput](#MongoDBResourcesMigrateMongoDBCollectionToManualThroughput)|MigrateMongoDBCollectionToManualThroughput|[Parameters](#ParametersMongoDBResourcesMigrateMongoDBCollectionToManualThroughput)|[Example](#ExamplesMongoDBResourcesMigrateMongoDBCollectionToManualThroughput)|
|[az cosmosdb mongo-db-resource migrate-mongo-db-database-to-autoscale](#MongoDBResourcesMigrateMongoDBDatabaseToAutoscale)|MigrateMongoDBDatabaseToAutoscale|[Parameters](#ParametersMongoDBResourcesMigrateMongoDBDatabaseToAutoscale)|[Example](#ExamplesMongoDBResourcesMigrateMongoDBDatabaseToAutoscale)|
|[az cosmosdb mongo-db-resource migrate-mongo-db-database-to-manual-throughput](#MongoDBResourcesMigrateMongoDBDatabaseToManualThroughput)|MigrateMongoDBDatabaseToManualThroughput|[Parameters](#ParametersMongoDBResourcesMigrateMongoDBDatabaseToManualThroughput)|[Example](#ExamplesMongoDBResourcesMigrateMongoDBDatabaseToManualThroughput)|
|[az cosmosdb mongo-db-resource show-mongo-db-collection](#MongoDBResourcesGetMongoDBCollection)|GetMongoDBCollection|[Parameters](#ParametersMongoDBResourcesGetMongoDBCollection)|[Example](#ExamplesMongoDBResourcesGetMongoDBCollection)|
|[az cosmosdb mongo-db-resource show-mongo-db-collection-throughput](#MongoDBResourcesGetMongoDBCollectionThroughput)|GetMongoDBCollectionThroughput|[Parameters](#ParametersMongoDBResourcesGetMongoDBCollectionThroughput)|[Example](#ExamplesMongoDBResourcesGetMongoDBCollectionThroughput)|
|[az cosmosdb mongo-db-resource show-mongo-db-database](#MongoDBResourcesGetMongoDBDatabase)|GetMongoDBDatabase|[Parameters](#ParametersMongoDBResourcesGetMongoDBDatabase)|[Example](#ExamplesMongoDBResourcesGetMongoDBDatabase)|
|[az cosmosdb mongo-db-resource show-mongo-db-database-throughput](#MongoDBResourcesGetMongoDBDatabaseThroughput)|GetMongoDBDatabaseThroughput|[Parameters](#ParametersMongoDBResourcesGetMongoDBDatabaseThroughput)|[Example](#ExamplesMongoDBResourcesGetMongoDBDatabaseThroughput)|
|[az cosmosdb mongo-db-resource update-mongo-db-collection-throughput](#MongoDBResourcesUpdateMongoDBCollectionThroughput)|UpdateMongoDBCollectionThroughput|[Parameters](#ParametersMongoDBResourcesUpdateMongoDBCollectionThroughput)|[Example](#ExamplesMongoDBResourcesUpdateMongoDBCollectionThroughput)|
|[az cosmosdb mongo-db-resource update-mongo-db-database-throughput](#MongoDBResourcesUpdateMongoDBDatabaseThroughput)|UpdateMongoDBDatabaseThroughput|[Parameters](#ParametersMongoDBResourcesUpdateMongoDBDatabaseThroughput)|[Example](#ExamplesMongoDBResourcesUpdateMongoDBDatabaseThroughput)|

### <a name="CommandsInNotebookWorkspaces">Commands in `az cosmosdb notebook-workspace` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb notebook-workspace list](#NotebookWorkspacesListByDatabaseAccount)|ListByDatabaseAccount|[Parameters](#ParametersNotebookWorkspacesListByDatabaseAccount)|[Example](#ExamplesNotebookWorkspacesListByDatabaseAccount)|
|[az cosmosdb notebook-workspace show](#NotebookWorkspacesGet)|Get|[Parameters](#ParametersNotebookWorkspacesGet)|[Example](#ExamplesNotebookWorkspacesGet)|
|[az cosmosdb notebook-workspace create](#NotebookWorkspacesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersNotebookWorkspacesCreateOrUpdate#Create)|[Example](#ExamplesNotebookWorkspacesCreateOrUpdate#Create)|
|[az cosmosdb notebook-workspace update](#NotebookWorkspacesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersNotebookWorkspacesCreateOrUpdate#Update)|Not Found|
|[az cosmosdb notebook-workspace delete](#NotebookWorkspacesDelete)|Delete|[Parameters](#ParametersNotebookWorkspacesDelete)|[Example](#ExamplesNotebookWorkspacesDelete)|
|[az cosmosdb notebook-workspace list-connection-info](#NotebookWorkspacesListConnectionInfo)|ListConnectionInfo|[Parameters](#ParametersNotebookWorkspacesListConnectionInfo)|[Example](#ExamplesNotebookWorkspacesListConnectionInfo)|
|[az cosmosdb notebook-workspace regenerate-auth-token](#NotebookWorkspacesRegenerateAuthToken)|RegenerateAuthToken|[Parameters](#ParametersNotebookWorkspacesRegenerateAuthToken)|[Example](#ExamplesNotebookWorkspacesRegenerateAuthToken)|
|[az cosmosdb notebook-workspace start](#NotebookWorkspacesStart)|Start|[Parameters](#ParametersNotebookWorkspacesStart)|[Example](#ExamplesNotebookWorkspacesStart)|

### <a name="CommandsInPartitionKeyRangeId">Commands in `az cosmosdb partition-key-range-id` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb partition-key-range-id list-metric](#PartitionKeyRangeIdListMetrics)|ListMetrics|[Parameters](#ParametersPartitionKeyRangeIdListMetrics)|[Example](#ExamplesPartitionKeyRangeIdListMetrics)|

### <a name="CommandsInPartitionKeyRangeIdRegion">Commands in `az cosmosdb partition-key-range-id-region` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb partition-key-range-id-region list-metric](#PartitionKeyRangeIdRegionListMetrics)|ListMetrics|[Parameters](#ParametersPartitionKeyRangeIdRegionListMetrics)|[Example](#ExamplesPartitionKeyRangeIdRegionListMetrics)|

### <a name="CommandsInPercentile">Commands in `az cosmosdb percentile` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb percentile list-metric](#PercentileListMetrics)|ListMetrics|[Parameters](#ParametersPercentileListMetrics)|[Example](#ExamplesPercentileListMetrics)|

### <a name="CommandsInPercentileSourceTarget">Commands in `az cosmosdb percentile-source-target` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb percentile-source-target list-metric](#PercentileSourceTargetListMetrics)|ListMetrics|[Parameters](#ParametersPercentileSourceTargetListMetrics)|[Example](#ExamplesPercentileSourceTargetListMetrics)|

### <a name="CommandsInPercentileTarget">Commands in `az cosmosdb percentile-target` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb percentile-target list-metric](#PercentileTargetListMetrics)|ListMetrics|[Parameters](#ParametersPercentileTargetListMetrics)|[Example](#ExamplesPercentileTargetListMetrics)|

### <a name="CommandsInPrivateEndpointConnections">Commands in `az cosmosdb private-endpoint-connection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb private-endpoint-connection list](#PrivateEndpointConnectionsListByDatabaseAccount)|ListByDatabaseAccount|[Parameters](#ParametersPrivateEndpointConnectionsListByDatabaseAccount)|[Example](#ExamplesPrivateEndpointConnectionsListByDatabaseAccount)|
|[az cosmosdb private-endpoint-connection show](#PrivateEndpointConnectionsGet)|Get|[Parameters](#ParametersPrivateEndpointConnectionsGet)|[Example](#ExamplesPrivateEndpointConnectionsGet)|
|[az cosmosdb private-endpoint-connection create](#PrivateEndpointConnectionsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersPrivateEndpointConnectionsCreateOrUpdate#Create)|[Example](#ExamplesPrivateEndpointConnectionsCreateOrUpdate#Create)|
|[az cosmosdb private-endpoint-connection update](#PrivateEndpointConnectionsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersPrivateEndpointConnectionsCreateOrUpdate#Update)|Not Found|
|[az cosmosdb private-endpoint-connection delete](#PrivateEndpointConnectionsDelete)|Delete|[Parameters](#ParametersPrivateEndpointConnectionsDelete)|[Example](#ExamplesPrivateEndpointConnectionsDelete)|

### <a name="CommandsInPrivateLinkResources">Commands in `az cosmosdb private-link-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb private-link-resource list](#PrivateLinkResourcesListByDatabaseAccount)|ListByDatabaseAccount|[Parameters](#ParametersPrivateLinkResourcesListByDatabaseAccount)|[Example](#ExamplesPrivateLinkResourcesListByDatabaseAccount)|
|[az cosmosdb private-link-resource show](#PrivateLinkResourcesGet)|Get|[Parameters](#ParametersPrivateLinkResourcesGet)|[Example](#ExamplesPrivateLinkResourcesGet)|

### <a name="CommandsInRestorableDatabaseAccounts">Commands in `az cosmosdb restorable-database-account` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb restorable-database-account list](#RestorableDatabaseAccountsListByLocation)|ListByLocation|[Parameters](#ParametersRestorableDatabaseAccountsListByLocation)|[Example](#ExamplesRestorableDatabaseAccountsListByLocation)|
|[az cosmosdb restorable-database-account list](#RestorableDatabaseAccountsList)|List|[Parameters](#ParametersRestorableDatabaseAccountsList)|[Example](#ExamplesRestorableDatabaseAccountsList)|
|[az cosmosdb restorable-database-account show](#RestorableDatabaseAccountsGetByLocation)|GetByLocation|[Parameters](#ParametersRestorableDatabaseAccountsGetByLocation)|[Example](#ExamplesRestorableDatabaseAccountsGetByLocation)|

### <a name="CommandsInRestorableMongodbCollections">Commands in `az cosmosdb restorable-mongodb-collection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb restorable-mongodb-collection list](#RestorableMongodbCollectionsList)|List|[Parameters](#ParametersRestorableMongodbCollectionsList)|[Example](#ExamplesRestorableMongodbCollectionsList)|

### <a name="CommandsInRestorableMongodbDatabases">Commands in `az cosmosdb restorable-mongodb-database` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb restorable-mongodb-database list](#RestorableMongodbDatabasesList)|List|[Parameters](#ParametersRestorableMongodbDatabasesList)|[Example](#ExamplesRestorableMongodbDatabasesList)|

### <a name="CommandsInRestorableMongodbResources">Commands in `az cosmosdb restorable-mongodb-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb restorable-mongodb-resource list](#RestorableMongodbResourcesList)|List|[Parameters](#ParametersRestorableMongodbResourcesList)|[Example](#ExamplesRestorableMongodbResourcesList)|

### <a name="CommandsInRestorableSqlContainers">Commands in `az cosmosdb restorable-sql-container` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb restorable-sql-container list](#RestorableSqlContainersList)|List|[Parameters](#ParametersRestorableSqlContainersList)|[Example](#ExamplesRestorableSqlContainersList)|

### <a name="CommandsInRestorableSqlDatabases">Commands in `az cosmosdb restorable-sql-database` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb restorable-sql-database list](#RestorableSqlDatabasesList)|List|[Parameters](#ParametersRestorableSqlDatabasesList)|[Example](#ExamplesRestorableSqlDatabasesList)|

### <a name="CommandsInRestorableSqlResources">Commands in `az cosmosdb restorable-sql-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb restorable-sql-resource list](#RestorableSqlResourcesList)|List|[Parameters](#ParametersRestorableSqlResourcesList)|[Example](#ExamplesRestorableSqlResourcesList)|

### <a name="CommandsInService">Commands in `az cosmosdb service` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb service list](#ServiceList)|List|[Parameters](#ParametersServiceList)|[Example](#ExamplesServiceList)|
|[az cosmosdb service show](#ServiceGet)|Get|[Parameters](#ParametersServiceGet)|[Example](#ExamplesServiceGet)|
|[az cosmosdb service create](#ServiceCreate)|Create|[Parameters](#ParametersServiceCreate)|[Example](#ExamplesServiceCreate)|
|[az cosmosdb service delete](#ServiceDelete)|Delete|[Parameters](#ParametersServiceDelete)|[Example](#ExamplesServiceDelete)|

### <a name="CommandsInSqlResources">Commands in `az cosmosdb sql-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb sql-resource create-update-sql-container](#SqlResourcesCreateUpdateSqlContainer)|CreateUpdateSqlContainer|[Parameters](#ParametersSqlResourcesCreateUpdateSqlContainer)|[Example](#ExamplesSqlResourcesCreateUpdateSqlContainer)|
|[az cosmosdb sql-resource create-update-sql-database](#SqlResourcesCreateUpdateSqlDatabase)|CreateUpdateSqlDatabase|[Parameters](#ParametersSqlResourcesCreateUpdateSqlDatabase)|[Example](#ExamplesSqlResourcesCreateUpdateSqlDatabase)|
|[az cosmosdb sql-resource create-update-sql-role-assignment](#SqlResourcesCreateUpdateSqlRoleAssignment)|CreateUpdateSqlRoleAssignment|[Parameters](#ParametersSqlResourcesCreateUpdateSqlRoleAssignment)|[Example](#ExamplesSqlResourcesCreateUpdateSqlRoleAssignment)|
|[az cosmosdb sql-resource create-update-sql-role-definition](#SqlResourcesCreateUpdateSqlRoleDefinition)|CreateUpdateSqlRoleDefinition|[Parameters](#ParametersSqlResourcesCreateUpdateSqlRoleDefinition)|[Example](#ExamplesSqlResourcesCreateUpdateSqlRoleDefinition)|
|[az cosmosdb sql-resource create-update-sql-stored-procedure](#SqlResourcesCreateUpdateSqlStoredProcedure)|CreateUpdateSqlStoredProcedure|[Parameters](#ParametersSqlResourcesCreateUpdateSqlStoredProcedure)|[Example](#ExamplesSqlResourcesCreateUpdateSqlStoredProcedure)|
|[az cosmosdb sql-resource create-update-sql-trigger](#SqlResourcesCreateUpdateSqlTrigger)|CreateUpdateSqlTrigger|[Parameters](#ParametersSqlResourcesCreateUpdateSqlTrigger)|[Example](#ExamplesSqlResourcesCreateUpdateSqlTrigger)|
|[az cosmosdb sql-resource create-update-sql-user-defined-function](#SqlResourcesCreateUpdateSqlUserDefinedFunction)|CreateUpdateSqlUserDefinedFunction|[Parameters](#ParametersSqlResourcesCreateUpdateSqlUserDefinedFunction)|[Example](#ExamplesSqlResourcesCreateUpdateSqlUserDefinedFunction)|
|[az cosmosdb sql-resource delete-sql-container](#SqlResourcesDeleteSqlContainer)|DeleteSqlContainer|[Parameters](#ParametersSqlResourcesDeleteSqlContainer)|[Example](#ExamplesSqlResourcesDeleteSqlContainer)|
|[az cosmosdb sql-resource delete-sql-database](#SqlResourcesDeleteSqlDatabase)|DeleteSqlDatabase|[Parameters](#ParametersSqlResourcesDeleteSqlDatabase)|[Example](#ExamplesSqlResourcesDeleteSqlDatabase)|
|[az cosmosdb sql-resource delete-sql-role-assignment](#SqlResourcesDeleteSqlRoleAssignment)|DeleteSqlRoleAssignment|[Parameters](#ParametersSqlResourcesDeleteSqlRoleAssignment)|[Example](#ExamplesSqlResourcesDeleteSqlRoleAssignment)|
|[az cosmosdb sql-resource delete-sql-role-definition](#SqlResourcesDeleteSqlRoleDefinition)|DeleteSqlRoleDefinition|[Parameters](#ParametersSqlResourcesDeleteSqlRoleDefinition)|[Example](#ExamplesSqlResourcesDeleteSqlRoleDefinition)|
|[az cosmosdb sql-resource delete-sql-stored-procedure](#SqlResourcesDeleteSqlStoredProcedure)|DeleteSqlStoredProcedure|[Parameters](#ParametersSqlResourcesDeleteSqlStoredProcedure)|[Example](#ExamplesSqlResourcesDeleteSqlStoredProcedure)|
|[az cosmosdb sql-resource delete-sql-trigger](#SqlResourcesDeleteSqlTrigger)|DeleteSqlTrigger|[Parameters](#ParametersSqlResourcesDeleteSqlTrigger)|[Example](#ExamplesSqlResourcesDeleteSqlTrigger)|
|[az cosmosdb sql-resource delete-sql-user-defined-function](#SqlResourcesDeleteSqlUserDefinedFunction)|DeleteSqlUserDefinedFunction|[Parameters](#ParametersSqlResourcesDeleteSqlUserDefinedFunction)|[Example](#ExamplesSqlResourcesDeleteSqlUserDefinedFunction)|
|[az cosmosdb sql-resource list-sql-container](#SqlResourcesListSqlContainers)|ListSqlContainers|[Parameters](#ParametersSqlResourcesListSqlContainers)|[Example](#ExamplesSqlResourcesListSqlContainers)|
|[az cosmosdb sql-resource list-sql-database](#SqlResourcesListSqlDatabases)|ListSqlDatabases|[Parameters](#ParametersSqlResourcesListSqlDatabases)|[Example](#ExamplesSqlResourcesListSqlDatabases)|
|[az cosmosdb sql-resource list-sql-role-assignment](#SqlResourcesListSqlRoleAssignments)|ListSqlRoleAssignments|[Parameters](#ParametersSqlResourcesListSqlRoleAssignments)|[Example](#ExamplesSqlResourcesListSqlRoleAssignments)|
|[az cosmosdb sql-resource list-sql-role-definition](#SqlResourcesListSqlRoleDefinitions)|ListSqlRoleDefinitions|[Parameters](#ParametersSqlResourcesListSqlRoleDefinitions)|[Example](#ExamplesSqlResourcesListSqlRoleDefinitions)|
|[az cosmosdb sql-resource list-sql-stored-procedure](#SqlResourcesListSqlStoredProcedures)|ListSqlStoredProcedures|[Parameters](#ParametersSqlResourcesListSqlStoredProcedures)|[Example](#ExamplesSqlResourcesListSqlStoredProcedures)|
|[az cosmosdb sql-resource list-sql-trigger](#SqlResourcesListSqlTriggers)|ListSqlTriggers|[Parameters](#ParametersSqlResourcesListSqlTriggers)|[Example](#ExamplesSqlResourcesListSqlTriggers)|
|[az cosmosdb sql-resource list-sql-user-defined-function](#SqlResourcesListSqlUserDefinedFunctions)|ListSqlUserDefinedFunctions|[Parameters](#ParametersSqlResourcesListSqlUserDefinedFunctions)|[Example](#ExamplesSqlResourcesListSqlUserDefinedFunctions)|
|[az cosmosdb sql-resource migrate-sql-container-to-autoscale](#SqlResourcesMigrateSqlContainerToAutoscale)|MigrateSqlContainerToAutoscale|[Parameters](#ParametersSqlResourcesMigrateSqlContainerToAutoscale)|[Example](#ExamplesSqlResourcesMigrateSqlContainerToAutoscale)|
|[az cosmosdb sql-resource migrate-sql-container-to-manual-throughput](#SqlResourcesMigrateSqlContainerToManualThroughput)|MigrateSqlContainerToManualThroughput|[Parameters](#ParametersSqlResourcesMigrateSqlContainerToManualThroughput)|[Example](#ExamplesSqlResourcesMigrateSqlContainerToManualThroughput)|
|[az cosmosdb sql-resource migrate-sql-database-to-autoscale](#SqlResourcesMigrateSqlDatabaseToAutoscale)|MigrateSqlDatabaseToAutoscale|[Parameters](#ParametersSqlResourcesMigrateSqlDatabaseToAutoscale)|[Example](#ExamplesSqlResourcesMigrateSqlDatabaseToAutoscale)|
|[az cosmosdb sql-resource migrate-sql-database-to-manual-throughput](#SqlResourcesMigrateSqlDatabaseToManualThroughput)|MigrateSqlDatabaseToManualThroughput|[Parameters](#ParametersSqlResourcesMigrateSqlDatabaseToManualThroughput)|[Example](#ExamplesSqlResourcesMigrateSqlDatabaseToManualThroughput)|
|[az cosmosdb sql-resource retrieve-continuou-backup-information](#SqlResourcesRetrieveContinuousBackupInformation)|RetrieveContinuousBackupInformation|[Parameters](#ParametersSqlResourcesRetrieveContinuousBackupInformation)|[Example](#ExamplesSqlResourcesRetrieveContinuousBackupInformation)|
|[az cosmosdb sql-resource show-sql-container](#SqlResourcesGetSqlContainer)|GetSqlContainer|[Parameters](#ParametersSqlResourcesGetSqlContainer)|[Example](#ExamplesSqlResourcesGetSqlContainer)|
|[az cosmosdb sql-resource show-sql-container-throughput](#SqlResourcesGetSqlContainerThroughput)|GetSqlContainerThroughput|[Parameters](#ParametersSqlResourcesGetSqlContainerThroughput)|[Example](#ExamplesSqlResourcesGetSqlContainerThroughput)|
|[az cosmosdb sql-resource show-sql-database](#SqlResourcesGetSqlDatabase)|GetSqlDatabase|[Parameters](#ParametersSqlResourcesGetSqlDatabase)|[Example](#ExamplesSqlResourcesGetSqlDatabase)|
|[az cosmosdb sql-resource show-sql-database-throughput](#SqlResourcesGetSqlDatabaseThroughput)|GetSqlDatabaseThroughput|[Parameters](#ParametersSqlResourcesGetSqlDatabaseThroughput)|[Example](#ExamplesSqlResourcesGetSqlDatabaseThroughput)|
|[az cosmosdb sql-resource show-sql-role-assignment](#SqlResourcesGetSqlRoleAssignment)|GetSqlRoleAssignment|[Parameters](#ParametersSqlResourcesGetSqlRoleAssignment)|[Example](#ExamplesSqlResourcesGetSqlRoleAssignment)|
|[az cosmosdb sql-resource show-sql-role-definition](#SqlResourcesGetSqlRoleDefinition)|GetSqlRoleDefinition|[Parameters](#ParametersSqlResourcesGetSqlRoleDefinition)|[Example](#ExamplesSqlResourcesGetSqlRoleDefinition)|
|[az cosmosdb sql-resource show-sql-stored-procedure](#SqlResourcesGetSqlStoredProcedure)|GetSqlStoredProcedure|[Parameters](#ParametersSqlResourcesGetSqlStoredProcedure)|[Example](#ExamplesSqlResourcesGetSqlStoredProcedure)|
|[az cosmosdb sql-resource show-sql-trigger](#SqlResourcesGetSqlTrigger)|GetSqlTrigger|[Parameters](#ParametersSqlResourcesGetSqlTrigger)|[Example](#ExamplesSqlResourcesGetSqlTrigger)|
|[az cosmosdb sql-resource show-sql-user-defined-function](#SqlResourcesGetSqlUserDefinedFunction)|GetSqlUserDefinedFunction|[Parameters](#ParametersSqlResourcesGetSqlUserDefinedFunction)|[Example](#ExamplesSqlResourcesGetSqlUserDefinedFunction)|
|[az cosmosdb sql-resource update-sql-container-throughput](#SqlResourcesUpdateSqlContainerThroughput)|UpdateSqlContainerThroughput|[Parameters](#ParametersSqlResourcesUpdateSqlContainerThroughput)|[Example](#ExamplesSqlResourcesUpdateSqlContainerThroughput)|
|[az cosmosdb sql-resource update-sql-database-throughput](#SqlResourcesUpdateSqlDatabaseThroughput)|UpdateSqlDatabaseThroughput|[Parameters](#ParametersSqlResourcesUpdateSqlDatabaseThroughput)|[Example](#ExamplesSqlResourcesUpdateSqlDatabaseThroughput)|

### <a name="CommandsInTableResources">Commands in `az cosmosdb table-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cosmosdb table-resource create-update-table](#TableResourcesCreateUpdateTable)|CreateUpdateTable|[Parameters](#ParametersTableResourcesCreateUpdateTable)|[Example](#ExamplesTableResourcesCreateUpdateTable)|
|[az cosmosdb table-resource delete-table](#TableResourcesDeleteTable)|DeleteTable|[Parameters](#ParametersTableResourcesDeleteTable)|[Example](#ExamplesTableResourcesDeleteTable)|
|[az cosmosdb table-resource list-table](#TableResourcesListTables)|ListTables|[Parameters](#ParametersTableResourcesListTables)|[Example](#ExamplesTableResourcesListTables)|
|[az cosmosdb table-resource migrate-table-to-autoscale](#TableResourcesMigrateTableToAutoscale)|MigrateTableToAutoscale|[Parameters](#ParametersTableResourcesMigrateTableToAutoscale)|[Example](#ExamplesTableResourcesMigrateTableToAutoscale)|
|[az cosmosdb table-resource migrate-table-to-manual-throughput](#TableResourcesMigrateTableToManualThroughput)|MigrateTableToManualThroughput|[Parameters](#ParametersTableResourcesMigrateTableToManualThroughput)|[Example](#ExamplesTableResourcesMigrateTableToManualThroughput)|
|[az cosmosdb table-resource show-table](#TableResourcesGetTable)|GetTable|[Parameters](#ParametersTableResourcesGetTable)|[Example](#ExamplesTableResourcesGetTable)|
|[az cosmosdb table-resource show-table-throughput](#TableResourcesGetTableThroughput)|GetTableThroughput|[Parameters](#ParametersTableResourcesGetTableThroughput)|[Example](#ExamplesTableResourcesGetTableThroughput)|
|[az cosmosdb table-resource update-table-throughput](#TableResourcesUpdateTableThroughput)|UpdateTableThroughput|[Parameters](#ParametersTableResourcesUpdateTableThroughput)|[Example](#ExamplesTableResourcesUpdateTableThroughput)|


## COMMAND DETAILS
### group `az cosmosdb`
#### <a name="LocationGet">Command `az cosmosdb location-get`</a>

##### <a name="ExamplesLocationGet">Example</a>
```
az cosmosdb location-get --location "westus"
```
##### <a name="ParametersLocationGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Cosmos DB region, with spaces between words and each word capitalized.|location|location|

#### <a name="LocationList">Command `az cosmosdb location-list`</a>

##### <a name="ExamplesLocationList">Example</a>
```
az cosmosdb location-list
```
##### <a name="ParametersLocationList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### group `az cosmosdb cassandra-cluster`
#### <a name="CassandraClustersListByResourceGroup">Command `az cosmosdb cassandra-cluster list`</a>

##### <a name="ExamplesCassandraClustersListByResourceGroup">Example</a>
```
az cosmosdb cassandra-cluster list --resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraClustersListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|

#### <a name="CassandraClustersListBySubscription">Command `az cosmosdb cassandra-cluster list`</a>

##### <a name="ExamplesCassandraClustersListBySubscription">Example</a>
```
az cosmosdb cassandra-cluster list
```
##### <a name="ParametersCassandraClustersListBySubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

#### <a name="CassandraClustersGet">Command `az cosmosdb cassandra-cluster show`</a>

##### <a name="ExamplesCassandraClustersGet">Example</a>
```
az cosmosdb cassandra-cluster show --cluster-name "cassandra-prod" --resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraClustersGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|

#### <a name="CassandraClustersUpdate">Command `az cosmosdb cassandra-cluster update`</a>

##### <a name="ExamplesCassandraClustersUpdate">Example</a>
```
az cosmosdb cassandra-cluster update --authentication-method "None" --external-gossip-certificates pem="-----BEGIN \
CERTIFICATE-----\\n...Base64 encoded certificate...\\n-----END CERTIFICATE-----" --external-seed-nodes \
ip-address="10.52.221.2" --external-seed-nodes ip-address="10.52.221.3" --external-seed-nodes ip-address="10.52.221.4" \
--hours-between-backups 12 --tags owner="mike" --cluster-name "cassandra-prod" --resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraClustersUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--provisioning-state**|choice|The status of the resource at the time the operation was called.|provisioning_state|provisioningState|
|**--restore-from-backup-id**|string|To create an empty cluster, omit this field or set it to null. To restore a backup into a new cluster, set this field to the resource id of the backup.|restore_from_backup_id|restoreFromBackupId|
|**--delegated-management-subnet-id**|string|Resource id of a subnet that this cluster's management service should have its network interface attached to. The subnet must be routable to all subnets that will be delegated to data centers. The resource id must be of the form '/subscriptions/<subscription id>/resourceGroups/<resource group>/providers/Microsoft.Network/virtualNetworks/<virtual network>/subnets/<subnet>'|delegated_management_subnet_id|delegatedManagementSubnetId|
|**--cassandra-version**|string|Which version of Cassandra should this cluster converge to running (e.g., 3.11). When updated, the cluster may take some time to migrate to the new version.|cassandra_version|cassandraVersion|
|**--cluster-name-override**|string|If you need to set the clusterName property in cassandra.yaml to something besides the resource name of the cluster, set the value to use on this property.|cluster_name_override|clusterNameOverride|
|**--authentication-method**|choice|Which authentication method Cassandra should use to authenticate clients. 'None' turns off authentication, so should not be used except in emergencies. 'Cassandra' is the default password based authentication. The default is 'Cassandra'.|authentication_method|authenticationMethod|
|**--initial-cassandra-admin-password**|string|Initial password for clients connecting as admin to the cluster. Should be changed after cluster creation. Returns null on GET. This field only applies when the authenticationMethod field is 'Cassandra'.|initial_cassandra_admin_password|initialCassandraAdminPassword|
|**--hours-between-backups**|integer|Number of hours to wait between taking a backup of the cluster. To disable backups, set this property to 0.|hours_between_backups|hoursBetweenBackups|
|**--repair-enabled**|boolean|Should automatic repairs run on this cluster? If omitted, this is true, and should stay true unless you are running a hybrid cluster where you are already doing your own repairs.|repair_enabled|repairEnabled|
|**--client-certificates**|array|List of TLS certificates used to authorize clients connecting to the cluster. All connections are TLS encrypted whether clientCertificates is set or not, but if clientCertificates is set, the managed Cassandra cluster will reject all connections not bearing a TLS client certificate that can be validated from one or more of the public certificates in this property.|client_certificates|clientCertificates|
|**--external-gossip-certificates**|array|List of TLS certificates used to authorize gossip from unmanaged data centers. The TLS certificates of all nodes in unmanaged data centers must be verifiable using one of the certificates provided in this property.|external_gossip_certificates|externalGossipCertificates|
|**--external-seed-nodes**|array|List of IP addresses of seed nodes in unmanaged data centers. These will be added to the seed node lists of all managed nodes.|external_seed_nodes|externalSeedNodes|
|**--ip-address**|string|IP address of this seed node.|ip_address|ipAddress|

#### <a name="CassandraClustersDelete">Command `az cosmosdb cassandra-cluster delete`</a>

##### <a name="ExamplesCassandraClustersDelete">Example</a>
```
az cosmosdb cassandra-cluster delete --cluster-name "cassandra-prod" --resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraClustersDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|

#### <a name="CassandraClustersCreateUpdate">Command `az cosmosdb cassandra-cluster create-update`</a>

##### <a name="ExamplesCassandraClustersCreateUpdate">Example</a>
```
az cosmosdb cassandra-cluster create-update --location "West US" --authentication-method "Cassandra" \
--cassandra-version "3.11" --client-certificates pem="-----BEGIN CERTIFICATE-----\\n...Base64 encoded \
certificate...\\n-----END CERTIFICATE-----" --cluster-name-override "ClusterNameIllegalForAzureResource" \
--delegated-management-subnet-id "/subscriptions/536e130b-d7d6-4ac7-98a5-de20d69588d2/resourceGroups/customer-vnet-rg/p\
roviders/Microsoft.Network/virtualNetworks/customer-vnet/subnets/management" --external-gossip-certificates \
pem="-----BEGIN CERTIFICATE-----\\n...Base64 encoded certificate...\\n-----END CERTIFICATE-----" --external-seed-nodes \
ip-address="10.52.221.2" --external-seed-nodes ip-address="10.52.221.3" --external-seed-nodes ip-address="10.52.221.4" \
--hours-between-backups 24 --initial-cassandra-admin-password "mypassword" --cluster-name "cassandra-prod" \
--resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraClustersCreateUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--provisioning-state**|choice|The status of the resource at the time the operation was called.|provisioning_state|provisioningState|
|**--restore-from-backup-id**|string|To create an empty cluster, omit this field or set it to null. To restore a backup into a new cluster, set this field to the resource id of the backup.|restore_from_backup_id|restoreFromBackupId|
|**--delegated-management-subnet-id**|string|Resource id of a subnet that this cluster's management service should have its network interface attached to. The subnet must be routable to all subnets that will be delegated to data centers. The resource id must be of the form '/subscriptions/<subscription id>/resourceGroups/<resource group>/providers/Microsoft.Network/virtualNetworks/<virtual network>/subnets/<subnet>'|delegated_management_subnet_id|delegatedManagementSubnetId|
|**--cassandra-version**|string|Which version of Cassandra should this cluster converge to running (e.g., 3.11). When updated, the cluster may take some time to migrate to the new version.|cassandra_version|cassandraVersion|
|**--cluster-name-override**|string|If you need to set the clusterName property in cassandra.yaml to something besides the resource name of the cluster, set the value to use on this property.|cluster_name_override|clusterNameOverride|
|**--authentication-method**|choice|Which authentication method Cassandra should use to authenticate clients. 'None' turns off authentication, so should not be used except in emergencies. 'Cassandra' is the default password based authentication. The default is 'Cassandra'.|authentication_method|authenticationMethod|
|**--initial-cassandra-admin-password**|string|Initial password for clients connecting as admin to the cluster. Should be changed after cluster creation. Returns null on GET. This field only applies when the authenticationMethod field is 'Cassandra'.|initial_cassandra_admin_password|initialCassandraAdminPassword|
|**--hours-between-backups**|integer|Number of hours to wait between taking a backup of the cluster. To disable backups, set this property to 0.|hours_between_backups|hoursBetweenBackups|
|**--repair-enabled**|boolean|Should automatic repairs run on this cluster? If omitted, this is true, and should stay true unless you are running a hybrid cluster where you are already doing your own repairs.|repair_enabled|repairEnabled|
|**--client-certificates**|array|List of TLS certificates used to authorize clients connecting to the cluster. All connections are TLS encrypted whether clientCertificates is set or not, but if clientCertificates is set, the managed Cassandra cluster will reject all connections not bearing a TLS client certificate that can be validated from one or more of the public certificates in this property.|client_certificates|clientCertificates|
|**--external-gossip-certificates**|array|List of TLS certificates used to authorize gossip from unmanaged data centers. The TLS certificates of all nodes in unmanaged data centers must be verifiable using one of the certificates provided in this property.|external_gossip_certificates|externalGossipCertificates|
|**--external-seed-nodes**|array|List of IP addresses of seed nodes in unmanaged data centers. These will be added to the seed node lists of all managed nodes.|external_seed_nodes|externalSeedNodes|
|**--ip-address**|string|IP address of this seed node.|ip_address|ipAddress|

#### <a name="CassandraClustersFetchNodeStatus">Command `az cosmosdb cassandra-cluster fetch-node-status`</a>

##### <a name="ExamplesCassandraClustersFetchNodeStatus">Example</a>
```
az cosmosdb cassandra-cluster fetch-node-status --cluster-name "cassandra-prod" --resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraClustersFetchNodeStatus">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|

#### <a name="CassandraClustersListBackups">Command `az cosmosdb cassandra-cluster list-backup`</a>

##### <a name="ExamplesCassandraClustersListBackups">Example</a>
```
az cosmosdb cassandra-cluster list-backup --cluster-name "cassandra-prod" --resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraClustersListBackups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|

#### <a name="CassandraClustersRequestRepair">Command `az cosmosdb cassandra-cluster request-repair`</a>

##### <a name="ExamplesCassandraClustersRequestRepair">Example</a>
```
az cosmosdb cassandra-cluster request-repair --keyspace "my-keyspace" --tables "table1" "table42" --cluster-name \
"cassandra-prod" --resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraClustersRequestRepair">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|
|**--keyspace**|string|The name of the keyspace that repair should be run on.|keyspace|keyspace|
|**--tables**|array|List of tables in the keyspace to repair. If omitted, repair all tables in the keyspace.|tables|tables|

#### <a name="CassandraClustersGetBackup">Command `az cosmosdb cassandra-cluster show-backup`</a>

##### <a name="ExamplesCassandraClustersGetBackup">Example</a>
```
az cosmosdb cassandra-cluster show-backup --backup-id "1611250348" --cluster-name "cassandra-prod" --resource-group \
"cassandra-prod-rg"
```
##### <a name="ParametersCassandraClustersGetBackup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|
|**--backup-id**|string|Id of a restorable backup of a Cassandra cluster.|backup_id|backupId|

### group `az cosmosdb cassandra-data-center`
#### <a name="CassandraDataCentersList">Command `az cosmosdb cassandra-data-center list`</a>

##### <a name="ExamplesCassandraDataCentersList">Example</a>
```
az cosmosdb cassandra-data-center list --cluster-name "cassandra-prod" --resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraDataCentersList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|

#### <a name="CassandraDataCentersGet">Command `az cosmosdb cassandra-data-center show`</a>

##### <a name="ExamplesCassandraDataCentersGet">Example</a>
```
az cosmosdb cassandra-data-center show --cluster-name "cassandra-prod" --data-center-name "dc1" --resource-group \
"cassandra-prod-rg"
```
##### <a name="ParametersCassandraDataCentersGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|
|**--data-center-name**|string|Data center name in a managed Cassandra cluster.|data_center_name|dataCenterName|

#### <a name="CassandraDataCentersUpdate">Command `az cosmosdb cassandra-data-center update`</a>

##### <a name="ExamplesCassandraDataCentersUpdate">Example</a>
```
az cosmosdb cassandra-data-center update --base64-encoded-cassandra-yaml-fragment "Y29tcGFjdGlvbl90aHJvdWdocHV0X21iX3Bl\
cl9zZWM6IDMyCmNvbXBhY3Rpb25fbGFyZ2VfcGFydGl0aW9uX3dhcm5pbmdfdGhyZXNob2xkX21iOiAxMDA=" --data-center-location "West US \
2" --delegated-subnet-id "/subscriptions/536e130b-d7d6-4ac7-98a5-de20d69588d2/resourceGroups/customer-vnet-rg/providers\
/Microsoft.Network/virtualNetworks/customer-vnet/subnets/dc1-subnet" --node-count 9 --cluster-name "cassandra-prod" \
--data-center-name "dc1" --resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraDataCentersUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|
|**--data-center-name**|string|Data center name in a managed Cassandra cluster.|data_center_name|dataCenterName|
|**--provisioning-state**|choice|The status of the resource at the time the operation was called.|provisioning_state|provisioningState|
|**--data-center-location**|string|The region this data center should be created in.|data_center_location|dataCenterLocation|
|**--delegated-subnet-id**|string|Resource id of a subnet the nodes in this data center should have their network interfaces connected to. The subnet must be in the same region specified in 'dataCenterLocation' and must be able to route to the subnet specified in the cluster's 'delegatedManagementSubnetId' property. This resource id will be of the form '/subscriptions/<subscription id>/resourceGroups/<resource group>/providers/Microsoft.Network/virtualNetworks/<virtual network>/subnets/<subnet>'.|delegated_subnet_id|delegatedSubnetId|
|**--node-count**|integer|The number of nodes the data center should have. This is the desired number. After it is set, it may take some time for the data center to be scaled to match. To monitor the number of nodes and their status, use the fetchNodeStatus method on the cluster.|node_count|nodeCount|
|**--base64-encoded-cassandra-yaml-fragment**|string|A fragment of a cassandra.yaml configuration file to be included in the cassandra.yaml for all nodes in this data center. The fragment should be Base64 encoded, and only a subset of keys are allowed.|base64_encoded_cassandra_yaml_fragment|base64EncodedCassandraYamlFragment|

#### <a name="CassandraDataCentersDelete">Command `az cosmosdb cassandra-data-center delete`</a>

##### <a name="ExamplesCassandraDataCentersDelete">Example</a>
```
az cosmosdb cassandra-data-center delete --cluster-name "cassandra-prod" --data-center-name "dc1" --resource-group \
"cassandra-prod-rg"
```
##### <a name="ParametersCassandraDataCentersDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|
|**--data-center-name**|string|Data center name in a managed Cassandra cluster.|data_center_name|dataCenterName|

#### <a name="CassandraDataCentersCreateUpdate">Command `az cosmosdb cassandra-data-center create-update`</a>

##### <a name="ExamplesCassandraDataCentersCreateUpdate">Example</a>
```
az cosmosdb cassandra-data-center create-update --base64-encoded-cassandra-yaml-fragment \
"Y29tcGFjdGlvbl90aHJvdWdocHV0X21iX3Blcl9zZWM6IDMyCmNvbXBhY3Rpb25fbGFyZ2VfcGFydGl0aW9uX3dhcm5pbmdfdGhyZXNob2xkX21iOiAxMD\
A=" --data-center-location "West US 2" --delegated-subnet-id "/subscriptions/536e130b-d7d6-4ac7-98a5-de20d69588d2/resou\
rceGroups/customer-vnet-rg/providers/Microsoft.Network/virtualNetworks/customer-vnet/subnets/dc1-subnet" --node-count \
9 --cluster-name "cassandra-prod" --data-center-name "dc1" --resource-group "cassandra-prod-rg"
```
##### <a name="ParametersCassandraDataCentersCreateUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--cluster-name**|string|Managed Cassandra cluster name.|cluster_name|clusterName|
|**--data-center-name**|string|Data center name in a managed Cassandra cluster.|data_center_name|dataCenterName|
|**--provisioning-state**|choice|The status of the resource at the time the operation was called.|provisioning_state|provisioningState|
|**--data-center-location**|string|The region this data center should be created in.|data_center_location|dataCenterLocation|
|**--delegated-subnet-id**|string|Resource id of a subnet the nodes in this data center should have their network interfaces connected to. The subnet must be in the same region specified in 'dataCenterLocation' and must be able to route to the subnet specified in the cluster's 'delegatedManagementSubnetId' property. This resource id will be of the form '/subscriptions/<subscription id>/resourceGroups/<resource group>/providers/Microsoft.Network/virtualNetworks/<virtual network>/subnets/<subnet>'.|delegated_subnet_id|delegatedSubnetId|
|**--node-count**|integer|The number of nodes the data center should have. This is the desired number. After it is set, it may take some time for the data center to be scaled to match. To monitor the number of nodes and their status, use the fetchNodeStatus method on the cluster.|node_count|nodeCount|
|**--base64-encoded-cassandra-yaml-fragment**|string|A fragment of a cassandra.yaml configuration file to be included in the cassandra.yaml for all nodes in this data center. The fragment should be Base64 encoded, and only a subset of keys are allowed.|base64_encoded_cassandra_yaml_fragment|base64EncodedCassandraYamlFragment|

### group `az cosmosdb cassandra-resource`
#### <a name="CassandraResourcesCreateUpdateCassandraKeyspace">Command `az cosmosdb cassandra-resource create-update-cassandra-keyspace`</a>

##### <a name="ExamplesCassandraResourcesCreateUpdateCassandraKeyspace">Example</a>
```
az cosmosdb cassandra-resource create-update-cassandra-keyspace --account-name "ddb1" --location "West US" --id \
"keyspaceName" --keyspace-name "keyspaceName" --resource-group "rg1"
```
##### <a name="ParametersCassandraResourcesCreateUpdateCassandraKeyspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--id**|string|Name of the Cosmos DB Cassandra keyspace|id|id|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|

#### <a name="CassandraResourcesCreateUpdateCassandraTable">Command `az cosmosdb cassandra-resource create-update-cassandra-table`</a>

##### <a name="ExamplesCassandraResourcesCreateUpdateCassandraTable">Example</a>
```
az cosmosdb cassandra-resource create-update-cassandra-table --account-name "ddb1" --location "West US" --cluster-keys \
name="columnA" order-by="Asc" --columns name="columnA" type="Ascii" --partition-keys name="columnA" \
--analytical-storage-ttl 500 --default-ttl 100 --id "tableName" --keyspace-name "keyspaceName" --resource-group "rg1" \
--table-name "tableName"
```
##### <a name="ParametersCassandraResourcesCreateUpdateCassandraTable">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--id**|string|Name of the Cosmos DB Cassandra table|id|id|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|
|**--default-ttl**|integer|Time to live of the Cosmos DB Cassandra table|default_ttl|defaultTtl|
|**--analytical-storage-ttl**|integer|Analytical TTL.|analytical_storage_ttl|analyticalStorageTtl|
|**--columns**|array|List of Cassandra table columns.|columns|columns|
|**--partition-keys**|array|List of partition key.|partition_keys|partitionKeys|
|**--cluster-keys**|array|List of cluster key.|cluster_keys|clusterKeys|

#### <a name="CassandraResourcesCreateUpdateCassandraView">Command `az cosmosdb cassandra-resource create-update-cassandra-view`</a>

##### <a name="ExamplesCassandraResourcesCreateUpdateCassandraView">Example</a>
```
az cosmosdb cassandra-resource create-update-cassandra-view --account-name "ddb1" --resource id="viewname" \
view-definition="SELECT columna, columnb, columnc FROM keyspacename.srctablename WHERE columna IS NOT NULL AND columnc \
IS NOT NULL PRIMARY (columnc, columna)" --keyspace-name "keyspacename" --resource-group "rg1" --view-name "viewname"
```
##### <a name="ParametersCassandraResourcesCreateUpdateCassandraView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--view-name**|string|Cosmos DB view name.|view_name|viewName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--resource**|object|The standard JSON format of a Cassandra view|resource|resource|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|

#### <a name="CassandraResourcesDeleteCassandraKeyspace">Command `az cosmosdb cassandra-resource delete-cassandra-keyspace`</a>

##### <a name="ExamplesCassandraResourcesDeleteCassandraKeyspace">Example</a>
```
az cosmosdb cassandra-resource delete-cassandra-keyspace --account-name "ddb1" --keyspace-name "keyspaceName" \
--resource-group "rg1"
```
##### <a name="ParametersCassandraResourcesDeleteCassandraKeyspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|

#### <a name="CassandraResourcesDeleteCassandraTable">Command `az cosmosdb cassandra-resource delete-cassandra-table`</a>

##### <a name="ExamplesCassandraResourcesDeleteCassandraTable">Example</a>
```
az cosmosdb cassandra-resource delete-cassandra-table --account-name "ddb1" --keyspace-name "keyspaceName" \
--resource-group "rg1" --table-name "tableName"
```
##### <a name="ParametersCassandraResourcesDeleteCassandraTable">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|

#### <a name="CassandraResourcesDeleteCassandraView">Command `az cosmosdb cassandra-resource delete-cassandra-view`</a>

##### <a name="ExamplesCassandraResourcesDeleteCassandraView">Example</a>
```
az cosmosdb cassandra-resource delete-cassandra-view --account-name "ddb1" --keyspace-name "keyspacename" \
--resource-group "rg1" --view-name "viewname"
```
##### <a name="ParametersCassandraResourcesDeleteCassandraView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--view-name**|string|Cosmos DB view name.|view_name|viewName|

#### <a name="CassandraResourcesListCassandraKeyspaces">Command `az cosmosdb cassandra-resource list-cassandra-keyspace`</a>

##### <a name="ExamplesCassandraResourcesListCassandraKeyspaces">Example</a>
```
az cosmosdb cassandra-resource list-cassandra-keyspace --account-name "ddb1" --resource-group "rgName"
```
##### <a name="ParametersCassandraResourcesListCassandraKeyspaces">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="CassandraResourcesListCassandraTables">Command `az cosmosdb cassandra-resource list-cassandra-table`</a>

##### <a name="ExamplesCassandraResourcesListCassandraTables">Example</a>
```
az cosmosdb cassandra-resource list-cassandra-table --account-name "ddb1" --keyspace-name "keyspaceName" \
--resource-group "rgName"
```
##### <a name="ParametersCassandraResourcesListCassandraTables">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|

#### <a name="CassandraResourcesListCassandraViews">Command `az cosmosdb cassandra-resource list-cassandra-view`</a>

##### <a name="ExamplesCassandraResourcesListCassandraViews">Example</a>
```
az cosmosdb cassandra-resource list-cassandra-view --account-name "ddb1" --keyspace-name "keyspacename" \
--resource-group "rgName"
```
##### <a name="ParametersCassandraResourcesListCassandraViews">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|

#### <a name="CassandraResourcesMigrateCassandraKeyspaceToAutoscale">Command `az cosmosdb cassandra-resource migrate-cassandra-keyspace-to-autoscale`</a>

##### <a name="ExamplesCassandraResourcesMigrateCassandraKeyspaceToAutoscale">Example</a>
```
az cosmosdb cassandra-resource migrate-cassandra-keyspace-to-autoscale --account-name "ddb1" --keyspace-name \
"keyspaceName" --resource-group "rg1"
```
##### <a name="ParametersCassandraResourcesMigrateCassandraKeyspaceToAutoscale">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|

#### <a name="CassandraResourcesMigrateCassandraKeyspaceToManualThroughput">Command `az cosmosdb cassandra-resource migrate-cassandra-keyspace-to-manual-throughput`</a>

##### <a name="ExamplesCassandraResourcesMigrateCassandraKeyspaceToManualThroughput">Example</a>
```
az cosmosdb cassandra-resource migrate-cassandra-keyspace-to-manual-throughput --account-name "ddb1" --keyspace-name \
"keyspaceName" --resource-group "rg1"
```
##### <a name="ParametersCassandraResourcesMigrateCassandraKeyspaceToManualThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|

#### <a name="CassandraResourcesMigrateCassandraTableToAutoscale">Command `az cosmosdb cassandra-resource migrate-cassandra-table-to-autoscale`</a>

##### <a name="ExamplesCassandraResourcesMigrateCassandraTableToAutoscale">Example</a>
```
az cosmosdb cassandra-resource migrate-cassandra-table-to-autoscale --account-name "ddb1" --keyspace-name \
"keyspaceName" --resource-group "rg1" --table-name "tableName"
```
##### <a name="ParametersCassandraResourcesMigrateCassandraTableToAutoscale">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|

#### <a name="CassandraResourcesMigrateCassandraTableToManualThroughput">Command `az cosmosdb cassandra-resource migrate-cassandra-table-to-manual-throughput`</a>

##### <a name="ExamplesCassandraResourcesMigrateCassandraTableToManualThroughput">Example</a>
```
az cosmosdb cassandra-resource migrate-cassandra-table-to-manual-throughput --account-name "ddb1" --keyspace-name \
"keyspaceName" --resource-group "rg1" --table-name "tableName"
```
##### <a name="ParametersCassandraResourcesMigrateCassandraTableToManualThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|

#### <a name="CassandraResourcesMigrateCassandraViewToAutoscale">Command `az cosmosdb cassandra-resource migrate-cassandra-view-to-autoscale`</a>

##### <a name="ExamplesCassandraResourcesMigrateCassandraViewToAutoscale">Example</a>
```
az cosmosdb cassandra-resource migrate-cassandra-view-to-autoscale --account-name "ddb1" --keyspace-name \
"keyspacename" --resource-group "rg1" --view-name "viewname"
```
##### <a name="ParametersCassandraResourcesMigrateCassandraViewToAutoscale">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--view-name**|string|Cosmos DB view name.|view_name|viewName|

#### <a name="CassandraResourcesMigrateCassandraViewToManualThroughput">Command `az cosmosdb cassandra-resource migrate-cassandra-view-to-manual-throughput`</a>

##### <a name="ExamplesCassandraResourcesMigrateCassandraViewToManualThroughput">Example</a>
```
az cosmosdb cassandra-resource migrate-cassandra-view-to-manual-throughput --account-name "ddb1" --keyspace-name \
"keyspacename" --resource-group "rg1" --view-name "viewname"
```
##### <a name="ParametersCassandraResourcesMigrateCassandraViewToManualThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--view-name**|string|Cosmos DB view name.|view_name|viewName|

#### <a name="CassandraResourcesGetCassandraKeyspace">Command `az cosmosdb cassandra-resource show-cassandra-keyspace`</a>

##### <a name="ExamplesCassandraResourcesGetCassandraKeyspace">Example</a>
```
az cosmosdb cassandra-resource show-cassandra-keyspace --account-name "ddb1" --keyspace-name "keyspaceName" \
--resource-group "rg1"
```
##### <a name="ParametersCassandraResourcesGetCassandraKeyspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|

#### <a name="CassandraResourcesGetCassandraKeyspaceThroughput">Command `az cosmosdb cassandra-resource show-cassandra-keyspace-throughput`</a>

##### <a name="ExamplesCassandraResourcesGetCassandraKeyspaceThroughput">Example</a>
```
az cosmosdb cassandra-resource show-cassandra-keyspace-throughput --account-name "ddb1" --keyspace-name "keyspaceName" \
--resource-group "rg1"
```
##### <a name="ParametersCassandraResourcesGetCassandraKeyspaceThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|

#### <a name="CassandraResourcesGetCassandraTable">Command `az cosmosdb cassandra-resource show-cassandra-table`</a>

##### <a name="ExamplesCassandraResourcesGetCassandraTable">Example</a>
```
az cosmosdb cassandra-resource show-cassandra-table --account-name "ddb1" --keyspace-name "keyspaceName" \
--resource-group "rg1" --table-name "tableName"
```
##### <a name="ParametersCassandraResourcesGetCassandraTable">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|

#### <a name="CassandraResourcesGetCassandraTableThroughput">Command `az cosmosdb cassandra-resource show-cassandra-table-throughput`</a>

##### <a name="ExamplesCassandraResourcesGetCassandraTableThroughput">Example</a>
```
az cosmosdb cassandra-resource show-cassandra-table-throughput --account-name "ddb1" --keyspace-name "keyspaceName" \
--resource-group "rg1" --table-name "tableName"
```
##### <a name="ParametersCassandraResourcesGetCassandraTableThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|

#### <a name="CassandraResourcesGetCassandraView">Command `az cosmosdb cassandra-resource show-cassandra-view`</a>

##### <a name="ExamplesCassandraResourcesGetCassandraView">Example</a>
```
az cosmosdb cassandra-resource show-cassandra-view --account-name "ddb1" --keyspace-name "keyspacename" \
--resource-group "rg1" --view-name "viewname"
```
##### <a name="ParametersCassandraResourcesGetCassandraView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--view-name**|string|Cosmos DB view name.|view_name|viewName|

#### <a name="CassandraResourcesGetCassandraViewThroughput">Command `az cosmosdb cassandra-resource show-cassandra-view-throughput`</a>

##### <a name="ExamplesCassandraResourcesGetCassandraViewThroughput">Example</a>
```
az cosmosdb cassandra-resource show-cassandra-view-throughput --account-name "ddb1" --keyspace-name "keyspacename" \
--resource-group "rg1" --view-name "viewname"
```
##### <a name="ParametersCassandraResourcesGetCassandraViewThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--view-name**|string|Cosmos DB view name.|view_name|viewName|

#### <a name="CassandraResourcesUpdateCassandraKeyspaceThroughput">Command `az cosmosdb cassandra-resource update-cassandra-keyspace-throughput`</a>

##### <a name="ExamplesCassandraResourcesUpdateCassandraKeyspaceThroughput">Example</a>
```
az cosmosdb cassandra-resource update-cassandra-keyspace-throughput --account-name "ddb1" --keyspace-name \
"keyspaceName" --resource-group "rg1" --location "West US" --throughput 400
```
##### <a name="ParametersCassandraResourcesUpdateCassandraKeyspaceThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--throughput**|integer|Value of the Cosmos DB resource throughput. Either throughput is required or autoscaleSettings is required, but not both.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput container can scale up to.|max_throughput|maxThroughput|
|**--throughput-policy**|object|Represents throughput policy which service must adhere to for auto-upgrade|throughput_policy|throughputPolicy|

#### <a name="CassandraResourcesUpdateCassandraTableThroughput">Command `az cosmosdb cassandra-resource update-cassandra-table-throughput`</a>

##### <a name="ExamplesCassandraResourcesUpdateCassandraTableThroughput">Example</a>
```
az cosmosdb cassandra-resource update-cassandra-table-throughput --account-name "ddb1" --keyspace-name "keyspaceName" \
--resource-group "rg1" --table-name "tableName" --location "West US" --throughput 400
```
##### <a name="ParametersCassandraResourcesUpdateCassandraTableThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--throughput**|integer|Value of the Cosmos DB resource throughput. Either throughput is required or autoscaleSettings is required, but not both.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput container can scale up to.|max_throughput|maxThroughput|
|**--throughput-policy**|object|Represents throughput policy which service must adhere to for auto-upgrade|throughput_policy|throughputPolicy|

#### <a name="CassandraResourcesUpdateCassandraViewThroughput">Command `az cosmosdb cassandra-resource update-cassandra-view-throughput`</a>

##### <a name="ExamplesCassandraResourcesUpdateCassandraViewThroughput">Example</a>
```
az cosmosdb cassandra-resource update-cassandra-view-throughput --account-name "ddb1" --keyspace-name "keyspacename" \
--resource-group "rg1" --throughput 400 --view-name "viewname"
```
##### <a name="ParametersCassandraResourcesUpdateCassandraViewThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--keyspace-name**|string|Cosmos DB keyspace name.|keyspace_name|keyspaceName|
|**--view-name**|string|Cosmos DB view name.|view_name|viewName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--throughput**|integer|Value of the Cosmos DB resource throughput. Either throughput is required or autoscaleSettings is required, but not both.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput container can scale up to.|max_throughput|maxThroughput|
|**--throughput-policy**|object|Represents throughput policy which service must adhere to for auto-upgrade|throughput_policy|throughputPolicy|

### group `az cosmosdb collection`
#### <a name="CollectionListMetrics">Command `az cosmosdb collection list-metric`</a>

##### <a name="ExamplesCollectionListMetrics">Example</a>
```
az cosmosdb collection list-metric --filter "$filter=(name.value eq \'Total Requests\') and timeGrain eq \
duration\'PT5M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \'2017-11-20T00:13:55.2780000Z" \
--account-name "ddb1" --collection-rid "collectionRid" --database-rid "databaseRid" --resource-group "rg1"
```
##### <a name="ParametersCollectionListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--collection-rid**|string|Cosmos DB collection rid.|collection_rid|collectionRid|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

#### <a name="CollectionListMetricDefinitions">Command `az cosmosdb collection list-metric-definition`</a>

##### <a name="ExamplesCollectionListMetricDefinitions">Example</a>
```
az cosmosdb collection list-metric-definition --account-name "ddb1" --collection-rid "collectionRid" --database-rid \
"databaseRid" --resource-group "rg1"
```
##### <a name="ParametersCollectionListMetricDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--collection-rid**|string|Cosmos DB collection rid.|collection_rid|collectionRid|

#### <a name="CollectionListUsages">Command `az cosmosdb collection list-usage`</a>

##### <a name="ExamplesCollectionListUsages">Example</a>
```
az cosmosdb collection list-usage --filter "$filter=name.value eq \'Storage\'" --account-name "ddb1" --collection-rid \
"collectionRid" --database-rid "databaseRid" --resource-group "rg1"
```
##### <a name="ParametersCollectionListUsages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--collection-rid**|string|Cosmos DB collection rid.|collection_rid|collectionRid|
|**--filter**|string|An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).|filter|$filter|

### group `az cosmosdb collection-partition`
#### <a name="CollectionPartitionListMetrics">Command `az cosmosdb collection-partition list-metric`</a>

##### <a name="ExamplesCollectionPartitionListMetrics">Example</a>
```
az cosmosdb collection-partition list-metric --filter "$filter=(name.value eq \'Max RUs Per Second\') and timeGrain eq \
duration\'PT1M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \'2017-11-20T23:58:55.2780000Z" \
--account-name "ddb1" --collection-rid "collectionRid" --database-rid "databaseRid" --resource-group "rg1"
```
##### <a name="ParametersCollectionPartitionListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--collection-rid**|string|Cosmos DB collection rid.|collection_rid|collectionRid|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

#### <a name="CollectionPartitionListUsages">Command `az cosmosdb collection-partition list-usage`</a>

##### <a name="ExamplesCollectionPartitionListUsages">Example</a>
```
az cosmosdb collection-partition list-usage --filter "$filter=name.value eq \'Partition Storage\'" --account-name \
"ddb1" --collection-rid "collectionRid" --database-rid "databaseRid" --resource-group "rg1"
```
##### <a name="ParametersCollectionPartitionListUsages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--collection-rid**|string|Cosmos DB collection rid.|collection_rid|collectionRid|
|**--filter**|string|An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).|filter|$filter|

### group `az cosmosdb collection-partition-region`
#### <a name="CollectionPartitionRegionListMetrics">Command `az cosmosdb collection-partition-region list-metric`</a>

##### <a name="ExamplesCollectionPartitionRegionListMetrics">Example</a>
```
az cosmosdb collection-partition-region list-metric --filter "$filter=(name.value eq \'Max RUs Per Second\') and \
timeGrain eq duration\'PT1M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \
\'2017-11-20T23:58:55.2780000Z" --account-name "ddb1" --collection-rid "collectionRid" --database-rid "databaseRid" \
--region "North Europe" --resource-group "rg1"
```
##### <a name="ParametersCollectionPartitionRegionListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--region**|string|Cosmos DB region, with spaces between words and each word capitalized.|region|region|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--collection-rid**|string|Cosmos DB collection rid.|collection_rid|collectionRid|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

### group `az cosmosdb collection-region`
#### <a name="CollectionRegionListMetrics">Command `az cosmosdb collection-region list-metric`</a>

##### <a name="ExamplesCollectionRegionListMetrics">Example</a>
```
az cosmosdb collection-region list-metric --filter "$filter=(name.value eq \'Total Requests\') and timeGrain eq \
duration\'PT5M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \'2017-11-20T00:13:55.2780000Z" \
--account-name "ddb1" --collection-rid "collectionRid" --database-rid "databaseRid" --region "North Europe" \
--resource-group "rg1"
```
##### <a name="ParametersCollectionRegionListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--region**|string|Cosmos DB region, with spaces between words and each word capitalized.|region|region|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--collection-rid**|string|Cosmos DB collection rid.|collection_rid|collectionRid|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

### group `az cosmosdb database`
#### <a name="DatabaseListMetrics">Command `az cosmosdb database list-metric`</a>

##### <a name="ExamplesDatabaseListMetrics">Example</a>
```
az cosmosdb database list-metric --filter "$filter=(name.value eq \'Total Requests\') and timeGrain eq \
duration\'PT5M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \'2017-11-20T00:13:55.2780000Z" \
--account-name "ddb1" --database-rid "rid" --resource-group "rg1"
```
##### <a name="ParametersDatabaseListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

#### <a name="DatabaseListMetricDefinitions">Command `az cosmosdb database list-metric-definition`</a>

##### <a name="ExamplesDatabaseListMetricDefinitions">Example</a>
```
az cosmosdb database list-metric-definition --account-name "ddb1" --database-rid "databaseRid" --resource-group "rg1"
```
##### <a name="ParametersDatabaseListMetricDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|

#### <a name="DatabaseListUsages">Command `az cosmosdb database list-usage`</a>

##### <a name="ExamplesDatabaseListUsages">Example</a>
```
az cosmosdb database list-usage --filter "$filter=name.value eq \'Storage\'" --account-name "ddb1" --database-rid \
"databaseRid" --resource-group "rg1"
```
##### <a name="ParametersDatabaseListUsages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--filter**|string|An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).|filter|$filter|

### group `az cosmosdb database-account`
#### <a name="DatabaseAccountsListByResourceGroup">Command `az cosmosdb database-account list`</a>

##### <a name="ExamplesDatabaseAccountsListByResourceGroup">Example</a>
```
az cosmosdb database-account list --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|

#### <a name="DatabaseAccountsList">Command `az cosmosdb database-account list`</a>

##### <a name="ExamplesDatabaseAccountsList">Example</a>
```
az cosmosdb database-account list
```
##### <a name="ParametersDatabaseAccountsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

#### <a name="DatabaseAccountsGet">Command `az cosmosdb database-account show`</a>

##### <a name="ExamplesDatabaseAccountsGet">Example</a>
```
az cosmosdb database-account show --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="DatabaseAccountsCreateOrUpdate#Create">Command `az cosmosdb database-account create`</a>

##### <a name="ExamplesDatabaseAccountsCreateOrUpdate#Create">Example</a>
```
az cosmosdb database-account create --account-name "ddb1" --type "SystemAssigned,UserAssigned" \
--user-assigned-identities "{\\"/subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/eu2cgroup/providers/\
Microsoft.ManagedIdentity/userAssignedIdentities/id1\\":{}}" --kind "MongoDB" --location "westus" --schema-type \
"WellDefined" --server-version "3.2" --periodic-mode-backup-policy backup-interval-in-minutes=240 \
backup-retention-interval-in-hours=8 backup-storage-redundancy="Geo" --consistency-policy \
default-consistency-level="BoundedStaleness" max-interval-in-seconds=10 max-staleness-prefix=200 --cors \
allowed-origins="https://test" --default-identity "FirstPartyIdentity" --enable-analytical-storage true \
--enable-free-tier false --ip-rules ip-address-or-range="23.43.230.120" --ip-rules ip-address-or-range="110.12.240.0/12\
" --is-virtual-network-filter-enabled true --key-vault-key-uri "https://myKeyVault.vault.azure.net" --locations \
failover-priority=0 is-zone-redundant=false location-name="southcentralus" --locations failover-priority=1 \
is-zone-redundant=false location-name="eastus" --network-acl-bypass "AzureServices" --network-acl-bypass-resource-ids \
"/subscriptions/subId/resourcegroups/rgName/providers/Microsoft.Synapse/workspaces/workspaceName" \
--public-network-access "Enabled" --virtual-network-rules id="/subscriptions/subId/resourceGroups/rg/providers/Microsof\
t.Network/virtualNetworks/vnet1/subnets/subnet1" ignore-missing-v-net-service-endpoint=false --resource-group "rg1"
az cosmosdb database-account create --account-name "ddb1" --location "westus" --locations failover-priority=0 \
is-zone-redundant=false location-name="southcentralus" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--locations**|array|An array that contains the georeplication locations enabled for the Cosmos DB account.|locations|locations|
|**--kind**|choice|Indicates the type of database account. This can only be set at database account creation.|kind|kind|
|**--consistency-policy**|object|The consistency policy for the Cosmos DB account.|consistency_policy|consistencyPolicy|
|**--ip-rules**|array|List of IpRules.|ip_rules|ipRules|
|**--is-virtual-network-filter-enabled**|boolean|Flag to indicate whether to enable/disable Virtual Network ACL rules.|is_virtual_network_filter_enabled|isVirtualNetworkFilterEnabled|
|**--enable-automatic-failover**|boolean|Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.|enable_automatic_failover|enableAutomaticFailover|
|**--capabilities**|array|List of Cosmos DB capabilities for the account|capabilities|capabilities|
|**--virtual-network-rules**|array|List of Virtual Network ACL rules configured for the Cosmos DB account.|virtual_network_rules|virtualNetworkRules|
|**--enable-multiple-write-locations**|boolean|Enables the account to write in multiple locations|enable_multiple_write_locations|enableMultipleWriteLocations|
|**--enable-cassandra-connector**|boolean|Enables the cassandra connector on the Cosmos DB C* account|enable_cassandra_connector|enableCassandraConnector|
|**--disable-key-based-metadata-write-access**|boolean|Disable write operations on metadata resources (databases, containers, throughput) via account keys|disable_key_based_metadata_write_access|disableKeyBasedMetadataWriteAccess|
|**--key-vault-key-uri**|string|The URI of the key vault|key_vault_key_uri|keyVaultKeyUri|
|**--default-identity**|string|The default identity for accessing key vault used in features like customer managed keys. The default identity needs to be explicitly set by the users. It can be "FirstPartyIdentity", "SystemAssignedIdentity" and more.|default_identity|defaultIdentity|
|**--public-network-access**|choice|Whether requests from Public Network are allowed|public_network_access|publicNetworkAccess|
|**--enable-free-tier**|boolean|Flag to indicate whether Free Tier is enabled.|enable_free_tier|enableFreeTier|
|**--enable-analytical-storage**|boolean|Flag to indicate whether to enable storage analytics.|enable_analytical_storage|enableAnalyticalStorage|
|**--periodic-mode-backup-policy**|object|The object representing periodic mode backup policy.|periodic_mode_backup_policy|PeriodicModeBackupPolicy|
|**--continuous-mode-backup-policy**|object|The object representing continuous mode backup policy.|continuous_mode_backup_policy|ContinuousModeBackupPolicy|
|**--cors**|array|The CORS policy for the Cosmos DB database account.|cors|cors|
|**--network-acl-bypass**|sealed-choice|Indicates what services are allowed to bypass firewall checks.|network_acl_bypass|networkAclBypass|
|**--network-acl-bypass-resource-ids**|array|An array that contains the Resource Ids for Network Acl Bypass for the Cosmos DB account.|network_acl_bypass_resource_ids|networkAclBypassResourceIds|
|**--disable-local-auth**|boolean|Opt-out of local authentication and ensure only MSI and AAD can be used exclusively for authentication.|disable_local_auth|disableLocalAuth|
|**--restore-source**|string|The id of the restorable database account from which the restore has to be initiated. For example: /subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts/{restorableDatabaseAccountName}|restore_source|restoreSource|
|**--restore-timestamp-in-utc**|date-time|Time to which the account has to be restored (ISO-8601 format).|restore_timestamp_in_utc|restoreTimestampInUtc|
|**--databases-to-restore**|array|List of specific databases available for restore.|databases_to_restore|databasesToRestore|
|**--enable-full-text-query**|sealed-choice|Describe the level of detail with which queries are to be logged.|enable_full_text_query|enableFullTextQuery|
|**--schema-type**|choice|Describes the types of schema for analytical storage.|schema_type|schemaType|
|**--server-version**|choice|Describes the ServerVersion of an a MongoDB account.|server_version|serverVersion|

#### <a name="DatabaseAccountsUpdate">Command `az cosmosdb database-account update`</a>

##### <a name="ExamplesDatabaseAccountsUpdate">Example</a>
```
az cosmosdb database-account update --account-name "ddb1" --resource-group "rg1" --type "SystemAssigned,UserAssigned" \
--user-assigned-identities "{\\"/subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/eu2cgroup/providers/\
Microsoft.ManagedIdentity/userAssignedIdentities/id1\\":{}}" --location "westus" --schema-type "WellDefined" \
--periodic-mode-backup-policy backup-interval-in-minutes=240 backup-retention-interval-in-hours=720 \
backup-storage-redundancy="Geo" --consistency-policy default-consistency-level="BoundedStaleness" \
max-interval-in-seconds=10 max-staleness-prefix=200 --default-identity "FirstPartyIdentity" --enable-full-text-query \
"True" --enable-analytical-storage true --enable-free-tier false --ip-rules ip-address-or-range="23.43.230.120" \
--ip-rules ip-address-or-range="110.12.240.0/12" --is-virtual-network-filter-enabled true --network-acl-bypass \
"AzureServices" --network-acl-bypass-resource-ids "/subscriptions/subId/resourcegroups/rgName/providers/Microsoft.Synap\
se/workspaces/workspaceName" --virtual-network-rules id="/subscriptions/subId/resourceGroups/rg/providers/Microsoft.Net\
work/virtualNetworks/vnet1/subnets/subnet1" ignore-missing-v-net-service-endpoint=false --tags dept="finance"
```
##### <a name="ParametersDatabaseAccountsUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--consistency-policy**|object|The consistency policy for the Cosmos DB account.|consistency_policy|consistencyPolicy|
|**--locations**|array|An array that contains the georeplication locations enabled for the Cosmos DB account.|locations|locations|
|**--ip-rules**|array|List of IpRules.|ip_rules|ipRules|
|**--is-virtual-network-filter-enabled**|boolean|Flag to indicate whether to enable/disable Virtual Network ACL rules.|is_virtual_network_filter_enabled|isVirtualNetworkFilterEnabled|
|**--enable-automatic-failover**|boolean|Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.|enable_automatic_failover|enableAutomaticFailover|
|**--capabilities**|array|List of Cosmos DB capabilities for the account|capabilities|capabilities|
|**--virtual-network-rules**|array|List of Virtual Network ACL rules configured for the Cosmos DB account.|virtual_network_rules|virtualNetworkRules|
|**--enable-multiple-write-locations**|boolean|Enables the account to write in multiple locations|enable_multiple_write_locations|enableMultipleWriteLocations|
|**--enable-cassandra-connector**|boolean|Enables the cassandra connector on the Cosmos DB C* account|enable_cassandra_connector|enableCassandraConnector|
|**--disable-key-based-metadata-write-access**|boolean|Disable write operations on metadata resources (databases, containers, throughput) via account keys|disable_key_based_metadata_write_access|disableKeyBasedMetadataWriteAccess|
|**--key-vault-key-uri**|string|The URI of the key vault|key_vault_key_uri|keyVaultKeyUri|
|**--default-identity**|string|The default identity for accessing key vault used in features like customer managed keys. The default identity needs to be explicitly set by the users. It can be "FirstPartyIdentity", "SystemAssignedIdentity" and more.|default_identity|defaultIdentity|
|**--public-network-access**|choice|Whether requests from Public Network are allowed|public_network_access|publicNetworkAccess|
|**--enable-free-tier**|boolean|Flag to indicate whether Free Tier is enabled.|enable_free_tier|enableFreeTier|
|**--enable-analytical-storage**|boolean|Flag to indicate whether to enable storage analytics.|enable_analytical_storage|enableAnalyticalStorage|
|**--periodic-mode-backup-policy**|object|The object representing periodic mode backup policy.|periodic_mode_backup_policy|PeriodicModeBackupPolicy|
|**--continuous-mode-backup-policy**|object|The object representing continuous mode backup policy.|continuous_mode_backup_policy|ContinuousModeBackupPolicy|
|**--cors**|array|The CORS policy for the Cosmos DB database account.|cors|cors|
|**--network-acl-bypass**|sealed-choice|Indicates what services are allowed to bypass firewall checks.|network_acl_bypass|networkAclBypass|
|**--network-acl-bypass-resource-ids**|array|An array that contains the Resource Ids for Network Acl Bypass for the Cosmos DB account.|network_acl_bypass_resource_ids|networkAclBypassResourceIds|
|**--disable-local-auth**|boolean|Opt-out of local authentication and ensure only MSI and AAD can be used exclusively for authentication.|disable_local_auth|disableLocalAuth|
|**--enable-full-text-query**|sealed-choice|Describe the level of detail with which queries are to be logged.|enable_full_text_query|enableFullTextQuery|
|**--schema-type**|choice|Describes the types of schema for analytical storage.|schema_type|schemaType|
|**--server-version**|choice|Describes the ServerVersion of an a MongoDB account.|server_version|serverVersion|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|

#### <a name="DatabaseAccountsDelete">Command `az cosmosdb database-account delete`</a>

##### <a name="ExamplesDatabaseAccountsDelete">Example</a>
```
az cosmosdb database-account delete --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="DatabaseAccountsCheckNameExists">Command `az cosmosdb database-account check-name-exist`</a>

##### <a name="ExamplesDatabaseAccountsCheckNameExists">Example</a>
```
az cosmosdb database-account check-name-exist --account-name "ddb1"
```
##### <a name="ParametersDatabaseAccountsCheckNameExists">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="DatabaseAccountsFailoverPriorityChange">Command `az cosmosdb database-account failover-priority-change`</a>

##### <a name="ExamplesDatabaseAccountsFailoverPriorityChange">Example</a>
```
az cosmosdb database-account failover-priority-change --account-name "ddb1-failover" --failover-policies \
failover-priority=0 location-name="eastus" --failover-policies failover-priority=1 location-name="westus" \
--resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsFailoverPriorityChange">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--failover-policies**|array|List of failover policies.|failover_policies|failoverPolicies|

#### <a name="DatabaseAccountsListConnectionStrings">Command `az cosmosdb database-account list-connection-string`</a>

##### <a name="ExamplesDatabaseAccountsListConnectionStrings">Example</a>
```
az cosmosdb database-account list-connection-string --account-name "ddb1" --resource-group "rg1"
az cosmosdb database-account list-connection-string --account-name "mongo-ddb1" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsListConnectionStrings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="DatabaseAccountsListKeys">Command `az cosmosdb database-account list-key`</a>

##### <a name="ExamplesDatabaseAccountsListKeys">Example</a>
```
az cosmosdb database-account list-key --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsListKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="DatabaseAccountsListMetrics">Command `az cosmosdb database-account list-metric`</a>

##### <a name="ExamplesDatabaseAccountsListMetrics">Example</a>
```
az cosmosdb database-account list-metric --filter "$filter=(name.value eq \'Total Requests\') and timeGrain eq \
duration\'PT5M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \'2017-11-20T00:13:55.2780000Z" \
--account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

#### <a name="DatabaseAccountsListMetricDefinitions">Command `az cosmosdb database-account list-metric-definition`</a>

##### <a name="ExamplesDatabaseAccountsListMetricDefinitions">Example</a>
```
az cosmosdb database-account list-metric-definition --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsListMetricDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="DatabaseAccountsListReadOnlyKeys">Command `az cosmosdb database-account list-read-only-key`</a>

##### <a name="ExamplesDatabaseAccountsListReadOnlyKeys">Example</a>
```
az cosmosdb database-account list-read-only-key --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsListReadOnlyKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="DatabaseAccountsListUsages">Command `az cosmosdb database-account list-usage`</a>

##### <a name="ExamplesDatabaseAccountsListUsages">Example</a>
```
az cosmosdb database-account list-usage --filter "$filter=name.value eq \'Storage\'" --account-name "ddb1" \
--resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsListUsages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--filter**|string|An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).|filter|$filter|

#### <a name="DatabaseAccountsOfflineRegion">Command `az cosmosdb database-account offline-region`</a>

##### <a name="ExamplesDatabaseAccountsOfflineRegion">Example</a>
```
az cosmosdb database-account offline-region --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsOfflineRegion">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--region**|string|Cosmos DB region, with spaces between words and each word capitalized.|region|region|

#### <a name="DatabaseAccountsOnlineRegion">Command `az cosmosdb database-account online-region`</a>

##### <a name="ExamplesDatabaseAccountsOnlineRegion">Example</a>
```
az cosmosdb database-account online-region --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsOnlineRegion">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--region**|string|Cosmos DB region, with spaces between words and each word capitalized.|region|region|

#### <a name="DatabaseAccountsRegenerateKey">Command `az cosmosdb database-account regenerate-key`</a>

##### <a name="ExamplesDatabaseAccountsRegenerateKey">Example</a>
```
az cosmosdb database-account regenerate-key --account-name "ddb1" --key-kind "primary" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsRegenerateKey">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--key-kind**|choice|The access key to regenerate.|key_kind|keyKind|

#### <a name="DatabaseAccountsGetReadOnlyKeys">Command `az cosmosdb database-account show-read-only-key`</a>

##### <a name="ExamplesDatabaseAccountsGetReadOnlyKeys">Example</a>
```
az cosmosdb database-account show-read-only-key --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountsGetReadOnlyKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

### group `az cosmosdb database-account-region`
#### <a name="DatabaseAccountRegionListMetrics">Command `az cosmosdb database-account-region list-metric`</a>

##### <a name="ExamplesDatabaseAccountRegionListMetrics">Example</a>
```
az cosmosdb database-account-region list-metric --filter "$filter=(name.value eq \'Total Requests\') and timeGrain eq \
duration\'PT5M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \'2017-11-20T00:13:55.2780000Z" \
--account-name "ddb1" --region "North Europe" --resource-group "rg1"
```
##### <a name="ParametersDatabaseAccountRegionListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--region**|string|Cosmos DB region, with spaces between words and each word capitalized.|region|region|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

### group `az cosmosdb dts`
#### <a name="DataTransferJobsListByDatabaseAccount">Command `az cosmosdb dts list`</a>

##### <a name="ExamplesDataTransferJobsListByDatabaseAccount">Example</a>
```
az cosmosdb dts list --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersDataTransferJobsListByDatabaseAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="DataTransferJobsGet">Command `az cosmosdb dts show`</a>

##### <a name="ExamplesDataTransferJobsGet">Example</a>
```
az cosmosdb dts show --account-name "ddb1" --job-name "j1" --resource-group "rg1"
```
##### <a name="ParametersDataTransferJobsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--job-name**|string|Name of the Data Transfer Job|job_name|jobName|

#### <a name="DataTransferJobsCreate">Command `az cosmosdb dts create`</a>

##### <a name="ExamplesDataTransferJobsCreate">Example</a>
```
az cosmosdb dts create --account-name "ddb1" --job-create-parameters "{\\"source\\":{\\"component\\":\\"CosmosDBCassand\
ra\\",\\"keyspaceName\\":\\"keyspace\\",\\"tableName\\":\\"table\\"},\\"destination\\":{\\"component\\":\\"AzureBlobSto\
rage\\",\\"containerName\\":\\"blob_container\\",\\"endpointUrl\\":\\"https://blob.windows.net\\"}}" --job-name "j1" \
--resource-group "rg1"
```
##### <a name="ParametersDataTransferJobsCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--job-name**|string|Name of the Data Transfer Job|job_name|jobName|
|**--job-create-parameters**|object||job_create_parameters|jobCreateParameters|

### group `az cosmosdb graph-resource`
#### <a name="GraphResourcesCreateUpdateGraph">Command `az cosmosdb graph-resource create-update-graph`</a>

##### <a name="ExamplesGraphResourcesCreateUpdateGraph">Example</a>
```
az cosmosdb graph-resource create-update-graph --account-name "ddb1" --location "West US" --id "graphName" \
--graph-name "graphName" --resource-group "rg1"
```
##### <a name="ParametersGraphResourcesCreateUpdateGraph">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--graph-name**|string|Cosmos DB graph resource name.|graph_name|graphName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--id**|string|Name of the Cosmos DB Graph|id|id|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|

#### <a name="GraphResourcesDeleteGraphResource">Command `az cosmosdb graph-resource delete-graph-resource`</a>

##### <a name="ExamplesGraphResourcesDeleteGraphResource">Example</a>
```
az cosmosdb graph-resource delete-graph-resource --account-name "ddb1" --graph-name "graphName" --resource-group "rg1"
```
##### <a name="ParametersGraphResourcesDeleteGraphResource">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--graph-name**|string|Cosmos DB graph resource name.|graph_name|graphName|

#### <a name="GraphResourcesListGraphs">Command `az cosmosdb graph-resource list-graph`</a>

##### <a name="ExamplesGraphResourcesListGraphs">Example</a>
```
az cosmosdb graph-resource list-graph --account-name "ddb1" --resource-group "rgName"
```
##### <a name="ParametersGraphResourcesListGraphs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="GraphResourcesGetGraph">Command `az cosmosdb graph-resource show-graph`</a>

##### <a name="ExamplesGraphResourcesGetGraph">Example</a>
```
az cosmosdb graph-resource show-graph --account-name "ddb1" --graph-name "graphName" --resource-group "rg1"
```
##### <a name="ParametersGraphResourcesGetGraph">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--graph-name**|string|Cosmos DB graph resource name.|graph_name|graphName|

### group `az cosmosdb gremlin-resource`
#### <a name="GremlinResourcesCreateUpdateGremlinDatabase">Command `az cosmosdb gremlin-resource create-update-gremlin-database`</a>

##### <a name="ExamplesGremlinResourcesCreateUpdateGremlinDatabase">Example</a>
```
az cosmosdb gremlin-resource create-update-gremlin-database --account-name "ddb1" --location "West US" --id \
"databaseName" --database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesCreateUpdateGremlinDatabase">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--id**|string|Name of the Cosmos DB Gremlin database|id|id|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|

#### <a name="GremlinResourcesCreateUpdateGremlinGraph">Command `az cosmosdb gremlin-resource create-update-gremlin-graph`</a>

##### <a name="ExamplesGremlinResourcesCreateUpdateGremlinGraph">Example</a>
```
az cosmosdb gremlin-resource create-update-gremlin-graph --account-name "ddb1" --create-update-gremlin-graph-parameters\
 "{\\"location\\":\\"West US\\",\\"tags\\":{},\\"resource\\":{\\"conflictResolutionPolicy\\":{\\"conflictResolutionPath\
\\":\\"/path\\",\\"mode\\":\\"LastWriterWins\\"},\\"defaultTtl\\":100,\\"id\\":\\"graphName\\",\\"indexingPolicy\\":{\\\
"automatic\\":true,\\"excludedPaths\\":[],\\"includedPaths\\":[{\\"path\\":\\"/*\\",\\"indexes\\":[{\\"dataType\\":\\"S\
tring\\",\\"kind\\":\\"Range\\",\\"precision\\":-1},{\\"dataType\\":\\"Number\\",\\"kind\\":\\"Range\\",\\"precision\\"\
:-1}]}],\\"indexingMode\\":\\"consistent\\"},\\"partitionKey\\":{\\"kind\\":\\"Hash\\",\\"paths\\":[\\"/AccountNumber\\\
"]},\\"uniqueKeyPolicy\\":{\\"uniqueKeys\\":[{\\"paths\\":[\\"/testPath\\"]}]}},\\"options\\":{}}" --database-name \
"databaseName" --graph-name "graphName" --resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesCreateUpdateGremlinGraph">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--graph-name**|string|Cosmos DB graph name.|graph_name|graphName|
|**--create-update-gremlin-graph-parameters**|object|The parameters to provide for the current Gremlin graph.|create_update_gremlin_graph_parameters|createUpdateGremlinGraphParameters|

#### <a name="GremlinResourcesDeleteGremlinDatabase">Command `az cosmosdb gremlin-resource delete-gremlin-database`</a>

##### <a name="ExamplesGremlinResourcesDeleteGremlinDatabase">Example</a>
```
az cosmosdb gremlin-resource delete-gremlin-database --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesDeleteGremlinDatabase">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="GremlinResourcesDeleteGremlinGraph">Command `az cosmosdb gremlin-resource delete-gremlin-graph`</a>

##### <a name="ExamplesGremlinResourcesDeleteGremlinGraph">Example</a>
```
az cosmosdb gremlin-resource delete-gremlin-graph --account-name "ddb1" --database-name "databaseName" --graph-name \
"graphName" --resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesDeleteGremlinGraph">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--graph-name**|string|Cosmos DB graph name.|graph_name|graphName|

#### <a name="GremlinResourcesListGremlinDatabases">Command `az cosmosdb gremlin-resource list-gremlin-database`</a>

##### <a name="ExamplesGremlinResourcesListGremlinDatabases">Example</a>
```
az cosmosdb gremlin-resource list-gremlin-database --account-name "ddb1" --resource-group "rgName"
```
##### <a name="ParametersGremlinResourcesListGremlinDatabases">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="GremlinResourcesListGremlinGraphs">Command `az cosmosdb gremlin-resource list-gremlin-graph`</a>

##### <a name="ExamplesGremlinResourcesListGremlinGraphs">Example</a>
```
az cosmosdb gremlin-resource list-gremlin-graph --account-name "ddb1" --database-name "databaseName" --resource-group \
"rgName"
```
##### <a name="ParametersGremlinResourcesListGremlinGraphs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="GremlinResourcesMigrateGremlinDatabaseToAutoscale">Command `az cosmosdb gremlin-resource migrate-gremlin-database-to-autoscale`</a>

##### <a name="ExamplesGremlinResourcesMigrateGremlinDatabaseToAutoscale">Example</a>
```
az cosmosdb gremlin-resource migrate-gremlin-database-to-autoscale --account-name "ddb1" --database-name \
"databaseName" --resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesMigrateGremlinDatabaseToAutoscale">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="GremlinResourcesMigrateGremlinDatabaseToManualThroughput">Command `az cosmosdb gremlin-resource migrate-gremlin-database-to-manual-throughput`</a>

##### <a name="ExamplesGremlinResourcesMigrateGremlinDatabaseToManualThroughput">Example</a>
```
az cosmosdb gremlin-resource migrate-gremlin-database-to-manual-throughput --account-name "ddb1" --database-name \
"databaseName" --resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesMigrateGremlinDatabaseToManualThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="GremlinResourcesMigrateGremlinGraphToAutoscale">Command `az cosmosdb gremlin-resource migrate-gremlin-graph-to-autoscale`</a>

##### <a name="ExamplesGremlinResourcesMigrateGremlinGraphToAutoscale">Example</a>
```
az cosmosdb gremlin-resource migrate-gremlin-graph-to-autoscale --account-name "ddb1" --database-name "databaseName" \
--graph-name "graphName" --resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesMigrateGremlinGraphToAutoscale">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--graph-name**|string|Cosmos DB graph name.|graph_name|graphName|

#### <a name="GremlinResourcesMigrateGremlinGraphToManualThroughput">Command `az cosmosdb gremlin-resource migrate-gremlin-graph-to-manual-throughput`</a>

##### <a name="ExamplesGremlinResourcesMigrateGremlinGraphToManualThroughput">Example</a>
```
az cosmosdb gremlin-resource migrate-gremlin-graph-to-manual-throughput --account-name "ddb1" --database-name \
"databaseName" --graph-name "graphName" --resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesMigrateGremlinGraphToManualThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--graph-name**|string|Cosmos DB graph name.|graph_name|graphName|

#### <a name="GremlinResourcesGetGremlinDatabase">Command `az cosmosdb gremlin-resource show-gremlin-database`</a>

##### <a name="ExamplesGremlinResourcesGetGremlinDatabase">Example</a>
```
az cosmosdb gremlin-resource show-gremlin-database --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesGetGremlinDatabase">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="GremlinResourcesGetGremlinDatabaseThroughput">Command `az cosmosdb gremlin-resource show-gremlin-database-throughput`</a>

##### <a name="ExamplesGremlinResourcesGetGremlinDatabaseThroughput">Example</a>
```
az cosmosdb gremlin-resource show-gremlin-database-throughput --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesGetGremlinDatabaseThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="GremlinResourcesGetGremlinGraph">Command `az cosmosdb gremlin-resource show-gremlin-graph`</a>

##### <a name="ExamplesGremlinResourcesGetGremlinGraph">Example</a>
```
az cosmosdb gremlin-resource show-gremlin-graph --account-name "ddb1" --database-name "databaseName" --graph-name \
"graphName" --resource-group "rgName"
```
##### <a name="ParametersGremlinResourcesGetGremlinGraph">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--graph-name**|string|Cosmos DB graph name.|graph_name|graphName|

#### <a name="GremlinResourcesGetGremlinGraphThroughput">Command `az cosmosdb gremlin-resource show-gremlin-graph-throughput`</a>

##### <a name="ExamplesGremlinResourcesGetGremlinGraphThroughput">Example</a>
```
az cosmosdb gremlin-resource show-gremlin-graph-throughput --account-name "ddb1" --database-name "databaseName" \
--graph-name "graphName" --resource-group "rg1"
```
##### <a name="ParametersGremlinResourcesGetGremlinGraphThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--graph-name**|string|Cosmos DB graph name.|graph_name|graphName|

#### <a name="GremlinResourcesUpdateGremlinDatabaseThroughput">Command `az cosmosdb gremlin-resource update-gremlin-database-throughput`</a>

##### <a name="ExamplesGremlinResourcesUpdateGremlinDatabaseThroughput">Example</a>
```
az cosmosdb gremlin-resource update-gremlin-database-throughput --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1" --location "West US" --throughput 400
```
##### <a name="ParametersGremlinResourcesUpdateGremlinDatabaseThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--throughput**|integer|Value of the Cosmos DB resource throughput. Either throughput is required or autoscaleSettings is required, but not both.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput container can scale up to.|max_throughput|maxThroughput|
|**--throughput-policy**|object|Represents throughput policy which service must adhere to for auto-upgrade|throughput_policy|throughputPolicy|

#### <a name="GremlinResourcesUpdateGremlinGraphThroughput">Command `az cosmosdb gremlin-resource update-gremlin-graph-throughput`</a>

##### <a name="ExamplesGremlinResourcesUpdateGremlinGraphThroughput">Example</a>
```
az cosmosdb gremlin-resource update-gremlin-graph-throughput --account-name "ddb1" --database-name "databaseName" \
--graph-name "graphName" --resource-group "rg1" --location "West US" --throughput 400
```
##### <a name="ParametersGremlinResourcesUpdateGremlinGraphThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--graph-name**|string|Cosmos DB graph name.|graph_name|graphName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--throughput**|integer|Value of the Cosmos DB resource throughput. Either throughput is required or autoscaleSettings is required, but not both.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput container can scale up to.|max_throughput|maxThroughput|
|**--throughput-policy**|object|Represents throughput policy which service must adhere to for auto-upgrade|throughput_policy|throughputPolicy|

### group `az cosmosdb mongo-db-resource`
#### <a name="MongoDBResourcesCreateUpdateMongoDBCollection">Command `az cosmosdb mongo-db-resource create-update-mongo-db-collection`</a>

##### <a name="ExamplesMongoDBResourcesCreateUpdateMongoDBCollection">Example</a>
```
az cosmosdb mongo-db-resource create-update-mongo-db-collection --account-name "ddb1" --collection-name \
"collectionName" --location "West US" --analytical-storage-ttl 500 --id "collectionName" --indexes \
"[{\\"key\\":{\\"keys\\":[\\"_ts\\"]},\\"options\\":{\\"expireAfterSeconds\\":100,\\"unique\\":true}},{\\"key\\":{\\"ke\
ys\\":[\\"_id\\"]}}]" --shard-key testKey="Hash" --database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesCreateUpdateMongoDBCollection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--collection-name**|string|Cosmos DB collection name.|collection_name|collectionName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--id**|string|Name of the Cosmos DB MongoDB collection|id|id|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|
|**--shard-key**|dictionary|A key-value pair of shard keys to be applied for the request.|shard_key|shardKey|
|**--indexes**|array|List of index keys|indexes|indexes|
|**--analytical-storage-ttl**|integer|Analytical TTL.|analytical_storage_ttl|analyticalStorageTtl|

#### <a name="MongoDBResourcesCreateUpdateMongoDBDatabase">Command `az cosmosdb mongo-db-resource create-update-mongo-db-database`</a>

##### <a name="ExamplesMongoDBResourcesCreateUpdateMongoDBDatabase">Example</a>
```
az cosmosdb mongo-db-resource create-update-mongo-db-database --account-name "ddb1" --location "West US" --id \
"databaseName" --database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesCreateUpdateMongoDBDatabase">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--id**|string|Name of the Cosmos DB MongoDB database|id|id|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|

#### <a name="MongoDBResourcesDeleteMongoDBCollection">Command `az cosmosdb mongo-db-resource delete-mongo-db-collection`</a>

##### <a name="ExamplesMongoDBResourcesDeleteMongoDBCollection">Example</a>
```
az cosmosdb mongo-db-resource delete-mongo-db-collection --account-name "ddb1" --collection-name "collectionName" \
--database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesDeleteMongoDBCollection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--collection-name**|string|Cosmos DB collection name.|collection_name|collectionName|

#### <a name="MongoDBResourcesDeleteMongoDBDatabase">Command `az cosmosdb mongo-db-resource delete-mongo-db-database`</a>

##### <a name="ExamplesMongoDBResourcesDeleteMongoDBDatabase">Example</a>
```
az cosmosdb mongo-db-resource delete-mongo-db-database --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesDeleteMongoDBDatabase">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="MongoDBResourcesListMongoDBCollections">Command `az cosmosdb mongo-db-resource list-mongo-db-collection`</a>

##### <a name="ExamplesMongoDBResourcesListMongoDBCollections">Example</a>
```
az cosmosdb mongo-db-resource list-mongo-db-collection --account-name "ddb1" --database-name "databaseName" \
--resource-group "rgName"
```
##### <a name="ParametersMongoDBResourcesListMongoDBCollections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="MongoDBResourcesListMongoDBDatabases">Command `az cosmosdb mongo-db-resource list-mongo-db-database`</a>

##### <a name="ExamplesMongoDBResourcesListMongoDBDatabases">Example</a>
```
az cosmosdb mongo-db-resource list-mongo-db-database --account-name "ddb1" --resource-group "rgName"
```
##### <a name="ParametersMongoDBResourcesListMongoDBDatabases">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="MongoDBResourcesMigrateMongoDBCollectionToAutoscale">Command `az cosmosdb mongo-db-resource migrate-mongo-db-collection-to-autoscale`</a>

##### <a name="ExamplesMongoDBResourcesMigrateMongoDBCollectionToAutoscale">Example</a>
```
az cosmosdb mongo-db-resource migrate-mongo-db-collection-to-autoscale --account-name "ddb1" --collection-name \
"collectionName" --database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesMigrateMongoDBCollectionToAutoscale">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--collection-name**|string|Cosmos DB collection name.|collection_name|collectionName|

#### <a name="MongoDBResourcesMigrateMongoDBCollectionToManualThroughput">Command `az cosmosdb mongo-db-resource migrate-mongo-db-collection-to-manual-throughput`</a>

##### <a name="ExamplesMongoDBResourcesMigrateMongoDBCollectionToManualThroughput">Example</a>
```
az cosmosdb mongo-db-resource migrate-mongo-db-collection-to-manual-throughput --account-name "ddb1" --collection-name \
"collectionName" --database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesMigrateMongoDBCollectionToManualThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--collection-name**|string|Cosmos DB collection name.|collection_name|collectionName|

#### <a name="MongoDBResourcesMigrateMongoDBDatabaseToAutoscale">Command `az cosmosdb mongo-db-resource migrate-mongo-db-database-to-autoscale`</a>

##### <a name="ExamplesMongoDBResourcesMigrateMongoDBDatabaseToAutoscale">Example</a>
```
az cosmosdb mongo-db-resource migrate-mongo-db-database-to-autoscale --account-name "ddb1" --database-name \
"databaseName" --resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesMigrateMongoDBDatabaseToAutoscale">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="MongoDBResourcesMigrateMongoDBDatabaseToManualThroughput">Command `az cosmosdb mongo-db-resource migrate-mongo-db-database-to-manual-throughput`</a>

##### <a name="ExamplesMongoDBResourcesMigrateMongoDBDatabaseToManualThroughput">Example</a>
```
az cosmosdb mongo-db-resource migrate-mongo-db-database-to-manual-throughput --account-name "ddb1" --database-name \
"databaseName" --resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesMigrateMongoDBDatabaseToManualThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="MongoDBResourcesGetMongoDBCollection">Command `az cosmosdb mongo-db-resource show-mongo-db-collection`</a>

##### <a name="ExamplesMongoDBResourcesGetMongoDBCollection">Example</a>
```
az cosmosdb mongo-db-resource show-mongo-db-collection --account-name "ddb1" --collection-name "collectionName" \
--database-name "databaseName" --resource-group "rgName"
```
##### <a name="ParametersMongoDBResourcesGetMongoDBCollection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--collection-name**|string|Cosmos DB collection name.|collection_name|collectionName|

#### <a name="MongoDBResourcesGetMongoDBCollectionThroughput">Command `az cosmosdb mongo-db-resource show-mongo-db-collection-throughput`</a>

##### <a name="ExamplesMongoDBResourcesGetMongoDBCollectionThroughput">Example</a>
```
az cosmosdb mongo-db-resource show-mongo-db-collection-throughput --account-name "ddb1" --collection-name \
"collectionName" --database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesGetMongoDBCollectionThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--collection-name**|string|Cosmos DB collection name.|collection_name|collectionName|

#### <a name="MongoDBResourcesGetMongoDBDatabase">Command `az cosmosdb mongo-db-resource show-mongo-db-database`</a>

##### <a name="ExamplesMongoDBResourcesGetMongoDBDatabase">Example</a>
```
az cosmosdb mongo-db-resource show-mongo-db-database --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesGetMongoDBDatabase">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="MongoDBResourcesGetMongoDBDatabaseThroughput">Command `az cosmosdb mongo-db-resource show-mongo-db-database-throughput`</a>

##### <a name="ExamplesMongoDBResourcesGetMongoDBDatabaseThroughput">Example</a>
```
az cosmosdb mongo-db-resource show-mongo-db-database-throughput --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1"
```
##### <a name="ParametersMongoDBResourcesGetMongoDBDatabaseThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="MongoDBResourcesUpdateMongoDBCollectionThroughput">Command `az cosmosdb mongo-db-resource update-mongo-db-collection-throughput`</a>

##### <a name="ExamplesMongoDBResourcesUpdateMongoDBCollectionThroughput">Example</a>
```
az cosmosdb mongo-db-resource update-mongo-db-collection-throughput --account-name "ddb1" --collection-name \
"collectionName" --database-name "databaseName" --resource-group "rg1" --location "West US" --throughput 400
```
##### <a name="ParametersMongoDBResourcesUpdateMongoDBCollectionThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--collection-name**|string|Cosmos DB collection name.|collection_name|collectionName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--throughput**|integer|Value of the Cosmos DB resource throughput. Either throughput is required or autoscaleSettings is required, but not both.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput container can scale up to.|max_throughput|maxThroughput|
|**--throughput-policy**|object|Represents throughput policy which service must adhere to for auto-upgrade|throughput_policy|throughputPolicy|

#### <a name="MongoDBResourcesUpdateMongoDBDatabaseThroughput">Command `az cosmosdb mongo-db-resource update-mongo-db-database-throughput`</a>

##### <a name="ExamplesMongoDBResourcesUpdateMongoDBDatabaseThroughput">Example</a>
```
az cosmosdb mongo-db-resource update-mongo-db-database-throughput --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1" --location "West US" --throughput 400
```
##### <a name="ParametersMongoDBResourcesUpdateMongoDBDatabaseThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--throughput**|integer|Value of the Cosmos DB resource throughput. Either throughput is required or autoscaleSettings is required, but not both.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput container can scale up to.|max_throughput|maxThroughput|
|**--throughput-policy**|object|Represents throughput policy which service must adhere to for auto-upgrade|throughput_policy|throughputPolicy|

### group `az cosmosdb notebook-workspace`
#### <a name="NotebookWorkspacesListByDatabaseAccount">Command `az cosmosdb notebook-workspace list`</a>

##### <a name="ExamplesNotebookWorkspacesListByDatabaseAccount">Example</a>
```
az cosmosdb notebook-workspace list --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersNotebookWorkspacesListByDatabaseAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="NotebookWorkspacesGet">Command `az cosmosdb notebook-workspace show`</a>

##### <a name="ExamplesNotebookWorkspacesGet">Example</a>
```
az cosmosdb notebook-workspace show --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersNotebookWorkspacesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="NotebookWorkspacesCreateOrUpdate#Create">Command `az cosmosdb notebook-workspace create`</a>

##### <a name="ExamplesNotebookWorkspacesCreateOrUpdate#Create">Example</a>
```
az cosmosdb notebook-workspace create --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersNotebookWorkspacesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="NotebookWorkspacesCreateOrUpdate#Update">Command `az cosmosdb notebook-workspace update`</a>


##### <a name="ParametersNotebookWorkspacesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="NotebookWorkspacesDelete">Command `az cosmosdb notebook-workspace delete`</a>

##### <a name="ExamplesNotebookWorkspacesDelete">Example</a>
```
az cosmosdb notebook-workspace delete --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersNotebookWorkspacesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="NotebookWorkspacesListConnectionInfo">Command `az cosmosdb notebook-workspace list-connection-info`</a>

##### <a name="ExamplesNotebookWorkspacesListConnectionInfo">Example</a>
```
az cosmosdb notebook-workspace list-connection-info --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersNotebookWorkspacesListConnectionInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="NotebookWorkspacesRegenerateAuthToken">Command `az cosmosdb notebook-workspace regenerate-auth-token`</a>

##### <a name="ExamplesNotebookWorkspacesRegenerateAuthToken">Example</a>
```
az cosmosdb notebook-workspace regenerate-auth-token --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersNotebookWorkspacesRegenerateAuthToken">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="NotebookWorkspacesStart">Command `az cosmosdb notebook-workspace start`</a>

##### <a name="ExamplesNotebookWorkspacesStart">Example</a>
```
az cosmosdb notebook-workspace start --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersNotebookWorkspacesStart">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

### group `az cosmosdb partition-key-range-id`
#### <a name="PartitionKeyRangeIdListMetrics">Command `az cosmosdb partition-key-range-id list-metric`</a>

##### <a name="ExamplesPartitionKeyRangeIdListMetrics">Example</a>
```
az cosmosdb partition-key-range-id list-metric --filter "$filter=(name.value eq \'Max RUs Per Second\') and timeGrain \
eq duration\'PT1M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \'2017-11-20T23:58:55.2780000Z" \
--account-name "ddb1" --collection-rid "collectionRid" --database-rid "databaseRid" --partition-key-range-id "0" \
--resource-group "rg1"
```
##### <a name="ParametersPartitionKeyRangeIdListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--collection-rid**|string|Cosmos DB collection rid.|collection_rid|collectionRid|
|**--partition-key-range-id**|string|Partition Key Range Id for which to get data.|partition_key_range_id|partitionKeyRangeId|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

### group `az cosmosdb partition-key-range-id-region`
#### <a name="PartitionKeyRangeIdRegionListMetrics">Command `az cosmosdb partition-key-range-id-region list-metric`</a>

##### <a name="ExamplesPartitionKeyRangeIdRegionListMetrics">Example</a>
```
az cosmosdb partition-key-range-id-region list-metric --filter "$filter=(name.value eq \'Max RUs Per Second\') and \
timeGrain eq duration\'PT1M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \
\'2017-11-20T23:58:55.2780000Z" --account-name "ddb1" --collection-rid "collectionRid" --database-rid "databaseRid" \
--partition-key-range-id "0" --region "West US" --resource-group "rg1"
```
##### <a name="ParametersPartitionKeyRangeIdRegionListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--region**|string|Cosmos DB region, with spaces between words and each word capitalized.|region|region|
|**--database-rid**|string|Cosmos DB database rid.|database_rid|databaseRid|
|**--collection-rid**|string|Cosmos DB collection rid.|collection_rid|collectionRid|
|**--partition-key-range-id**|string|Partition Key Range Id for which to get data.|partition_key_range_id|partitionKeyRangeId|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

### group `az cosmosdb percentile`
#### <a name="PercentileListMetrics">Command `az cosmosdb percentile list-metric`</a>

##### <a name="ExamplesPercentileListMetrics">Example</a>
```
az cosmosdb percentile list-metric --filter "$filter=(name.value eq \'Probabilistic Bounded Staleness\') and timeGrain \
eq duration\'PT5M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \'2017-11-20T00:13:55.2780000Z" \
--account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersPercentileListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

### group `az cosmosdb percentile-source-target`
#### <a name="PercentileSourceTargetListMetrics">Command `az cosmosdb percentile-source-target list-metric`</a>

##### <a name="ExamplesPercentileSourceTargetListMetrics">Example</a>
```
az cosmosdb percentile-source-target list-metric --filter "$filter=(name.value eq \'Probabilistic Bounded Staleness\') \
and timeGrain eq duration\'PT5M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \
\'2017-11-20T00:13:55.2780000Z" --account-name "ddb1" --resource-group "rg1" --source-region "West Central US" \
--target-region "East US"
```
##### <a name="ParametersPercentileSourceTargetListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--source-region**|string|Source region from which data is written. Cosmos DB region, with spaces between words and each word capitalized.|source_region|sourceRegion|
|**--target-region**|string|Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized.|target_region|targetRegion|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

### group `az cosmosdb percentile-target`
#### <a name="PercentileTargetListMetrics">Command `az cosmosdb percentile-target list-metric`</a>

##### <a name="ExamplesPercentileTargetListMetrics">Example</a>
```
az cosmosdb percentile-target list-metric --filter "$filter=(name.value eq \'Probabilistic Bounded Staleness\') and \
timeGrain eq duration\'PT5M\' and startTime eq \'2017-11-19T23:53:55.2780000Z\' and endTime eq \
\'2017-11-20T00:13:55.2780000Z" --account-name "ddb1" --resource-group "rg1" --target-region "East US"
```
##### <a name="ParametersPercentileTargetListMetrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--target-region**|string|Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized.|target_region|targetRegion|
|**--filter**|string|An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.|filter|$filter|

### group `az cosmosdb private-endpoint-connection`
#### <a name="PrivateEndpointConnectionsListByDatabaseAccount">Command `az cosmosdb private-endpoint-connection list`</a>

##### <a name="ExamplesPrivateEndpointConnectionsListByDatabaseAccount">Example</a>
```
az cosmosdb private-endpoint-connection list --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersPrivateEndpointConnectionsListByDatabaseAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="PrivateEndpointConnectionsGet">Command `az cosmosdb private-endpoint-connection show`</a>

##### <a name="ExamplesPrivateEndpointConnectionsGet">Example</a>
```
az cosmosdb private-endpoint-connection show --account-name "ddb1" --name "privateEndpointConnectionName" \
--resource-group "rg1"
```
##### <a name="ParametersPrivateEndpointConnectionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection.|private_endpoint_connection_name|privateEndpointConnectionName|

#### <a name="PrivateEndpointConnectionsCreateOrUpdate#Create">Command `az cosmosdb private-endpoint-connection create`</a>

##### <a name="ExamplesPrivateEndpointConnectionsCreateOrUpdate#Create">Example</a>
```
az cosmosdb private-endpoint-connection create --account-name "ddb1" --private-link-service-connection-state \
description="Approved by johndoe@contoso.com" status="Approved" --name "privateEndpointConnectionName" \
--resource-group "rg1"
```
##### <a name="ParametersPrivateEndpointConnectionsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection.|private_endpoint_connection_name|privateEndpointConnectionName|
|**--private-link-service-connection-state**|object|Connection State of the Private Endpoint Connection.|private_link_service_connection_state|privateLinkServiceConnectionState|
|**--group-id**|string|Group id of the private endpoint.|group_id|groupId|
|**--provisioning-state**|string|Provisioning state of the private endpoint.|provisioning_state|provisioningState|
|**--id**|string|Resource id of the private endpoint.|id|id|

#### <a name="PrivateEndpointConnectionsCreateOrUpdate#Update">Command `az cosmosdb private-endpoint-connection update`</a>


##### <a name="ParametersPrivateEndpointConnectionsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection.|private_endpoint_connection_name|privateEndpointConnectionName|
|**--private-link-service-connection-state**|object|Connection State of the Private Endpoint Connection.|private_link_service_connection_state|privateLinkServiceConnectionState|
|**--group-id**|string|Group id of the private endpoint.|group_id|groupId|
|**--provisioning-state**|string|Provisioning state of the private endpoint.|provisioning_state|provisioningState|
|**--id**|string|Resource id of the private endpoint.|id|id|

#### <a name="PrivateEndpointConnectionsDelete">Command `az cosmosdb private-endpoint-connection delete`</a>

##### <a name="ExamplesPrivateEndpointConnectionsDelete">Example</a>
```
az cosmosdb private-endpoint-connection delete --account-name "ddb1" --name "privateEndpointConnectionName" \
--resource-group "rg1"
```
##### <a name="ParametersPrivateEndpointConnectionsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection.|private_endpoint_connection_name|privateEndpointConnectionName|

### group `az cosmosdb private-link-resource`
#### <a name="PrivateLinkResourcesListByDatabaseAccount">Command `az cosmosdb private-link-resource list`</a>

##### <a name="ExamplesPrivateLinkResourcesListByDatabaseAccount">Example</a>
```
az cosmosdb private-link-resource list --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersPrivateLinkResourcesListByDatabaseAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="PrivateLinkResourcesGet">Command `az cosmosdb private-link-resource show`</a>

##### <a name="ExamplesPrivateLinkResourcesGet">Example</a>
```
az cosmosdb private-link-resource show --account-name "ddb1" --group-name "sql" --resource-group "rg1"
```
##### <a name="ParametersPrivateLinkResourcesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--group-name**|string|The name of the private link resource.|group_name|groupName|

### group `az cosmosdb restorable-database-account`
#### <a name="RestorableDatabaseAccountsListByLocation">Command `az cosmosdb restorable-database-account list`</a>

##### <a name="ExamplesRestorableDatabaseAccountsListByLocation">Example</a>
```
az cosmosdb restorable-database-account list --location "West US"
```
##### <a name="ParametersRestorableDatabaseAccountsListByLocation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Cosmos DB region, with spaces between words and each word capitalized.|location|location|

#### <a name="RestorableDatabaseAccountsList">Command `az cosmosdb restorable-database-account list`</a>

##### <a name="ExamplesRestorableDatabaseAccountsList">Example</a>
```
az cosmosdb restorable-database-account list
```
##### <a name="ParametersRestorableDatabaseAccountsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

#### <a name="RestorableDatabaseAccountsGetByLocation">Command `az cosmosdb restorable-database-account show`</a>

##### <a name="ExamplesRestorableDatabaseAccountsGetByLocation">Example</a>
```
az cosmosdb restorable-database-account show --instance-id "d9b26648-2f53-4541-b3d8-3044f4f9810d" --location "West US"
```
##### <a name="ParametersRestorableDatabaseAccountsGetByLocation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Cosmos DB region, with spaces between words and each word capitalized.|location|location|
|**--instance-id**|string|The instanceId GUID of a restorable database account.|instance_id|instanceId|

### group `az cosmosdb restorable-mongodb-collection`
#### <a name="RestorableMongodbCollectionsList">Command `az cosmosdb restorable-mongodb-collection list`</a>

##### <a name="ExamplesRestorableMongodbCollectionsList">Example</a>
```
az cosmosdb restorable-mongodb-collection list --instance-id "98a570f2-63db-4117-91f0-366327b7b353" --location \
"WestUS" --restorable-mongodb-database-rid "PD5DALigDgw="
```
##### <a name="ParametersRestorableMongodbCollectionsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Cosmos DB region, with spaces between words and each word capitalized.|location|location|
|**--instance-id**|string|The instanceId GUID of a restorable database account.|instance_id|instanceId|
|**--restorable-mongodb-database-rid**|string|The resource ID of the MongoDB database.|restorable_mongodb_database_rid|restorableMongodbDatabaseRid|

### group `az cosmosdb restorable-mongodb-database`
#### <a name="RestorableMongodbDatabasesList">Command `az cosmosdb restorable-mongodb-database list`</a>

##### <a name="ExamplesRestorableMongodbDatabasesList">Example</a>
```
az cosmosdb restorable-mongodb-database list --instance-id "d9b26648-2f53-4541-b3d8-3044f4f9810d" --location "WestUS"
```
##### <a name="ParametersRestorableMongodbDatabasesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Cosmos DB region, with spaces between words and each word capitalized.|location|location|
|**--instance-id**|string|The instanceId GUID of a restorable database account.|instance_id|instanceId|

### group `az cosmosdb restorable-mongodb-resource`
#### <a name="RestorableMongodbResourcesList">Command `az cosmosdb restorable-mongodb-resource list`</a>

##### <a name="ExamplesRestorableMongodbResourcesList">Example</a>
```
az cosmosdb restorable-mongodb-resource list --instance-id "d9b26648-2f53-4541-b3d8-3044f4f9810d" --location "WestUS" \
--restore-location "WestUS" --restore-timestamp-in-utc "10/13/2020 4:56"
```
##### <a name="ParametersRestorableMongodbResourcesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Cosmos DB region, with spaces between words and each word capitalized.|location|location|
|**--instance-id**|string|The instanceId GUID of a restorable database account.|instance_id|instanceId|
|**--restore-location**|string|The location where the restorable resources are located.|restore_location|restoreLocation|
|**--restore-timestamp-in-utc**|string|The timestamp when the restorable resources existed.|restore_timestamp_in_utc|restoreTimestampInUtc|

### group `az cosmosdb restorable-sql-container`
#### <a name="RestorableSqlContainersList">Command `az cosmosdb restorable-sql-container list`</a>

##### <a name="ExamplesRestorableSqlContainersList">Example</a>
```
az cosmosdb restorable-sql-container list --instance-id "98a570f2-63db-4117-91f0-366327b7b353" --location "WestUS" \
--restorable-sql-database-rid "3fu-hg=="
```
##### <a name="ParametersRestorableSqlContainersList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Cosmos DB region, with spaces between words and each word capitalized.|location|location|
|**--instance-id**|string|The instanceId GUID of a restorable database account.|instance_id|instanceId|
|**--restorable-sql-database-rid**|string|The resource ID of the SQL database.|restorable_sql_database_rid|restorableSqlDatabaseRid|
|**--start-time**|string|The snapshot create timestamp after which snapshots need to be listed.|start_time|startTime|
|**--end-time**|string|The snapshot create timestamp before which snapshots need to be listed.|end_time|endTime|

### group `az cosmosdb restorable-sql-database`
#### <a name="RestorableSqlDatabasesList">Command `az cosmosdb restorable-sql-database list`</a>

##### <a name="ExamplesRestorableSqlDatabasesList">Example</a>
```
az cosmosdb restorable-sql-database list --instance-id "d9b26648-2f53-4541-b3d8-3044f4f9810d" --location "WestUS"
```
##### <a name="ParametersRestorableSqlDatabasesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Cosmos DB region, with spaces between words and each word capitalized.|location|location|
|**--instance-id**|string|The instanceId GUID of a restorable database account.|instance_id|instanceId|

### group `az cosmosdb restorable-sql-resource`
#### <a name="RestorableSqlResourcesList">Command `az cosmosdb restorable-sql-resource list`</a>

##### <a name="ExamplesRestorableSqlResourcesList">Example</a>
```
az cosmosdb restorable-sql-resource list --instance-id "d9b26648-2f53-4541-b3d8-3044f4f9810d" --location "WestUS" \
--restore-location "WestUS" --restore-timestamp-in-utc "10/13/2020 4:56"
```
##### <a name="ParametersRestorableSqlResourcesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Cosmos DB region, with spaces between words and each word capitalized.|location|location|
|**--instance-id**|string|The instanceId GUID of a restorable database account.|instance_id|instanceId|
|**--restore-location**|string|The location where the restorable resources are located.|restore_location|restoreLocation|
|**--restore-timestamp-in-utc**|string|The timestamp when the restorable resources existed.|restore_timestamp_in_utc|restoreTimestampInUtc|

### group `az cosmosdb service`
#### <a name="ServiceList">Command `az cosmosdb service list`</a>

##### <a name="ExamplesServiceList">Example</a>
```
az cosmosdb service list --account-name "ddb1" --resource-group "rg1"
```
##### <a name="ParametersServiceList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="ServiceGet">Command `az cosmosdb service show`</a>

##### <a name="ExamplesServiceGet">Example</a>
```
az cosmosdb service show --account-name "ddb1" --resource-group "rg1" --name "DataTransfer"
az cosmosdb service show --account-name "ddb1" --resource-group "rg1" --name "GraphAPICompute"
az cosmosdb service show --account-name "ddb1" --resource-group "rg1" --name "SqlDedicatedGateway"
```
##### <a name="ParametersServiceGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--service-name**|string|Cosmos DB service name.|service_name|serviceName|

#### <a name="ServiceCreate">Command `az cosmosdb service create`</a>

##### <a name="ExamplesServiceCreate">Example</a>
```
az cosmosdb service create --account-name "ddb1" --instance-count 1 --instance-size "Cosmos.D4s" --service-type \
"DataTransfer" --resource-group "rg1" --name "DataTransfer"
az cosmosdb service create --account-name "ddb1" --instance-count 1 --instance-size "Cosmos.D4s" --service-type \
"GraphAPICompute" --resource-group "rg1" --name "GraphAPICompute"
az cosmosdb service create --account-name "ddb1" --instance-count 1 --instance-size "Cosmos.D4s" --service-type \
"SqlDedicatedGateway" --resource-group "rg1" --name "SqlDedicatedGateway"
```
##### <a name="ParametersServiceCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--service-name**|string|Cosmos DB service name.|service_name|serviceName|
|**--instance-size**|choice|Instance type for the service.|instance_size|instanceSize|
|**--instance-count**|integer|Instance count for the service.|instance_count|instanceCount|
|**--service-type**|choice|ServiceType for the service.|service_type|serviceType|

#### <a name="ServiceDelete">Command `az cosmosdb service delete`</a>

##### <a name="ExamplesServiceDelete">Example</a>
```
az cosmosdb service delete --account-name "ddb1" --resource-group "rg1" --name "DataTransfer"
az cosmosdb service delete --account-name "ddb1" --resource-group "rg1" --name "GraphAPICompute"
az cosmosdb service delete --account-name "ddb1" --resource-group "rg1" --name "SqlDedicatedGateway"
```
##### <a name="ParametersServiceDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--service-name**|string|Cosmos DB service name.|service_name|serviceName|

### group `az cosmosdb sql-resource`
#### <a name="SqlResourcesCreateUpdateSqlContainer">Command `az cosmosdb sql-resource create-update-sql-container`</a>

##### <a name="ExamplesSqlResourcesCreateUpdateSqlContainer">Example</a>
```
az cosmosdb sql-resource create-update-sql-container --account-name "ddb1" --container-name "containerName" \
--create-update-sql-container-parameters "{\\"location\\":\\"West US\\",\\"tags\\":{},\\"resource\\":{\\"conflictResolu\
tionPolicy\\":{\\"conflictResolutionPath\\":\\"/path\\",\\"mode\\":\\"LastWriterWins\\"},\\"defaultTtl\\":100,\\"id\\":\
\\"containerName\\",\\"indexingPolicy\\":{\\"automatic\\":true,\\"excludedPaths\\":[],\\"includedPaths\\":[{\\"path\\":\
\\"/*\\",\\"indexes\\":[{\\"dataType\\":\\"String\\",\\"kind\\":\\"Range\\",\\"precision\\":-1},{\\"dataType\\":\\"Numb\
er\\",\\"kind\\":\\"Range\\",\\"precision\\":-1}]}],\\"indexingMode\\":\\"consistent\\"},\\"partitionKey\\":{\\"kind\\"\
:\\"Hash\\",\\"paths\\":[\\"/AccountNumber\\"]},\\"uniqueKeyPolicy\\":{\\"uniqueKeys\\":[{\\"paths\\":[\\"/testPath\\"]\
}]}},\\"options\\":{}}" --database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersSqlResourcesCreateUpdateSqlContainer">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--create-update-sql-container-parameters**|object|The parameters to provide for the current SQL container.|create_update_sql_container_parameters|createUpdateSqlContainerParameters|

#### <a name="SqlResourcesCreateUpdateSqlDatabase">Command `az cosmosdb sql-resource create-update-sql-database`</a>

##### <a name="ExamplesSqlResourcesCreateUpdateSqlDatabase">Example</a>
```
az cosmosdb sql-resource create-update-sql-database --account-name "ddb1" --location "West US" --id "databaseName" \
--database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersSqlResourcesCreateUpdateSqlDatabase">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--id**|string|Name of the Cosmos DB SQL database|id|id|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|

#### <a name="SqlResourcesCreateUpdateSqlRoleAssignment">Command `az cosmosdb sql-resource create-update-sql-role-assignment`</a>

##### <a name="ExamplesSqlResourcesCreateUpdateSqlRoleAssignment">Example</a>
```
az cosmosdb sql-resource create-update-sql-role-assignment --account-name "myAccountName" --principal-id \
"myPrincipalId" --role-definition-id "/subscriptions/mySubscriptionId/resourceGroups/myResourceGroupName/providers/Micr\
osoft.DocumentDB/databaseAccounts/myAccountName/sqlRoleDefinitions/myRoleDefinitionId" --scope \
"/subscriptions/mySubscriptionId/resourceGroups/myResourceGroupName/providers/Microsoft.DocumentDB/databaseAccounts/myA\
ccountName/dbs/purchases/colls/redmond-purchases" --resource-group "myResourceGroupName" --role-assignment-id \
"myRoleAssignmentId"
```
##### <a name="ParametersSqlResourcesCreateUpdateSqlRoleAssignment">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--role-assignment-id**|string|The GUID for the Role Assignment.|role_assignment_id|roleAssignmentId|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--role-definition-id**|string|The unique identifier for the associated Role Definition.|role_definition_id|roleDefinitionId|
|**--scope**|string|The data plane resource path for which access is being granted through this Role Assignment.|scope|scope|
|**--principal-id**|string|The unique identifier for the associated AAD principal in the AAD graph to which access is being granted through this Role Assignment. Tenant ID for the principal is inferred using the tenant associated with the subscription.|principal_id|principalId|

#### <a name="SqlResourcesCreateUpdateSqlRoleDefinition">Command `az cosmosdb sql-resource create-update-sql-role-definition`</a>

##### <a name="ExamplesSqlResourcesCreateUpdateSqlRoleDefinition">Example</a>
```
az cosmosdb sql-resource create-update-sql-role-definition --account-name "myAccountName" --type "CustomRole" \
--assignable-scopes "/subscriptions/mySubscriptionId/resourceGroups/myResourceGroupName/providers/Microsoft.DocumentDB/\
databaseAccounts/myAccountName/dbs/sales" "/subscriptions/mySubscriptionId/resourceGroups/myResourceGroupName/providers\
/Microsoft.DocumentDB/databaseAccounts/myAccountName/dbs/purchases" --permissions data-actions="Microsoft.DocumentDB/da\
tabaseAccounts/sqlDatabases/containers/items/create" data-actions="Microsoft.DocumentDB/databaseAccounts/sqlDatabases/c\
ontainers/items/read" --role-name "myRoleName" --resource-group "myResourceGroupName" --role-definition-id \
"myRoleDefinitionId"
```
##### <a name="ParametersSqlResourcesCreateUpdateSqlRoleDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--role-definition-id**|string|The GUID for the Role Definition.|role_definition_id|roleDefinitionId|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--role-name**|string|A user-friendly name for the Role Definition. Must be unique for the database account.|role_name|roleName|
|**--type**|sealed-choice|Indicates whether the Role Definition was built-in or user created.|type|type|
|**--assignable-scopes**|array|A set of fully qualified Scopes at or below which Role Assignments may be created using this Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Must have at least one element. Scopes higher than Database account are not enforceable as assignable Scopes. Note that resources referenced in assignable Scopes need not exist.|assignable_scopes|assignableScopes|
|**--permissions**|array|The set of operations allowed through this Role Definition.|permissions|permissions|

#### <a name="SqlResourcesCreateUpdateSqlStoredProcedure">Command `az cosmosdb sql-resource create-update-sql-stored-procedure`</a>

##### <a name="ExamplesSqlResourcesCreateUpdateSqlStoredProcedure">Example</a>
```
az cosmosdb sql-resource create-update-sql-stored-procedure --account-name "ddb1" --container-name "containerName" \
--resource body="body" id="storedProcedureName" --database-name "databaseName" --resource-group "rg1" \
--stored-procedure-name "storedProcedureName"
```
##### <a name="ParametersSqlResourcesCreateUpdateSqlStoredProcedure">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--stored-procedure-name**|string|Cosmos DB storedProcedure name.|stored_procedure_name|storedProcedureName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--resource**|object|The standard JSON format of a storedProcedure|resource|resource|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|

#### <a name="SqlResourcesCreateUpdateSqlTrigger">Command `az cosmosdb sql-resource create-update-sql-trigger`</a>

##### <a name="ExamplesSqlResourcesCreateUpdateSqlTrigger">Example</a>
```
az cosmosdb sql-resource create-update-sql-trigger --account-name "ddb1" --container-name "containerName" --resource \
body="body" id="triggerName" trigger-operation="triggerOperation" trigger-type="triggerType" --database-name \
"databaseName" --resource-group "rg1" --trigger-name "triggerName"
```
##### <a name="ParametersSqlResourcesCreateUpdateSqlTrigger">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--trigger-name**|string|Cosmos DB trigger name.|trigger_name|triggerName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--resource**|object|The standard JSON format of a trigger|resource|resource|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|

#### <a name="SqlResourcesCreateUpdateSqlUserDefinedFunction">Command `az cosmosdb sql-resource create-update-sql-user-defined-function`</a>

##### <a name="ExamplesSqlResourcesCreateUpdateSqlUserDefinedFunction">Example</a>
```
az cosmosdb sql-resource create-update-sql-user-defined-function --account-name "ddb1" --container-name \
"containerName" --resource body="body" id="userDefinedFunctionName" --database-name "databaseName" --resource-group \
"rg1" --user-defined-function-name "userDefinedFunctionName"
```
##### <a name="ParametersSqlResourcesCreateUpdateSqlUserDefinedFunction">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--user-defined-function-name**|string|Cosmos DB userDefinedFunction name.|user_defined_function_name|userDefinedFunctionName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--resource**|object|The standard JSON format of a userDefinedFunction|resource|resource|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|

#### <a name="SqlResourcesDeleteSqlContainer">Command `az cosmosdb sql-resource delete-sql-container`</a>

##### <a name="ExamplesSqlResourcesDeleteSqlContainer">Example</a>
```
az cosmosdb sql-resource delete-sql-container --account-name "ddb1" --container-name "containerName" --database-name \
"databaseName" --resource-group "rg1"
```
##### <a name="ParametersSqlResourcesDeleteSqlContainer">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|

#### <a name="SqlResourcesDeleteSqlDatabase">Command `az cosmosdb sql-resource delete-sql-database`</a>

##### <a name="ExamplesSqlResourcesDeleteSqlDatabase">Example</a>
```
az cosmosdb sql-resource delete-sql-database --account-name "ddb1" --database-name "databaseName" --resource-group \
"rg1"
```
##### <a name="ParametersSqlResourcesDeleteSqlDatabase">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="SqlResourcesDeleteSqlRoleAssignment">Command `az cosmosdb sql-resource delete-sql-role-assignment`</a>

##### <a name="ExamplesSqlResourcesDeleteSqlRoleAssignment">Example</a>
```
az cosmosdb sql-resource delete-sql-role-assignment --account-name "myAccountName" --resource-group \
"myResourceGroupName" --role-assignment-id "myRoleAssignmentId"
```
##### <a name="ParametersSqlResourcesDeleteSqlRoleAssignment">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--role-assignment-id**|string|The GUID for the Role Assignment.|role_assignment_id|roleAssignmentId|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="SqlResourcesDeleteSqlRoleDefinition">Command `az cosmosdb sql-resource delete-sql-role-definition`</a>

##### <a name="ExamplesSqlResourcesDeleteSqlRoleDefinition">Example</a>
```
az cosmosdb sql-resource delete-sql-role-definition --account-name "myAccountName" --resource-group \
"myResourceGroupName" --role-definition-id "myRoleDefinitionId"
```
##### <a name="ParametersSqlResourcesDeleteSqlRoleDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--role-definition-id**|string|The GUID for the Role Definition.|role_definition_id|roleDefinitionId|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="SqlResourcesDeleteSqlStoredProcedure">Command `az cosmosdb sql-resource delete-sql-stored-procedure`</a>

##### <a name="ExamplesSqlResourcesDeleteSqlStoredProcedure">Example</a>
```
az cosmosdb sql-resource delete-sql-stored-procedure --account-name "ddb1" --container-name "containerName" \
--database-name "databaseName" --resource-group "rg1" --stored-procedure-name "storedProcedureName"
```
##### <a name="ParametersSqlResourcesDeleteSqlStoredProcedure">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--stored-procedure-name**|string|Cosmos DB storedProcedure name.|stored_procedure_name|storedProcedureName|

#### <a name="SqlResourcesDeleteSqlTrigger">Command `az cosmosdb sql-resource delete-sql-trigger`</a>

##### <a name="ExamplesSqlResourcesDeleteSqlTrigger">Example</a>
```
az cosmosdb sql-resource delete-sql-trigger --account-name "ddb1" --container-name "containerName" --database-name \
"databaseName" --resource-group "rg1" --trigger-name "triggerName"
```
##### <a name="ParametersSqlResourcesDeleteSqlTrigger">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--trigger-name**|string|Cosmos DB trigger name.|trigger_name|triggerName|

#### <a name="SqlResourcesDeleteSqlUserDefinedFunction">Command `az cosmosdb sql-resource delete-sql-user-defined-function`</a>

##### <a name="ExamplesSqlResourcesDeleteSqlUserDefinedFunction">Example</a>
```
az cosmosdb sql-resource delete-sql-user-defined-function --account-name "ddb1" --container-name "containerName" \
--database-name "databaseName" --resource-group "rg1" --user-defined-function-name "userDefinedFunctionName"
```
##### <a name="ParametersSqlResourcesDeleteSqlUserDefinedFunction">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--user-defined-function-name**|string|Cosmos DB userDefinedFunction name.|user_defined_function_name|userDefinedFunctionName|

#### <a name="SqlResourcesListSqlContainers">Command `az cosmosdb sql-resource list-sql-container`</a>

##### <a name="ExamplesSqlResourcesListSqlContainers">Example</a>
```
az cosmosdb sql-resource list-sql-container --account-name "ddb1" --database-name "databaseName" --resource-group \
"rgName"
```
##### <a name="ParametersSqlResourcesListSqlContainers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="SqlResourcesListSqlDatabases">Command `az cosmosdb sql-resource list-sql-database`</a>

##### <a name="ExamplesSqlResourcesListSqlDatabases">Example</a>
```
az cosmosdb sql-resource list-sql-database --account-name "ddb1" --resource-group "rgName"
```
##### <a name="ParametersSqlResourcesListSqlDatabases">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="SqlResourcesListSqlRoleAssignments">Command `az cosmosdb sql-resource list-sql-role-assignment`</a>

##### <a name="ExamplesSqlResourcesListSqlRoleAssignments">Example</a>
```
az cosmosdb sql-resource list-sql-role-assignment --account-name "myAccountName" --resource-group \
"myResourceGroupName"
```
##### <a name="ParametersSqlResourcesListSqlRoleAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="SqlResourcesListSqlRoleDefinitions">Command `az cosmosdb sql-resource list-sql-role-definition`</a>

##### <a name="ExamplesSqlResourcesListSqlRoleDefinitions">Example</a>
```
az cosmosdb sql-resource list-sql-role-definition --account-name "myAccountName" --resource-group \
"myResourceGroupName"
```
##### <a name="ParametersSqlResourcesListSqlRoleDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="SqlResourcesListSqlStoredProcedures">Command `az cosmosdb sql-resource list-sql-stored-procedure`</a>

##### <a name="ExamplesSqlResourcesListSqlStoredProcedures">Example</a>
```
az cosmosdb sql-resource list-sql-stored-procedure --account-name "ddb1" --container-name "containerName" \
--database-name "databaseName" --resource-group "rgName"
```
##### <a name="ParametersSqlResourcesListSqlStoredProcedures">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|

#### <a name="SqlResourcesListSqlTriggers">Command `az cosmosdb sql-resource list-sql-trigger`</a>

##### <a name="ExamplesSqlResourcesListSqlTriggers">Example</a>
```
az cosmosdb sql-resource list-sql-trigger --account-name "ddb1" --container-name "containerName" --database-name \
"databaseName" --resource-group "rgName"
```
##### <a name="ParametersSqlResourcesListSqlTriggers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|

#### <a name="SqlResourcesListSqlUserDefinedFunctions">Command `az cosmosdb sql-resource list-sql-user-defined-function`</a>

##### <a name="ExamplesSqlResourcesListSqlUserDefinedFunctions">Example</a>
```
az cosmosdb sql-resource list-sql-user-defined-function --account-name "ddb1" --container-name "containerName" \
--database-name "databaseName" --resource-group "rgName"
```
##### <a name="ParametersSqlResourcesListSqlUserDefinedFunctions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|

#### <a name="SqlResourcesMigrateSqlContainerToAutoscale">Command `az cosmosdb sql-resource migrate-sql-container-to-autoscale`</a>

##### <a name="ExamplesSqlResourcesMigrateSqlContainerToAutoscale">Example</a>
```
az cosmosdb sql-resource migrate-sql-container-to-autoscale --account-name "ddb1" --container-name "containerName" \
--database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersSqlResourcesMigrateSqlContainerToAutoscale">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|

#### <a name="SqlResourcesMigrateSqlContainerToManualThroughput">Command `az cosmosdb sql-resource migrate-sql-container-to-manual-throughput`</a>

##### <a name="ExamplesSqlResourcesMigrateSqlContainerToManualThroughput">Example</a>
```
az cosmosdb sql-resource migrate-sql-container-to-manual-throughput --account-name "ddb1" --container-name \
"containerName" --database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersSqlResourcesMigrateSqlContainerToManualThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|

#### <a name="SqlResourcesMigrateSqlDatabaseToAutoscale">Command `az cosmosdb sql-resource migrate-sql-database-to-autoscale`</a>

##### <a name="ExamplesSqlResourcesMigrateSqlDatabaseToAutoscale">Example</a>
```
az cosmosdb sql-resource migrate-sql-database-to-autoscale --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1"
```
##### <a name="ParametersSqlResourcesMigrateSqlDatabaseToAutoscale">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="SqlResourcesMigrateSqlDatabaseToManualThroughput">Command `az cosmosdb sql-resource migrate-sql-database-to-manual-throughput`</a>

##### <a name="ExamplesSqlResourcesMigrateSqlDatabaseToManualThroughput">Example</a>
```
az cosmosdb sql-resource migrate-sql-database-to-manual-throughput --account-name "ddb1" --database-name \
"databaseName" --resource-group "rg1"
```
##### <a name="ParametersSqlResourcesMigrateSqlDatabaseToManualThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="SqlResourcesRetrieveContinuousBackupInformation">Command `az cosmosdb sql-resource retrieve-continuou-backup-information`</a>

##### <a name="ExamplesSqlResourcesRetrieveContinuousBackupInformation">Example</a>
```
az cosmosdb sql-resource retrieve-continuou-backup-information --account-name "ddb1" --container-name "containerName" \
--database-name "databaseName" --location "North Europe" --resource-group "rgName"
```
##### <a name="ParametersSqlResourcesRetrieveContinuousBackupInformation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--location**|string|The name of the continuous backup restore location.|location|location|

#### <a name="SqlResourcesGetSqlContainer">Command `az cosmosdb sql-resource show-sql-container`</a>

##### <a name="ExamplesSqlResourcesGetSqlContainer">Example</a>
```
az cosmosdb sql-resource show-sql-container --account-name "ddb1" --container-name "containerName" --database-name \
"databaseName" --resource-group "rgName"
```
##### <a name="ParametersSqlResourcesGetSqlContainer">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|

#### <a name="SqlResourcesGetSqlContainerThroughput">Command `az cosmosdb sql-resource show-sql-container-throughput`</a>

##### <a name="ExamplesSqlResourcesGetSqlContainerThroughput">Example</a>
```
az cosmosdb sql-resource show-sql-container-throughput --account-name "ddb1" --container-name "containerName" \
--database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersSqlResourcesGetSqlContainerThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|

#### <a name="SqlResourcesGetSqlDatabase">Command `az cosmosdb sql-resource show-sql-database`</a>

##### <a name="ExamplesSqlResourcesGetSqlDatabase">Example</a>
```
az cosmosdb sql-resource show-sql-database --account-name "ddb1" --database-name "databaseName" --resource-group "rg1"
```
##### <a name="ParametersSqlResourcesGetSqlDatabase">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="SqlResourcesGetSqlDatabaseThroughput">Command `az cosmosdb sql-resource show-sql-database-throughput`</a>

##### <a name="ExamplesSqlResourcesGetSqlDatabaseThroughput">Example</a>
```
az cosmosdb sql-resource show-sql-database-throughput --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1"
```
##### <a name="ParametersSqlResourcesGetSqlDatabaseThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|

#### <a name="SqlResourcesGetSqlRoleAssignment">Command `az cosmosdb sql-resource show-sql-role-assignment`</a>

##### <a name="ExamplesSqlResourcesGetSqlRoleAssignment">Example</a>
```
az cosmosdb sql-resource show-sql-role-assignment --account-name "myAccountName" --resource-group \
"myResourceGroupName" --role-assignment-id "myRoleAssignmentId"
```
##### <a name="ParametersSqlResourcesGetSqlRoleAssignment">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--role-assignment-id**|string|The GUID for the Role Assignment.|role_assignment_id|roleAssignmentId|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="SqlResourcesGetSqlRoleDefinition">Command `az cosmosdb sql-resource show-sql-role-definition`</a>

##### <a name="ExamplesSqlResourcesGetSqlRoleDefinition">Example</a>
```
az cosmosdb sql-resource show-sql-role-definition --account-name "myAccountName" --resource-group \
"myResourceGroupName" --role-definition-id "myRoleDefinitionId"
```
##### <a name="ParametersSqlResourcesGetSqlRoleDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--role-definition-id**|string|The GUID for the Role Definition.|role_definition_id|roleDefinitionId|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="SqlResourcesGetSqlStoredProcedure">Command `az cosmosdb sql-resource show-sql-stored-procedure`</a>

##### <a name="ExamplesSqlResourcesGetSqlStoredProcedure">Example</a>
```
az cosmosdb sql-resource show-sql-stored-procedure --account-name "ddb1" --container-name "containerName" \
--database-name "databaseName" --resource-group "rgName" --stored-procedure-name "storedProcedureName"
```
##### <a name="ParametersSqlResourcesGetSqlStoredProcedure">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--stored-procedure-name**|string|Cosmos DB storedProcedure name.|stored_procedure_name|storedProcedureName|

#### <a name="SqlResourcesGetSqlTrigger">Command `az cosmosdb sql-resource show-sql-trigger`</a>

##### <a name="ExamplesSqlResourcesGetSqlTrigger">Example</a>
```
az cosmosdb sql-resource show-sql-trigger --account-name "ddb1" --container-name "containerName" --database-name \
"databaseName" --resource-group "rgName" --trigger-name "triggerName"
```
##### <a name="ParametersSqlResourcesGetSqlTrigger">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--trigger-name**|string|Cosmos DB trigger name.|trigger_name|triggerName|

#### <a name="SqlResourcesGetSqlUserDefinedFunction">Command `az cosmosdb sql-resource show-sql-user-defined-function`</a>

##### <a name="ExamplesSqlResourcesGetSqlUserDefinedFunction">Example</a>
```
az cosmosdb sql-resource show-sql-user-defined-function --account-name "ddb1" --container-name "containerName" \
--database-name "databaseName" --resource-group "rgName" --user-defined-function-name "userDefinedFunctionName"
```
##### <a name="ParametersSqlResourcesGetSqlUserDefinedFunction">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--user-defined-function-name**|string|Cosmos DB userDefinedFunction name.|user_defined_function_name|userDefinedFunctionName|

#### <a name="SqlResourcesUpdateSqlContainerThroughput">Command `az cosmosdb sql-resource update-sql-container-throughput`</a>

##### <a name="ExamplesSqlResourcesUpdateSqlContainerThroughput">Example</a>
```
az cosmosdb sql-resource update-sql-container-throughput --account-name "ddb1" --container-name "containerName" \
--database-name "databaseName" --resource-group "rg1" --location "West US" --throughput 400
```
##### <a name="ParametersSqlResourcesUpdateSqlContainerThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--container-name**|string|Cosmos DB container name.|container_name|containerName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--throughput**|integer|Value of the Cosmos DB resource throughput. Either throughput is required or autoscaleSettings is required, but not both.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput container can scale up to.|max_throughput|maxThroughput|
|**--throughput-policy**|object|Represents throughput policy which service must adhere to for auto-upgrade|throughput_policy|throughputPolicy|

#### <a name="SqlResourcesUpdateSqlDatabaseThroughput">Command `az cosmosdb sql-resource update-sql-database-throughput`</a>

##### <a name="ExamplesSqlResourcesUpdateSqlDatabaseThroughput">Example</a>
```
az cosmosdb sql-resource update-sql-database-throughput --account-name "ddb1" --database-name "databaseName" \
--resource-group "rg1" --location "West US" --throughput 400
```
##### <a name="ParametersSqlResourcesUpdateSqlDatabaseThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--database-name**|string|Cosmos DB database name.|database_name|databaseName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--throughput**|integer|Value of the Cosmos DB resource throughput. Either throughput is required or autoscaleSettings is required, but not both.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput container can scale up to.|max_throughput|maxThroughput|
|**--throughput-policy**|object|Represents throughput policy which service must adhere to for auto-upgrade|throughput_policy|throughputPolicy|

### group `az cosmosdb table-resource`
#### <a name="TableResourcesCreateUpdateTable">Command `az cosmosdb table-resource create-update-table`</a>

##### <a name="ExamplesTableResourcesCreateUpdateTable">Example</a>
```
az cosmosdb table-resource create-update-table --account-name "ddb1" --location "West US" --id "tableName" \
--resource-group "rg1" --table-name "tableName"
```
##### <a name="ParametersTableResourcesCreateUpdateTable">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--id**|string|Name of the Cosmos DB table|id|id|
|**--throughput**|integer|Request Units per second. For example, "throughput": 10000.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput, the resource can scale up to.|max_throughput|maxThroughput|

#### <a name="TableResourcesDeleteTable">Command `az cosmosdb table-resource delete-table`</a>

##### <a name="ExamplesTableResourcesDeleteTable">Example</a>
```
az cosmosdb table-resource delete-table --account-name "ddb1" --resource-group "rg1" --table-name "tableName"
```
##### <a name="ParametersTableResourcesDeleteTable">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|

#### <a name="TableResourcesListTables">Command `az cosmosdb table-resource list-table`</a>

##### <a name="ExamplesTableResourcesListTables">Example</a>
```
az cosmosdb table-resource list-table --account-name "ddb1" --resource-group "rgName"
```
##### <a name="ParametersTableResourcesListTables">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|

#### <a name="TableResourcesMigrateTableToAutoscale">Command `az cosmosdb table-resource migrate-table-to-autoscale`</a>

##### <a name="ExamplesTableResourcesMigrateTableToAutoscale">Example</a>
```
az cosmosdb table-resource migrate-table-to-autoscale --account-name "ddb1" --resource-group "rg1" --table-name \
"tableName"
```
##### <a name="ParametersTableResourcesMigrateTableToAutoscale">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|

#### <a name="TableResourcesMigrateTableToManualThroughput">Command `az cosmosdb table-resource migrate-table-to-manual-throughput`</a>

##### <a name="ExamplesTableResourcesMigrateTableToManualThroughput">Example</a>
```
az cosmosdb table-resource migrate-table-to-manual-throughput --account-name "ddb1" --resource-group "rg1" \
--table-name "tableName"
```
##### <a name="ParametersTableResourcesMigrateTableToManualThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|

#### <a name="TableResourcesGetTable">Command `az cosmosdb table-resource show-table`</a>

##### <a name="ExamplesTableResourcesGetTable">Example</a>
```
az cosmosdb table-resource show-table --account-name "ddb1" --resource-group "rg1" --table-name "tableName"
```
##### <a name="ParametersTableResourcesGetTable">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|

#### <a name="TableResourcesGetTableThroughput">Command `az cosmosdb table-resource show-table-throughput`</a>

##### <a name="ExamplesTableResourcesGetTableThroughput">Example</a>
```
az cosmosdb table-resource show-table-throughput --account-name "ddb1" --resource-group "rg1" --table-name "tableName"
```
##### <a name="ParametersTableResourcesGetTableThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|

#### <a name="TableResourcesUpdateTableThroughput">Command `az cosmosdb table-resource update-table-throughput`</a>

##### <a name="ExamplesTableResourcesUpdateTableThroughput">Example</a>
```
az cosmosdb table-resource update-table-throughput --account-name "ddb1" --resource-group "rg1" --table-name \
"tableName" --location "West US" --throughput 400
```
##### <a name="ParametersTableResourcesUpdateTableThroughput">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|Cosmos DB database account name.|account_name|accountName|
|**--table-name**|string|Cosmos DB table name.|table_name|tableName|
|**--location**|string|The location of the resource group to which the resource belongs.|location|location|
|**--tags**|dictionary|Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".|tags|tags|
|**--type**|sealed-choice|The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.|type|type|
|**--user-assigned-identities**|dictionary|The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|userAssignedIdentities|
|**--throughput**|integer|Value of the Cosmos DB resource throughput. Either throughput is required or autoscaleSettings is required, but not both.|throughput|throughput|
|**--max-throughput**|integer|Represents maximum throughput container can scale up to.|max_throughput|maxThroughput|
|**--throughput-policy**|object|Represents throughput policy which service must adhere to for auto-upgrade|throughput_policy|throughputPolicy|
