# create a file in '/tmp', Using Puppet
#!/usr/bin/pup

file { '/tmp/school':
  ensure  => 'present',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
