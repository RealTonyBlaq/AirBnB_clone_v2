# Puppet installs Nginx and sets up your web servers for the deployment of web_static

package {'nginx':
    ensure => 'installed'
}

exec {'make_rel':
    command => 'mkdir -p /data/web_static/releases/test/',
    path    => '/usr/bin/'
}

exec {'make_shared':
    command => 'mkdir -p /data/web_static/shared/',
    path    => '/usr/bin/'
}

file {'/data/web_static/releases/test/index.html':
    ensure => 'present
}

file {'/data/':
    ensure  => 'directory',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => true,
    require => Exec['make_rel', 'make_shared']
}

service {'nginx':
    ensure  => 'running',
    require => Package['nginx']
}
