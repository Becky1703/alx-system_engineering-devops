#Creates a manifest that kills a process called killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
