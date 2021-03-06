# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.clustering.v1 import _proxy
from openstack.clustering.v1 import cluster
from openstack.tests.unit import test_proxy_base


class TestClusteringProxy(test_proxy_base.TestProxyBase):
    def setUp(self):
        super(TestClusteringProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_cluster_create(self):
        self.verify_create(self.proxy.create_cluster, cluster.Cluster)

    def test_cluster_delete(self):
        self.verify_delete2(cluster.Cluster, self.proxy.delete_cluster, False)

    def test_cluster_delete_ignore(self):
        self.verify_delete2(cluster.Cluster, self.proxy.delete_cluster, True)

    def test_cluster_find(self):
        self.verify_find('openstack.clustering.v1.cluster.Cluster.find',
                         self.proxy.find_cluster)

    def test_cluster_get(self):
        self.verify_get2('openstack.proxy.BaseProxy._get',
                         self.proxy.get_cluster,
                         method_args=["resource_or_id"],
                         expected_args=[cluster.Cluster, "resource_or_id"])

    def test_clusters(self):
        self.verify_list2(self.proxy.clusters,
                          method_kwargs={'limit': 2},
                          expected_args=[cluster.Cluster],
                          expected_kwargs={'paginated': True, 'limit': 2})

    def test_cluster_update(self):
        kwargs = {"name": "new-name"}
        self.verify_update2('openstack.proxy.BaseProxy._update',
                            self.proxy.update_cluster,
                            method_args=['resource_or_id'],
                            method_kwargs=kwargs,
                            expected_args=[cluster.Cluster, "resource_or_id"],
                            expected_kwargs=kwargs)
