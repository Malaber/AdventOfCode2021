require_relative '../helpers/input'
lines = get_lines $PROGRAM_NAME

positions = lines.first.split(',')

positions = positions.map(&:to_i)

minfuel = nil
best_pos = -1

(positions.min..positions.max).each do |pos|
  fuel = 0
  positions.each do |p|
    fuel += (pos - p).abs
  end
  if minfuel.nil? || minfuel > fuel
    minfuel = fuel
    best_pos = pos
  end
end

puts "Fuel: #{minfuel}, position: #{best_pos}"
