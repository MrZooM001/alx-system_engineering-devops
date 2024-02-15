# Fix `wp-settings.pphp` extensions to `php`.

exec { 'fix_wp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
