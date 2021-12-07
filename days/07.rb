require_relative '../helpers/input'
lines = get_lines $PROGRAM_NAME

positions = lines.first.split(',')

positions = positions.map(&:to_i)

puts "PART 1"
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

puts
puts "PART 2"

minfuel = nil
best_pos = -1

(positions.min..positions.max).each do |pos|
  fuel = 0
  positions.each do |p|
    move = (pos - p).abs
    if move > 0
      move_fuel = (1..move).inject(:+)
      fuel += move_fuel
    end
  end
  if minfuel.nil? || minfuel > fuel
    minfuel = fuel
    best_pos = pos
  end
end

puts "Fuel: #{minfuel}, position: #{best_pos}"
