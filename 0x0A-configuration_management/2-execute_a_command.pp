# Using Puppet, create a manifest that kills a process named killmenow

exec { 'kill_process':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
  returns => '0',
}
