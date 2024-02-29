# Set OS configuration to login with holberton user
exec {'OS security config':
  command => 'sed -i "s/holberton/" /etc/security/limits.conf',
  path    => '/bin/:/usr/bin/env/:/usr/bin/:/usr/sbin/'
}
