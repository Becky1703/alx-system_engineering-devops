#Installs and configures nginx on Ubuntu using puppet

#installs Nginx package
package { 'nginx':
  ensure => installed,
}

#Configuration for Nginx server
file { '/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => @(EOF),
    server {
      listen 80;
      root /var/www/html;
      
      location / {
        return 200 'Hello World!':
      }

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4/;
      }
    }
 EOF
}

#To restart Nginx service after configuration
service { 'nginx':
  ensure  => running,
  enable  => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
