import numpy as np
from scipy.stats import ttest_ind
from scipy import stats

# # 给定数据 (-3 items)
# new_participants_score_desert = [('A1', 41), ('A10', 59), ('A11', 59), ('A12', 36), ('A13', 62), ('A14', 64), ('A15', 45), ('A16', 62), ('A17', 48), ('A2', 26), ('A3', 51), ('A4', 39), ('A5', 43), ('A6', 57), ('A7', 64), ('A8', 48), ('A9', 52), ('B1', 49), ('B10', 56), ('B11', 58), ('B12', 50), ('B13', 56), ('B14', 45), ('B15', 59), ('B16', 59), ('B17', 60), ('B18', 52), ('B19', 47), ('B2', 50), ('B20', 61), ('B21', 50), ('B22', 43), ('B23', 63), ('B24', 46), ('B25', 43), ('B26', 33), ('B27', 50), ('B3', 42), ('B4', 35), ('B5', 52), ('B6', 44), ('B7', 58), ('B8', 65), ('B9', 56)]
# new_participants_score_moon = [('A1', 25), ('A10', 64), ('A11', 49), ('A12', 51), ('A13', 41), ('A14', 39), ('A15', 39), ('A16', 24), ('A17', 49), ('A2', 19), ('A3', 46), ('A4', 39), ('A5', 35), ('A6', 67), ('A7', 34), ('A8', 37), ('A9', 51), ('B1', 48), ('B10', 69), ('B11', 63), ('B12', 41), ('B13', 33), ('B14', 45), ('B15', 49), ('B16', 65), ('B17', 38), ('B18', 69), ('B19', 62), ('B2', 27), ('B20', 30), ('B21', 38), ('B22', 56), ('B23', 43), ('B24', 43), ('B25', 56), ('B26', 58), ('B27', 47), ('B3', 47), ('B4', 25), ('B5', 61), ('B6', 36), ('B7', 39), ('B8', 49), ('B9', 54)]

# all
# new_participants_score_desert = [('A1', 66), ('A10', 82), ('A11', 80), ('A12', 62), ('A13', 88), ('A14', 94), ('A15', 64), ('A16', 90), ('A17', 80), ('A2', 42), ('A3', 82), ('A4', 62), ('A5', 60), ('A6', 82), ('A7', 78), ('A8', 64), ('A9', 74), ('B1', 84), ('B10', 86), ('B11', 86), ('B12', 72), ('B13', 90), ('B14', 76), ('B15', 80), ('B16', 90), ('B17', 78), ('B18', 82), ('B19', 82), ('B2', 64), ('B20', 88), ('B21', 82), ('B22', 76), ('B23', 84), ('B24', 80), ('B25', 72), ('B26', 48), ('B27', 84), ('B3', 54), ('B4', 56), ('B5', 74), ('B6', 68), ('B7', 90), ('B8', 94), ('B9', 90)]
# new_participants_score_moon = [('A1', 32), ('A10', 74), ('A11', 60), ('A12', 58), ('A13', 52), ('A14', 42), ('A15', 44), ('A16', 30), ('A17', 56), ('A2', 20), ('A3', 48), ('A4', 48), ('A5', 38), ('A6', 74), ('A7', 40), ('A8', 44), ('A9', 56), ('B1', 54), ('B10', 76), ('B11', 72), ('B12', 58), ('B13', 38), ('B14', 54), ('B15', 60), ('B16', 78), ('B17', 42), ('B18', 84), ('B19', 70), ('B2', 32), ('B20', 32), ('B21', 42), ('B22', 68), ('B23', 50), ('B24', 58), ('B25', 70), ('B26', 78), ('B27', 62), ('B3', 54), ('B4', 34), ('B5', 68), ('B6', 40), ('B7', 48), ('B8', 56), ('B9', 72)]

