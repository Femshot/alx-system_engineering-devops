# Puppet to set changes in a server
file_line { 'remove passphrase login':
  path => '/etc/ssh/ssh_config',
  line => '		PasswordAuthentication no',
}
file_line { 'add path to find the keys':
  path => '/etc/ssh/ssh_config',
  line => '		IdentityFile ~/.ssh/school',
}
