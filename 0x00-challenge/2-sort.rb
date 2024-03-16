# Sort integer arguments in ascending order using insertion sort

result = []

ARGV.each do |arg|
  # Skip if not an integer
  next unless arg.match?(/^(-?\d+)$/)

  i_arg = arg.to_i

  # Insert result at the right position using binary search
  index = result.bsearch_index { |num| num >= i_arg } || result.size
  result.insert(index, i_arg)
end

puts result
