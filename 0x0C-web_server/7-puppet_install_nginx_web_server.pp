# Task 5. Install Nginx web server (w/ Puppet)
exec { 'update packages':
    command => 'apt update -y',
    path    => '/usr/bin:/usr/sbin:/usr/local/sbin:/usr/local/bin:/sbin:/bin',
}

package { 'nginx':
    ensure => 'installed',
}

exec { 'allow HTTP':
    command => 'ufw allow "Nginx HTTP"',
    path    => '/usr/bin:/usr/sbin:/usr/local/sbin:/usr/local/bin:/sbin:/bin',
}

exec { 'chmod www directory':
    command => 'chmod -R 755 /var/www/',
    path    => '/usr/bin:/usr/sbin:/usr/local/sbin:/usr/local/bin:/sbin:/bin',
}

file { 'index.nginx-debian.html':
    path    => '/var/www/html/index.nginx-debian.html',
    content => 'Hello World!',
}

exec { 'config':
    command  => 'sed -i "53i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-enabled/default',
    provider => 'shell',
}
exec { 'restart':
    command => 'sudo service nginx restart',
    provider => 'shell',
}
