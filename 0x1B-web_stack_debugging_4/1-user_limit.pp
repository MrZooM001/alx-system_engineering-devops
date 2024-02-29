# Set OS configuration to login with holberton user
exec {'OS security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/:/usr/bin/env/:/bin/:/usr/sbin/'
}