# 54 ppl
new_participants_score_desert = [('A1', 66), ('A2', 42), ('A3', 82), ('A4', 62), ('A5', 60), ('A6', 82), ('A7', 78), ('A8', 64), ('A9', 74), ('A10', 82), ('A11', 80), ('A12', 62), ('A13', 88), ('A14', 94), ('A15', 64), ('A16', 90), ('A17', 80), ('A18', 68), ('A19', 80), ('A20', 70), ('A22', 72), ('A23', 76), ('A24', 82), ('A25', 74), ('A26', 92), ('B1', 84), ('B2', 64), ('B3', 54), ('B4', 56), ('B5', 74), ('B6', 68), ('B7', 90), ('B8', 94), ('B9', 90), ('B10', 86), ('B11', 86), ('B12', 72), ('B13', 90), ('B14', 76), ('B15', 80), ('B16', 90), ('B18', 82), ('B20', 88), ('B21', 82), ('B22', 76), ('B23', 84), ('B25', 72), ('B26', 48), ('B27', 84), ('B28', 80), ('AI', 102)]
new_participants_score_moon = [('A1', 32), ('A2', 20), ('A3', 48), ('A4', 48), ('A5', 38), ('A6', 74), ('A7', 40), ('A8', 44), ('A9', 56), ('A10', 74), ('A11', 60), ('A12', 58), ('A13', 52), ('A14', 42), ('A15', 44), ('A16', 30), ('A17', 56), ('A18', 78), ('A19', 46), ('A20', 48), ('A22', 66), ('A23', 56), ('A24', 44), ('A25', 50), ('A26', 94), ('B1', 54), ('B2', 32), ('B3', 54), ('B4', 34), ('B5', 68), ('B6', 40), ('B7', 48), ('B8', 56), ('B9', 72), ('B10', 76), ('B11', 72), ('B12', 58), ('B13', 38), ('B14', 54), ('B15', 60), ('B16', 78), ('B18', 84), ('B20', 32), ('B21', 42), ('B22', 68), ('B23', 50), ('B25', 70), ('B26', 78), ('B27', 62), ('B28', 24), ('AI', 76)]

# # 54 ppl (-3)desert: 9,14,15; moon: 2.6.10
# new_participants_score_desert = [('A1', 40), ('A2', 29), ('A3', 44), ('A4', 41), ('A5', 43), ('A6', 56), ('A7', 67), ('A8', 55), ('A9', 46), ('A10', 63), ('A11', 56), ('A12', 43), ('A13', 57), ('A14', 65), ('A15', 45), ('A16', 54), ('A17', 52), ('A18', 44), ('A19', 56), ('A20', 48), ('A22', 35), ('A23', 41), ('A24', 49), ('A25', 38), ('A26', 59), ('B1', 49), ('B2', 47), ('B3', 30), ('B4', 42), ('B5', 55), ('B6', 45), ('B7', 56), ('B8', 63), ('B9', 53), ('B10', 49), ('B11', 56), ('B12', 42), ('B13', 57), ('B14', 46), ('B15', 56), ('B16', 54), ('B18', 57), ('B20', 56), ('B21', 44), ('B22', 46), ('B23', 54), ('B25', 42), ('B26', 33), ('B27', 55), ('B28', 59)]
# new_participants_score_moon = [('A1', 25), ('A2', 18), ('A3', 45), ('A4', 31), ('A5', 34), ('A6', 58), ('A7', 33), ('A8', 37), ('A9', 48), ('A10', 67), ('A11', 47), ('A12', 49), ('A13', 42), ('A14', 39), ('A15', 37), ('A16', 23), ('A17', 49), ('A18', 65), ('A19', 36), ('A20', 36), ('A22', 57), ('A23', 49), ('A24', 36), ('A25', 39), ('A26', 80), ('B1', 46), ('B2', 28), ('B3', 46), ('B4', 25), ('B5', 64), ('B6', 34), ('B7', 37), ('B8', 47), ('B9', 55), ('B10', 64), ('B11', 65), ('B12', 49), ('B13', 25), ('B14', 49), ('B15', 47), ('B16', 68), ('B18', 68), ('B20', 29), ('B21', 39), ('B22', 58), ('B23', 42), ('B25', 64), ('B26', 65), ('B27', 44), ('B28', 21)]

