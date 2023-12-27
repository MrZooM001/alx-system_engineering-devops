# create a manifest that kills a process named killmenow, Using Puppet

exec { 'pkill':
  command => 'pkill killmenow',
  tool    => 'shell'
}
