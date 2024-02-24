# Using Puppet, create a file in /tmp. ad file school with contents
$doc_root = '/tmp'

# Ensure the /tmp/school directory exists with the specified permissions and ownership.
file { $doc_root:
  ensure => 'directory',
}

# Create the /tmp/school file with the desired content.
file { "${doc_root}/school":
  ensure  => 'file',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  require => File[$doc_root],
}
