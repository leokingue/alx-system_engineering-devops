# Increse the request's limit

# Increse ulimit value
exec { 'fix-config-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart nginex service
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
