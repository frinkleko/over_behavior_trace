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
# new_participants_score_moon = [('A1', 32), ('A2', 20), ('A3', 48), ('A4', 48), ('A5', 38), ('A6', 74), ('A7', 40), ('A8', 44), ('A9', 56), ('A10', 74), ('A11', 60), ('A12', 58), ('A13', 52), ('A14', 42), ('A15', 44), ('A16', 30), ('A17', 56), ('A18', 78), ('A19', 46), ('A20', 48), ('A21', 66), ('A22', 66), ('A23', 56), ('A24', 44), ('A25', 50), ('A26', 94), ('A27', 32), ('B1', 54), ('B2', 32), ('B3', 54), ('B4', 34), ('B5', 68), ('B6', 40), ('B7', 48), ('B8', 56), ('B9', 72), ('B10', 76), ('B11', 72), ('B12', 58), ('B13', 38), ('B14', 54), ('B15', 60), ('B16', 78), ('B17', 42), ('B18', 84), ('B19', 70), ('B20', 32), ('B21', 42), ('B22', 68), ('B23', 50), ('B24', 58), ('B25', 70), ('B26', 78), ('B27', 62)]
# new_participants_score_desert = [('A1', 66), ('A2', 42), ('A3', 82), ('A4', 62), ('A5', 60), ('A6', 82), ('A7', 78), ('A8', 64), ('A9', 74), ('A10', 82), ('A11', 80), ('A12', 62), ('A13', 88), ('A14', 94), ('A15', 64), ('A16', 90), ('A17', 80), ('A18', 68), ('A19', 80), ('A20', 70), ('A21', 80), ('A22', 72), ('A23', 76), ('A24', 82), ('A25', 74), ('A26', 92), ('A27', 78), ('B1', 84), ('B2', 64), ('B3', 54), ('B4', 56), ('B5', 74), ('B6', 68), ('B7', 90), ('B8', 94), ('B9', 90), ('B10', 86), ('B11', 86), ('B12', 72), ('B13', 90), ('B14', 76), ('B15', 80), ('B16', 90), ('B17', 78), ('B18', 82), ('B19', 82), ('B20', 88), ('B21', 82), ('B22', 76), ('B23', 84), ('B24', 80), ('B25', 72), ('B26', 48), ('B27', 84)]

# 54 ppl (-3)
new_participants_score_moon = [('A1', 25), ('A2', 19), ('A3', 46), ('A4', 39), ('A5', 35), ('A6', 67), ('A7', 34), ('A8', 37), ('A9', 51), ('A10', 64), ('A11', 49), ('A12', 51), ('A13', 41), ('A14', 39), ('A15', 39), ('A16', 24), ('A17', 49), ('A18', 65), ('A19', 38), ('A20', 38), ('A21', 59), ('A22', 49), ('A23', 51), ('A24', 38), ('A25', 34), ('A26', 80), ('A27', 27), ('B1', 48), ('B2', 27), ('B3', 47), ('B4', 25), ('B5', 61), ('B6', 36), ('B7', 39), ('B8', 49), ('B9', 54), ('B10', 69), ('B11', 63), ('B12', 41), ('B13', 33), ('B14', 45), ('B15', 49), ('B16', 65), ('B17', 38), ('B18', 69), ('B19', 62), ('B20', 30), ('B21', 38), ('B22', 56), ('B23', 43), ('B24', 43), ('B25', 56), ('B26', 58), ('B27', 47)]
new_participants_score_desert = [('A1', 41), ('A2', 26), ('A3', 51), ('A4', 39), ('A5', 43), ('A6', 57), ('A7', 64), ('A8', 48), ('A9', 52), ('A10', 59), ('A11', 59), ('A12', 36), ('A13', 62), ('A14', 64), ('A15', 45), ('A16', 62), ('A17', 48), ('A18', 54), ('A19', 59), ('A20', 50), ('A21', 52), ('A22', 44), ('A23', 43), ('A24', 50), ('A25', 46), ('A26', 64), ('A27', 52), ('B1', 49), ('B2', 50), ('B3', 42), ('B4', 35), ('B5', 52), ('B6', 44), ('B7', 58), ('B8', 65), ('B9', 56), ('B10', 56), ('B11', 58), ('B12', 50), ('B13', 56), ('B14', 45), ('B15', 59), ('B16', 59), ('B17', 60), ('B18', 52), ('B19', 47), ('B20', 61), ('B21', 50), ('B22', 43), ('B23', 63), ('B24', 46), ('B25', 43), ('B26', 33), ('B27', 50)]

# 提取分数
moon_scores = [score for _, score in new_participants_score_moon]
desert_scores = [score for _, score in new_participants_score_desert]

# 平均分数
desert_avg = np.mean(desert_scores)
moon_avg = np.mean(moon_scores)
print(f"Desert average: {desert_avg}")
print(f"Moon average: {moon_avg}")

# 标准差
desert_std = np.std(desert_scores)
moon_std = np.std(moon_scores)
print(f"Desert std: {desert_std}")
print(f"Moon std: {moon_std}")

# 显著性检验 t-test
t_stat, p_val = ttest_ind(desert_scores, moon_scores)
print(f"t-statistic: {t_stat}")
print(f"p-value: {p_val}")