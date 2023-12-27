# install flask from pip3, Using Puppet
#!/usr/bin/pup

# install python3 from pip3
package { 'python3':
  ensure   => '3.8.10',
  provider => 'pip3'
}

# install flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

# install Werkzeug from pip3
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
