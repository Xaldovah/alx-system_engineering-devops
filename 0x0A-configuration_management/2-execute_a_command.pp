# Define an exec resource to kill the "killmenow" process

exec { 'killmenow':
command => '/usr/bin/pkill killmenow',
}
