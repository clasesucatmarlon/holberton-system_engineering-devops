# Change the OS configuration so that it is possible to login with
# the holberton user and open a file without any error message.

exec { 'one':
    command =>  'sed -i "/holberton hard nofile 5/d" /etc/security/limits.conf'
    path    =>  '/bin'
}

exec { 'Two':
    command =>  'sed -i "/holberton soft nofile 4/d" /etc/security/limits.conf'
    path    =>  '/bin'
}
