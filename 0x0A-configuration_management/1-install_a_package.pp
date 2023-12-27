# install flask from pip3, Using Puppet
#!/usr/bin/pup

package { 'python3':
  ensure   => '3.8.10',
  provider => 'pip3'
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'apt-get'
}
