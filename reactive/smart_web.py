import pwd
import os
from charmhelpers.core.hookenv import status_set
from charmhelpers.core.templating import render
from charms.reactive import when, when_not, set_flag
from charms.reactive import set_state, remove_state

@when_not('smart-web.installed')
@when('layer-basic.installed')
@when('interface-http.installed')
@when('interface-tls.installed')
@when('interface-tls-certificates.installed')
@when('interface-etcd.installed')
@when('interface-docker-registry.installed')
@when('interface-docker-image-host.installed')
@when('interface-dockerhost.installed')
@when('interface-pgsql.installed')
@when('interface-redis.installed')
@when('layer-docker-resource.installed')
@when('layer-docker.installed')
def install_smart_web():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    @when('layer-tls.installed')
    @when('layer-tls-client.installed')
    set_flag('smart-web.installed')
