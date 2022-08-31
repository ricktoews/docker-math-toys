import math
from modules.non_repeating import tally

letter_digit = ['A', 'B', 'C', 'D', 'E', 'F']
def get_digit(value):
	if value > 9:
		value = letter_digit[value-10]
	return value

def calc_decimal(reduced_num, reduced_denom, base):
	section_list = ['', '', '']
	section_ndx = 0

	non_repeating = tally(reduced_denom, base)
	if (non_repeating == -1):
		non_repeating_tally = reduced_denom - 1
	else:
		non_repeating_tally = non_repeating

	# either find how to fill an array in Python, or take a different approach.
	remainder_flag_list = [False] * (reduced_denom - 1)

	repeating_decimal_flag = non_repeating != -1
	start_repeat = 0
	step_digit = 0
	step_remainder = reduced_num
	decimal_length = 0

	# BEGIN LONG DIVISION -----
	while step_remainder != 0 and not step_remainder in remainder_flag_list:
		remainder_flag_list.append(step_remainder)
		step_value = math.floor(step_remainder * base / reduced_denom)
		step_digit = get_digit(step_value)

		if decimal_length == non_repeating_tally:
			section_ndx += 1
			# Store this digit; it'll be used to determine when/if the complement begins.
			start_repeat = step_remainder

		section_list[section_ndx] += str(step_digit)

		step_remainder = step_remainder * base - step_value * reduced_denom
		if step_remainder + start_repeat == reduced_denom:
			section_ndx += 1

		decimal_length += 1

	# END LONG DIVISION -----

	if repeating_decimal_flag:
		repeating = decimal_length - non_repeating_tally
	else:
		repeating = 0

	period_length = decimal_length
	repeating = repeating
	period = ''.join(section_list)
	decimal_object = {
		"fraction": str(reduced_num) + ' / ' + str(reduced_denom),
		"non_repeating": section_list[0],
		"repeating_1": section_list[1],
		"repeating_complement": section_list[2],
		"period_length": period_length,
		"repeating": repeating,
		"period": period,
	}
	return decimal_object

