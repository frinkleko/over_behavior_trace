import csv
#这里替换analysis的结果
user_behavior_data = [
    {'total_focus_time': 0, 'windowswitch_count': 0, 'windowswitch_speed': 0, 'totaltime': 1053.332, 'click_count': 5, 'total_mouse_movement': 21549.270601635504, 'scroll_count': 0, 'total_scroll_distance': 0, 'average_scroll_distance': 0, 'med_scroll_distance': 0, 'mousewheel_count': 0, 'total_mousewheel_distance': 0, 'average_mousewheel_distance': 0, 'med_mousewheel_distance': 0, 'copy_count': 0, 'average_copy_length': 0, 'med_copy_length': 0, 'paste_count': 0, 'average_paste_length': 0, 'med_paste_length': 0, 'delete_count': 24, 'keypress_count': 448, 'highlight_count': 2, 'average_highlight_length': 92.0, 'med_highlight_length': 92.0, 'idle_count': 41, 'med_idle_duration': 2011, 'total_idle_duration': 89738, 'keyboard_input_count': 0, 'average_input_length': 0, 'average_input_duration': 0, 'total_input_duration': 0, 'med_input_length': 0, 'med_input_duration': 0},
    {'total_focus_time': 0, 'windowswitch_count': 0, 'windowswitch_speed': 0, 'totaltime': 1081.64, 'click_count': 10, 'total_mouse_movement': 15850.565791415327, 'scroll_count': 0, 'total_scroll_distance': 0, 'average_scroll_distance': 0, 'med_scroll_distance': 0, 'mousewheel_count': 0, 'total_mousewheel_distance': 0, 'average_mousewheel_distance': 0, 'med_mousewheel_distance': 0, 'copy_count': 1, 'average_copy_length': 2.0, 'med_copy_length': 2, 'paste_count': 1, 'average_paste_length': 7.0, 'med_paste_length': 7, 'delete_count': 48, 'keypress_count': 18, 'highlight_count': 0, 'average_highlight_length': 0, 'med_highlight_length': 0, 'idle_count': 34, 'med_idle_duration': 2008.0, 'total_idle_duration': 71840, 'keyboard_input_count': 0, 'average_input_length': 0, 'average_input_duration': 0, 'total_input_duration': 0, 'med_input_length': 0, 'med_input_duration': 0},
    {'total_focus_time': 0, 'windowswitch_count': 0, 'windowswitch_speed': 0, 'totaltime': 1037.118, 'click_count': 50, 'total_mouse_movement': 64003.810518191756, 'scroll_count': 2, 'total_scroll_distance': 200, 'average_scroll_distance': 100.0, 'med_scroll_distance': 100.0, 'mousewheel_count': 0, 'total_mousewheel_distance': 0, 'average_mousewheel_distance': 0, 'med_mousewheel_distance': 0, 'copy_count': 0, 'average_copy_length': 0, 'med_copy_length': 0, 'paste_count': 1, 'average_paste_length': 119.0, 'med_paste_length': 119, 'delete_count': 41, 'keypress_count': 25, 'highlight_count': 0, 'average_highlight_length': 0, 'med_highlight_length': 0, 'idle_count': 77, 'med_idle_duration': 2006, 'total_idle_duration': 155846, 'keyboard_input_count': 24, 'average_input_length': 22.958333333333332, 'average_input_duration': 11462.541666666666, 'total_input_duration': 275101, 'med_input_length': 12.5, 'med_input_duration': 10368.5},
    {'total_focus_time': 0, 'windowswitch_count': 0, 'windowswitch_speed': 0, 'totaltime': 468.151, 'click_count': 23, 'total_mouse_movement': 30754.61141620428, 'scroll_count': 14, 'total_scroll_distance': 1400, 'average_scroll_distance': 100.0, 'med_scroll_distance': 100.0, 'mousewheel_count': 0, 'total_mousewheel_distance': 0, 'average_mousewheel_distance': 0, 'med_mousewheel_distance': 0, 'copy_count': 0, 'average_copy_length': 0, 'med_copy_length': 0, 'paste_count': 0, 'average_paste_length': 0, 'med_paste_length': 0, 'delete_count': 9, 'keypress_count': 249, 'highlight_count': 8, 'average_highlight_length': 240.375, 'med_highlight_length': 82.5, 'idle_count': 12, 'med_idle_duration': 2010.0, 'total_idle_duration': 24106, 'keyboard_input_count': 5, 'average_input_length': 46.8, 'average_input_duration': 8574.6, 'total_input_duration': 42873, 'med_input_length': 46, 'med_input_duration': 8011},
    {'total_focus_time': 0, 'windowswitch_count': 0, 'windowswitch_speed': 0, 'totaltime': 986.776, 'click_count': 23, 'total_mouse_movement': 33701.00622506411, 'scroll_count': 95, 'total_scroll_distance': 9500, 'average_scroll_distance': 100.0, 'med_scroll_distance': 100, 'mousewheel_count': 0, 'total_mousewheel_distance': 0, 'average_mousewheel_distance': 0, 'med_mousewheel_distance': 0, 'copy_count': 1, 'average_copy_length': 37.0, 'med_copy_length': 37, 'paste_count': 2, 'average_paste_length': 888.0, 'med_paste_length': 888.0, 'delete_count': 80, 'keypress_count': 567, 'highlight_count': 3, 'average_highlight_length': 15.666666666666666, 'med_highlight_length': 5, 'idle_count': 60, 'med_idle_duration': 2006.0, 'total_idle_duration': 120421, 'keyboard_input_count': 9, 'average_input_length': 246.44444444444446, 'average_input_duration': 18967.333333333332, 'total_input_duration': 170706, 'med_input_length': 60, 'med_input_duration': 14652},
    {'total_focus_time': 0, 'windowswitch_count': 0, 'windowswitch_speed': 0, 'totaltime': 623.797, 'click_count': 22, 'total_mouse_movement': 43589.00217624885, 'scroll_count': 65, 'total_scroll_distance': 6400, 'average_scroll_distance': 98.46153846153847, 'med_scroll_distance': 100, 'mousewheel_count': 0, 'total_mousewheel_distance': 0, 'average_mousewheel_distance': 0, 'med_mousewheel_distance': 0, 'copy_count': 1, 'average_copy_length': 21.0, 'med_copy_length': 21, 'paste_count': 3, 'average_paste_length': 540.3333333333334, 'med_paste_length': 126, 'delete_count': 71, 'keypress_count': 636, 'highlight_count': 2, 'average_highlight_length': 14.0, 'med_highlight_length': 14.0, 'idle_count': 37, 'med_idle_duration': 2006, 'total_idle_duration': 74612, 'keyboard_input_count': 7, 'average_input_length': 306.0, 'average_input_duration': 19281.14285714286, 'total_input_duration': 134968, 'med_input_length': 57, 'med_input_duration': 10355},
    {'total_focus_time': 0, 'windowswitch_count': 10, 'windowswitch_speed': 101.9091, 'totaltime': 1019.091, 'click_count': 33, 'total_mouse_movement': 47271.6694587303, 'scroll_count': 0, 'total_scroll_distance': 0, 'average_scroll_distance': 0, 'med_scroll_distance': 0, 'mousewheel_count': 325, 'total_mousewheel_distance': 33400, 'average_mousewheel_distance': 102.76923076923077, 'med_mousewheel_distance': 100, 'copy_count': 0, 'average_copy_length': 0, 'med_copy_length': 0, 'paste_count': 4, 'average_paste_length': 123.0, 'med_paste_length': 45.0, 'delete_count': 33, 'keypress_count': 24, 'highlight_count': 1, 'average_highlight_length': 1.0, 'med_highlight_length': 1, 'idle_count': 60, 'med_idle_duration': 2004.0, 'total_idle_duration': 120319, 'keyboard_input_count': 14, 'average_input_length': 51.357142857142854, 'average_input_duration': 84136.78571428571, 'total_input_duration': 1177915, 'med_input_length': 19.5, 'med_input_duration': 16451.0}
]

# 分数数据
scores = [0, -361, -1225, -64,-1521, -1444, -81]

# 提取特定值并组合数据
combined_data = []
for i, user in enumerate(user_behavior_data):
    user_id = f'P{i+1}'
    score = scores[i]
    total_mouse_movement = user['total_mouse_movement']
    combined_data.append([user_id, score, total_mouse_movement])

# 将组合的数据写入CSV文件
with open('storage.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(combined_data)
