# Puppet installs Nginx and sets up your web servers for the deployment of web_static

package {'nginx':
    ensure => 'installed'
}

file {'/data':
    ensure => 'directory',
    owner  => 
}

service {'nginx':
    ensure  => 'running',
    require => Package['nginx']
}
