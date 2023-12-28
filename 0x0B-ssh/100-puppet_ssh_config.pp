# set up client SSH configuration file to connect without a password
#!/usr/bin/pup

# use the private key ~/.ssh/school
file_line { 'Use private key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}

# refuse to authenticate using a password
file_line { 'No password authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
