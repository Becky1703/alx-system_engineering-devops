#Installs and configures nginx on Ubuntu using puppet

#installs Nginx package
package { 'nginx':
  ensure => installed,
}

#Configuration for Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "
    server {
      listen 80;
      ubuntu /var/www/html;
      
      location / {
        return 200 'Hello World!':
      }

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4/;
      }
    }
  ",
}

#To restart Nginx service after configuration
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
