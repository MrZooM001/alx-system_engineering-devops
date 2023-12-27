# create a file in /tmp, Using Puppet

file { '/tmp/school':
 'mod'    => '0744',
 'owner'   => 'www-data',
 'group'   => 'www-data'
 'content' => 'I love Puppet'
}
