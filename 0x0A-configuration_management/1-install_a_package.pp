# Ensure Flask package is installed with version 2.1.0

package { 'Flask':
ensure   => '2.1.0',
provider => 'pip3',
}
