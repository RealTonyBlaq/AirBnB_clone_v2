# Puppet installs Nginx and sets up your web servers for the deployment of web_static

package {'nginx':
    ensure => 'installed',
}

exec {'make_rel':
    command => 'mkdir -p /data/web_static/releases/test/',
    path    => '/usr/bin/',
}

exec {'make_shared':
    command => 'mkdir -p /data/web_static/shared/',
    path    => '/usr/bin/',
}

file {'/data/web_static/releases/test/index.html':
    ensure  => 'present',
    mode    => '0644',
    content => 'Testing my Nginx configuration',
    require => Exec['make_rel'],
}

exec {'sym_link':
    command => 'ln -s /data/web_static/releases/test/ /data/web_static/current',
    path    => '/usr/bin/',
    require => Exec['make_rel'],
}

file {'/data/':
    ensure  => 'directory',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => true,
    require => Exec['make_rel'],
}

exec {'serve_static':
    command => 'sed -i "48i\        location /hbnb_static {        alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
    path    => '/usr/bin/',
    require => Package['nginx'],
}

service {'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
}
