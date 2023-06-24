# Seting up my client config file


file { '/root/.ssh/config':
  ensure => present,
  mode   => '0600',
  owner  => 'root',
  group  => 'root',
  content => @(EOF)
    Host ubuntu
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
    EOF
}
