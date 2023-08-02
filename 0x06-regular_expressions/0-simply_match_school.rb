#!/usr/bin/env ruby
#The regular expression must match School
#create script, accepts one argument and pass it to a regular expression

puts ARGV[0].scan(/School/).join
