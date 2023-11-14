# fix stack so that we get to 0 failed requests

exec { 'fix--nginx-config':
  command => "/bin/sed -i /etc/default/nginx -e 's/15/3000/'"
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Exec['fix--nginx-config']
}
