# create a file in '/tmp', Using Puppet

file { '/tmp/school':
  'content'    => 'I love Puppet',
  'permission' => '0744',
  'owner'      => 'www-data',
  'group'      => 'www-data'
}
