def auto_time_unit(time_in_second):
    unit = ['ms', 'µs', 'ns']
    unit2 = ['mins', 'hours', 'days', 'years']
    unit2_quality = [60, 60*60, 24*60*60, 365*24*60*60]

    if time_in_second < 1:
        current_unit = -1
        while time_in_second < 1 and current_unit < len(unit):
            time_in_second = time_in_second * 1000
            current_unit = current_unit + 1

        return time_in_second, unit[current_unit]
    else:
        current_unit = 0
        for index, quality in enumerate(unit2_quality):
            if time_in_second < quality and index > 0:
                current_unit = index - 1
                break

        return time_in_second, 's'
