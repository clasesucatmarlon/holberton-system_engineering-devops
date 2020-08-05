# configurate the client SSH file configuration

file_line { 'password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => '^.?.*PasswordAuthentication yes$',
  line   => 'PasswordAuthentication no',
}

file_line { 'identity':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^.*IdentityFile ~/.ssh/holberton$',
  path   => '/etc/ssh/ssh_config',
}
