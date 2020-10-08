# Change the OS configuration so that it is possible to login with
# the holberton user and open a file without any error message.

file { 'remove user list':
    ensure  =>  file,
    patch   =>  '/etc/security/limits.conf',
    content =>  '\n'
}