# 54 ppl (-2)
# new_participants_score_moon = [('A1', 42), ('A2', 29), ('A3', 54), ('A4', 42), ('A5', 45), ('A6', 63), ('A7', 50), ('A8', 48), ('A9', 51), ('A10', 70), ('A11', 58), ('A12', 58), ('A13', 43), ('A14', 48), ('A15', 38), ('A16', 32), ('A17', 54), ('A18', 76), ('A19', 47), ('A20', 53), ('A21', 61), ('A22', 52), ('A23', 58), ('A24', 51), ('A25', 40), ('A26', 87), ('A27', 39), ('B1', 55), ('B2', 43), ('B3', 51), ('B4', 42), ('B5', 63), ('B6', 45), ('B7', 52), ('B8', 62), ('B9', 58), ('B10', 73), ('B11', 62), ('B12', 42), ('B13', 34), ('B14', 58), ('B15', 58), ('B16', 75), ('B17', 44), ('B18', 81), ('B19', 77), ('B20', 48), ('B21', 46), ('B22', 73), ('B23', 45), ('B24', 42), ('B25', 57), ('B26', 54), ('B27', 39)]
# new_participants_score_desert = [('A1', 48), ('A2', 43), ('A3', 46), ('A4', 31), ('A5', 45), ('A6', 48), ('A7', 53), ('A8', 51), ('A9', 40), ('A10', 63), ('A11', 56), ('A12', 37), ('A13', 51), ('A14', 59), ('A15', 47), ('A16', 42), ('A17', 52), ('A18', 34), ('A19', 56), ('A20', 38), ('A21', 51), ('A22', 33), ('A23', 51), ('A24', 57), ('A25', 44), ('A26', 55), ('A27', 47), ('B1', 45), ('B2', 57), ('B3', 38), ('B4', 42), ('B5', 59), ('B6', 47), ('B7', 54), ('B8', 67), ('B9', 41), ('B10', 61), ('B11', 52), ('B12', 32), ('B13', 63), ('B14', 56), ('B15', 56), ('B16', 44), ('B17', 42), ('B18', 61), ('B19', 60), ('B20', 46), ('B21', 56), ('B22', 54), ('B23', 48), ('B24', 42), ('B25', 48), ('B26', 21), ('B27', 59)]
# 50 ppl (-3) ;desert:5,14,15 ;moon: 6,8,10
# new_participants_score_moon = [('A1', 25), ('A2', 19), ('A3', 46), ('A4', 39), ('A5', 35), ('A6', 67), ('A7', 34), ('A8', 37), ('A9', 51), ('A10', 64), ('A11', 49), ('A12', 51), ('A13', 41), ('A14', 39), ('A15', 39), ('A16', 24), ('A17', 49), ('A18', 65), ('A19', 38), ('A20', 38), ('A22', 49), ('A23', 51), ('A24', 38), ('A25', 34), ('A26', 80), ('B1', 48), ('B2', 27), ('B3', 47), ('B4', 25), ('B5', 61), ('B6', 36), ('B7', 39), ('B8', 49), ('B9', 54), ('B10', 69), ('B11', 63), ('B12', 41), ('B13', 33), ('B14', 45), ('B15', 49), ('B16', 65), ('B18', 69), ('B20', 30), ('B21', 38), ('B22', 56), ('B23', 43), ('B24', 43), ('B25', 56), ('B26', 58), ('B27', 47), ('B28', 22)]
# new_participants_score_desert = [('A1', 41), ('A2', 26), ('A3', 51), ('A4', 39), ('A5', 43), ('A6', 57), ('A7', 64), ('A8', 48), ('A9', 52), ('A10', 59), ('A11', 59), ('A12', 36), ('A13', 62), ('A14', 64), ('A15', 45), ('A16', 62), ('A17', 48), ('A18', 54), ('A19', 59), ('A20', 50), ('A22', 44), ('A23', 43), ('A24', 50), ('A25', 46), ('A26', 64), ('B1', 49), ('B2', 50), ('B3', 42), ('B4', 35), ('B5', 52), ('B6', 44), ('B7', 58), ('B8', 65), ('B9', 56), ('B10', 56), ('B11', 58), ('B12', 50), ('B13', 56), ('B14', 45), ('B15', 59), ('B16', 59), ('B18', 52), ('B20', 61), ('B21', 50), ('B22', 43), ('B23', 63), ('B24', 46), ('B25', 43), ('B26', 33), ('B27', 50), ('B28', 55)]

# 提取分数
moon_scores = [score for _, score in new_participants_score_moon]
desert_scores = [score for _, score in new_participants_score_desert]

# # 平均分数
# desert_avg = np.mean(desert_scores)
# moon_avg = np.mean(moon_scores)
# print(f"Desert average: {desert_avg}")
# print(f"Moon average: {moon_avg}")
#
# # 标准差
# desert_std = np.std(desert_scores)
# moon_std = np.std(moon_scores)
# print(f"Desert std: {desert_std}")
# print(f"Moon std: {moon_std}")
#
# # 显著性检验 t-test
# t_stat, p_val = ttest_ind(desert_scores, moon_scores)
# print(f"t-statistic: {t_stat}")
# print(f"p-value: {p_val}")
# 执行独立样本t检验
t_statistic, p_value = stats.ttest_ind(moon_scores, desert_scores)

# 计算每个任务的平均分和标准差
moon_mean = np.mean(moon_scores)
desert_mean = np.mean(desert_scores)
moon_std = np.std(moon_scores, ddof=1)
desert_std = np.std(desert_scores, ddof=1)

# 打印结果
print(f"Moon task - Mean: {moon_mean:.2f}, Std Dev: {moon_std:.2f}")
print(f"Desert task - Mean: {desert_mean:.2f}, Std Dev: {desert_std:.2f}")
print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

# 判断结果显著性
alpha = 0.05
if p_value < alpha:
    print("The difference in task difficulty is statistically significant.")
else:
    print("There is no statistically significant difference in task difficulty.")